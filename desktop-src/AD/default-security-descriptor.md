---
title: Default Security Descriptor
description: With Active Directory Domain Services, you can also specify default security for each type of object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 6642c966-c163-4d63-8707-62a545d15094
ms.tgt_platform: multiple
keywords:
- Default Security Descriptor AD
- security descriptors AD , default
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Default Security Descriptor

With Active Directory Domain Services, you can also specify default security for each type of object. This is specified in the [**defaultSecurityDescriptor**](https://msdn.microsoft.com/library/ms675488) attribute in the [**classSchema**](https://msdn.microsoft.com/library/ms680982) object definition in the [Active Directory schema](active-directory-schema.md). This security descriptor is used to provide default protection on the object if there is no security descriptor specified during the creation of the object.

> [!Note]  
> ACEs from a default security descriptor are handled as if they were specified as part of object creation. Therefore, the default ACEs are placed preceding inherited ACEs and override them as appropriate. For more information, see [Order of ACEs in a DACL](https://msdn.microsoft.com/library/windows/desktop/aa379298).

 

The [**defaultSecurityDescriptor**](https://msdn.microsoft.com/library/ms675488) is specified in a special string format using the [Security Descriptor Definition Language](https://msdn.microsoft.com/library/windows/desktop/aa379567) (SDDL). Two functions can be used to convert binary form of the security descriptor to string format and vice versa. These functions are:

-   [ConvertSecurityDescriptorToStringSecurityDescriptor](https://msdn.microsoft.com/library/windows/desktop/aa376397)
-   [ConvertStringSecurityDescriptorToSecurityDescriptor](https://msdn.microsoft.com/library/windows/desktop/aa376401)

For more information and the default security descriptors of the predefined object classes, see the class reference pages in the Active Directory Schema Reference of the [Active Directory Domain Services Reference](active-directory-domain-services-reference.md).

For more information and a code example that reads or modifies the [**defaultSecurityDescriptor**](https://msdn.microsoft.com/library/ms675488) property of an object class, see [Reading the defaultSecurityDescriptor for an Object Class](reading-the-defaultsecuritydescriptor-for-an-object-class.md) and [Modifying the defaultSecurityDescriptor for an Object Class](modifying-the-defaultsecuritydescriptor-for-an-object-class.md).

 

 




