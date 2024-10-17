Name: automoc4
Summary: Automoc is a development moc auto generator for kde4 development
Version: 0.9.88
Release: 15
Url: https://websvn.kde.org/trunk/kdesupport/automoc
License: GPLv2+
Group: Development/KDE and Qt
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Source0: %{name}-%{version}.tar.bz2
BuildRequires: qt4-devel >= 4.4.0
BuildRequires: kde4-macros
Obsoletes: automoc < 0.9.83
Provides: automoc = %version

%description
Automoc is a development moc auto generator for kde4 development

%files
%defattr(-,root,root)
%{_kde_bindir}/automoc4
%{_kde_libdir}/automoc4

#------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%clean
rm -rf "%{buildroot}"


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.88-4mdv2011.0
+ Revision: 662901
- mass rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.88-3mdv2011.0
+ Revision: 522112
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.88-2mdv2010.0
+ Revision: 413150
- rebuild

* Thu Jan 22 2009 Helio Chissini de Castro <helio@mandriva.com> 0.9.88-1mdv2009.1
+ Revision: 332634
- New upstream release tied to KDE 4.2.0 release

* Mon Aug 18 2008 Helio Chissini de Castro <helio@mandriva.com> 0.9.87-1mdv2009.0
+ Revision: 273255
- Update automoc with current fixes.

* Thu Jul 24 2008 Helio Chissini de Castro <helio@mandriva.com> 0.9.84-1mdv2009.0
+ Revision: 246155
- New upstream release 4.0.84

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Use correct name
    - Use correct name

* Fri Jun 20 2008 Helio Chissini de Castro <helio@mandriva.com> 0.9.83-1mdv2009.0
+ Revision: 227559
- New upstream release from kdesupport
- Moving to right package name

* Thu May 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.0-0.805344.2mdv2009.0
+ Revision: 204488
- Add patch0 to fix lib install
- import automoc

