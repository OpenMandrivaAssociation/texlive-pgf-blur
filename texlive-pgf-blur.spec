# revision 26134
# category Package
# catalog-ctan /graphics/pgf/contrib/pgf-blur
# catalog-date 2012-04-24 16:17:04 +0200
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-pgf-blur
Version:	1.01
Release:	3
Summary:	PGF/TikZ package for "blurred" shadows
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/pgf-blur
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-blur.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-blur.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-blur.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package adds blurred/faded/fuzzy shadows to TikZ/PGF
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
%{_texmfdistdir}/tex/latex/pgf-blur/tikzlibraryshadows.blur.code.tex
%doc %{_texmfdistdir}/doc/latex/pgf-blur/README
%doc %{_texmfdistdir}/doc/latex/pgf-blur/pgf-blur.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pgf-blur/pgf-blur.dtx
%doc %{_texmfdistdir}/source/latex/pgf-blur/pgf-blur.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.01-2
+ Revision: 813697
- Update to latest release.
- Import texlive-pgf-blur
- Import texlive-pgf-blur

