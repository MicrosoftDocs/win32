---
title: LDAP Dialect
description: The LDAP dialect is a format for query statements that use the LDAP search filter syntax.
ms.assetid: 29aca7e6-3ed5-4efd-8b03-6a2ee0571f1f
ms.tgt_platform: multiple
keywords:
- LDAP Dialect ADSI
- dialects ADSI , LDAP dialect
ms.topic: article
ms.date: 05/31/2018
---

# LDAP Dialect

The LDAP dialect is a format for query statements that use the [LDAP search filter syntax](search-filter-syntax.md). Use an LDAP query statement with the following ADSI search interfaces:

-   The [ActiveX Data Object (ADO)](searching-with-activex-data-objects-ado.md) interfaces, which are Automation interfaces that use OLE DB.
-   [OLE DB](searching-with-ole-db.md), which is a set of C/C++ interfaces for querying databases.
-   [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch), which is the C/C++ interface for Active Directory.

An LDAP dialect string consists of four parts separated by semicolons (;).

-   Base distinguished name. For example:

    ```VB
    <LDAP://DC=Fabrikam,DC=COM>
    ```

    

-   LDAP search filters. For more information about search filters, see [Search Filter Syntax](search-filter-syntax.md).
-   The LDAP display name of the attributes to retrieve. Multiple attributes are separated by a comma.
-   Specifies the scope of the search. Valid values are "base", "onelevel", and "subtree". The scope specified in an LDAP query string overrides any search scope specified with the "SearchScope" property of the ADO Command object.

The following is a code example of the LDAP dialect in ADSI that searches all the objects in the subtree.


```VB
"<LDAP://DC=Fabrikam,DC=com>;(objectClass=*);AdsPath, cn;subTree"
```



Not all search options (search page size, for example) can be expressed in the LDAP dialect, so you must set the options before the actual query execution starts.

## Example Code for Performing an LDAP Query

The following code example shows how to use an LDAP query


```VB
Dim con As New Connection, rs As New Recordset
Dim adVariant
Dim i 'Used for counter
Dim j 'Used for counter
Dim Com As New Command
Dim strDomain As String
Dim strPassword As String
 
' Open a Connection object.
con.Provider = "ADsDSOObject"
con.Properties("ADSI Flag") = 1
con.Properties("User ID") = strDomain + "\" + strUserID
con.Properties("Password") = strPassword

con.Open "Active Directory Provider"
 
' Create a command object on this connection.
Set Com.ActiveConnection = con
 
' Set the query string.
Com.CommandText = "<LDAP://MyServer/DC=MyDomain,DC=Fabrikam,DC=com>;
     (objectClass=*);ADsPath, objectclass;base"
 
' Set search preferences.
Com.Properties("Page Size") = 1000
Com.Properties("Timeout") = 30 'seconds
 
' Execute the query.
Set rs = Com.Execute
 
' Navigate the record set.
rs.MoveFirst
While Not rs.EOF
    For i = 0 To rs.Fields.Count - 1
        If rs.Fields(i).Type = adVariant And Not (IsNull(rs.Fields(i).Value)) Then
            Debug.Print rs.Fields(i).Name, " = "
            For j = LBound(rs.Fields(i).Value) To UBound(rs.Fields(i).Value)
                Debug.Print rs.Fields(i).Value(j), " # "
            Next j
        Else
            Debug.Print rs.Fields(i).Name, " = ", rs.Fields(i).Value
        End If
    Next i
    rs.MoveNext
Wend
 
rs.MoveLast
Debug.Print "No. of rows = ", rs.RecordCount
```



For details about the query syntax, see [Search Filter Syntax](search-filter-syntax.md).

## Related topics

<dl> <dt>

[Search Filter Syntax](search-filter-syntax.md)
</dt> <dt>

[SQL dialect](sql-dialect.md)
</dt> <dt>

[Searching with the IDirectorySearch Interface](searching-with-idirectorysearch.md)
</dt> <dt>

[Searching with ActiveX Data Objects](searching-with-activex-data-objects-ado.md)
</dt> <dt>

[Searching with OLE DB](searching-with-ole-db.md)
</dt> </dl>

 

 




