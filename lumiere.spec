Summary:	Lumiere - movie player for GNOME based on mplayer
Summary(pl):	Lumiere - odtwarzacz filmów dla GNOME bazuj±cy na mplayerze
Name:		lumiere
Version:	0.3.0
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://brain.shacknet.nu/%{name}-%{version}.tar.gz
# Source0-md5:	93af0abe6a81fe52b94b92e9f4a098f2
Patch0:		%{name}-schemas.patch
URL:		http://brain.shacknet.nu/lumiere.html
BuildRequires:	ORBit2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-activation-devel >= 0.9.7
BuildRequires:	gnome-vfs2-devel >= 1.9.12
BuildRequires:	gob2 >= 2.0.0
BuildRequires:	libbonoboui-devel >= 1.115.0
BuildRequires:	libgnomeui-devel >= 1.115.0
BuildRequires:	libtool
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lumiere, a movie player for GNOME based on mplayer.

%description -l pl
Lumiere - odtwarzacz filmów dla GNOME bazuj±cy na mplayerze.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--with-mplayer=/usr/bin/mplayer

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install

%postun	-p /sbin/ldconfig

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lumiere
%attr(755,root,root) %{_libdir}/lumiere-control
%attr(755,root,root) %{_libdir}/midentify
%{_libdir}/bonobo/servers/GNOME_LUM.server
%{_desktopdir}/lumiere.desktop
%{_datadir}/gnome-2.0/ui/*
%dir %{_datadir}/lumiere
%dir %{_datadir}/lumiere/glade
%{_datadir}/lumiere/glade/lumiere.glade
%{_pixmapsdir}/lumiere
%{_pixmapsdir}/gnome-lumiere.png
%{_sysconfdir}/gconf/schemas/*
