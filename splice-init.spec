Name:       splice-init
Version:	0.1
Release:	1%{?dist}
Summary:	Initialize a cloud instance for Splice.

Group:		Development/Languages
License:	GPLv2+
URL:		https://github.com/splice/splice-init
Source0:	%{name}-%{version}.tar.gz


BuildRequires:	
Requires:	

%description
Initialize a cloud instance for Splice.


%prep
%setup -q


%build
%configure

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
cp  usr/bin/splice-init %{buildroot}/%{_bindir}/


%files
%defattr(-,root,root,-)
%{_bindir}/splice-init


%changelog

