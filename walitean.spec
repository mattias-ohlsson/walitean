%global gitcommit 6c3f6af3c47b2ca8b69c6268db6aeb94bceb6961
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})

Name:           walitean
Version:        0
Release:        1.git.20170907.%{gitshortcommit}%{?dist}
Summary:        Written-Ahead Log Analyzer for SQLite

# License information:
# - README.md: GPLv2
# - _helpersBinaryOperations.py: GPLv3+
# - _sqliteVarInt.py: GPLv3+
# - sqliteDB.py: GPLv3+
# - sqlitePage.py: GPLv3+
# - walitean.py: GPLv3+
License:        GPLv2 and GPLv3+

URL:            https://github.com/n0fate/walitean
Source0:        https://github.com/n0fate/walitean/archive/%{gitcommit}/%{name}-%{gitshortcommit}.tar.gz
Source1:        https://www.gnu.org/licenses/gpl-3.0.txt

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  /usr/bin/pathfix.py

%description
Written-Ahead Log Analyzer for SQLite, WAL Journal Forensic Toolkit.

%prep
%autosetup -n %{name}-%{gitcommit}

install --preserve-timestamps -m 0644 %{SOURCE1} COPYING

/usr/bin/pathfix.py -pni "%{__python2} %{py2_shbang_opts}" walitean.py \
 _helpersBinaryOperations.py _sqliteVarInt.py sqliteDB.py sqlitePage.py

%build

%install
install --preserve-timestamps -D walitean.py \
 %{buildroot}%{_bindir}/walitean.py
install --mode=644 --preserve-timestamps -D _helpersBinaryOperations.py \
 %{buildroot}%{python2_sitelib}/_helpersBinaryOperations.py
install --mode=644 --preserve-timestamps -D _sqliteVarInt.py \
 %{buildroot}%{python2_sitelib}/_sqliteVarInt.py
install --mode=644 --preserve-timestamps -D exportdb.py \
 %{buildroot}%{python2_sitelib}/exportdb.py
install --mode=644 --preserve-timestamps -D sqliteDB.py \
 %{buildroot}%{python2_sitelib}/sqliteDB.py
install --mode=644 --preserve-timestamps -D sqlitePage.py \
 %{buildroot}%{python2_sitelib}/sqlitePage.py

%files
%license COPYING
%doc README.md
%{_bindir}/walitean.py
%{python2_sitelib}/*

%changelog
* Sat Nov 28 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0-1.git.20170907.6c3f6af
- Initial package
