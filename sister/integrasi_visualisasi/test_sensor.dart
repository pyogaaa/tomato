import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:tomacare/firebase_options.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // 🔥 Gunakan konfigurasi platform yang benar
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Monitoring Dashboard',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blueAccent),
        useMaterial3: true,
      ),
      home: const DashboardPage(),
    );
  }
}

class DashboardPage extends StatelessWidget {
  const DashboardPage({super.key});

  @override
  Widget build(BuildContext context) {
    // Stream dokumen Firestore untuk data real-time
    final Stream<DocumentSnapshot> dataStream = FirebaseFirestore.instance
        .collection('monitoring')
        .doc('data_terkini')
        .snapshots();

    return Scaffold(
      appBar: AppBar(
        title: const Text('Live Monitoring Dashboard'),
      ),
      body: Center(
        child: StreamBuilder<DocumentSnapshot>(
          stream: dataStream,
          builder:
              (BuildContext context, AsyncSnapshot<DocumentSnapshot> snapshot) {
            // Error handling
            if (snapshot.hasError) {
              return const Text('Terjadi error saat mengambil data!');
            }

            // Loading state
            if (snapshot.connectionState == ConnectionState.waiting) {
              return const CircularProgressIndicator();
            }

            // Jika data tidak ada
            if (!snapshot.hasData || !snapshot.data!.exists) {
              return const Text(
                  'Dokumen tidak ditemukan.\nPastikan perangkat mengirim data.');
            }

            // Ambil data dari dokumen
            Map<String, dynamic> data =
                snapshot.data!.data() as Map<String, dynamic>;

            // Parsing data dengan aman
            double jarak = (data['jarak'] ?? 0.0).toDouble();
            int tdsRaw = (data['tds'] ?? 0);
            double suhuAir = (data['suhu_air'] ?? 0.0).toDouble();

            // UI Dashboard
            return Padding(
              padding: const EdgeInsets.all(24.0),
              child: SingleChildScrollView(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: <Widget>[
                    // Card: Jarak (Ketinggian Air)
                    SensorCard(
                      title: 'Jarak (Ketinggian Air)',
                      value: '${jarak.toStringAsFixed(1)} cm',
                      color: Colors.blueAccent,
                      subtitle: 'Sensor ultrasonik',
                    ),
                    const SizedBox(height: 20),

                    // Card: TDS Raw
                    SensorCard(
                      title: 'TDS (Nilai Raw)',
                      value: '$tdsRaw',
                      color: Colors.green,
                      subtitle: 'Perlu dikalibrasi ke PPM',
                    ),
                    const SizedBox(height: 20),

                    // Card: Suhu Air
                    SensorCard(
                      title: 'Suhu Air',
                      value: '${suhuAir.toStringAsFixed(1)} °C',
                      color: Colors.redAccent,
                      subtitle: 'Sensor suhu air (DS18B20 / sejenis)',
                    ),
                  ],
                ),
              ),
            );
          },
        ),
      ),
    );
  }
}

/// Widget reusable untuk menampilkan data sensor
class SensorCard extends StatelessWidget {
  final String title;
  final String value;
  final Color color;
  final String subtitle;

  const SensorCard({
    super.key,
    required this.title,
    required this.value,
    required this.color,
    this.subtitle = '',
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 4,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      child: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          children: [
            Text(
              title,
              style: Theme.of(context).textTheme.headlineSmall,
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 8),
            Text(
              value,
              style: Theme.of(context).textTheme.displayMedium?.copyWith(
                    color: color,
                    fontWeight: FontWeight.bold,
                  ),
              textAlign: TextAlign.center,
            ),
            if (subtitle.isNotEmpty) ...[
              const SizedBox(height: 8),
              Text(
                subtitle,
                style: Theme.of(context).textTheme.bodySmall,
                textAlign: TextAlign.center,
              ),
            ],
          ],
        ),
      ),
    );
  }
}
