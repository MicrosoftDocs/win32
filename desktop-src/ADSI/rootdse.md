---
title: RootDSE (ADSI)
description: Each directory server has a unique entry called RootDSE. It provides data about the server, such as its capabilities, the LDAP version it supports, and the naming contexts it uses.
ms.assetid: bb6b7676-7042-453f-83f9-b0dd2e377a13
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# RootDSE (ADSI)

Each directory server has a unique entry called **RootDSE**. It provides data about the server, such as its capabilities, the LDAP version it supports, and the naming contexts it uses.

For example, to create a script, or application, that can run on any Windows domain environment. You can specify either the distinguished name, server name, or domain name when connecting to Active Directory. If you do not have this information, you can then use the **RootDSE** object to establish a connection. The following code example changes the domain description in any domain.


```VB
Set rootDSE = GetObject("LDAP://RootDSE")
Set dom = GetObject( "LDAP://" & rootDSE.Get("defaultNamingContext"))
dom.Put "description", "My domain"
dom.SetInfo
```



By getting the **defaultNamingContext** attribute from **RootDSE**, you can bind to the current domain, for example, the Fabrikam **defaultNamingContext** is DC=Fabrikam, DC=COM.

To enumerate the properties of the **RootDSE**, use the [**IADsPropertyList**](/windows/desktop/api/Iads/nn-iads-iadspropertylist) interface. [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject) cannot be used for this task.

For more information, see [Serverless Binding and RootDSE](/windows/desktop/AD/serverless-binding-and-rootdse).

 

 