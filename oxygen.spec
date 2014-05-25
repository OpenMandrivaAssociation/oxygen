%define major 5
%define libname %mklibname oxygenstyle%{major} %{major}
%define clibname %mklibname oxygenstyleconfig%{major} %{major}
%define debug_package %{nil}

Name: oxygen
Version: 4.96.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
Source100: %{name}.rpmlintrc
Summary: The Oxygen style for KDE 5
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(XCB)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5)
BuildRequires: cmake(KDecorations)
BuildRequires: cmake(XCB)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(KF5FrameworkIntegration)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
The Oxygen style for KDE 5

%package -n %{libname}
Summary: KDE Frameworks 5 Oxygen framework
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE Frameworks 5 Oxygen framework

%package -n %{clibname}
Summary: KDE Frameworks 5 Oxygen configuration framework
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{clibname}
KDE Frameworks 5 Oxygen configuration framework

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files
%{_bindir}/oxygen-demo5
%{_bindir}/oxygen-settings5
%{_bindir}/oxygen-shadow-demo5
%{_datadir}/sounds/Oxygen*
%{_datadir}/icons/KDE_Classic
%{_datadir}/icons/Oxygen_Black
%{_datadir}/icons/Oxygen_Blue
%{_datadir}/icons/Oxygen_White
%{_datadir}/icons/Oxygen_Yellow
%{_datadir}/icons/Oxygen_Zion
%{_datadir}/kstyle/themes/oxygen.*
%{_libdir}/plugins/styles/oxygen.so
%{_libdir}/plugins/kstyle_oxygen_config.so
%{_libdir}/plugins/kwin/kdecorations/config/kwin_oxygen_config.so
%{_libdir}/plugins/kwin/kdecorations/kwin3_oxygen.so

%files -n %{libname}
%{_libdir}/liboxygenstyle%{major}.so.%{major}*
%{_libdir}/liboxygenstyle%{major}.so

%files -n %{clibname}
%{_libdir}/liboxygenstyleconfig%{major}.so.%{major}*
%{_libdir}/liboxygenstyleconfig%{major}.so
