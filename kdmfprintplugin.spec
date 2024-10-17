%define     oname KDMFprintPlugin
%define     svn_snapshot 1050414

Summary:	Fingerprint support for KDM
Name:		kdmfprintplugin
Version:	0.0
Release:	0.%{svn_snapshot}.8
License:	GPLv2+
Group:		System/Configuration/Packaging
Url:		https://websvn.kde.org/trunk/playground/base/kfingerprint/KDMFprintPlugin/
Source0:	%{oname}-%{version}.%{svn_snapshot}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel
Requires:	kfingermanager
Requires:	fprintd-pam
# Unlikely really needed, must be re-checked
Requires:	libfprint

%description
Fingerprint support for KDM.

%files
%{_sysconfdir}/pam.d/kdm-fprintd
%{_sysconfdir}/pam.d/kscreensaver-fprintd
%{_sysconfdir}/pam.d/system-auth-fprintd
%{_kde_libdir}/kde4/kgreet_fprintd.so
%{_kde_appsdir}/kgreet_fprintd/pics/swipe.gif

#--------------------------------------------------------------------

%prep
%setup -qn %{oname}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

