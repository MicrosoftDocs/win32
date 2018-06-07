---
title: Setting Rights to Specific Types of Objects
description: The following procedure shows how to set an ACE that can be inherited only by a specific class of objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 42712458-69c7-4fe1-bfb3-b3fb28092a56
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- setting rights to types of objects AD
- objects AD , setting rights to
- Active Directory, using, security, setting rights to types of objects
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Setting Rights to Specific Types of Objects

The following procedure shows how to set an ACE that can be inherited only by a specific class of objects.

 **To set an ACE that can be inherited only by a specific class of objects**

1.  Set the [**IADsAccessControlEntry.AceType**](https://msdn.microsoft.com/library/aa705952) property to **ADS\_ACETYPE\_ACCESS\_ALLOWED\_OBJECT** or **ADS\_ACETYPE\_ACCESS\_DENIED\_OBJECT**.
2.  Set the [**IADsAccessControlEntry.AceFlags**](https://msdn.microsoft.com/library/aa705952) property to include the ADS\_ACEFLAG\_INHERIT\_ACE flag.
3.  Set the [**IADsAccessControlEntry.InheritedObjectType**](https://msdn.microsoft.com/library/aa705952) property to the **schemaIDGUID** of the object class that can inherit the ACE.
4.  Set the [**IADsAccessControlEntry.Flags**](https://msdn.microsoft.com/library/aa705952) property to **ADS\_FLAG\_INHERITED OBJECT\_TYPE\_PRESENT**.

> \[!Important\]  
> Set **ADS\_ACEFLAG\_INHERIT\_ACE** to cause the ACE to be inherited. In addition, you must set **ADS\_ACEFLAG\_INHERIT\_ONLY\_ACE** if the object type this ACE applies to does not match the object type of the container where the ACE is specified. If this is not done, the ACE will also become effective on the container and can grant unintended rights.

 

For more information and code examples that can be used to set this type of ACE, see [Example Code for Setting an ACE on a Directory Object](example-code-for-setting-an-ace-on-a-directory-object.md).

 

 




