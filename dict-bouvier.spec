Summary:	John Bouvier's Law Dictionary dated 1856 for the USA in the DICTD format
Summary(pl.UTF-8):	Słownik prawa USA Johna Bouviera z 1856 roku w formacie DICTD
Name:		dict-bouvier
Version:	6
Release:	4
License:	GPL
# it was downloaded from http://www.constitution.org/bouv/bouvier.htm
# Upstream Author(s): John Bouvier, 1856.
# Copyright claims to this work have expired; it is now public domain.
# so it's compatible w/ Gnu GPL ???
Group:		Applications/Dictionaries
Source0:	%{name}_%{version}.tar.gz
# Source0-md5:	1c03c5338e6fb5223b0ce341d0ca38ac
Patch0:		%{name}_%{version}.revised-1.diff
# from debian
URL:		http://www.constitution.org/bouv/bouvier.htm
BuildRequires:	dictzip
BuildRequires:	python
BuildRequires:	python-dictlib
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	%{_sysconfdir}/dictd
Requires:	dictd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the 1856 Revised Sixth Edition of John Bouvier's law
dictionary, formatted for use with the dictd server. It is an
excellent, if dated, way to look up information about legal words and
principles.

%description -l pl.UTF-8
Jest to szóste wydanie słownika prawa amerykańskiego z 1856 roku,
autorstwa Johna Bouviera. Jest wspaniałym źródłem informacji o prawie
z tamtych czasów.

%prep
%setup -n %{name}-%{version}.revised.orig -q
%patch0 -p1

%build
python conv.py *.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd/,%{_sysconfdir}/dictd}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q dictd restart

%postun
if [ "$1" = 0 ]; then
	%service -q dictd restart
fi

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/bouvier*
%{_datadir}/dictd/bouvier*
