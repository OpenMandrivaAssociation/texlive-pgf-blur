%global tl_name pgf-blur
%global tl_revision 54512

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02
Release:	%{tl_revision}.1
Summary:	PGF/TikZ package for blurred shadows
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/pgf-blur
License:	lppl pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-blur.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-blur.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-blur.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package adds blurred/faded/fuzzy shadows to PGF/TikZ pictures. It is
configured as a TikZ/PGF library module. The method is similar to that
of the author's pst-blur package for PSTricks.

