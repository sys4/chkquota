Name:		chkquota
Version:	1.0.0
Release:	1%{?dist}
Summary:	A Postfix policy server that checks another SMTP server for a recipients quota

Group:		System Environment/Daemons
License:	GPLv2+
URL:		https://sys4.de
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

Requires:	python
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig

%description
chkquota is a RFC 1870 quota check policy service. Contacted by a Postfix
check_policy_service client it will contact a remote SMTP or LMTP server. It
will specify the recipient and the current messages size to find out if the
server would accept the message for that particular recipient. Depending on the
outcome it will tell the check_policy_service client to accept or reject the
message.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_sbindir}/
cp -p usr/sbin/chkquota %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_initrddir}/
cp -p etc/rc.d/init.d/chkquota %{buildroot}%{_initrddir}/
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p usr/share/man/man1/chkquota.1 %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
cp -p etc/sysconfig/chkquota %{buildroot}%{_sysconfdir}/sysconfig/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/sbin/chkquota
/etc/rc.d/init.d/chkquota
/usr/share/man/man1/chkquota.1.gz
/etc/sysconfig/chkquota
%doc

%post
/sbin/chkconfig --add chkquota

%preun                                                                                                                                                 
if [ "$1" = 0 ]; then
    # stop chkquota silently, but only if it's running
    /sbin/service chkquota stop &>/dev/null
    /sbin/chkconfig --del chkquota
fi

exit 0


%changelog
* Sun Aug 03 2014 Patrick Ben Koetter <p@sys4.de> 1.0.0
- created RPM package

