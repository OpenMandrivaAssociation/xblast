%define name xblast
%define version 2.10.4
%define release  4

Summary: XBlast TNT a bomberman like game (Multiplayer)
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-complete-sounds-%{version}.tar.bz2
Patch0: xblast-complete-sounds-2.10.4-localedir.patch
License: GPLv2+
Group: Games/Arcade
Url: https://xblast.sf.net
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xt)


%description
XBlast is a multi-player arcade game for X11 and MS Windows with raytraced 
graphics. The game can be played with at least two players and up to six 
players. It was inspired by the video/computer game Bomberman (Dynablaster).

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%configure2_5x --bindir=%{_gamesbindir} --enable-sound --with-otherdatadir=%{_gamesdatadir}/XBlast-TNT
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=arcade_section
Categories=Game;ArcadeGame;
Name=X blast
Comment=%{summary}
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc README NEWS COPYING AUTHORS
%{_gamesbindir}/xblast
%{_gamesbindir}/xbsndsrv
%{_gamesdatadir}/XBlast-TNT
%{_datadir}/applications/mandriva-*.desktop



%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 2.10.4-2mdv2011.0
+ Revision: 634876
- simplify BR
- use correct localedir

* Fri May 15 2009 Samuel Verschelde <stormi@mandriva.org> 2.10.4-1mdv2010.0
+ Revision: 376289
- update to version 2.10.4
- fix license

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 2.10.0-4mdv2009.0
+ Revision: 262257
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.10.0-3mdv2009.0
+ Revision: 256589
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 2.10.0-1mdv2008.1
+ Revision: 132309
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import xblast


* Wed Dec 07 2005 Lenny Cartier <lenny@mandriva.com> 2.10.0-1mdk
- 2.10.0

* Mon Nov  1 2004 Michael Scherer <misc@mandrake.org> 2.9.22-2mdk
- Buildrequires
- [DIRM]

* Fri Sep 17 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.9.22-1mdk
- from Fernando Benites <iskywalker@users.sourceforge.net> :
	- first build
- menu
- fix group
