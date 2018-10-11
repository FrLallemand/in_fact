import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from random import randint

ICONS = ['face-sick','face-smile', 'face-surprise', 'face-uncertain', 'face-wink', 'face-monkey', 'face-laugh', 'face-devilish', 'face-plain', 'face-raspberry','face-smile-big', 'face-smirk', 'face-wink', 'face-embarrassed', 'face-kiss', 'emblem-favorite']

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="In Fact")

        self.button = Gtk.Button(label="One more time !")
        self.button.connect("clicked", self.on_button_clicked)
        self.box = Gtk.Box()
        self.add(self.box)
        self.in_fact = 0
        self.box.pack_start(self.button, True, True, 0)

        self.label = Gtk.Label("In fact : " + str(self.in_fact))
        self.box.pack_start(self.label, True, True, 0)

        self.icons_box = Gtk.VBox()
        self.trophy_box = Gtk.HBox()


        self.icons_box.pack_start(self.trophy_box, True, True, 0)
        self.box.pack_start(self.icons_box, True, True, 0)


        #self.pixbuf = Gtk.IconTheme.get_default().load_icon(ICONS[randint(0, len(ICONS))], 64, 0)
        self.pixbuf = Gtk.Image.new_from_icon_name(ICONS[randint(0, len(ICONS))], Gtk.IconSize.DIALOG)

        self.icons_box.pack_start(self.pixbuf, True, True, 0)

    def on_button_clicked(self, widget):
        self.in_fact = self.in_fact +1
        if self.in_fact % 25 == 0:
            self.change_icon()

        if self.in_fact == 5:
            self.add_icon_trophy_gold()

        if self.in_fact == 3:
            self.add_icon_trophy_silver()

        if self.in_fact == 1:
            self.add_icon_trophy_bronze()

        self.label.set_text("In fact : " + str(self.in_fact))

    def change_icon(self, icon=None):
        self.icons_box.remove(self.pixbuf)
        if icon is None:
            self.pixbuf = Gtk.Image.new_from_icon_name(ICONS[randint(0, len(ICONS)-1)], Gtk.IconSize.DIALOG)
        else:
            self.pixbuf = Gtk.Image.new_from_icon_name(icon, Gtk.IconSize.DIALOG)

        self.icons_box.pack_start(self.pixbuf, True, True, 0)

        self.pixbuf.set_visible(True)

    def add_trophy(self, icon=None):
        trophy = Gtk.Image.new_from_icon_name(icon, Gtk.IconSize.MENU)
        trophy.set_visible(True)
        self.trophy_box.pack_start(trophy, True, True, 0)

    def add_icon_trophy_gold(self):
        self.add_trophy('trophy-gold')

    def add_icon_trophy_silver(self):
        self.add_trophy('trophy-silver')

    def add_icon_trophy_bronze(self):
        self.add_trophy('trophy-bronze')


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
