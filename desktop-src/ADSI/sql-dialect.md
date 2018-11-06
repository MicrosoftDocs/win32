---
title: SQL Dialect
description: The SQL dialect, derived from the Structured Query Language, uses human-readable expressions to define query statements.
ms.assetid: c1032268-e0f5-4d74-ab72-864cdd36851d
ms.tgt_platform: multiple
keywords:
- SQL Dialect ADSI
- dialect ADSI , SQL dialect
ms.topic: article
ms.date: 05/31/2018
---

# SQL Dialect

The SQL dialect, derived from the Structured Query Language, uses human-readable expressions to define query statements. Use a SQL query statement with the following ADSI search interfaces:

-   The [ActiveX Data Object (ADO)](searching-with-activex-data-objects-ado.md) interfaces, which are Automation interfaces that use OLE DB.
-   [OLE DB](searching-with-ole-db.md), which is a set of C/C++ interfaces for querying databases.

SQL statements require the following syntax.


```sql
SELECT [ALL] * | select-list FROM 'ADsPath' [WHERE search-condition] [ORDER BY sort-list]
```



The following table lists SQL query statement keywords.



| Keyword  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SELECT   | Specifies a comma-separated list of attributes to retrieve for each object. If you specify \*, the query retrieves only the ADsPath of each object.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| FROM     | Specifies the ADsPath of the base of the search. For example, the ADsPath of the Users container in an Active Directory domain might be 'LDAP://CN=Users,DC=Fabrikam,DC=COM'. Be aware that the path is enclosed in a pair of single quotation marks (').                                                                                                                                                                                                                                                                                                                                                    |
| WHERE    | An optional keyword that specifies the query filter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ORDER BY | An optional keyword that generates a server-side sort if the server supports the LDAP sort control. Active Directory supports the sort control, but it can impact server performance, particularly if the results set is large. The sort-list is a comma-separated list of attributes on which to sort. Be aware that Active Directory supports only a single sort key. You can use the optional ASC and DESC keywords to specify ascending or descending sort order; the default is ascending. The ORDER BY keyword overrides any sort key specified with the "Sort on" property of the ADO Command object. |



 

> [!Note]  
> In cases where a MultiByte Character Set is being used, if the search is performed by ADO with the SQL dialect, then a backslash cannot be used to escape characters. Instead, the escape sequences listed in [Special Characters](search-filter-syntax.md) must be used. For example, for a statement that used the syntax "samAccountName=\(Test", which uses the backslash, "\\", to escape the open parenthesis, "(", instead, you would replace the backslash with the special character "\\28", as follows: "samAccountName=\\28Test".

 

The following query statements are examples of SQL dialect in ADSI.

To search for all the group objects.


```sql
SELECT ADsPath, cn FROM 'LDAP://DC=Fabrikam,DC=COM' WHERE objectCategory='group'
```



To search for all the users whose Last Name starts with letter H.


```sql
SELECT ADsPath, cn FROM 'LDAP://OU=Sales,DC=Fabrikam,DC=COM' WHERE objectCategory='person' AND objectClass='user' AND sn = 'H*' ORDER BY sn
```



The formal grammar for SQL queries is defined in the following code example. All keywords are case-insensitive.


```sql
statement ::= select-statement
select-statement ::= SELECT [ALL] select-list FROM table-identifier [WHERE search-condition] [ORDER BY sort-list]
select-list ::= * | select-sublist [, select-sublist]... 
select-sublist ::= column-identifier
column-identifier ::= user-defined-name 
table-identifier ::= string-literal
search-condition ::= boolean-term [OR search-condition]
sort-list ::= column-identifier [ASC | DESC] [,column-identifier [ASC | DESC]]... 
boolean-term ::= boolean-factor [AND boolean-term]
boolean-factor ::= [NOT] boolean-primary
boolean-primary ::= comparison-predicate | (search-condition)
comparison-predicate ::= column-identifier comparison-operator literal
comparison-operator ::= < | > | <= | >= | = | <>
user-defined-name ::= letter [letter | digit]...
literal ::= string-literal | numeric-literal | boolean-literal 
string-literal ::= '{character}...' (Any sequence of characters delimited by quotes)
numeric-literal ::= digits [fraction] [exponent]
digits ::= digit [digit]...
fraction ::= . digits 
exponent ::= E digits
boolean-literal ::= TRUE | FALSE | YES | NO | ON | OFF
```



SQL inner joins are not supported by the Active Directory OLE DB provider, but you can use SQL to join SQL and Active Directory data. For more information, see [Creating a Heterogeneous Join between SQL Server and Active Directory](creating-a-heterogeneous-join-between-sql-server-and-active-directory.md).

## Related topics

<dl> <dt>

[Search Filter Syntax](search-filter-syntax.md)
</dt> <dt>

[LDAP dialect](ldap-dialect.md)
</dt> <dt>

[Searching with the IDirectorySearch Interface](searching-with-idirectorysearch.md)
</dt> <dt>

[Searching with ActiveX Data Objects](searching-with-activex-data-objects-ado.md)
</dt> <dt>

[Searching with OLE DB](searching-with-ole-db.md)
</dt> </dl>

 

 




