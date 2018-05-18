---
title: Access Control and Object Creation
description: The Active Directory server will fail to create a child object if the caller does not have the ADS\_RIGHT\_DS\_CREATE\_CHILD for that object type on the parent container.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '52f56e2a-580c-44b5-ba97-21388f6258bc'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Access Control and Object Creation AD"]
---

# Access Control and Object Creation

The Active Directory server will fail to create a child object if the caller does not have the **ADS\_RIGHT\_DS\_CREATE\_CHILD** for that object type on the parent container. To determine the types of child objects that the caller can create in a directory object, read the object's **allowedChildClassesEffective** attribute.

When you use the [**IADsContainer::Create**](https://msdn.microsoft.com/library/aa705987) method to create a child object, the object is not made persistent until [**IADs::SetInfo**](https://msdn.microsoft.com/library/aa746354) is called on the new object. Between the **Create** and **SetInfo** calls, the creating thread can put values into any of the new object's properties. After the **SetInfo** call, the creating thread does not necessarily have the access rights to set the new object's properties. To ensure that the caller has these rights, specify an explicit security descriptor during creation. The DACL should have an ACE that gives the caller the necessary access rights on the object.

For more information about access control and object creation, see [How Security Descriptors are Set on New Directory Objects](how-security-descriptors-are-set-on-new-directory-objects.md).

 

 




