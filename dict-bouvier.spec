#  $Id: dict-bouvier.spec,v 1.1 2002-10-10 05:36:14 hunter Exp $
Summary:	John Bouvier's Law Dictionary dated 1856 for the USA in the DICTD format.
Summary(pl):	S³ownik prawa USA z 1856 w formacie DICTD.
Name:		dict-bouvier
Version:	1
Release:	1
License:	GPL
# it was downloaded from http://www.constitution.org/bouv/bouvier.htm
# Upstream Author(s): John Bouvier, 1856.
# Copyright claims to this work have expired; it is now public domain.
# so it's compatible w/ Gnu GPL ???
Group:		Applications/Dictionaries
Source0:	dict-bouvier_6.tar.gz
Patch0:		dict-bouvier_6.revised-1.diff 
# from debian
URL:		http://www.constitution.org/bouv/bouvier.htm
BuildRequires:	dictfmt
BuildRequires:	dictzip
BuildRequires:	python
Requires:	dictd
Requires:	%{_sysconfdir}/dictd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the 1856 Revised Sixth Ediition of John Bouvier's law dictionary,
formatted for use with the dictd server.  It is an excellent, if dated,
way to look up information about legal words and principles.

%description -l pl
Jest to s³ownik prawa amerykañskiego z 1856 roku, autorstwa John Bouvier.

%prep
%setup -n dict-bouvier-6.revised.orig
%patch0 -p1

%build

# ./conv.py ???
# ???

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd/,%{_sysconfdir}/dictd}

#database $i {
#	data  \"$dictprefix.dict.dz\"
#	index \"$dictprefix.index\"
#}" > $RPM_BUILD_ROOT%{_sysconfdir}/dictd/%{dictname}-$i.dictconf
#	install %{dictname}_$i.* $RPM_BUILD_ROOT%{_datadir}/dictd/
#done

%clean
rm -rf $RPM_BUILD_ROOT

%post 
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict6}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict6}.*
