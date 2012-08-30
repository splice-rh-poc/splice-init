Name:       splice-init
Version:    0.3
Release:    1%{?dist}
Summary:    Initialize a cloud instance for Splice.

Group:      Development/Languages
License:    GPLv2+
URL:        https://github.com/splice/splice-init
Source0:    %{name}-%{version}.tar.gz

Requires:   m2crypto


%description
Initialize a cloud instance for Splice.


%prep
%setup -q


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_initddir}
cp usr/bin/splice-init %{buildroot}/%{_bindir}/
cp etc/init.d/splice-init %{buildroot}/%{_initddir}/


%files
%defattr(-,root,root,-)
%{_bindir}/splice-init
%{_initddir}/splice-init


%changelog
* Thu Aug 30 2012 James Slagle <jslagle@redhat.com> 0.3-1
- Replace REGION string in rhsm conf file (jslagle@redhat.com)
- Basic init script output (jslagle@redhat.com)
- Create needed dir (jslagle@redhat.com)
- Add init script (jslagle@redhat.com)
- Improved error handling (jslagle@redhat.com)
- read and write the rhic (jslagle@redhat.com)
- Remove configure (jslagle@redhat.com)

* Wed Aug 29 2012 James Slagle <jslagle@redhat.com> 0.2-1
- new package built with tito


