Summary:	Graphical Equalizer for XMMS
Summary(pl.UTF-8):	Korektor dla XMMS
Name:		xmms-effect-equalizer
Version:	0.7
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/equ/eq-xmms-%{version}.tar.gz
# Source0-md5:	a211f894906696c5bb1cfa65f57e8155
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
signal passed to it by XMMS, not just MP3's. It features three
different numbers of bands, all of them with ISO central frequencies
(10, 15, and 31), independent gain settings for left and right
channels, and more than +-14dB of gain per band.

%description -l pl.UTF-8
EQ jest wtyczką do XMMS-a, która działa jako equalizer sygnału audio
przekazywanego przez XMMS, nie tylko MP3. Posiada 3 różne liczby pasm,
wszystkie zgodne z częstotliwościami ISO (10, 15 i 31), niezależne
ustawianie wzmocnienia dla prawego i lewego kanału oraz ponad +-14dB
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
