---
title: Connection Caching
description: When a connection to a server is made, the connection handle is cached on the client computer for that process until that connection is closed.
ms.assetid: 927afd35-8703-4234-b6a8-6320a3667532
ms.tgt_platform: multiple
keywords:
- connection caching ADSI
- connection caching
ms.topic: article
ms.date: 05/31/2018
---

# Connection Caching

When a connection to a server is made, the connection handle is cached on the client computer for that process until that connection is closed. If the same server, port, and credentials are used in a subsequent connection, and only the **ADS\_FAST\_BIND** or **ADS\_SERVER\_BIND** authentication flags differ, ADSI will reuse the existing connection. ADSI performs this connection caching on a per-process basis.

To increase performance, reuse existing connections when possible.

The following code example shows how connection caching works.


```VB
Dim cachedConn As IADs
Dim obj As IADs
Dim cachedName As String
Dim objName As String
 
' Connect to the server and maintain this handle to cache the connection.
Set cachedConn = GetObject("LDAP://MyMachine/DC=MyDomain,DC=Fabrikam,DC=com")
 
cachedName = cachedConn.Get("distinguishedName")
Debug.Print (cachedName)
 
' Reuse the connection to MyMachine opened by cachedConn.
' Be aware that this line executes quickly because it is not required
' to transmit over the network again.
Set obj = GetObject("LDAP://MyMachine/CN=Bob,CN=Users,DC=MyDomain,DC=Fabrikam,DC=com")
 
objName = obj.Get("distinguishedName")
Debug.Print (objName)
 
' Release the second connection.
Set obj = Nothing
 
' Reuse the connection to MyMachine opened by cachedConn again.
Set obj = GetObject("LDAP://MyMachine/CN=Administrator,CN=Users,DC=MyDomain,DC=Fabrikam,DC=com")
 
objName = obj.Get("distinguishedName")
Debug.Print (objName)
 
' Release the second connection again.
Set obj = Nothing
 
' Release the first connection.
Set cachedConn = Nothing
 
' The connection to MyMachine is closed.
```



 

 




