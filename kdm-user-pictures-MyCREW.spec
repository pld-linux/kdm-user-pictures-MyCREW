#$Revision: 1.5 $, $Date: 2005-02-08 18:51:28 $

%define         _name MYCREW

Summary:	kdm user pictures - %{_name}
Summary(pl):	Obrazki u¿ytkowników do kdm - %{_name}
Name:		kdm-user-pictures-%{_name}
Version:	2.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://kde-look.org/content/files/18996-%{_name}%{version}.zip
# Source0-md5:	18a59f750271ee2eef463cbb1403d206
URL:		http://www.kde-look.org/content/show.php?content=18996
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is icons of user avantars for kdm-a.

%description -l pl
%{_name} to ikony obrazków u¿ytkowników dla kdm-a.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/users/%{_name}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/users/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kdm/pics/users/%{_name}
