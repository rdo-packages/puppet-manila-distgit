%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-manila
Version:        12.5.1
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Manila
License:        ASL 2.0

URL:            https://launchpad.net/puppet-manila

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-keystone
Requires:       puppet-glance
Requires:       puppet-rabbitmq
Requires:       puppet-stdlib
Requires:       puppet-openstacklib
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Manila

%prep
%setup -q -n openstack-manila-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/manila/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/manila/



%files
%{_datadir}/openstack-puppet/modules/manila/


%changelog
* Thu Jun 20 2019 RDO <dev@lists.rdoproject.org> 12.5.1-1
- Update to 12.5.1

* Fri Jul 27 2018 RDO <dev@lists.rdoproject.org> 12.5.0-1
- Update to 12.5.0

* Thu Mar 29 2018 RDO <dev@lists.rdoproject.org> 12.4.0-1
- Update to 12.4.0

* Wed Feb 21 2018 RDO <dev@lists.rdoproject.org> 12.3.0-1
- Update to 12.3.0



