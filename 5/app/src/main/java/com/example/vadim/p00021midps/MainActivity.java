package com.example.vadim.p00021midps;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;



public class MainActivity extends AppCompatActivity implements OnClickListener {
    Button btnActTwo;
    Button btnActThree;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnActTwo = (Button) findViewById(R.id.btnActTwo);
        btnActTwo.setOnClickListener(this);
        btnActThree = (Button) findViewById(R.id.btnActThree);
        btnActThree.setOnClickListener(this);
    }


    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.btnActTwo:
                Intent intent = new Intent(this, Main2Activity.class);
                startActivity(intent);// Вызывает переход
                break;}

                switch (v.getId()) {
                    case R.id.btnActThree:
                        Intent intent = new Intent(this, Main3Activity.class);
                        startActivity(intent);

                        break;
                    default:
                        break;

                }
        }
    }


