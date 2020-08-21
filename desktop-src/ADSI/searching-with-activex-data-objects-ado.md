---
title: Searching with ActiveX Data Objects (ADO)
description: The ActiveX Data Object (ADO) model consists of objects listed in the following table.
ms.assetid: 27298f53-a652-49f2-a6e6-d92c7c6022af
ms.tgt_platform: multiple
keywords:
- ActiveX Data Objects ADSI , Searching with ADO
- Searching with ActiveX Data Objects ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Searching with ActiveX Data Objects (ADO)

The ActiveX Data Object (ADO) model consists of objects listed in the following table.



| Object         | Description                                                                                                                        |
|----------------|------------------------------------------------------------------------------------------------------------------------------------|
| **Connection** | An open connection to an OLE DB data source such as ADSI.                                                                          |
| **Command**    | Defines a specific command to run against the data source.                                                                         |
| **Parameter**  | An optional collection for any parameters to provide to the command object.                                                        |
| **RecordSet**  | A set of records from a table, command object, or SQL syntax. A recordset can be created without any underlying connection object. |
| **Field**      | A single column of data in a recordset.                                                                                            |
| **Property**   | A collection of values supplied by the provider for ADO.                                                                           |
| **Error**      | Contains data about data access errors. Refreshed when an error occurs in a single operation.                                      |



 

For ADO to communicate with ADSI, there must be, at least, two ADO objects: **Connection** and **RecordSet**. These ADO objects serve to authenticate users and enumerate results, respectively. Typically, you will also use a **Command** object to maintain an active connection, specify query parameters, such as page size and search scope, and perform a query. For more information about the search filter syntax, see [Search Filter Syntax](search-filter-syntax.md).

The **Connection** object loads the OLE DB provider, and validates user credentials. In Visual Basic, call the **CreateObject** function with "ADODB.Connection" to create an instance of a **Connection** object, and then set the **Provider** property of the **Connection** object to "ADsDSOObject". "ADODB.Connection" is the ProgID of the **Connection** object and "ADsDSOObject" is the name of the OLE DB provider in ADSI. If no credentials are specified, the credentials of the currently logged on user are used.

The following code example shows how to create an instance of a **Connection** object.


```VB
Set con = CreateObject("ADODB.Connection")
con.Provider = "ADsDSOObject"
```



The following code example shows how to create an instance of a **Connection** object.


```VB
<%
Set con = Server.CreateObject("ADODB.Connection")
con.Provider = "ADsDSOObject"
%>
```



The following code example shows how to create an instance of a **Connection** object. Be aware that you must include the ADO type library (msadoXX.dll) as one of the references in the Visual Basic project.


```VB
Dim Con As New Connection
con.Provider = "ADsDSOObject"
```



Specify user authentication data by setting the properties of the **Connection** object. The following table lists ADSI-supported user-authentication properties.



| Property           | Description                                                                                                                                                                                                                                                                                                                                    |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "User ID"          | A string that identifies the user whose security context is used when performing the search. For more information about the format of the user name string, see [**IADsOpenDSObject::OpenDSObject**](/windows/desktop/api/Iads/nf-iads-iadsopendsobject-opendsobject). If not specified, the default is the logged on user, or the user impersonated by the calling process. |
| "Password"         | A string that specifies the password of the user identified by "User ID".                                                                                                                                                                                                                                                                      |
| "Encrypt Password" | A Boolean value that specifies whether the password is encrypted. The default is **false**.                                                                                                                                                                                                                                                    |
| "ADSI Flag"        | A set of flags from the [**ADS\_AUTHENTICATION\_ENUM**](/windows/win32/api/iads/ne-iads-ads_authentication_enum) enumeration that specify the binding authentication options. The default is zero.                                                                                                                                                                         |



 

The following code example shows how the properties are set before creating the **Command** object.


```VB
Set oConnect = CreateObject("ADODB.Connection")
oConnect.Provider = "ADsDSOObject"
oConnect.Properties("User ID") = stUser
oConnect.Properties("Password") = stPass
oConnect.Properties("Encrypt Password") = True
oConnect.Open "DS Query", stUser, stPass
```



The second ADO object is the **Command** object. The ProgID of the **Command** object is "ADODB.Command". This object enables you to issue query statements and other commands to ADSI using the active connection. The **Command** object uses its **ActiveConnection** property to maintain an active connection. It also maintains the **CommandText** property to hold query statements issued by a user. The query statements are expressed in either the [SQL dialect](sql-dialect.md) or the [LDAP dialect](ldap-dialect.md).

The following code examples show how to create a **Command** object.


```VB
Set command = CreateObject("ADODB.Command")
Set command.ActiveConnection = oConnect
command.CommandText = 
"SELECT AdsPath, cn FROM 'LDAP://DC=Fabrikam,DC=com' WHERE objectClass = '*'"
```



In the following code example, include ADO type library (msadoXX.dll) as one of the references.


```VB
Dim command As New Command
Set command.ActiveConnection = oConnect
command.CommandText = "<LDAP://DC=Fabrikam,DC=com>;(objectClass=*);AdsPath, cn; subTree"
```



Search options for the **Command** object are specified by setting the **Properties** property. The following table lists acceptable named properties for **Properties**.



