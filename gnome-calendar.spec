#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-calendar
Version  : 3.32.0
Release  : 25
URL      : https://download.gnome.org/sources/gnome-calendar/3.32/gnome-calendar-3.32.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-calendar/3.32/gnome-calendar-3.32.0.tar.xz
Summary  : Simple and beautiful calendar application designed to perfectly fit the GNOME desktop
Group    : Development/Tools
License  : GPL-3.0
Requires: gnome-calendar-bin = %{version}-%{release}
Requires: gnome-calendar-data = %{version}-%{release}
Requires: gnome-calendar-license = %{version}-%{release}
Requires: gnome-calendar-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : geoclue-dev
BuildRequires : libdazzle-dev
BuildRequires : libgweather-dev
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libecal-1.2)

%description
# GNOME Calendar
GNOME Calendar is a simple and beautiful calendar application for GNOME. We give
a lot of attention to details, and as such, design is an essential and ongoing
effort.

%package bin
Summary: bin components for the gnome-calendar package.
Group: Binaries
Requires: gnome-calendar-data = %{version}-%{release}
Requires: gnome-calendar-license = %{version}-%{release}

%description bin
bin components for the gnome-calendar package.


%package data
Summary: data components for the gnome-calendar package.
Group: Data

%description data
data components for the gnome-calendar package.


%package license
Summary: license components for the gnome-calendar package.
Group: Default

%description license
license components for the gnome-calendar package.


%package locales
Summary: locales components for the gnome-calendar package.
Group: Default

%description locales
locales components for the gnome-calendar package.


%prep
%setup -q -n gnome-calendar-3.32.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552324320
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-calendar
cp COPYING %{buildroot}/usr/share/package-licenses/gnome-calendar/COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-calendar

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-calendar

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Calendar.desktop
/usr/share/dbus-1/services/org.gnome.Calendar.service
/usr/share/glib-2.0/schemas/org.gnome.calendar.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.calendar.gschema.xml
/usr/share/gnome-shell/search-providers/org.gnome.Calendar.search-provider.ini
/usr/share/icons/hicolor/scalable/apps/org.gnome.Calendar.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Calendar-symbolic.svg
/usr/share/metainfo/org.gnome.Calendar.appdata.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-calendar/COPYING

%files locales -f gnome-calendar.lang
%defattr(-,root,root,-)

