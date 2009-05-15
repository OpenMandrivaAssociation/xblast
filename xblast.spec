%define name xblast
%define version 2.10.4
%define release %mkrel 1

Summary: XBlast TNT a bomberman like game (Multiplayer)
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-complete-sounds-%{version}.tar.bz2
License: GPLv2+
Group: Games/Arcade
Url: http://xblast.sf.net
BuildRequires:   X11-devel 
BuildRoot: %{_tmppath}/%{name}-buildroot


%description
XBlast is a multi-player arcade game for X11 and MS Windows with raytraced 
graphics. The game can be played with at least two players and up to six 
players. It was inspired by the video/computer game Bomberman (Dynablaster).

%prep

%setup -q

%build

%configure  --enable-sound --with-otherdatadir=%{_gamesdatadir}/XBlast-TNT/

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall  game_datadir=$RPM_BUILD_ROOT%{_gamesdatadir}/XBlast-TNT

%{find_lang} %{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name}
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
%{_bindir}/xblast
%{_bindir}/xbsndsrv
%{_gamesdatadir}/XBlast-TNT/level/
%{_gamesdatadir}/XBlast-TNT/image/
%{_gamesdatadir}/XBlast-TNT/sounds/
%dir %{_gamesdatadir}/XBlast-TNT
%{_datadir}/applications/mandriva-*.desktop

