Name: automoc4
Summary: Automoc is a development moc auto generator for kde4 development
Version: 0.9.84
Release: %mkrel 1
Url: http://websvn.kde.org/trunk/kdesupport/automoc
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
