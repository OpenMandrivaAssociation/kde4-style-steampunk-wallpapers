Summary:	"SteampunK Powered Linux" wallpapers
Name:		kde4-style-steampunk-wallpapers
Version:	3.0
Release:	2
License:	Creative Commons Attribution-ShareAlike
Group:		Graphical desktop/KDE
Url:		https://kde-look.org/content/show.php?content=149320
Source0:	http://sites.google.com/site/binaryinspiration/download/SPL_Wlpr_Engine.tar.gz
Source1:	http://sites.google.com/site/binaryinspiration/download/SPL_Wlpr_Machine.tar.gz
Source2:	http://sites.google.com/site/binaryinspiration/download/SPL_Wlpr_Simple.tar.gz
BuildArch:	noarch

%description
This package contains the "SteampunK Powered Linux" wallpapers.

%files
%{_datadir}/wallpapers/SteampunK_Engine
%{_datadir}/wallpapers/SteampunK_Machine
%{_datadir}/wallpapers/SteampunK_Simple

#----------------------------------------------------------------------------

%prep
%setup -q -c -a1 -a2
find . -type f | xargs chmod 0644

%build
# nothing

%install
mkdir -p %{buildroot}%{_datadir}/wallpapers

cp -r SteampunK_{Engine,Machine,Simple} %{buildroot}%{_datadir}/wallpapers/

