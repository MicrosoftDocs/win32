---
title: Binding to Well-Known Objects Using WKGUID
description: This topic shows how to bind to objects using the WKGUID binding string.
ms.assetid: cc9846c4-415e-48ee-ae08-6631636d3a63
ms.tgt_platform: multiple
keywords:
- Binding to Well-Known Objects Using WKGUID AD
- Active Directory, using, binding, using WKGUID to bind to well-known objects
- well-known objects AD
- well-known objects AD , binding to using WKGUID
ms.topic: article
ms.date: 05/31/2018
---

# Binding to Well-Known Objects Using WKGUID

Containers can have one, or more, important subobjects that can be renamed or moved. It can be difficult to track these subobjects and build correct binding strings for them, especially if they are renamed or moved.

To support rename-safe binding to these objects within these containers, Active Directory Domain Services have two attributes: **wellKnownObjects** and **otherWellKnownObjects**. These attributes have an attribute syntax of ADSTYPE\_DN\_WITH\_BINARY. They allow multiple values and contain the GUID/DN tuples of well-known objects within the containers on which they are set. The Active Directory server maintains the distinguished name portion of each **wellKnownObjects** and **otherWellKnownObjects** entry so that it contains the current distinguished name of the object specified when the entry was created.

The **otherWellKnownObjects** property can be set and used on any object.

The **wellKnownObjects** property is used on the domainDNS and configuration containers. The **wellKnownObjects** property is a system-only property and can only be modified by the operating system.

The **domainDNS** container has the following well-known objects:

-   Users
-   Computers
-   System
-   Domain Controllers
-   Infrastructure
-   Deleted Objects
-   Lost and Found

The configuration container has the well-known object: Deleted Objects.

These objects are in every **domainDNS** and configuration container in an Active Directory Domain Service.

You can bind to a well-known object using the WKGUID binding format. Binding with WKGUID is only supported in Active Directory Domain Services, that is, the LDAP provider.

> [!IMPORTANT]
> Always use the WKGUID binding format to bind to the well-known objects, as listed above, in the domain and configuration containers. This ensures that these containers can be bound to even if they are moved or renamed.

 

The WKGUID binding string format is as follows:


```C++
LDAP://<servername>/<WKGUID=<XXXXX>,<container DN>>
```



"&lt;server name&gt;" is the directory server name. The "&lt;server name&gt;" is optional.

"&lt;XXXXX&gt;" is the string representation of the hexadecimal value of the GUID that represents the well-known object. The GUID string is specified in the "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" form and is not the same form as the GUID string produced by the [**StringFromGUID2**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromguid2) function, which takes the form "{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}". For more information and a code example that shows how to create a bindable string from a GUID, see [Example Code for Creating a Bindable String Representation of a GUID](example-code-for-creating-a-bindable-string-representation-of-a-guid.md).

To bind to an object specified in **otherWellKnownObjects** in an object, specify "&lt;XXXXX&gt;" as the bind string form of the well-known object GUID of the object. For more information, see [Reading an Object's objectGUID and Creating a String Representation of the GUID](reading-an-objectampaposs-objectguid-and-creating-a-string-representation-of-the-guid.md). For more information about setting the **otherWellKnownObjects** property on objects, see [Enabling Rename-Safe Binding with the otherWellKnownObjects Property](enabling-rename-safe-binding-with-the-otherwellknownobjects-property.md).

To bind to an object specified in **wellKnownObjects** in domainDNS or configuration containers, specify "&lt;XXXXX&gt;" as one of the following constants, listed in the following table, as defined in Ntdsapi.h.



| Container          | GUID Identifier                         |
|--------------------|-----------------------------------------|
| Users              | GUID\_USERS\_CONTAINER\_W               |
| Computers          | GUID\_COMPUTRS\_CONTAINER\_W            |
| System             | GUID\_SYSTEMS\_CONTAINER\_W             |
| Domain Controllers | GUID\_DOMAIN\_CONTROLLERS\_CONTAINER\_W |
| Infrastructure     | GUID\_INFRASTRUCTURE\_CONTAINER\_W      |
| Deleted Objects    | GUID\_DELETED\_OBJECTS\_CONTAINER\_W    |
| Lost and Found     | GUID\_LOSTANDFOUND\_CONTAINER\_W        |



 

For example, to bind to the user container in a domain, specify **GUID\_USERS\_CONTAINER\_W** as "&lt;XXXXX&gt;".

"&lt;container DN&gt;" is the distinguished name of the container object that has this object represented as a value in its **wellKnownObjects** property. For example, to bind to the users container in a domain, specify the domain distinguished name as the "&lt;container DN&gt;".

For example, to bind to the users container of the domain Fabrikam.com, use the following binding string.

``` syntax
LDAP://<WKGUID=a9d1ca15768811d1aded00c04fd8d5cd,dc=Fabrikam,dc=com>
```

For more information and a code example that shows how to bind to a well-known GUID, see [Example Code for Binding to Well Known Objects](example-code-for-binding-to-well-known-objects.md).

 

 