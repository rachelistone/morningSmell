import 'package:flutter/material.dart';
import './baseWidgets.dart';

class AccountPage extends StatelessWidget {
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
          child: ListView(
            padding: const EdgeInsets.all(8),
            children: <Widget>[
              Container(
                height: 50,
                child: const Center(child: Text('Entry A')),
              ),
              Container(
                height: 50,
                child: const Center(child: Text('Entry B')),
              ),
              Container(
                height: 50,
                child: const Center(child: Text('Entry C')),
              ),
            ],
          ),
        ),
      );
}
