import 'package:flutter/material.dart';
import './baseWidgets.dart';

class CartPage extends StatelessWidget {
  void _addItem() {}

  @override
  Widget build(BuildContext context) => Scaffold(
        drawer: NavigationDrawerWidget(),
        appBar: MyAppBar(),
        body: Container(
          decoration: linear,
          child: Center(
            child: GridView.count(
              padding: const EdgeInsets.all(20),
              crossAxisSpacing: 10,
              mainAxisSpacing: 20,
              crossAxisCount: 1,
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
        floatingActionButton: FloatingActionButton(
          onPressed: _addItem,
          tooltip: 'Increment',
          child: const Icon(Icons.add),
        ),
      ); // This trailing comma makes auto-formatting nicer for build methods.

}
