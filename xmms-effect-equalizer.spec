Summary:	Graphical Equalizer for XMMS
Summary(pl):	Korektor dla XMMS
Name:		xmms-effect-equalizer
Version:	0.3
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://telia.dl.sourceforge.net/sourceforge/equ/eq-xmms-%{version}.tar.gz
URL:		http://equ.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xmms-devel >= 1.2.7
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
EQ is an effect plugin for XMMS that acts as an equalizer of the audio
signal passed to it by XMMS, not just mp3's. It features three
different numbers of bands, all of them with ISO central frequencies
(10, 15, and 31), independent gain settings for left and right
channels, and more than +-14dB of gain per band.

%description -l pl
EQ jest wtyczk� do XMMS-a, kt�ra dzia�a jako equalizer sygna�u audio
przekazywanego przez XMMS, nie tylko mp3. Posiada 3 r�ne liczby pasm,
wszystkie zgodne z cz�stotliwo�ciami ISO (10, 15 i 31), niezale�ne
ustawianie wzmocnienia dla prawego i lewego kana�u oraz ponad +-14dB
wzmocnienia na pasmo.

%prep
%setup -q -n eq-xmms-%{version}

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=`%{_bindir}/xmms-config --effect-plugin-dir`

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/xmms/*/*
