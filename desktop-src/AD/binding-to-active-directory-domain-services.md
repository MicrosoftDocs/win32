---
title: Binding to Active Directory Domain Services
description: In Active Directory Domain Services, the act of associating a programmatic object with a specific Active Directory Domain Services object is known as binding.
ms.assetid: f48de4d4-c53a-4e40-a34e-4236c3e6cb21
ms.tgt_platform: multiple
keywords:
- binding to Active Directory Domain Services Active Directory
- Active Directory Domain Services Active Directory , binding to
ms.topic: article
ms.date: 05/31/2018
---

# Binding to Active Directory Domain Services

In Active Directory Domain Services, the act of associating a programmatic object with a specific Active Directory Domain Services object is known as *binding*. When a programmatic object, such as an [**IADs**](/windows/desktop/api/iads/nn-iads-iads) or [DirectoryEntry](/dotnet/api/system.directoryservices.directoryentry?view=dotnet-plat-ext-3.1&preserve-view=true) object, is associated with a specific directory object, the programmatic object is considered to be *bound to* the directory object.

## Binding Functions and Methods

The method for programmatically binding to an Active Directory object will depend on the programming technology that is used. For more information about binding to objects in Active Directory Domain Services with a specific programming technology, see the topics listed in the following table.



| Programming technology                                                                       | For more information                                                           |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [Active Directory Service Interfaces](/windows/desktop/ADSI/active-directory-service-interfaces-adsi)         | [Binding to an ADSI Object](/windows/desktop/ADSI/binding-to-an-adsi-object)                    |
| [Lightweight Directory Access Protocol](/previous-versions/windows/desktop/ldap/lightweight-directory-access-protocol-ldap-api) | [Establishing an LDAP Session](/previous-versions/windows/desktop/ldap/establishing-an-ldap-session)              |
| [System.DirectoryServices](/dotnet/api/system.directoryservices)                 | [Binding to Directory Objects](/previous-versions/ms180840(v=vs.90)) |



 

## Binding Strings

All bind functions and methods require a binding string. The form of the binding string depends on the provider. Active Directory Domain Services are supported by two providers, LDAP and WinNT.

Beginning with Windows 2000, the LDAP provider is used to access Active Directory Domain Services. The LDAP binding string can take one of the following forms:

-   "LDAP://\<host name\>/\<object name\>"
-   "GC://\<host name\>/\<object name\>"

In the examples above, "LDAP:" specifies the LDAP provider. "GC:" uses the LDAP provider to bind to the Global Catalog service to execute fast queries.

"&lt;host name&gt;" specifies the server to bind to and is optional. If possible, do not specify a server. It is also possible to bind to an object in a different domain. To do this pass the domain naming system (DNS) name of the target domain for "&lt;host name&gt;". For example, to bind to the Users container in the domain2 domain of fabrikam.com, the binding string would be "LDAP://domain2.fabrikam.com/CN=Users,DC=domain2,DC=fabrikam,DC=com".

"&lt;object name&gt;" represents a specific object in Active Directory Domain Services. The object name can be a distinguished name or an object GUID.

For more information about LDAP binding strings, see [LDAP ADsPath](/windows/desktop/ADSI/ldap-adspath).

For Windows NT 4.0, the WinNT provider is used for access to directory data such as users, user groups, computers, services, and other network objects in the Windows 2000. The WinNT provider on Windows 2000 and later systems has limited functionality compared to the LDAP provider. For more information about WinNT binding strings, see [WinNT ADsPath](/windows/desktop/ADSI/winnt-adspath).

An ADsPath of "LDAP://" or "GC://" can be used to bind to the root of the namespace. When bound to the root of the namespace, the supplied namespace object contains no properties and contains the domain object for LDAP and a container object containing a partial replica of all domains in the forest for GC.

For more information about binding in Active Directory Domain Services, see:

-   [Serverless Binding and RootDSE](serverless-binding-and-rootdse.md)
-   [Binding to the Global Catalog](binding-to-the-global-catalog.md)
-   [Using objectGUID to Bind to an Object](using-objectguid-to-bind-to-an-object.md)
-   [Binding to Well-Known Objects Using WKGUID](binding-to-well-known-objects-using-wkguid.md)
-   [Binding to an Object Using a SID](binding-to-an-object-using-a-sid.md)
-   [Enabling Rename-Safe Binding with the otherWellKnownObjects Property](enabling-rename-safe-binding-with-the-otherwellknownobjects-property.md)
-   [Authentication](authentication.md)

 

 
