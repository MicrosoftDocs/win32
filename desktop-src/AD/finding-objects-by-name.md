---
title: Finding Objects by Name
description: Most objects in Active Directory Domain Services use the cn property as their naming attribute.
ms.assetid: c5df7403-23bc-440e-8cd6-215ab8037aed
ms.tgt_platform: multiple
keywords:
- Active Directory, using, searching, by name
- object AD , searching by name
- Finding Objects by Name
ms.topic: article
ms.date: 05/31/2018
---

# Finding Objects by Name

Most objects in Active Directory Domain Services use the **cn** property as their naming attribute. Some objects, however, use a naming attribute other than **cn**. For example, a domain controller uses the **domainDNS** property for the naming attribute and an organizational unit uses the **organizationalUnit** property for the naming attribute. To avoid having to use a different naming attribute for different object types, the **name** property, which contains the relative distinguished name of the object, should be used to search for objects by name.

## Examples

The following code examples show different query strings that can be used to find objects by name.

The following query string finds all objects with a name that begins with "Jeff".


```C++
(name=Jeff*)
```



The following query string finds all computer objects with a name that begins with "leased" or "corp".


```C++
(&(objectCategory=computer)(|(name=leased*)(name=corp*)))
```



The following query string finds all users and with a name that begins with "Karen" or "Jeff".


```C++
(&(&(objectClass=user)(objectCategory=person))(|(name=Karen*)(name=Jeff*)))
```



 

 




