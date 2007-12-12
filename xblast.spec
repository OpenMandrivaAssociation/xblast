%define name xblast
%define version 2.10.0
%define release %mkrel 1

Summary: XBlast TNT a bomberman like game (Multiplayer)
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-complete-sounds-%{version}.tar.bz2
License: GPL
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

mkdir -p %{buildroot}%{_menudir}
install -d %{buildroot}%{_menudir}
cat <<EOF > %{buildroot}%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/%{name}" \
                  icon="arcade_section.png" \
                  needs="x11" \
                  section="Amusement/Arcade" \
                  title="X blast"\
                  longtitle="%{summary}"
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README NEWS COPYING AUTHORS
%{_bindir}/xblast
%{_bindir}/xbsndsrv
%{_gamesdatadir}/XBlast-TNT/level/
%{_gamesdatadir}/XBlast-TNT/image/
%{_gamesdatadir}/XBlast-TNT/sounds/
%dir %{_gamesdatadir}/XBlast-TNT
%_menudir/*

