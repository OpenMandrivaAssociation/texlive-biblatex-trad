# revision 27852
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-trad
# catalog-date 2012-09-29 14:32:13 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-biblatex-trad
Version:	0.2
Release:	10
Summary:	"Traditional" BibTeX styles with BibLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-trad
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-trad.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-trad.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides implementations of the "traditional" BibTeX
styles (plain, abbrev, unsrt and alpha) with BibLaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-trad/bbx/trad-abbrv.bbx
%{_texmfdistdir}/tex/latex/biblatex-trad/bbx/trad-alpha.bbx
%{_texmfdistdir}/tex/latex/biblatex-trad/bbx/trad-plain.bbx
%{_texmfdistdir}/tex/latex/biblatex-trad/bbx/trad-standard.bbx
%{_texmfdistdir}/tex/latex/biblatex-trad/bbx/trad-unsrt.bbx
%{_texmfdistdir}/tex/latex/biblatex-trad/cbx/trad-abbrv.cbx
%{_texmfdistdir}/tex/latex/biblatex-trad/cbx/trad-alpha.cbx
%{_texmfdistdir}/tex/latex/biblatex-trad/cbx/trad-plain.cbx
%{_texmfdistdir}/tex/latex/biblatex-trad/cbx/trad-standard.cbx
%{_texmfdistdir}/tex/latex/biblatex-trad/cbx/trad-unsrt.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-trad/README.txt
%doc %{_texmfdistdir}/doc/latex/biblatex-trad/biblatex-trad.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-trad/biblatex-trad.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
