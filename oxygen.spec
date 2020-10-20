%define major 5
%define libname %mklibname oxygenstyle%{major} %{major}
%define clibname %mklibname oxygenstyleconfig%{major} %{major}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary: The Oxygen style for KDE 5
Name: oxygen
Version:	5.20.1
Release:	1
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Source100: %{name}.rpmlintrc
Patch0: oxygen-5.5.3-use-openmandriva-icon-and-background.patch
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(xcb)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KDecoration2)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(KF5FrameworkIntegration)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5Wayland)
Requires: %{libname} = %{EVRD}
Requires: oxygen-icons >= 1:15.04.3
Requires: oxygen-sounds
# needed for backgrounds and patch 2
Requires: distro-theme-OpenMandriva

%description
The Oxygen style for KDE 5.

%package sounds
Summary: Oxygen sounds
Group: Graphical desktop/KDE
Conflicts: %{name} < 5.6.4-2

%description sounds
Oxygen sounds.

%package -n %{libname}
Summary: KDE Frameworks 5 Oxygen framework
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE Frameworks 5 Oxygen framework.

%package -n %{clibname}
Summary: KDE Frameworks 5 Oxygen configuration framework
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{clibname}
KDE Frameworks 5 Oxygen configuration framework.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# omv backgrounds
rm -rf %{buildroot}%{_datadir}/plasma/look-and-feel/org.kde.oxygen/contents/splash/images/background.png
ln -sf %{_datadir}/mdk/backgrounds/default.png %{buildroot}%{_datadir}/plasma/look-and-feel/org.kde.oxygen/contents/splash/images/background.png

# Useless, we don't have headers
rm -f %{buildroot}%{_libdir}/liboxygenstyle%{major}.so
rm -f %{buildroot}%{_libdir}/liboxygenstyleconfig%{major}.so

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %{buildroot}%{_var}/lib/rpm/filetriggers
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-plasma-oxygen.filter << EOF
^./usr/share/icons/KDE_Classic
^./usr/share/icons/Oxygen_Black
^./usr/share/icons/Oxygen_Blue
^./usr/share/icons/Oxygen_White
^./usr/share/icons/Oxygen_Yellow
^./usr/share/icons/Oxygen_Zion
EOF

cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-plasma-oxygen.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then
    for i in KDE_Classic Oxygen_Black Oxygen_Blue Oxygen_White Oxygen_Yellow Oxygen_Zion; do
	/usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/$i
    done
fi
EOF

chmod 755 %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-plasma-oxygen.script

%find_lang liboxygenstyleconfig || touch liboxygenstyleconfig.lang
%find_lang oxygen_style_config || touch oxygen_style_config.lang
%find_lang oxygen_style_demo || touch oxygen_style_demo.lang
%find_lang oxygen_kdecoration || touch oxygen_kdecoration.lang

cat *.lang >oxygen-all.lang

%files -f oxygen-all.lang
%{_bindir}/oxygen-demo5
%{_bindir}/oxygen-settings5
%{_datadir}/color-schemes/Oxygen.colors
%{_datadir}/color-schemes/OxygenCold.colors
%{_iconsdir}/KDE_Classic
%{_iconsdir}/Oxygen_Black
%{_iconsdir}/Oxygen_Blue
%{_iconsdir}/Oxygen_White
%{_iconsdir}/Oxygen_Yellow
%{_iconsdir}/Oxygen_Zion
%{_iconsdir}/hicolor/*/apps/oxygen-settings.png
%{_datadir}/kstyle/themes/oxygen.*
%{_datadir}/kservices5/*.desktop
%{_datadir}/plasma/look-and-feel/org.kde.oxygen
%{_libdir}/qt5/plugins/styles/oxygen.so
%{_libdir}/qt5/plugins/kstyle_oxygen_config.so
%{_libdir}/qt5/plugins/org.kde.kdecoration2/oxygendecoration.so
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-plasma-oxygen.*

%files sounds
%{_datadir}/sounds/Oxygen-*.ogg

%files -n %{libname}
%{_libdir}/liboxygenstyle%{major}.so.%{major}*

%files -n %{clibname}
%{_libdir}/liboxygenstyleconfig%{major}.so.%{major}*