| Named property      | Description                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "Asynchronous"      | A Boolean value that specifies whether the search is synchronous or asynchronous. The default is False (synchronous). A synchronous search blocks until the server returns the entire result, or for a paged search, the entire page. An asynchronous search blocks until one row of the search results is available, or until the time specified by the "Timeout" property elapses.                           |
| "Cache results"     | A Boolean value that specifies whether the result should be cached on the client side. The default is **true**; ADSI caches the result set. Turning off this option may be desirable for large result sets.                                                                                                                                                                                                    |
| "Chase referrals"   | A value from the [**ADS\_CHASE\_REFERRALS\_ENUM**](/windows/win32/api/iads/ne-iads-ads_chase_referrals_enum) that specifies how the search chases referrals. The default is **ADS\_CHASE\_REFERRALS\_NEVER**.For more information about this property, see [Referrals](/windows/desktop/AD/referrals).<br/>                                                                                                                                           |
| "Column Names Only" | A Boolean value that indicates that the search should retrieve only the name of attributes to which values have been assigned. The default is **false**.                                                                                                                                                                                                                                                       |
| "Deref Aliases"     | A Boolean value that specifies whether aliases of found objects are resolved. The default is **false**.                                                                                                                                                                                                                                                                                                        |
| "Page size"         | An integer value that turns on paging and specifies the maximum number of objects to return in a results set. The default is no page size. For more information, see [Retrieving Large Results Sets](retrieving-large-results-sets.md).                                                                                                                                                                       |
| "SearchScope"       | A value from the [**ADS\_SCOPEENUM**](/windows/win32/api/iads/ne-iads-ads_scopeenum) enumeration that specifies the search scope. The default is **ADS\_SCOPE\_SUBTREE**.                                                                                                                                                                                                                                                                  |
| "Size Limit"        | An integer value that specifies the size limit for the search. For Active Directory, the size limit specifies the maximum number of returned objects. The server stops searching when the size limit is reached and returns the results accumulated. The default is no limit.                                                                                                                                  |
| "Sort on"           | A string that specifies a comma-separated list of attributes to use as sort keys. This property works only for directory servers that support the LDAP control for server-side sorting. Active Directory supports the sort control, but it can impact server performance, particularly if the results set is large. Be aware that Active Directory supports only a single sort key. The default is no sorting. |
| "Time Limit"        | An integer value that specifies the time limit, in seconds, for the search. When the time limit is reached, the server stops searching and returns the results accumulated. The default is no time limit.                                                                                                                                                                                                      |
| "Timeout"           | An integer value that specifies the client-side timeout value, in seconds. This value indicates the time the client waits for results from the server before stopping the search. The default is no time-out.                                                                                                                                                                                                  |



 

The following code example shows how to set search options.


```VB
Const ADS_SCOPE_ONELEVEL = 1
Const ADS_CHASE_REFERRALS_EXTERNAL = &H40

Dim Com As New Command
 
Com.Properties("Page Size") = 999
Com.Properties("Timeout") = 30     ' Seconds
Com.Properties("searchscope") = ADS_SCOPE_ONELEVEL
Com.Properties("Chase referrals") = ADS_CHASE_REFERRALS_EXTERNAL
Com.Properties("Cache Results") = False     ' Do not cache the result set.
```



The third ADO object is **RecordSet**. You obtain this object when you invoke the **Execute** method on a **Command** object. The primary function of the **RecordSet** object is to enumerate the result set and obtain the data. The result set can contain values for attributes that have both single or multiple values. Getting a single-valued attribute is simple, similar to getting the column value in the relational database, for example:


```VB
Fields('name').Value
```



Getting an attribute with multiple values, however, is more challenging. In this case, the **Field.Value** is an array and you must check the lower and upper bound of the array, as shown in the following code example.


```VB
Set rs = Com.Execute
 
For i = 0 To rs.Fields.Count - 1
    Debug.Print rs.Fields(i).Name, rs.Fields(i).Type
Next i
 
'--------------------------
' Navigate the record set.
'--------------------------
rs.MoveFirst
lstResult.Clear      ' Clear the user interface.
While Not rs.EOF
For i = 0 To rs.Fields.Count - 1
    ' For Multi Value attribute
    If rs.Fields(i).Type = adVariant And Not (IsNull(rs.Fields(i).Value)) Then
        Debug.Print rs.Fields(i).Name, " = "
        For j = LBound(rs.Fields(i).Value) To UBound(rs.Fields(i).Value)
            Debug.Print rs.Fields(i).Value(j), " # "
            lstResult.AddItem rs.Fields(i).Value(j)
        Next j
    Else
        ' For Single Value attribute.
         Debug.Print rs.Fields(i).Name, " = ", rs.Fields(i).Value
         lstResult.AddItem rs.Fields(i).Value
    End If
Next i
rs.MoveNext
Wend
```



The following code example disables the user accounts on an LDAP server.


```VB
Dim X as IADs
Dim con As New Connection, rs As New Recordset
Dim MyUser As IADsUser
 
con.Provider = "ADsDSOObject"
con.Open "Active Directory Provider", "CN=Test,CN=Users,DC=Fabrikam,DC=COM,O=INTERNET", "Password"
Set rs = con.Execute("<LDAP://MyMachine/DC=MyDomain,DC=Fabrikam,DC=com>;(objectClass=User);ADsPath;onelevel")
 
While Not rs.EOF
    ' Bind to the object to make changes 
    ' to it because ADO is currently read-only.
    MyUser = GetObject(rs.Fields(0).Value)
    MyUser.AccountDisabled = True
    MyUser.SetInfo
    rs.MoveNext
Wend
```



For more information about the ADO object model, see [Microsoft ActiveX Data Objects](/sql/ado/microsoft-activex-data-objects-ado?view=sql-server-ver15).

 

