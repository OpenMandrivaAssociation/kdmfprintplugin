%define     oname KDMFprintPlugin
%define     svn_snapshot 1050414

Summary:	Fingerprint support for KDM
Name:	  	kdmfprintplugin
Version:	0.0
Release:	%mkrel 0.%svn_snapshot.1
License:	GPLv2+
Group:		System/Configuration/Packaging
Source0: 	%oname-%version.%svn_snapshot.tar.bz2
URL:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/kde4-migrate-wizard/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdelibs4-devel
BuildRequires:  kdebase4-workspace-devel
%description
Fingerprint support for KDM

%files -f %name.lang
%defattr(-,root,root)
%_sysconfdir/pam.d/kdm-fprintd
%_sysconfdir/pam.d/kscreensaver-fprintd
%_sysconfdir/pam.d/system-auth-fprintd
%_kde_libdir/kde4/kgreet_fprintd.so
%_kde_appsdir/kgreet_fprintd/pics/swipe.gif

#--------------------------------------------------------------------

%prep
%setup -q -n %oname

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT
