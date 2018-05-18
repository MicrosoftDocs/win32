---
title: Setting Permissions on a Group of Properties
description: Permissions can be applied to a group of properties.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'cb9f6c04-be94-45b4-ba84-2a79b7625fdd'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Setting Permissions on a Group of Properties AD"]
---

# Setting Permissions on a Group of Properties

Permissions can be applied to a group of properties. A property set is identified by the GUID in the [**rightsGUID**](https://msdn.microsoft.com/library/ms679464) attribute of a [**controlAccessRight**](https://msdn.microsoft.com/library/ms681001) object. This GUID is set in the [**attributeSecurityGUID**](https://msdn.microsoft.com/library/ms675235) attribute of the [**attributeSchema**](https://msdn.microsoft.com/library/ms680969) object of each attribute in the group.

The following procedure shows how to set permissions that apply to a group of object properties.

**To set permissions that apply to a group of object properties**

1.  Set the [**IADsAccessControlEntry.AccessMask**](https://msdn.microsoft.com/library/aa705952) property to **ADS\_RIGHT\_DS\_READ\_PROP**, **ADS\_RIGHT\_DS\_WRITE\_PROP** or both values combined.
2.  Set the [**IADsAccessControlEntry.AceType**](https://msdn.microsoft.com/library/aa705952) property to either **ADS\_ACETYPE\_ACCESS\_ALLOWED\_OBJECT** or **ADS\_ACETYPE\_ACCESS\_DENIED\_OBJECT**.
3.  Set the [**IADsAccessControlEntry.ObjectType**](https://msdn.microsoft.com/library/aa705952) property to the GUID of the property set. This is the [**rightsGUID**](https://msdn.microsoft.com/library/ms679464) property of the [**controlAccessRight**](https://msdn.microsoft.com/library/ms681001) object that identifies the property set. This GUID is also set as the [**attributeSecurityGUID**](https://msdn.microsoft.com/library/ms675235) in the attributeSchema object of each property in the group.
4.  Set the [**IADsAccessControlEntry.Flags**](https://msdn.microsoft.com/library/aa705952) property to **ADS\_FLAG\_OBJECT\_TYPE\_PRESENT**.

Be aware that you should not set the **ADS\_RIGHT\_DS\_CONTROL\_ACCESS** flag in the [**IADsAccessControlEntry.AccessMask**](https://msdn.microsoft.com/library/aa705952) property. This flag is only used to specify a control access right.

For more information and a code example that can be used to set access rights for a property set, see [Example Code for Setting Permissions on a Group of Properties](example-code-for-setting-permissions-on-a-group-of-properties.md).

For more information about creating an ACE, see [Setting Access Rights on an Object](setting-access-rights-on-an-object.md).

For more information and a code example that can be used to set an ACE for a property set, see [Example Code for Setting an ACE on a Directory Object](example-code-for-setting-an-ace-on-a-directory-object.md).

 

 




