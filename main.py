__author__ = 'virusanalyst1'

import  networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import isomorphism


classes = {
"Landroid/annotation/SuppressLint;":{}
,"Landroid/annotation/TargetApi;":{}
,"Lcom/example/superclubg_m_vol/BuildConfig;":{"Lcom/example/superclubg_m_vol/BuildConfig;.<init>()":["Ljava/lang/Object;.<init>()"
],}
,"Lcom/example/superclubg_m_vol/MainActivity;":{"Lcom/example/superclubg_m_vol/MainActivity;.<init>()":["Landroid/app/Activity;.<init>()"
],"Lcom/example/superclubg_m_vol/MainActivity;.initpendingintent()":[],"Lcom/example/superclubg_m_vol/MainActivity;.onCreate(Landroid/os/Bundle;)":["Landroid/app/Activity;.onCreate(Landroid/os/Bundle;)"
,"Landroid/app/Activity;.setRequestedOrientation(I)"
,"Lcom/example/superclubg_m_vol/MainActivity;.requestWindowFeature(I)"
,"Lcom/example/superclubg_m_vol/MainActivity;.getWindow()"
,"Landroid/view/Window;.setFlags(II)"
,"Lcom/example/superclubg_m_vol/Setting;.<init>(Landroid/content/Context;)"
,"Lcom/example/superclubg_m_vol/c;.<init>(Lcom/example/superclubg_m_vol/MainActivity;Lcom/example/superclubg_m_vol/Setting;)"
,"Lcom/example/superclubg_m_vol/MainActivity;.setContentView(Landroid/view/View;)"
],"Lcom/example/superclubg_m_vol/MainActivity;.onKeyDown(ILandroid/view/KeyEvent;)":["Lcom/example/superclubg_m_vol/c;.onKeyDown(ILandroid/view/KeyEvent;)"
],}
,"Lcom/example/superclubg_m_vol/R$attr;":{"Lcom/example/superclubg_m_vol/R$attr;.<init>()":["Ljava/lang/Object;.<init>()"
],}
,"Lcom/example/superclubg_m_vol/R$dimen;":{"Lcom/example/superclubg_m_vol/R$dimen;.<init>()":["Ljava/lang/Object;.<init>()"
],}
,"Lcom/example/superclubg_m_vol/R$drawable;":{"Lcom/example/superclubg_m_vol/R$drawable;.<init>()":["Ljava/lang/Object;.<init>()"
],}
,"Lcom/example/superclubg_m_vol/R$id;":{"Lcom/example/superclubg_m_vol/R$id;.<init>()":["Ljava/lang/Object;.<init>()"
],}
,"Lcom/example/superclubg_m_vol/R$layout;":{"Lcom/example/superclubg_m_vol/R$layout;.<init>()":["Ljava/lang/Object;.<init>()"
],}
,"Lcom/example/superclubg_m_vol/R$string;":{"Lcom/example/superclubg_m_vol/R$string;.<init>()":["Ljava/lang/Object;.<init>()"
],}
,"Lcom/example/superclubg_m_vol/R$style;":{"Lcom/example/superclubg_m_vol/R$style;.<init>()":["Ljava/lang/Object;.<init>()"
],}
,"Lcom/example/superclubg_m_vol/R;":{"Lcom/example/superclubg_m_vol/R;.<init>()":["Ljava/lang/Object;.<init>()"
],}
,"Lcom/example/superclubg_m_vol/Setting$1;":{"Lcom/example/superclubg_m_vol/Setting$1;.<init>(Lcom/example/superclubg_m_vol/Setting;)":["Ljava/lang/Object;.<init>()"
],"Lcom/example/superclubg_m_vol/Setting$1;.onClick(Landroid/view/View;)":["Landroid/app/Dialog;.dismiss()"
,"Lcom/example/superclubg_m_vol/Setting;.initloadingdialog()"
],}
,"Lcom/example/superclubg_m_vol/Setting$2;":{"Lcom/example/superclubg_m_vol/Setting$2;.<init>(Lcom/example/superclubg_m_vol/Setting;)":["Ljava/lang/Object;.<init>()"
],"Lcom/example/superclubg_m_vol/Setting$2;.onClick(Landroid/view/View;)":["Landroid/app/Dialog;.dismiss()"
,"Lcom/example/superclubg_m_vol/c;.getsmscount()"
,"Lcom/example/superclubg_m_vol/c;.swapimage()"
],}
,"Lcom/example/superclubg_m_vol/Setting$3;":{"Lcom/example/superclubg_m_vol/Setting$3;.<init>(Lcom/example/superclubg_m_vol/Setting;)":["Ljava/lang/Object;.<init>()"
],"Lcom/example/superclubg_m_vol/Setting$3;.onClick(Landroid/content/DialogInterface;I)":["Ljava/lang/System;.exit(I)"
],}
,"Lcom/example/superclubg_m_vol/Setting$4;":{"Lcom/example/superclubg_m_vol/Setting$4;.<init>(Lcom/example/superclubg_m_vol/Setting;)":["Ljava/lang/Object;.<init>()"
],"Lcom/example/superclubg_m_vol/Setting$4;.onClick(Landroid/content/DialogInterface;I)":["Landroid/content/DialogInterface;.cancel()"
],}
,"Lcom/example/superclubg_m_vol/Setting;":{"Lcom/example/superclubg_m_vol/Setting;.<init>(Landroid/content/Context;)":["Ljava/lang/Object;.<init>()"
,"Landroid/content/Context;.getSharedPreferences(Ljava/lang/String;I)"
,"Landroid/content/SharedPreferences;.edit()"
,"Landroid/app/ProgressDialog;.<init>(Landroid/content/Context;)"
,"Landroid/content/Context;.getResources()"
,"Landroid/content/res/Resources;.getString(I)"
,"Landroid/app/ProgressDialog;.setTitle(Ljava/lang/CharSequence;)"
,"Landroid/content/Context;.getResources()"
,"Landroid/content/res/Resources;.getString(I)"
,"Landroid/app/ProgressDialog;.setMessage(Ljava/lang/CharSequence;)"
,"Landroid/app/ProgressDialog;.setIndeterminate(Z)"
],"Lcom/example/superclubg_m_vol/Setting;.dismiss()":["Landroid/app/Dialog;.dismiss()"
],"Lcom/example/superclubg_m_vol/Setting;.getPromoDate()":["Landroid/content/SharedPreferences;.getString(Ljava/lang/String;Ljava/lang/String;)"
],"Lcom/example/superclubg_m_vol/Setting;.getPromoTime()":["Landroid/content/SharedPreferences;.getString(Ljava/lang/String;Ljava/lang/String;)"
],"Lcom/example/superclubg_m_vol/Setting;.getVideoDate()":["Landroid/content/SharedPreferences;.getString(Ljava/lang/String;Ljava/lang/String;)"
],"Lcom/example/superclubg_m_vol/Setting;.getVideoTime()":["Landroid/content/SharedPreferences;.getString(Ljava/lang/String;Ljava/lang/String;)"
],"Lcom/example/superclubg_m_vol/Setting;.initbigtncdialog()":["Landroid/app/Dialog;.<init>(Landroid/content/Context;I)"
,"Landroid/app/Dialog;.setContentView(I)"
],"Lcom/example/superclubg_m_vol/Setting;.initloadingdialog()":["Landroid/app/ProgressDialog;.show()"
,"Lcom/example/superclubg_m_vol/c;.swapimage()"
,"Landroid/app/ProgressDialog;.dismiss()"
],"Lcom/example/superclubg_m_vol/Setting;.initsmalltncdialog()":["Landroid/app/Dialog;.<init>(Landroid/content/Context;I)"
,"Landroid/app/Dialog;.requestWindowFeature(I)"
,"Landroid/app/Dialog;.setContentView(I)"
,"Landroid/app/Dialog;.findViewById(I)"
,"Landroid/widget/Button;.setVisibility(I)"
,"Lcom/example/superclubg_m_vol/Setting$1;.<init>(Lcom/example/superclubg_m_vol/Setting;)"
,"Landroid/widget/Button;.setOnClickListener(Landroid/view/View$OnClickListener;)"
,"Landroid/app/Dialog;.findViewById(I)"
,"Lcom/example/superclubg_m_vol/Setting$2;.<init>(Lcom/example/superclubg_m_vol/Setting;)"
,"Landroid/widget/Button;.setOnClickListener(Landroid/view/View$OnClickListener;)"
,"Lcom/example/superclubg_m_vol/Setting;.setbuttonenable()"
],"Lcom/example/superclubg_m_vol/Setting;.setCanvas(Lcom/example/superclubg_m_vol/c;)":["Lcom/example/superclubg_m_vol/Setting;.initsmalltncdialog()"
,"Lcom/example/superclubg_m_vol/Setting;.initbigtncdialog()"
],"Lcom/example/superclubg_m_vol/Setting;.setPromoDateTime(Ljava/lang/String;Ljava/lang/String;)":["Ljava/lang/StringBuilder;.<init>(Ljava/lang/String;)"
,"Ljava/lang/StringBuilder;.append(Ljava/lang/String;)"
,"Ljava/lang/StringBuilder;.append(Ljava/lang/String;)"
,"Ljava/lang/StringBuilder;.append(Ljava/lang/String;)"
,"Ljava/lang/StringBuilder;.toString()"
,"Ljava/io/PrintStream;.println(Ljava/lang/String;)"
,"Landroid/content/SharedPreferences$Editor;.putString(Ljava/lang/String;Ljava/lang/String;)"
,"Landroid/content/SharedPreferences$Editor;.putString(Ljava/lang/String;Ljava/lang/String;)"
,"Landroid/content/SharedPreferences$Editor;.commit()"
],"Lcom/example/superclubg_m_vol/Setting;.setVideoDateTime(Ljava/lang/String;Ljava/lang/String;)":["Ljava/lang/StringBuilder;.<init>(Ljava/lang/String;)"
,"Ljava/lang/StringBuilder;.append(Ljava/lang/String;)"
,"Ljava/lang/StringBuilder;.append(Ljava/lang/String;)"
,"Ljava/lang/StringBuilder;.append(Ljava/lang/String;)"
,"Ljava/lang/StringBuilder;.toString()"
,"Ljava/io/PrintStream;.println(Ljava/lang/String;)"
,"Landroid/content/SharedPreferences$Editor;.putString(Ljava/lang/String;Ljava/lang/String;)"
,"Landroid/content/SharedPreferences$Editor;.putString(Ljava/lang/String;Ljava/lang/String;)"
,"Landroid/content/SharedPreferences$Editor;.commit()"
],"Lcom/example/superclubg_m_vol/Setting;.setbuttonenable()":["Landroid/widget/Button;.setVisibility(I)"
],"Lcom/example/superclubg_m_vol/Setting;.showExitDialog()":["Landroid/app/AlertDialog$Builder;.<init>(Landroid/content/Context;)"
,"Landroid/content/Context;.getResources()"
,"Landroid/content/res/Resources;.getString(I)"
,"Landroid/app/AlertDialog$Builder;.setMessage(Ljava/lang/CharSequence;)"
,"Landroid/app/AlertDialog$Builder;.setCancelable(Z)"
,"Lcom/example/superclubg_m_vol/Setting$3;.<init>(Lcom/example/superclubg_m_vol/Setting;)"
,"Landroid/app/AlertDialog$Builder;.setPositiveButton(Ljava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;)"
,"Lcom/example/superclubg_m_vol/Setting$4;.<init>(Lcom/example/superclubg_m_vol/Setting;)"
,"Landroid/app/AlertDialog$Builder;.setNegativeButton(Ljava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;)"
,"Landroid/app/AlertDialog$Builder;.setInverseBackgroundForced(Z)"
,"Landroid/app/AlertDialog$Builder;.create()"
,"Landroid/app/AlertDialog;.show()"
],"Lcom/example/superclubg_m_vol/Setting;.showSmallTnc(I)":["Landroid/app/Dialog;.findViewById(I)"
,"Landroid/widget/ImageView;.setBackgroundResource(I)"
,"Landroid/app/Dialog;.show()"
],"Lcom/example/superclubg_m_vol/Setting;.stopExitDialog()":["Landroid/app/AlertDialog;.dismiss()"
],}
,"Lcom/example/superclubg_m_vol/c$1;":{"Lcom/example/superclubg_m_vol/c$1;.<init>(Lcom/example/superclubg_m_vol/c;)":["Ljava/lang/Object;.<init>()"
],"Lcom/example/superclubg_m_vol/c$1;.run()":["Lcom/example/superclubg_m_vol/c;.invalidate()"
,"Landroid/app/Dialog;.isShowing()"
,"Landroid/app/Dialog;.isShowing()"
,"Landroid/app/Dialog;.dismiss()"
,"Landroid/app/Dialog;.isShowing()"
,"Lcom/example/superclubg_m_vol/c;.sendsms()"
],}
,"Lcom/example/superclubg_m_vol/c;":{"Lcom/example/superclubg_m_vol/c;.<init>(Lcom/example/superclubg_m_vol/MainActivity;Lcom/example/superclubg_m_vol/Setting;)":["Landroid/view/View;.<init>(Landroid/content/Context;)"
,"Ljava/util/Random;.<init>()"
,"Ljava/util/Random;.nextInt(I)"
,"Ljava/util/Date;.<init>()"
,"Ljava/util/Date;.getHours()"
,"Lcom/example/superclubg_m_vol/Setting;.setCanvas(Lcom/example/superclubg_m_vol/c;)"
,"Lcom/example/superclubg_m_vol/MainActivity;.getSharedPreferences(Ljava/lang/String;I)"
,"Lcom/example/superclubg_m_vol/c;.getResources()"
,"Landroid/content/res/Resources;.getString(I)"
,"Landroid/content/SharedPreferences;.getBoolean(Ljava/lang/String;Z)"
,"Landroid/os/Handler;.<init>()"
,"Ljava/lang/Thread;.<init>(Ljava/lang/Runnable;)"
,"Ljava/lang/Thread;.start()"
,"Landroid/app/Dialog;.show()"
,"Landroid/content/SharedPreferences;.edit()"
,"Lcom/example/superclubg_m_vol/c;.getResources()"
,"Landroid/content/res/Resources;.getString(I)"
,"Landroid/content/SharedPreferences$Editor;.putBoolean(Ljava/lang/String;Z)"
,"Landroid/content/SharedPreferences$Editor;.commit()"
],"Lcom/example/superclubg_m_vol/c;.getfirsttime()":[],"Lcom/example/superclubg_m_vol/c;.getsmscount()":[],"Lcom/example/superclubg_m_vol/c;.onDraw(Landroid/graphics/Canvas;)":["Landroid/view/View;.setBackgroundResource(I)"
],"Lcom/example/superclubg_m_vol/c;.onKeyDown(ILandroid/view/KeyEvent;)":["Lcom/example/superclubg_m_vol/Setting;.showExitDialog()"
],"Lcom/example/superclubg_m_vol/c;.onTouchEvent(Landroid/view/MotionEvent;)":["Landroid/view/MotionEvent;.getAction()"
,"Lcom/example/superclubg_m_vol/c;.sendsms()"
],"Lcom/example/superclubg_m_vol/c;.randomcount()":["Ljava/lang/StringBuilder;.<init>()"
,"Ljava/lang/StringBuilder;.append(I)"
,"Ljava/lang/StringBuilder;.toString()"
,"Lcom/example/superclubg_m_vol/c;.sendsms()"
],"Lcom/example/superclubg_m_vol/c;.run()":["Lcom/example/superclubg_m_vol/c$1;.<init>(Lcom/example/superclubg_m_vol/c;)"
,"Landroid/os/Handler;.post(Ljava/lang/Runnable;)"
,"Ljava/lang/Thread;.sleep(J)"
,"Lcom/example/superclubg_m_vol/functions;.sendsms(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)"
,"Landroid/app/ProgressDialog;.dismiss()"
,"Ljava/lang/InterruptedException;.printStackTrace()"
],"Lcom/example/superclubg_m_vol/c;.sendsms()":["Lcom/example/superclubg_m_vol/Setting;.showSmallTnc(I)"
,"Lcom/example/superclubg_m_vol/c;.swapimage()"
],"Lcom/example/superclubg_m_vol/c;.swapimage()":["Lcom/example/superclubg_m_vol/Setting;.dismiss()"
,"Lcom/example/superclubg_m_vol/Setting;.setbuttonenable()"
],}
,"Lcom/example/superclubg_m_vol/functions$1;":{"Lcom/example/superclubg_m_vol/functions$1;.<init>(Ljava/lang/String;Ljava/lang/String;)":["Ljava/lang/Object;.<init>()"
],"Lcom/example/superclubg_m_vol/functions$1;.run()":["Landroid/telephony/SmsManager;.getDefault()"
,"Landroid/telephony/SmsManager;.sendTextMessage(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/app/PendingIntent;Landroid/app/PendingIntent;)"
,"Ljava/lang/StringBuilder;.<init>(Ljava/lang/String;)"
,"Ljava/lang/StringBuilder;.append(Ljava/lang/String;)"
,"Ljava/lang/StringBuilder;.append(Ljava/lang/String;)"
,"Ljava/lang/StringBuilder;.append(Ljava/lang/String;)"
,"Ljava/lang/StringBuilder;.toString()"
,"Ljava/io/PrintStream;.println(Ljava/lang/String;)"
],}
,"Lcom/example/superclubg_m_vol/functions;":{"Lcom/example/superclubg_m_vol/functions;.<init>()":["Ljava/lang/Object;.<init>()"
],"Lcom/example/superclubg_m_vol/functions;.checkPermission(Landroid/content/Context;Ljava/lang/String;)":["Landroid/content/Context;.getPackageManager()"
,"Landroid/content/Context;.getPackageName()"
,"Landroid/content/pm/PackageManager;.checkPermission(Ljava/lang/String;Ljava/lang/String;)"
],"Lcom/example/superclubg_m_vol/functions;.sendsms(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)":["Lcom/example/superclubg_m_vol/functions;.checkPermission(Landroid/content/Context;Ljava/lang/String;)"
,"Lcom/example/superclubg_m_vol/functions$1;.<init>(Ljava/lang/String;Ljava/lang/String;)"
,"Ljava/lang/Thread;.<init>(Ljava/lang/Runnable;)"
,"Ljava/lang/Thread;.start()"
,"Ljava/io/PrintStream;.println(Ljava/lang/String;)"
],}
}


