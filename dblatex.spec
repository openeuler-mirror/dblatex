Name:           dblatex
Version:        0.3.10
Release:        8
Summary:        DocBook to LaTeX/ConTeXt Publishing
BuildArch:      noarch
License:        GPLv2+ and GPLv2 and LPPL and DMIT and Public Domain
URL:            http://dblatex.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        COPYING-docbook-xsl
Patch0000:      dblatex-0.2.7-external-which.patch
Patch0001:      dblatex-disable-debian.patch

BuildRequires:  python2-devel python2-which libxslt texlive-base texlive-collection-latex texlive-collection-xetex
BuildRequires:  texlive-collection-htmlxml texlive-xmltex-bin texlive-anysize texlive-appendix texlive-changebar
BuildRequires:  texlive-fancybox texlive-jknapltx texlive-multirow  texlive-overpic texlive-pdfpages texlive-subfigure
BuildRequires:  texlive-stmaryrd texlive-wasysym

Requires:       texlive-base texlive-collection-latex texlive-collection-xetex texlive-collection-htmlxml
Requires:       texlive-passivetex texlive-xmltex texlive-xmltex-bin texlive-anysize texlive-appendix texlive-bibtopic
Requires:       texlive-changebar texlive-ec texlive-fancybox texlive-jknapltx texlive-multirow texlive-overpic
Requires:       texlive-pdfpages texlive-subfigure texlive-stmaryrd texlive-wasysym texlive-xmltex-bin libxslt
Requires:       texlive-collection-fontsrecommended docbook-dtds

Recommends:     ImageMagick texlive-epstopdf-bin transfig inkscape

%description
dblatex can transforms your SGML/XMLDocBook documents to DVI,
PostScript or PDF by translating them into pure LaTeX as a first process.
MathML 2.0 markups are supported, too.

%package help
Summary:   Introduce how to use dblatex

%description help
Introduce how to use dblatex

%prep
%autosetup -n %{name}-%{version} -p1
rm -rf lib/contrib

%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --root $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/texlive/texmf-dist/tex/latex/dblatex
for file in ` find $RPM_BUILD_ROOT%{_datadir}/dblatex/latex/ -name '*.sty' ` ; do
  mv $file $RPM_BUILD_ROOT%{_datadir}/texlive/texmf-dist/tex/latex/dblatex/`basename $file`;
done

for file in ` find $RPM_BUILD_ROOT%{_datadir}/dblatex/latex/ -name '*.xetex' ` ; do
  mv $file $RPM_BUILD_ROOT%{_datadir}/texlive/texmf-dist/tex/latex/dblatex/`basename $file`;
done

install -d  $RPM_BUILD_ROOT%{_sysconfdir}/dblatex

awk '{sub("\r$","",$0);print $0}' xsl/mathml2/README > README-xsltml
touch -r xsl/mathml2/README README-xsltml
cp -p %{SOURCE1} COPYING-docbook-xsl

%post -p /usr/bin/texhash

%postun -p /usr/bin/texhash

%files
%doc COPYRIGHT COPYING-docbook-xsl
%{python2_sitelib}/dbtexmf/
%{python2_sitelib}/dblatex-*.egg-info
%{_bindir}/dblatex
%{_datadir}/dblatex/
%{_datadir}/texlive/texmf-dist/tex/latex/dblatex/
%dir %{_sysconfdir}/dblatex
%exclude %{_datadir}/doc/
%exclude %{_datadir}/dblatex/latex/{misc,contrib/example,style}
%exclude %{_datadir}/dblatex/latex/misc/bibtopic.sty
%exclude %{_datadir}/dblatex/latex/misc/enumitem.sty
%exclude %{_datadir}/dblatex/latex/misc/ragged2e.sty
%exclude %{_datadir}/dblatex/latex/misc/passivetex/
%exclude %{_datadir}/dblatex/latex/misc/xelatex/

%files help
%doc docs/manual.pdf README-xsltml
%{_mandir}/man1/dblatex.1*

%changelog
* Fri Nov 22 2019 yangjian<yangjian79@huawei.com> - 0.3.10-8
- Package init
