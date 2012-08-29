Name:       splice-init
Version:    0.2
Release:    1%{?dist}
Summary:    Initialize a cloud instance for Splice.

Group:      Development/Languages
License:    GPLv2+
URL:        https://github.com/splice/splice-init
Source0:    %{name}-%{version}.tar.gz


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
* Wed Aug 29 2012 James Slagle <jslagle@redhat.com> 0.2-1
- new package built with tito

