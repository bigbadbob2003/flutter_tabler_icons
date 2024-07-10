# flutter_tabler_icons

The [Tabler Icon Pack](https://github.com/tabler/tabler-icons) in Flutter

Tabler icons version: v3.10.0

## pubspec.yaml
```yml
dependencies:
  flutter:
    sdk: flutter
  flutter_tabler_icons: ^1.34.0
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

## Updating Icons

This package can be updated to use a newer release of Tabler Icons with `tabler_gen.py` in `/util`. It takes the codepoints from the CSS file of the release and generates a Flutter class of all of the icons.

![Screenshot of example app](https://github.com/bigbadbob2003/flutter_tabler_icons/raw/master/.github/screenshot.png)
