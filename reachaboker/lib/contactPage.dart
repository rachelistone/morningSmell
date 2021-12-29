import 'package:flutter/material.dart';
import './baseWidgets.dart';

class ContactPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Scaffold(
        drawer: NavigationDrawerWidget(),
        appBar: AppBar(
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
          toolbarHeight: 80.0,
        ),
        body: Container(
          decoration: linear,
        ),
      );
}
