%global tl_name shdoc
%global tl_revision 41991

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1b
Release:	%{tl_revision}.1
Summary:	Float environment to document the shell commands of a terminal session
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/shdoc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/shdoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/shdoc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/shdoc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a simple, though fancy float environment to
document terminal sessions -- like command executions or shell
operations. The look and feel of the package output imitates the look of
a shell prompt.

