---
title: Enabling Rename-Safe Binding with the otherWellKnownObjects Property
description: Objects of the Container class have an otherWellKnownObjects attribute that you can use to associate a GUID with the distinguished name (DN) of a child object in the container.
ms.assetid: 54f7468b-03e5-46b9-8b43-e3571dccdceb
ms.tgt_platform: multiple
keywords:
- otherWellKnownObjects property
- otherWellKnownObjects property, using for rename-safe binding
- Active Directory, using, binding, rename-safe binding
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Rename-Safe Binding with the otherWellKnownObjects Property

Objects of the Container class have an **otherWellKnownObjects** attribute that you can use to associate a GUID with the distinguished name (DN) of a child object in the container. If the child object is moved or renamed, the Active Directory server updates the DN in the **otherWellKnownObjects** value for that child object. This enables use of the WKGUID binding feature to bind to the child object using the GUID and the DN of the container rather than the child object's DN.

The **otherWellKnownObjects** attribute is equivalent to the **wellKnownObjects** attribute except that applications and services can write an **otherWellKnownObjects** value, but only the system can write **wellKnownObjects**.

Using **otherWellKnownObjects** attribute and WKGUID binding is beneficial in the following situations where rename-safe binding is required in relation to a specific container object.

If a container object contains other important objects, or if important objects can be renamed or moved.

If the important objects exist for each instance of the container object. For example, the system uses the **wellKnownObjects** attribute of each **domainDNS** object to store a value for the Users container, which exists in every instance of a **domainDNS** object. This enables applications to bind to the Users container in a rename-safe way by specifying the well-known GUID and the DN of the **domainDNS** container. Applications can use a container's **otherWellKnownObjects** attribute similarly.

If you require rename-safe binding and/or search capability on the important objects.

**To add rename-safe binding and search capabilities**

1.  Add a value to the **otherWellKnownObjects** property of the container object when the important object is created within that container. The value contains the GUID that represents the well-known object. Be aware that this is not the **objectGUID** and the **distinguishedName** for that object.
2.  Use the WKGUID binding feature to bind to or search the important object.

The **otherWellKnownObjects** attribute can have multiple values and contains the GUID/DN tuples of well-known objects within the containers on which they are set. The **otherWellKnownObjects** attribute has the DNWithBinary syntax in which values have the following form:


```C++
B:<char count>:<well known GUID>:<object DN>
```



In this example, "&lt;char count&gt;" is the count of hexadecimal digits in "&lt;well known GUID&gt;", which is 32 (number of hex digits in a GUID) for both **otherWellKnownObjects** and **wellKnownObjects**. "&lt;well known GUID&gt;" is the hexadecimal digit representation of the well-known GUID. "&lt;object DN&gt;" is the distinguished name of the object represented by this WKO value. The server maintains the ObjectDN portion of each **wellKnownObjects** and **otherWellKnownObjects** value so that it contains the current distinguished name of the object originally specified when the value was created.

For example, if {df447b5e-aa5b-11d2-8d53-00c04f79ab81} is the well-known GUID of the MyObject object in the MyContainer container in the Fabrikam.com domain, the **otherWellKnownObjects** value would specify the well-known GUID and the DN of MyObject:


```C++
B:32:df447b5eaa5b11d28d5300c04f79ab81:cn=MyObject,cn=MyContainer,dc=Fabrikam,dc=com
```



To bind to this object, use the following WKGUID binding string that specifies the well-known GUID of the object and the DN of the container:


```C++
LDAP://<WKGUID=df447b5eaa5b11d28d5300c04f79ab81,cn=MyContainer,dc=Fabrikam,dc=com>
```



After binding to this object, you can use the ADSI COM interfaces to search, read, modify, or delete the object.

For more information and a code example that shows how to add an object to the **otherWellKnownObjects** attribute, see [Example Code for Creating a Container Object](example-code-for-creating-a-container-object.md).

 

 




