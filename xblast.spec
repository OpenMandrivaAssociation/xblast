%define name xblast
%define version 2.10.4
%define release %mkrel 2

Summary: XBlast TNT a bomberman like game (Multiplayer)
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-complete-sounds-%{version}.tar.bz2
Patch0: xblast-complete-sounds-2.10.4-localedir.patch
License: GPLv2+
Group: Games/Arcade
Url: http://xblast.sf.net
BuildRequires: libx11-devel
BuildRequires: libxt-devel
BuildRoot: %{_tmppath}/%{name}-buildroot


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

