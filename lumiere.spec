Summary:	Lumiere - movie player for GNOME based on mplayer
Summary(pl):	Lumiere - odtwarzacz filmów dla GNOME bazuj±cy na mplayerze
Name:		lumiere
Version:	0.2.0
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://users.aber.ac.uk/ssk01/prog/sources/%{name}-0.2.tar.gz
URL:		http://users.aber.ac.uk/ssk01/lumiere/
#BuildRequires:	TODO
Requires:	mplayer
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lumiere, a movie player for GNOME based on mplayer.

%description -l pl
Lumiere - odtwarzacz filmów dla GNOME bazujacy na mplayerze.

%prep
%setup -q -n lum

%build
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lumiere
%attr(755,root,root) %{_libdir}/lumiere-control
%attr(755,root,root) %{_libdir}/midentify
%{_libdir}/bonobo/servers/GNOME_LUM.server
%{_datadir}/applications/lumiere.desktop
%{_datadir}/gnome-2.0/ui/*
%{_pixmapsdir}/lumiere
%{_pixmapsdir}/gnome-lumiere.png
