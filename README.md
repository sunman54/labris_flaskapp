# labris_flaskapp


## database commands for creating tables :


### Users table : 
```SQL
CREATE TABLE users (id serial PRIMARY KEY,
            
                                 username varchar (50) NOT NULL,
            
                                 firstname varchar (50) NOT NULL,
                                 middlename varchar (50),
                                 lastname varchar (50) NOT NULL,
                                 birthdate date,
            
                                 email varchar (150) NOT NULL,
                                 password varchar (200) NOT NULL,
                                 UNIQUE(username),
                                 UNIQUE(email)
                                 
                                 ) 
                                 
                                 
                                 ;

```


### loged_in_users table : 


```SQL
CREATE TABLE loged_in_users (id serial PRIMARY KEY,
                    username varchar (50),
                    login_time varchar (50),
                    login_date varchar (50));

```
 %define name netflow2ng
%define version 1.0.0
%define release 1
%define buildroot %{_tmppath}/%{name}-%{version}-%{release}-root

Name: %{name}
Version: %{version}
Release: %{release}
Summary: NetFlow v5/v9/sFlow collector and analyzer
License: MIT
URL: https://github.com/synfinatic/netflow2ng
Source0: %{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
Netflow2ng is a NetFlow v5/v9/sFlow collector and analyzer.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%{_sbindir}/netflow2ng
%{_mandir}/man8/netflow2ng.8*

%changelog
* Fri Mar 11 2023 ChatGPT <chatgpt@openai.com> - %{version}-%{release}
- Initial package for netflow2ng.
