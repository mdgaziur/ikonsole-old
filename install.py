#! /usr/bin/python3.5

import gi,os,time
from ic import *
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class InstallWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="iKonsole Installer")

        vbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        self.add(vbox)

        self.label=Gtk.Label("iKonsole Installer")
        vbox.pack_start(self.label,True,True,0)

        hbox=Gtk.Box(spacing=10)
        vbox.pack_start(hbox,True,True,0)

        button1=Gtk.Button("Install")
        button1.connect("clicked",self.on_install_clicked)
        hbox.pack_start(button1,True,True,0)


        button2=Gtk.Button("Uninstall")
        button2.connect("clicked",self.on_uninstall_clicked)
        hbox.pack_start(button2,True,True,0)

        button3=Gtk.Button("Exit")
        button3.connect("clicked",Gtk.main_quit)
        hbox.pack_start(button3,True,True,0)

    def on_install_clicked(self,widget):
        s=install()
        if s==7:
                self.label.set_text('Installed Successfully!')
        elif s<7 and s>0:
                self.label.set_text('Warning! Some packages cannot be installed!')
        else:
                self.label.set_text('Fatal error! Cannot install iKonsole!')

    def on_uninstall_clicked(self,widget):
        print("Uninstalling iKonsole...")
        os.system("rm -r /usr/bin/lib-ikonsole && rm -r /usr/bin/ikonsole && rm -r /usr/bin/encrypt && rm -r /usr/bin/strpal")
        print("Successfully Uninstalled!")
        self.label.set_text("Successfully Uninstalled!")
if os.popen("id -u").read()=="0" or os.popen("id -u").read()=="0\n":
    win=InstallWindow()
    win.connect("destroy",Gtk.main_quit)
    win.show_all()
    Gtk.main()
else:
    print("Run as root!")
