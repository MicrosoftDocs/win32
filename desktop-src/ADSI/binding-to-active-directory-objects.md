---
title: Binding to Active Directory Objects
description: Before you continue with this scenario, you must understand how ADSI objects are named in Active Directory, and how to bind them. Binding an ADSI object connects the object with the directory service, and allows you to access the methods of the object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '0d8d8f1c-786f-4d87-977c-91a167bcf118'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
---

# Binding to Active Directory Objects

Before you continue with this scenario, you must understand how ADSI objects are named in Active Directory, and how to bind them. Binding an ADSI object connects the object with the directory service, and allows you to access the methods of the object.

## ADsPath

An ADSI object is uniquely identified by its binding string, which is also referred to as an ADsPath. An ADsPath is a combination of a programmatic identifier (progID) of the ADSI provider, and the distinguished name (DN) of the object.

Here's the format of an ADsPath:

"progID://DN"

-   pogID — the programmatic identifier of the ADSI provider, such as LDAP or WinNT.

-   :// — separates the progID from the DN.

-   DN — the distinguished name of the ADSI object, which is the full path of the object, where the path consists of relative distinguished names (RDNs).

An RDN is the name of the object without the path, and is unique from its sibling objects. An RDN consists of an attribute ID and value, such as "DC=Fabrikam", where DC is the attribute, and Fabrikam is the value. DC is an RDN attribute ID that stands for domain component.

Here’s an example of an ADsPath:

"LDAP://DC=Fabrikam,DC=Com"

## Binding the object

Here's how you can bind the domain object in this scenario:


```VB
Set dom = GetObject("LDAP://DC=Fabrikam,DC=Com")
```



When you run this code example, ADSI uses the DN to determine the ADSI objects to bind. After ADSI binds these objects, you can access their methods. The previous code example binds a domain object to [**IADs**](iads.md) and [**IADsContainer**](iadscontainer.md). You can now use methods on those interfaces such as [**Get**](iads-get.md), [**Put**](iads-put.md), [**Create**](iadscontainer-create.md), [**Delete**](iadscontainer-delete.md), and [**MoveHere**](iadscontainer-movehere.md).

After you bind a domain object, you can print some of its attributes:


```VB
Debug.Print dom.Get("Name")
Debug.Print dom.Get("whenCreated")
```



For more information about ADsPath, see [Binding String](binding-string.md). For more information about binding, see [Binding to an ADSI Object](binding-to-an-adsi-object.md).

## Related topics

<dl> <dt>

[Creating an Organizational Unit](creating-an-organizational-unit.md)
</dt> </dl>

 

 




