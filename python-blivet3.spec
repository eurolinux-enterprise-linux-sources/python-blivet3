%define is_rhel 0%{?rhel} != 0

# python3 is not available on RHEL <=7
%if %{is_rhel} && 0%{?rhel} <= 7
# disable python3 by default
%bcond_with python3
%else
%bcond_without python3
%endif

# python2 is not available on RHEL > 7 and not needed on Fedora > 28
%if 0%{?rhel} > 7 || 0%{?fedora} > 28
# disable python2 by default
%bcond_with python2
%else
%bcond_without python2
%endif

Summary:  A python module for system storage configuration
Name: python-blivet3
Url: https://storageapis.wordpress.com/projects/blivet
Version: 3.1.3

#%%global prerelease .b2
# prerelease, if defined, should be something like .a1, .b1, .b2.dev1, or .c2
Release: 3%{?prerelease}%{?dist}
Epoch: 1
License: LGPLv2+
Group: System Environment/Libraries
%global realname blivet3
%global realversion %{version}%{?prerelease}
Source0: http://github.com/storaged-project/blivet/archive/blivet-%{realversion}.tar.gz
Patch0: 0001-Move-blivet-module-package-to-blivet3.patch
Patch1: 0002-Adjust-rpm-spec-file-to-new-blivet3-name.patch
Patch2: 0003-Rename-rpm-spec-file-according-to-new-name.patch
Patch3: 0004-Adjust-Makefile-et-al-to-renamed-package.patch
Patch4: 0005-Adjust-translation-domain-to-match-new-package-name.patch
Patch5: 0006-Update-logging-facility-to-match-new-package-name.patch
Patch6: 0007-Regenerate-translations.patch
Patch7: 0008-Remove-Obsoletes-for-compat-package.patch
Patch8: 0009-Dont-require-python3-for-the-dbus-service.patch
Patch9: 0010-Handle-older-pyudev-w-o-Device.properties.patch
Patch10: 0011-Adapt-to-older-pyudev-API-for-instantiating-Device.patch
Patch11: 0012-Adapt-device-tags-to-absence-of-enum-in-python2.patch
Patch12: 0013-Update-factory-example-to-work-w-latest-API.patch
Patch13: 0014-Fix-bare-blivet-imports-in-the-examples.patch


# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).
%global partedver 1.8.1
%global pypartedver 3.9
%global utillinuxver 2.15.1
%global libblockdevver 2.17
%global libbytesizever 0.3
%global pyudevver 0.15

BuildArch: noarch

%description
The python-blivet package is a python module for examining and modifying
storage configuration.

%package -n %{realname}-data
Summary: Data for the %{realname} python module.

BuildRequires: systemd

%description -n %{realname}-data
The %{realname}-data package provides data files required by the %{realname}
python module.

%if %{with python3}
%package -n python3-%{realname}
Summary: A python3 package for examining and modifying storage configuration.

%{?python_provide:%python_provide python3-%{realname}}

BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: python3
Requires: python3-six
Requires: python3-pyudev >= %{pyudevver}
Requires: parted >= %{partedver}
Requires: python3-pyparted >= %{pypartedver}
Requires: libselinux-python3
Requires: python3-blockdev >= %{libblockdevver}
%if 0%{?rhel} > 7 || 0%{?fedora}
Recommends: libblockdev-btrfs >= %{libblockdevver}
Recommends: libblockdev-crypto >= %{libblockdevver}
Recommends: libblockdev-dm >= %{libblockdevver}
Recommends: libblockdev-kbd >= %{libblockdevver}
Recommends: libblockdev-loop >= %{libblockdevver}
Recommends: libblockdev-lvm >= %{libblockdevver}
Recommends: libblockdev-mdraid >= %{libblockdevver}
Recommends: libblockdev-mpath >= %{libblockdevver}
Recommends: libblockdev-nvdimm >= %{libblockdevver}
Recommends: libblockdev-swap >= %{libblockdevver}
Recommends: libblockdev-s390 >= %{libblockdevver}
%endif
Requires: python3-bytesize >= %{libbytesizever}
Requires: util-linux >= %{utillinuxver}
Requires: lsof
Requires: python3-gobject-base
Requires: systemd-udev
Requires: %{realname}-data = %{epoch}:%{version}-%{release}

%description -n python3-%{realname}
The python3-%{realname} is a python3 package for examining and modifying storage
configuration.
%endif

%if %{with python2}
%package -n python2-%{realname}
Summary: A python2 package for examining and modifying storage configuration.

