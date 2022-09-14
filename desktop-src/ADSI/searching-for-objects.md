---
title: Searching for Objects
description: Julie Bankert must find telephone numbers for all Program Managers who work in Department 101. She can create a script that uses ADO and ADSI to accomplish this.
ms.assetid: c6325068-4ae2-4348-9938-96402262cd43
ms.tgt_platform: multiple
keywords:
- searching for objects ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Searching for Objects

Julie Bankert must find telephone numbers for all Program Managers who work in Department 101. She can create a script that uses ADO and ADSI to accomplish this.

When using the ADO provider to perform a query, the result set will only return the first 1000 objects. For this reason, it is important to use a paged query so that you can retrieve all of the objects in the result set, as long as the directory service has not been set to limit the number of items in a result set. Return sets will contain the number of items that you specify in the page size, and paged sets will continue to be returned until all items in the result set have been returned.


```VB
' Create the connection and command object.
Set oConnection1 = CreateObject("ADODB.Connection")
Set oCommand1 = CreateObject("ADODB.Command")
' Open the connection.
oConnection1.Provider = "ADsDSOObject"  ' This is the ADSI OLE-DB provider name
oConnection1.Open "Active Directory Provider"
' Create a command object for this connection.
Set oCommand1.ActiveConnection = oConnection1

' Compose a search string.
oCommand1.CommandText = "select name,telephoneNumber " & _
"from 'LDAP://DC=Fabrikam,DC=com'" & _
"WHERE objectCategory='Person'" & _
"AND objectClass='user'" & _
"AND title='Program Manager'" & _
"AND department=101"

' Execute the query.
Set rs = oCommand1.Execute
'--------------------------------------
' Navigate the record set
'--------------------------------------
While Not rs.EOF
    Debug.Print rs.Fields("Name") & " , " & rs.Fields("telephoneNumber")
    rs.MoveNext
Wend
```



To perform an ADSI search in Visual Basic or a scripting environment, three ADO components are required: **Connection**, **Command**, and **Recordset**. The **Connection** object enables you to specify the provider name, alternate credentials, if applicable, and other flags. The **Command** object enables you to specify search preferences and the query string. You must associate the **Connection** object to a **Command** object before the execution of the query. Finally, the **Recordset** object is used to iterate the result set.

ADSI supports two types of query strings or dialects. The preceding code example uses the SQL dialect. You can also use the LDAP dialect. The LDAP dialect query string is based on [RFC 2254](https://www.ietf.org/rfc/rfc2254.txt) (an RFC is a Request For Comments document, which is the basis for developing LDAP standards). The preceding example can be translated to the following code example.


```VB
oCommand1.CommandText = "<LDAP://DC=fabrikam,DC=COM>;" & _
"(&(objectCategory=Person)" & _
"(objectClass=user)" & _
"(title=ProgramManager)" & _
"(department=101));" & _
"name,telephoneNumber;subTree"
```



Why is the word "subtree" at the end of the string? In the directory world, you can specify the scope of search. The choices are: "base", "onelevel", and "subtree". "base" is used to read the object itself; "onelevel" refers to the immediate children, similar to the **dir** command; "subtree" is used to search deep or down multiple levels (similar to **dir /s**).

With the SQL dialect, you can specify scope in the command property, such as in the following code example.


```VB
oCommand1.Properties("SearchScope") = ADS_SCOPE_ONELEVEL
```



If scope is not specified, by default it uses a subtree search.

> [!Note]  
> If you use C++, you can use the [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch) interface from ADSI.

 

## Related topics

<dl> <dt>

[Reorganization](reorganization.md)
</dt> </dl>

 

 




