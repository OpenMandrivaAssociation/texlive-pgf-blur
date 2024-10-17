Name:		texlive-pgf-blur
Version:	54512
Release:	2
Summary:	PGF/TikZ package for "blurred" shadows
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/pgf-blur
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-blur.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-blur.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-blur.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package adds blurred/faded/fuzzy shadows to PGF/TikZ
pictures. It is configured as a TikZ/PGF library module. The
method is similar to that of the author's pst-blur package for
PSTricks.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pgf-blur
%doc %{_texmfdistdir}/doc/latex/pgf-blur
#- source
%doc %{_texmfdistdir}/source/latex/pgf-blur

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
