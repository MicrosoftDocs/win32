---
title: Modifying an ADSI Object from ADO
description: ADSI for Windows 2000 and DS Client includes a read-only OLE DB provider. This means that you cannot, at present, issue the UPDATE statement in the SQL dialect.
ms.assetid: b0a107ed-0271-45ab-b971-f589f34472e2
ms.tgt_platform: multiple
keywords:
- Modifying an ADSI Object from ADO ADSI
- ActiveX data object ADSI , modifying an ADSI object from ADO
- ADSI ADSI , example code C/C++ , modifying an ADSI object
ms.topic: article
ms.date: 05/31/2018
---

# Modifying an ADSI Object from ADO

ADSI for Windows 2000 and DS Client includes a read-only OLE DB provider. This means that you cannot, at present, issue the UPDATE statement in the SQL dialect.

**To modify an object returned from an ADO query**

1.  Request the **ADsPath** when specifying an attribute name, as in "SELECT ADsPath, ..."
2.  Execute the query and get the **ADsPath** attribute.
3.  Bind to the record set using **ADsPath**, and modify the attributes.

The following code example shows how to modify an ADSI object after performing the steps outlined in the preceding example.


```VB
Dim Con As New Connection
Dim rs As New Recordset
Dim command As New Command
Dim usr As IADsUser

' Replace department for all users in OU=sales.
Set con = Server.CreateObject("ADODB.Connection")
con.Provider = "ADsDSOObject"
 
Set command = CreateObject("ADODB.Command")
Set command.ActiveConnection = con
 
command.CommandText = "SELECT AdsPath, cn FROM 'LDAP://OU=Sales,DC=Fabrikam,DC=com' WHERE objectClass = 'user'"
 
command.Properties("searchscope") = ADS_SCOPE_ONELEVEL
Set rs = command.Execute
While Not rs.EOF
    Set usr = GetObject(rs.Fields("AdsPath").Value)
    usr.Put "department", "1001"
    usr.SetInfo
    rs.MoveNext
Wend
```



 

 




