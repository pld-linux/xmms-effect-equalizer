Summary:	Graphical Equalizer for XMMS
Summary(pl):	Korektor dla XMMS
Name:		xmms-effect-equalizer
Version:	0.6
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/equ/eq-xmms-%{version}.tar.gz
# Source0-md5:	911bcc81619d27dc466f20e17bb80d16
URL:		http://equ.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.7
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.7
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EQ is an effect plugin for XMMS that acts as an equalizer of the audio
signal passed to it by XMMS, not just mp3's. It features three
different numbers of bands, all of them with ISO central frequencies
(10, 15, and 31), independent gain settings for left and right
channels, and more than +-14dB of gain per band.

%description -l pl
EQ jest wtyczk± do XMMS-a, która dzia³a jako equalizer sygna³u audio
przekazywanego przez XMMS, nie tylko mp3. Posiada 3 ró¿ne liczby pasm,
wszystkie zgodne z czêstotliwo¶ciami ISO (10, 15 i 31), niezale¿ne
ustawianie wzmocnienia dla prawego i lewego kana³u oraz ponad +-14dB
wzmocnienia na pasmo.

%prep
%setup -q -n eq-xmms-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	XMMS="%{_bindir}/xmms"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{xmms_effect_plugindir}

rm -f $RPM_BUILD_ROOT%{xmms_effect_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{xmms_effect_plugindir}/libeq.so