%{?python_provide:%python_provide python2-%{realname}}

BuildRequires: gettext
BuildRequires: python2-devel
BuildRequires: python2-setuptools

Requires: python2
Requires: python-six
Requires: python-pyudev >= %{pyudevver}
Requires: parted >= %{partedver}
# XXX pyparted can mean both python2 and python3
Requires: pyparted >= %{pypartedver}
Requires: libselinux-python
Requires: python2-blockdev >= %{libblockdevver}
%if 0%{?rhel} > 7 || 0%{?fedora}
Recommends: libblockdev-btrfs >= %{libblockdevver}
Recommends: libblockdev-crypto >= %{libblockdevver}
Recommends: libblockdev-dm >= %{libblockdevver}
Recommends: libblockdev-fs >= %{libblockdevver}
Recommends: libblockdev-kbd >= %{libblockdevver}
Recommends: libblockdev-loop >= %{libblockdevver}
Recommends: libblockdev-lvm >= %{libblockdevver}
Recommends: libblockdev-mdraid >= %{libblockdevver}
Recommends: libblockdev-mpath >= %{libblockdevver}
Recommends: libblockdev-nvdimm >= %{libblockdevver}
Recommends: libblockdev-part >= %{libblockdevver}
Recommends: libblockdev-swap >= %{libblockdevver}
Recommends: libblockdev-s390 >= %{libblockdevver}
%endif
Requires: python2-bytesize >= %{libbytesizever}
Requires: util-linux >= %{utillinuxver}
Requires: lsof
Requires: python2-hawkey
Requires: %{realname}-data = %{epoch}:%{version}-%{release}

Requires: udev
Requires: python-gobject-base

%description -n python2-%{realname}
The python2-%{realname} is a python2 package for examining and modifying storage
configuration.
%endif

%prep
%autosetup -n blivet-%{realversion} -p1

%build
%{?with_python2:make PYTHON=%{__python2}}
%{?with_python3:make PYTHON=%{__python3}}

%install
%{?with_python2:make PYTHON=%{__python2} DESTDIR=%{buildroot} install}
%{?with_python3:make PYTHON=%{__python3} DESTDIR=%{buildroot} install}

%find_lang %{realname}

%files -n %{realname}-data -f %{realname}.lang
%{_sysconfdir}/dbus-1/system.d/*
%{_datadir}/dbus-1/system-services/*
%{_libexecdir}/*
%{_unitdir}/*

%if %{with python2}
%files -n python2-%{realname}
%license COPYING
%doc README ChangeLog examples
%{python2_sitelib}/*
%endif

%if %{with python3}
%files -n python3-%{realname}
%license COPYING
%doc README ChangeLog examples
%{python3_sitelib}/*
%endif

%changelog
* Fri Mar 29 2019 David Lehman <dlehman@redhat.com> - 3.1.3-3
- spec file requires fixes from pcahyna
- adjust to older pyudev API
- adjust tags implementation to absence of enum in python-2.7
- fix bare imports in example scripts
- update factory example to match latest API

* Mon Mar 25 2019 Pavel Cahyna <pcahyna@redhat.com> - 3.1.3-2
- Initial import of python-blivet3 by David Lehman <dlehman@redhat.com>
  derived from python-blivet-3.1.2-1
- clear the old python-blivet %%changelog except the most recent entry.

* Wed Feb 27 2019 Vojtech Trefny <vtrefny@redhat.com> - 3.1.3-1
- Don't crash if blockdev mpath plugin isn't available. (#1672971) (dlehman)
- iscsi: Add default value to unused 'storage' argument in 'write' (vtrefny)
- Add exported property to LVMVolumeGroupDevice (vtrefny)
- Add VG data to static_data (vtrefny)
- Do not try to get format free space for non-existing formats (vtrefny)
- Do not raise exception if can't get PV free space (vtrefny)
- Fix undefined attribute in LVM info cache (vtrefny)
- Use raw_device to get thinpool device in LVMThinPFactory (#1490174) (vtrefny)
- Do not crash if DM RAID activation fails (#1661712) (vtrefny)
- Remove the unused sysroot property (vponcova)
- Remove unused attributes from the Blivet class (vponcova)
- Remove the unused gpt flag (vponcova)
- Copy the iSCSI initiator name file to the installed system (vtrefny)
- Use udev to determine if disk is a multipath member. (dlehman)
- Require libfc instead of fcoe for offloaded FCoE. (#1575953) (dlehman)
