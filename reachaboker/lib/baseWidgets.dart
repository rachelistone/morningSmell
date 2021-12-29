import 'package:flutter/material.dart';
import './accountPage.dart';
import './cartPage.dart';
import './selectProductsPage.dart';
import './contactPage.dart';
import './aboutPage.dart';
import './logoutPage.dart';

class NavigationDrawerWidget extends StatelessWidget {
  final padding = EdgeInsets.symmetric(horizontal: 25);

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: Material(
        color: Color(0xFFFFEE44),
        child: ListView(
          padding: padding,
          children: <Widget>[
            const SizedBox(
              height: 48,
            ),
            buildMenuItem(
              text: 'החשבון שלי',
              icon: Icons.person,
              onClicked: () => selectedMenuItem(context, 0),
            ),
            buildMenuItem(
              text: 'הסל שלי',
              icon: Icons.shopping_bag,
              onClicked: () => selectedMenuItem(context, 1),
            ),
            buildMenuItem(
              text: 'בחירת מוצרים',
              icon: Icons.add,
              onClicked: () => selectedMenuItem(context, 2),
            ),
            buildMenuItem(
              text: 'יצירת קשר',
              icon: Icons.message,
              onClicked: () => selectedMenuItem(context, 3),
            ),
            buildMenuItem(
              text: 'אודות',
              icon: Icons.info,
              onClicked: () => selectedMenuItem(context, 4),
            ),
            buildMenuItem(
              text: 'התנתקות',
              icon: Icons.logout,
              onClicked: () => selectedMenuItem(context, 5),
            ),
            // const SizedBox(
            //   height: 24,
            // ),
            // Divider(
            //   color: Colors.black,
            // ),
            // const SizedBox(
            //   height: 24,
            // ),
          ],
        ),
      ),
    );
  }

  Widget buildMenuItem({
    required String text,
    required IconData icon,
    VoidCallback? onClicked,
  }) {
    final color = Colors.black;
    // final hoverColor = Colors.black;

    return ListTile(
      leading: Icon(icon, color: color),
      title: Text(text, style: TextStyle(fontSize: 20, color: color)),
      // hoverColor: hoverColor,
      onTap: onClicked,
    );
  }

  void selectedMenuItem(BuildContext context, int index) {
    switch (index) {
      case 0:
        Navigator.of(context).push(MaterialPageRoute(
          builder: (context) => AccountPage(),
        ));
        break;
      case 1:
        Navigator.of(context).push(MaterialPageRoute(
          builder: (context) => CartPage(),
        ));
        break;
      case 2:
        Navigator.of(context).push(MaterialPageRoute(
          builder: (context) => SelectProductsPage(),
        ));
        break;
      case 3:
        Navigator.of(context).push(MaterialPageRoute(
          builder: (context) => ContactPage(),
        ));
        break;
      case 4:
        Navigator.of(context).push(MaterialPageRoute(
          builder: (context) => AboutPage(),
        ));
        break;
      case 5:
        Navigator.of(context).push(MaterialPageRoute(
          builder: (context) => LogoutPage(),
        ));
        break;
    }
  }
}

class MyAppBar extends StatelessWidget implements PreferredSizeWidget {
  const MyAppBar({
    Key? key,
  }) : super(key: key);

  @override
  Size get preferredSize => Size.fromHeight(80.0);

  @override
  Widget build(BuildContext context) {
    return AppBar(
      title: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Image.asset(
            'assets/logomorningsmell.png',
            //sfit: BoxFit.contain,
            height: 170,
          ),
        ],
      ),
    );
  }
}

BoxDecoration linear = const BoxDecoration(
  gradient: LinearGradient(
      colors: [
        Color(0xFFFFB300),
        Color(0xFFFFFF85),
      ],
      stops: [
        0.0,
        1.0
      ],
      begin: FractionalOffset.topRight,
      end: FractionalOffset.bottomLeft,
      tileMode: TileMode.repeated),
);
