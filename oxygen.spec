%define major 5
%define libname %mklibname oxygenstyle%{major} %{major}
%define clibname %mklibname oxygenstyleconfig%{major} %{major}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: oxygen
Version: 5.3.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Source100: %{name}.rpmlintrc
Summary: The Oxygen style for KDE 5
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
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
Requires: %{libname} = %{EVRD}

%description
The Oxygen style for KDE 5.

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
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# Useless, we don't have headers
rm -f %{buildroot}%{_libdir}/liboxygenstyle%{major}.so
rm -f %{buildroot}%{_libdir}/liboxygenstyleconfig%{major}.so

%find_lang liboxygenstyleconfig
%find_lang oxygen_kwin_deco
%find_lang oxygen_style_config
%find_lang oxygen_style_demo

cat *.lang >oxygen-all.lang

%files -f oxygen-all.lang
%{_bindir}/oxygen-demo5
%{_bindir}/oxygen-settings5
%{_datadir}/sounds/Oxygen*
%{_datadir}/icons/KDE_Classic
%{_datadir}/icons/Oxygen_Black
%{_datadir}/icons/Oxygen_Blue
%{_datadir}/icons/Oxygen_White
%{_datadir}/icons/Oxygen_Yellow
%{_datadir}/icons/Oxygen_Zion
%{_datadir}/kstyle/themes/oxygen.*
%{_datadir}/plasma/look-and-feel/org.kde.oxygen
%{_libdir}/qt5/plugins/styles/oxygen.so
%{_libdir}/qt5/plugins/kstyle_oxygen_config.so

%files -n %{libname}
%{_libdir}/liboxygenstyle%{major}.so.%{major}*

%files -n %{clibname}
%{_libdir}/liboxygenstyleconfig%{major}.so.%{major}*
