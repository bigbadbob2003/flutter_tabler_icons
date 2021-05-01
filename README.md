# flutter_tabler_icons

The [Tabler Icon Pack](https://github.com/tabler/tabler-icons) in Flutter

Tabler icons version: 1.41.1

## pubspec.yaml
```yml
dependencies:
  flutter:
    sdk: flutter
  flutter_tabler_icons: ^1.1.1
```

## Usage
```Dart
import 'package:flutter_tabler_icons/flutter_tabler_icons.dart';

class MyWidget extends StatelessWidget {
  Widget build(BuildContext context) {
    return new IconButton(
      icon: new Icon(TablerIcons.ambulance),
      onPressed: () { print('Ambulance pressed'); }
     );
  }
}
```
![alt text](https://github.com/bigbadbob2003/flutter_tabler_icons/raw/master/.github/screenshot.png)
