%global tl_name biblatex-trad
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Traditional BibTeX styles with BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-trad
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-trad.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-trad.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides implementations of the "traditional" BibTeX styles
(plain, abbrev, unsrt and alpha) with BibLaTeX.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-trad
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-trad
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-trad/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-trad/biblatex-trad.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-trad/biblatex-trad.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-trad/trad-abbrv.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-trad/trad-abbrv.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-trad/trad-alpha.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-trad/trad-alpha.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-trad/trad-plain.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-trad/trad-plain.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-trad/trad-standard.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-trad/trad-standard.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-trad/trad-unsrt.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-trad/trad-unsrt.cbx
