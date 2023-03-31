Name:		texlive-shdoc
Version:	41991
Release:	2
Summary:	Float environment to document the shell commands of a terminal session
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/shdoc
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shdoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shdoc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shdoc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a simple, though fancy float environment
to document terminal sessions -- like command executions or
shell operations. The look and feel of the package output
imitates the look of a shell prompt.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/shdoc
%{_texmfdistdir}/tex/latex/shdoc
%doc %{_texmfdistdir}/doc/latex/shdoc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
