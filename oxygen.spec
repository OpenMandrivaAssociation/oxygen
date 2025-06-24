%bcond_without qt5

%define major 6
%define oldlibname %mklibname oxygenstyle5 5
%define oldclibname %mklibname oxygenstyleconfig5 5
%define lib5name %mklibname oxygenstyle5 %{major}
%define clib5name %mklibname oxygenstyleconfig5 %{major}
%define libname %mklibname oxygenstyle%{major} %{major}
%define clibname %mklibname oxygenstyleconfig%{major} %{major}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	The Oxygen style for KDE 6
Name:		oxygen
Version:	6.4.1
Release:	%{?git:0.%{git}.}1
URL:		https://kde.org/
License:	GPL
Group:		Graphical desktop/KDE
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/oxygen/-/archive/%{gitbranch}/oxygen-%{gitbranchd}.tar.bz2#/oxygen-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%{plasmaver}/oxygen-%{version}.tar.xz
%endif
Patch0:		oxygen-5.5.3-use-openmandriva-icon-and-background.patch
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KDecoration3)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(KF6FrameworkIntegration)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(Wayland) >= 5.90.0
BuildRequires:	cmake(Plasma) >= 5.90.0
BuildRequires:	cmake(PlasmaQuick) >= 5.90.0
%if %{with qt5}
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5FrameworkIntegration)
BuildRequires:	cmake(KF5WindowSystem)
%endif
Requires:	%{libname} = %{EVRD}
Requires:	kf6-oxygen-icons
Recommends:	plasma6-oxygen-sounds
# needed for backgrounds and patch 2
Requires:	distro-theme-OpenMandriva
%if %{with qt5}
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
%endif
BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=true
# Renamed after 6.0 2025-05-03
%rename plasma6-oxygen

%description
The Oxygen style for KDE 6.

%package -n %{lib5name}
Summary: KDE Frameworks 5 Oxygen framework
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{lib5name}
KDE Frameworks 5 Oxygen framework.

%package -n %{clib5name}
Summary: KDE Frameworks 5 Oxygen configuration framework
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{clib5name}
KDE Frameworks 5 Oxygen configuration framework.

%package -n %{libname}
Summary: KDE Frameworks 6 Oxygen framework
Group: System/Libraries
Requires: %{name} = %{EVRD}
%rename %{oldlibname}

%description -n %{libname}
KDE Frameworks 6 Oxygen framework.

%package -n %{clibname}
Summary: KDE Frameworks 6 Oxygen configuration framework
Group: System/Libraries
Requires: %{name} = %{EVRD}
%rename %{oldclibname}

%description -n %{clibname}
KDE Frameworks 6 Oxygen configuration framework.

%package qt5
Summary: Qt 5.x support for the Plasma 6.x Oxygen style
Requires: %{name} = %{EVRD}
# Renamed after 6.0 2025-05-03
%rename plasma6-oxygen-qt5

%description qt5
Qt 5.x support for the Plasma 6.x Oxygen style

%install -a
# omv backgrounds
rm -rf %{buildroot}%{_datadir}/plasma/look-and-feel/org.kde.oxygen/contents/splash/images/background.png
ln -sf %{_datadir}/mdk/backgrounds/default.png %{buildroot}%{_datadir}/plasma/look-and-feel/org.kde.oxygen/contents/splash/images/background.png

# Useless, we don't have headers
rm -f %{buildroot}%{_libdir}/liboxygenstyle%{major}.so
rm -f %{buildroot}%{_libdir}/liboxygenstyleconfig%{major}.so

%files -f %{name}.lang
%{_bindir}/oxygen-demo6
%{_libdir}/liboxygenstyle6.so.6*
%{_libdir}/liboxygenstyleconfig6.so.6*
%{_bindir}/oxygen-settings6
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
%{_datadir}/plasma/look-and-feel/org.kde.oxygen
%{_qtdir}/plugins/styles/oxygen6.so
%{_qtdir}/plugins/org.kde.kdecoration3/org.kde.oxygen.so
%{_qtdir}/plugins/kstyle_config/kstyle_oxygen_config.so
%{_qtdir}/plugins/org.kde.kdecoration3.kcm/kcm_oxygendecoration.so
%{_datadir}/applications/kcm_oxygendecoration.desktop
%{_datadir}/metainfo/org.kde.oxygen.appdata.xml
%{_datadir}/plasma/desktoptheme/oxygen

%files qt5
%{_bindir}/oxygen-demo5
%{_libdir}/qt5/plugins/styles/oxygen5.so

%files -n %{lib5name}
%{_libdir}/liboxygenstyle5.so.%{major}*

%files -n %{clib5name}
%{_libdir}/liboxygenstyleconfig5.so.%{major}*

%files -n %{libname}
%{_libdir}/liboxygenstyle%{major}.so.%{major}*

%files -n %{clibname}
%{_libdir}/liboxygenstyleconfig%{major}.so.%{major}*
