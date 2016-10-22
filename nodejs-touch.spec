%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name touch

# Tests disabled due to dependencies not in brew yet
%global enable_tests 0

Summary:       like touch in node
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       1.0.0
Release:       5%{?dist}
License:       ISC
URL:           https://github.com/isaacs/node-touch
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%if 0%{?enable_tests}
BuildRequires: %{?scl_prefix}nodejs(tap)
%endif

%description
For all your node touching needs.

%prep
%setup -q -n package
%nodejs_fixdep nopt

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr bin package.json touch.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/touch.js %{buildroot}%{_bindir}/touch.js

%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
tap test/*.js
%endif

%files
%doc README.md
%doc LICENSE
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/touch.js

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-5
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-4
- Rebuilt with updated metapackage

* Wed Jan 06 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-3
- Enable scl macros

* Thu Dec 17 2015 Troy Dawson <tdawson@redhat.com> - 1.0.0-2
- Fix dependencies

* Mon Dec 14 2015 Troy Dawson <tdawson@redhat.com> - 1.0.0-1
- Initial package