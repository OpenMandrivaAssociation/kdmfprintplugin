%define     oname KDMFprintPlugin
%define     svn_snapshot 1050414

Summary:	Fingerprint support for KDM
Name:		kdmfprintplugin
Version:	0.0
Release:	0.%{svn_snapshot}.6
License:	GPLv2+
Group:		System/Configuration/Packaging
URL:		http://websvn.kde.org/trunk/playground/base/kfingerprint/KDMFprintPlugin/
Source0:	%{oname}-%{version}.%{svn_snapshot}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel
Requires:	kfingermanager
Requires:	pam_fprint
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
%setup -q -n %{oname}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0-0.1050414.5mdv2011.0
+ Revision: 666021
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0-0.1050414.4mdv2011.0
+ Revision: 606261
- rebuild

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - We need fprint stuffs too

* Sun Dec 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.0-0.1050414.2mdv2010.1
+ Revision: 482602
- Requires kfingermanager needed to create the fingerprints

* Tue Nov 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.0-0.1050414.1mdv2010.1
+ Revision: 466921
- import kdmfprintplugin

