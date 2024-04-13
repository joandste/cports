pkgname = "labwc"
pkgver = "0.7.1"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "cairo-devel",
    "libxml2-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.17-devel",
]
pkgdesc = "Wayland window-stacking compositor"
maintainer = "joandste <joandste@abo.fi>"
license = "GPL-2.0-or-later"
url = "https://labwc.github.io"
source = f"https://github.com/labwc/labwc/archive/{pkgver}.tar.gz"
sha256 = "1810ec55e287708e7a3cd44c726aa887db02480704db82b3d0bd550a6c4bfb76"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE")
