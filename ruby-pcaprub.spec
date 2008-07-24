Summary:	PcapRub provides raw libpcap bindings for Ruby
Name:		ruby-pcaprub
Version:	0.6
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/14567/pcaprub-%{version}.tar.gz
# Source0-md5:	8abad6bb909dff279d5acf2ca39e28eb
URL:		http://rubyforge.org/projects/pcaprub/
BuildRequires:	pcap-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PcapRub provides raw libpcap bindings for Ruby.

%prep
%setup -q -n pcaprub
mkdir -p ext/pcaprub
mv extconf.rb pcaprub.c ext/pcaprub
touch ext/pcaprub/MANIFEST

%build
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README
%attr(755,root,root) %{ruby_archdir}/pcaprub.so
