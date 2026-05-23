%bcond clang 1

# TDE variables
%define tde_pkg kopete-otr
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	Off-The-Record encryption for Kopete [Trinity]
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/internet/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DKOPETE_INCLUDE_DIR=%{tde_prefix}/include/tde/kopete
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DBUILD_ALL=ON -DWITH_ALL_OPTIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tdenetwork-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils

# Kopete is provided by tdenetwork
Requires:		trinity-kopete >= %{version}


%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

# OTR support
BuildRequires:  pkgconfig(libotr)

BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

%description
This plugin enables Off-The-Record encryption for the TDE instant
messenger Kopete. Using this plugin you can encrypt chatsessions to other
users with IM-Cients supporting the OTR encryption method.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"


%install -a
# Unwanted files
%__rm -f %{?buildroot}%{tde_prefix}/%{_lib}/libkotr.so

%find_lang kopete_otr


%files -f kopete_otr.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.md
%{tde_prefix}/%{_lib}/libkotr.la
%{tde_prefix}/%{_lib}/libkotr.so.0
%{tde_prefix}/%{_lib}/libkotr.so.0.0.0
%{tde_prefix}/%{_lib}/trinity/kcm_kopete_otr.la
%{tde_prefix}/%{_lib}/trinity/kcm_kopete_otr.so
%{tde_prefix}/%{_lib}/trinity/kopete_otr.la
%{tde_prefix}/%{_lib}/trinity/kopete_otr.so
%{tde_prefix}/share/apps/kopete_otr
%{tde_prefix}/share/config.kcfg/kopete_otr.kcfg
%{tde_prefix}/share/doc/tde/HTML/en/kopete_otr/
%{tde_prefix}/share/icons/crystalsvg/16x16/apps/kopete_otr.png
%{tde_prefix}/share/services/tdeconfiguredialog/kopete_otr_config.desktop
%{tde_prefix}/share/services/kopete_otr.desktop

