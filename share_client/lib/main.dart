import 'package:flutter/material.dart';
import 'package:share/share.dart';
import 'package:share/receive_share_state.dart';
import 'package:http/http.dart' as http;

void main() => runApp(MyApp());

final serverIp = 'http://0.0.0.0:5555';

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'NW Share Helper',
      home: Scaffold(
        appBar: AppBar(
          title: Text('NW Share Helper'),
        ),
        body: ShareManager(),
      ),
    );
  }
}

class ShareManager extends StatefulWidget {
  @override
  ShareManagerState createState() => new ShareManagerState();
}

class ShareManagerState extends ReceiveShareState<ShareManager> {

  String _result = '';

  @override
  void receiveShare(Share shared) {
    // debugPrint("Share received - $shared");
    http.put(serverIp, body: {'url': shared.text}).then((response) {
      debugPrint(response.body);
      setState(() {
        _result = response.body;
      });
    });
  }
  @override
  Widget build(BuildContext context) {
    enableShareReceiving();
    return Center(
          child: Text(_result),
    );
  }
}