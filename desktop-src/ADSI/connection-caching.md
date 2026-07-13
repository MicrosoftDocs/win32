---
title: Connection Caching
description: When a connection to a server is made, the connection handle is cached on the client computer for that process until that connection is closed.
ms.assetid: 927afd35-8703-4234-b6a8-6320a3667532
ms.tgt_platform: multiple
keywords:
- connection caching ADSI
- connection caching
ms.topic: concept-article
ms.date: 03/12/2024
---

# Connection Caching

When a connection to a server is made, the connection handle is cached on the client computer for that process until that connection is closed. If the same server, port, and credentials are used in a subsequent connection, and only the **ADS_FAST_BIND** or **ADS_SERVER_BIND** authentication flags differ, ADSI will reuse the existing connection. ADSI performs this connection caching on a per-process basis.

To increase performance, reuse existing connections when possible.

The following is an example using IADs in Visual Basic (also see [Using the IADs Interfaces](using-the-iads-interfaces.md)):

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

The following alternative example shows how connection caching works using the [DirectoryEntry](/dotnet/api/system.directoryservices.directoryentry) object in .NET:

```csharp
// Connect to the server and maintain this handle to cache the connection.
using (DirectoryEntry? cachedConn = new DirectoryEntry("LDAP://MyMachine/DC=MyDomain,DC=Fabrikam,DC=com")) 
{
    DirectoryEntry? secondConn;
    string? cachedName;
    string? objName;

    cachedName = cachedConn.Properties["distinguishedName"].Value?.ToString();
    Debug.WriteLine(cachedName);

    // Reuse the connection to MyMachine opened by cachedConn.
    // Be aware that this line executes quickly because it is not required
    // to transmit over the network again.
    using (secondConn = new DirectoryEntry("LDAP://MyMachine/CN=Bob,CN=Users,DC=MyDomain,DC=Fabrikam,DC=com"))
    {
        objName = secondConn.Properties["distinguishedName"].Value?.ToString();
        Debug.WriteLine(objName);

        // Release the second connection.
        secondConn = null;

        // Reuse the connection to MyMachine opened by cachedConn again.
        secondConn = new DirectoryEntry("LDAP://MyMachine/CN=Administrator,CN=Users,DC=MyDomain,DC=Fabrikam,DC=com");

        objName = secondConn.Properties["distinguishedName"].Value?.ToString();
        Debug.WriteLine(objName);
    }
    // Release and dispose the second connection
}
// The connection to MyMachine is closed and disposed
```

## See also

[DirectoryEntry](/dotnet/api/system.directoryservices.directoryentry)

[Using the IADs Interfaces](using-the-iads-interfaces.md)
