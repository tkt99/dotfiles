# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage

#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

import os
import subprocess
#from xmonad import MonadTall, MonadWide

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

mod = "mod1" # alt
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.shrink(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.grow(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.up(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.up(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    # Key([mod, "control"], "h", lazy.layout.shrink(), desc="Grow window to the left"),
    # Key([mod, "control"], "l", lazy.layout.grow(), desc="Grow window to the right"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "w", lazy.to_screen(0)),
    Key([mod], "e", lazy.to_screen(1)),
    Key([mod], "comma", lazy.layout.increase_nmaster()),
    Key([mod], "period", lazy.layout.decrease_nmaster()),
    
    # Launching applications
    Key([mod], "space", lazy.spawn("/home/_2k/.config/rofi/launchers/misc/launcher.sh"), desc="Spawn a command using a prompt widget"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch firefox"),
    Key([mod], "d", lazy.spawn("discord"), desc="Launch discord"),
    Key([mod], "s", lazy.spawn("spotify"), desc="Launch spotify"),
    Key(["mod4", "shift"], "s", lazy.spawn("flameshot gui"), desc="Launch screen capture"),
    Key([mod, "shift"], "e", lazy.spawn("alacritty -e vifm"), desc="Launch file explorer"),

    # Media
    Key([mod], "period", lazy.spawn("playerctl next"), desc="next song"),
    Key([mod], "comma", lazy.spawn("playerctl previous"), desc="previous song"),
    Key([mod], "slash", lazy.spawn("playerctl play-pause"), desc="pause spotify"),

    Key([mod], "Up", lazy.spawn("playerctl volume 0.1+"), desc="raise volume by 10%"),
    Key([mod], "Down", lazy.spawn("playerctl volume 0.1-"), desc="lower volume by 10%"),
    Key(["control"], "Up", lazy.spawn("playerctl volume 0.1+"), desc="raise volume by 10%"),
    Key(["control"], "Down", lazy.spawn("playerctl volume 0.1-"), desc="lower volume by 10%"),

    # Windows 
    Key([mod], "r", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "t", lazy.window.toggle_floating()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "f", lazy.layout.flip()),

    # Power stuff
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "b", lazy.restart(), desc="Restart"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "Delete", lazy.spawn("/home/_2k/.config/rofi/powermenu/powermenu.sh"), desc="Shutdown Qtile"),

    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),

            # # mod1 + shift + letter of group = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )


layouts = [
    # Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    # layout.Bsp(),
    #layout.Matrix(),
    #layout.Columns(),
    layout.MonadTall(
        border_focus='#6ef8fa',
        border_width=3,
        single_border_width=1,
        margin=12,
        single_margin=6,
        ),
    layout.MonadWide(
        border_focus='#6ef8fa',
        border_width=3,
        single_border_width=1,
        margin=12,
        single_margin=6,
        ),
    layout.Stack(
        border_focus='#6ef8fa',
        border_width=1,
        num_stacks=1,
        margin=6,

        ),
    #layout.Tile(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def get_rounded_background(color):
    decor = {
        "decorations": [
            RectDecoration(colour='#b195bf', radius=16, filled=True)
        ],
    }

    return decor

screens = [

    # Left screen
    Screen(
        top=bar.Bar(
            [
                # Left
                widget.Spacer(length=5),
                widget.Image(filename='/home/_2k/Pictures/cube.png', margin=3),
                widget.GroupBox(highlight_method='block', disable_drag=True, fontsize=17),
                widget.LaunchBar(progs=[('steam', 'steam', 'launch Steam')], default_icon='/home/_2k/Pictures/cube.png'),
                widget.LaunchBar(progs=[('firefox', 'firefox', 'launch firefox')], default_icon='/home/_2k/Pictures/cube.png'),
                widget.CurrentLayout(fontsize=15, fmt='| {} |'),
                widget.WindowName(fontsize=15, width=805, foreground='e7c0fa', max_chars=50),

                # Center
                widget.Clock(format="%-I:%M %p", fontsize=21, foreground='f2f794', fontshadow='000000'),
                # widget.Clock(**get_rounded_background('#b195bf'), format="%-I:%M %p", fontsize=21, foreground='000000', fontshadow='000000'),
                widget.Spacer(),
                
                # Right
                widget.Mpris2(
                    name="spotify",
                    scroll_chars=None,
                    display_metadata=["xesam:title", "xesam:artist"],
                    objname="org.mpris.MediaPlayer2.spotify",
                    foreground='45a33e',
                    padding=10,
                    mouse_callbacak = {
                        "Button1": lambda: qtile.cmd_spawn("playerctl play-pause"), 
                    }
                ),
                widget.CheckUpdates(fontsize=17, display_format='{updates} Packages', padding=10, update_interval=1800),
                widget.NvidiaSensors(fmt='{} (GPU)', fontsize=17, threshold=79, foreground_alert= 'ff6000', foreground='fcf944'),
                # widget.Clock(**get_rounded_background('#6e5170'), fontsize=17, format="%A  |  %b %d, %Y", padding=10),
                widget.Clock(fontsize=17, format="|  %A  |  %b %d, %Y", padding=10),
                widget.Spacer(length=10),
            ],
            size=35,
            background='#222e4a',
            # background='#00000000',
            # border_color=['#00000000','#00000000','#00000000','#00000000'],
            margin=[5, 5, 0, 5],
            # border_width=30,
            opacity=0.99,

        ),
        #wallpaper='~/Backgrounds/Wallpapers/4380210.jpg',
        #wallpaper_mode='stretch',

    ),

    # Right screen
    Screen(
        top=bar.Bar(
            [
                # Left 
                widget.Spacer(length=10),
                widget.Image(filename='/home/_2k/Pictures/cube.png', margin=3),
                widget.GroupBox(highlight_method='block', disable_drag=True),
                widget.LaunchBar(progs=[('steam', 'steam', 'launch Steam')], default_icon='/home/_2k/Pictures/cube.png'),
                widget.LaunchBar(progs=[('firefox', 'firefox', 'launch firefox')], default_icon='/home/_2k/Pictures/cube.png'),
                widget.CurrentLayout(fontsize=12, fmt='| {} |'),
                widget.WindowName(width=520, fontsize=12, foreground='66fa9d', max_chars=50),

                # Center 
                widget.Clock(format="%-I:%M %p", fontsize=19, foreground='f2f794'),
                widget.Spacer(),

                # Right
                widget.CheckUpdates(padding=7, display_format='{updates} Packages', update_interval=1800),
                widget.NvidiaSensors(fmt='{} (GPU)', threshold=79, foreground_alert= 'ff6000', foreground='fcf944'),
                widget.Clock(format="|  %A  |  %b %d, %Y", padding=7),
                widget.Spacer(length=10),
            ],
            size=31,
            background='#1e2738',
            margin=[10, 5, 0, 5],
            #border_width=[0, 0, 20, 0],  # Draw top and bottom borders
        ),
        #bottom=bar.Bar(
            #[
            #    widget.LaunchBar(progs=[('steam', 'steam', 'launch Steam')], default_icon='/home/_2k/Pictures/cube.png'),
            #],
            #size=20,
        #),
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
