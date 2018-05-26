---
title: Adding Users to a Group
description: Joe Worden, the enterprise administrator, will now add Julie Bankert to the Management group. To add an object to a group, use the IADsGroup.Add method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 57a9f5b2-2e48-401d-8d3b-eceb711a1df9
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Adding Users to a Group ADSI
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Adding Users to a Group

Joe Worden, the enterprise administrator, will now add Julie Bankert to the Management group. To add an object to a group, use the [**IADsGroup.Add**](/windows/win32/Iads/nf-iads-iadsgroup-add?branch=master) method.


```VB
Dim grp as IADsGroup

Set grp = GetObject("LDAP://CN=Management,OU=Sales,DC=Fabrikam,DC=COM") 
grp.Add ("LDAP://CN=Julie Bankert,OU=Sales,DC=Fabrikam,DC=COM")
```



## Related topics

<dl> <dt>

[Creating a New Group](creating-a-new-group.md)
</dt> </dl>

 

 




