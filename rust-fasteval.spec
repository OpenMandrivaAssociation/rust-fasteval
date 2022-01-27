%bcond_with check
%global debug_package %{nil}

%global crate fasteval

Name:           rust-%{crate}
Version:        0.2.4
Release:        1
Summary:        Fast evaluation of algebraic expressions

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/fasteval
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fast evaluation of algebraic expressions.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(fasteval) = 0.2.4
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc examples README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(fasteval/default) = 0.2.4
Requires:       cargo
Requires:       crate(fasteval) = 0.2.4
Requires:       crate(fasteval/alpha-keywords) = 0.2.4

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+alpha-keywords-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(fasteval/alpha-keywords) = 0.2.4
Requires:       cargo
Requires:       crate(fasteval) = 0.2.4

%description -n %{name}+alpha-keywords-devel %{_description}

This package contains library source intended for building other packages
which use "alpha-keywords" feature of "%{crate}" crate.

%files       -n %{name}+alpha-keywords-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(fasteval/nightly) = 0.2.4
Requires:       cargo
Requires:       crate(fasteval) = 0.2.4

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unsafe-vars-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(fasteval/unsafe-vars) = 0.2.4
Requires:       cargo
Requires:       crate(fasteval) = 0.2.4

%description -n %{name}+unsafe-vars-devel %{_description}

This package contains library source intended for building other packages
which use "unsafe-vars" feature of "%{crate}" crate.

%files       -n %{name}+unsafe-vars-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
