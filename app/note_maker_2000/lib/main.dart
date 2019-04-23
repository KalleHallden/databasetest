import 'package:flutter/material.dart';
import 'note.dart';
import 'package:http/http.dart' as http;
import 'dart:async';


void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

String url = 'http://127.0.0.1:5000/18/note';

Future<Note> getPost() async{
  final response = await http.get('$url');
  return postFromJson(response.body);
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void addNewNote(String note) {
    setState(() {
      // http://127.0.0.1:5000/
      DateTime date = DateTime.now();
      Note mynote = new Note(id: 45, notepadId: 8, text: date.toIso8601String(), title: note);
      createNote(mynote).then((response){
        if(response.statusCode == 200)
          print("All good");
        else
        print(response.statusCode);
        });
      _counter++;
    });
  }

  Future<http.Response> createNote(Note note) async{
    final response = await http.post('$url',
        body: postToJson(note)
    );
    return response;
  }

  TextEditingController noteControl = new TextEditingController();

  @override
  Widget build(BuildContext context) {

    TextField noteField = new TextField(
      controller: noteControl,
    );
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            FutureBuilder<Note>(
              future: getPost(),
              builder: (context, snapshot) {
                if(snapshot.connectionState == ConnectionState.done)
                  return Text('Title: ${snapshot.data.title} \nNote: ${snapshot.data.text}');
                else
                  return CircularProgressIndicator();
            }
          ),
          noteField
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          if (noteField.controller.text != null) {
            addNewNote(noteField.controller.text);
          }
        },
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