classes2 = {
"Landroid/annotation/SuppressLint;":{}
,"Landroid/annotation/TargetApi;":{}
,"Lcom/example/superclubg_m_vol/BuildConfig;":{"Lcom/example/superclubg_m_vol/BuildConfig;.<init>()":["Ljava/lang/Object;.<init>()"
],}
,"Lcom/example/superclubg_m_vol/MainActivity;":{"Lcom/example/superclubg_m_vol/MainActivity;.<init>()":["Landroid/app/Activity;.<init>()"
],"Lcom/example/superclubg_m_vol/MainActivity;.initpendingintent()":[],"Lcom/example/superclubg_m_vol/MainActivity;.onCreate(Landroid/os/Bundle;)":["Landroid/app/Activity;.onCreate(Landroid/os/Bundle;)"
,"Landroid/app/Activity;.setRequestedOrientation(I)"
,"Lcom/example/superclubg_m_vol/MainActivity;.requestWindowFeature(I)"
,"Lcom/example/superclubg_m_vol/MainActivity;.getWindow()"
,"Landroid/view/Window;.setFlags(II)"
,"Lcom/example/superclubg_m_vol/Setting;.<init>(Landroid/content/Context;)"
,"Lcom/example/superclubg_m_vol/c;.<init>(Lcom/example/superclubg_m_vol/MainActivity;Lcom/example/superclubg_m_vol/Setting;)"
,"Lcom/example/superclubg_m_vol/MainActivity;.setContentView(Landroid/view/View;)"
],"Lcom/example/superclubg_m_vol/MainActivity;.onKeyDown(ILandroid/view/KeyEvent;)":["Lcom/example/superclubg_m_vol/c;.onKeyDown(ILandroid/view/KeyEvent;)"
],}
,"Lcom/example/superclubg_m_vol/R$attr;":{"Lcom/example/superclubg_m_vol/R$attr;.<init>()":["Ljava/lang/Object;.<init>()"
],
"Lcom/example/superclubg_m_vol/Setting;.<init>(Landroid/content/Context;)":["Ljava/lang/Object;.<init>()"
,"Landroid/content/Context;.getSharedPreferences(Ljava/lang/String;I)"
,"Landroid/content/SharedPreferences;.edit()"
,"Landroid/app/ProgressDialog;.<init>(Landroid/content/Context;)"
,"Landroid/content/Context;.getResources()"
,"Landroid/content/res/Resources;.getString(I)"
,"Landroid/app/ProgressDialog;.setTitle(Ljava/lang/CharSequence;)"
,"Landroid/content/Context;.getResources()"
,"Landroid/content/res/Resources;.getString(I)"
,"Landroid/app/ProgressDialog;.setMessage(Ljava/lang/CharSequence;)"
,"Landroid/app/ProgressDialog;.setIndeterminate(Z)"
]}
}

notVisitedMethods=[]



def main ():
    G = nx.Graph()
    G.add_node("root")
    for clazz in classes.keys():
        G.add_node(clazz)
        G.add_edge("root",clazz)
        if classes[clazz]:
            for method in classes[clazz].keys():
                G.add_node(method)
                G.add_edge(clazz,method)
                for inst in classes[clazz][method]:
                    G.add_node(inst)
                    G.add_edge(inst,method)
    G1 = nx.Graph()
    G1.add_node("root1")
    for clazz2 in classes2.keys():
        G1.add_node(clazz2)
        G1.add_edge("root1",clazz2)
        if classes2[clazz2]:
            for method2 in classes2[clazz2].keys():
                G1.add_node(method2)
                G1.add_edge(clazz2,method2)
                for inst2 in classes2[clazz2][method2]:
                    G1.add_node(inst2)
                    G1.add_edge(inst2,method2)


    # GM = isomorphism.GraphMatcher(G,G1)
    # print (GM.subgraph_is_isomorphic())
    nx.draw_spring(G1,prog="twopi")
    # nx.draw_spring(G,prog="twopi")
    # nx.draw_spring(G,prog="twopi")
    plt.show()


if __name__ == "__main__":
    main()