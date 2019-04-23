

import 'dart:convert';

// "id": 10, 
// "notepad_id": 8, 
// "text": "text", 
// "title": "title"

Note postFromJson(String str) {
    final jsonData = json.decode(str);
    print(jsonData);
    return Note.fromJson(jsonData);
}

String postToJson(Note data) {
    final dyn = data.toJson();
    return json.encode(dyn);
}

class Note {
    int id;
    int notepadId;
    String title;
    String text;

    Note({
        this.notepadId,
        this.id,
        this.title,
        this.text,
    });

    factory Note.fromJson(Map<String, dynamic> json) => new Note(
        notepadId: json["notepad_id"],
        id: json["id"],
        title: json["title"],
        text: json["text"],
    );

    Map<String, dynamic> toJson() => {
        "notepad_id": notepadId,
        "id": id,
        "title": title,
        "text": text,
    };
}