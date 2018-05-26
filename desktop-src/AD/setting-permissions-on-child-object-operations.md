---
title: Setting Permissions on Child Object Operations
description: Permissions, such as Create Child and Delete Child, can also be granted or denied for operations on all subobjects or subobjects of a specific class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: fe2f8939-7562-4c03-a7a9-3ac5fc3e81bb
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Setting Permissions on Child Object Operations AD
- objects AD , child, setting permissions on child object operations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Setting Permissions on Child Object Operations

Permissions, such as Create Child and Delete Child, can also be granted or denied for operations on all subobjects or subobjects of a specific class.

The following procedure can be used to set permissions for a specific subobject type.

**To set permissions for a specific subobject type**

1.  Set the [**IADsAccessControlEntry.AceType**](https://msdn.microsoft.com/library/aa705952) property to **ADS\_ACETYPE\_ACCESS\_ALLOWED\_OBJECT** or **ADS\_ACETYPE\_ACCESS\_DENIED\_OBJECT**.
2.  Set the [**IADsAccessControlEntry.ObjectType**](https://msdn.microsoft.com/library/aa705952) property to the GUID for object class. This is the **schemaIDGUID** property of the classSchema object that defines the object class. If the **ObjectType** property is **NULL**, the ACE applies to subobjects of any class.
3.  Set the [**IADsAccessControlEntry.Flags**](https://msdn.microsoft.com/library/aa705952) property to **ADS\_FLAG\_OBJECT\_TYPE\_PRESENT**.

For more information and a procedure for creating an ACE, see [Setting Access Rights on an Object](setting-access-rights-on-an-object.md).

For more information and a code example that can be used to set an ACE that controls child object operations, see [Example Code for Setting an ACE on a Directory Object](example-code-for-setting-an-ace-on-a-directory-object.md).

 

 




