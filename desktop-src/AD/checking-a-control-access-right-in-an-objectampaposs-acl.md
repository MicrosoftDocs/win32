---
title: Checking a Control Access Right in an Object's ACL
description: To check a control access right on an object's ACL, use the AccessCheckByTypeResultList function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5a609622-6a1a-46ae-a336-afec504225c7
ms.tgt_platform: multiple
keywords:
- Checking a Control Access Right in an Object ACL AD
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Checking a Control Access Right in an Object's ACL

To check a control access right on an object's ACL, use the [**AccessCheckByTypeResultList**](https://msdn.microsoft.com/library/windows/desktop/aa374836) function. To use this function, an application requires a pointer to the [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/desktop/aa379561) for the object instead of an [**IADsSecurityDescriptor**](https://msdn.microsoft.com/library/aa706128) interface to an ADSI security descriptor COM object.

Use the following steps to check access for an controlled access right on an object:

1.  Get an [**IDirectoryObject**](https://msdn.microsoft.com/library/aa746355) interface pointer to the object.
2.  Use the [**IDirectoryObject::GetObjectAttributes**](https://msdn.microsoft.com/library/aa746358) method to get the security descriptor of the object. The name of the property containing the security descriptor is [**nTSecurityDescriptor**](https://msdn.microsoft.com/library/ms679006). The property is returned as a pointer to a [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/desktop/aa379561) structure.
3.  Use the [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/desktop/aa379561) structure with the [**AccessCheckByTypeResultList**](https://msdn.microsoft.com/library/windows/desktop/aa374836) function to check the permissions for the specified control access right for the specified client.

The example code in [Example Code for Checking a Control Access Right in an Object's ACL](example-code-for-checking-a-control-access-right-in-an-objectampaposs-acl.md) shows, in detail, how to do this.

 

 




