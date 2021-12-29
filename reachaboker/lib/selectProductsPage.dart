import 'package:flutter/material.dart';
import './baseWidgets.dart';

class SelectProductsPage extends StatelessWidget {
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
          child: Center(
            child: GridView.count(
              padding: const EdgeInsets.all(20),
              crossAxisSpacing: 10,
              mainAxisSpacing: 10,
              crossAxisCount: 2,
              children: const <Widget>[
                Placeholder(),
                Placeholder(),
                Placeholder(),
                Placeholder(),
                Placeholder(),
                Placeholder(),
                Placeholder(),
                Placeholder(),
              ],
            ),
          ),
        ),
      );
}
