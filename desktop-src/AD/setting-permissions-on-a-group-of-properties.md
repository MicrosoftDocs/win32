---
title: Setting Permissions on a Group of Properties
description: Permissions can be applied to a group of properties.
ms.assetid: cb9f6c04-be94-45b4-ba84-2a79b7625fdd
ms.tgt_platform: multiple
keywords:
- Setting Permissions on a Group of Properties AD
ms.topic: article
ms.date: 05/31/2018
---

# Setting Permissions on a Group of Properties

Permissions can be applied to a group of properties. A property set is identified by the GUID in the [**rightsGUID**](/windows/desktop/ADSchema/a-rightsguid) attribute of a [**controlAccessRight**](/windows/desktop/ADSchema/c-controlaccessright) object. This GUID is set in the [**attributeSecurityGUID**](/windows/desktop/ADSchema/a-attributesecurityguid) attribute of the [**attributeSchema**](/windows/desktop/ADSchema/c-attributeschema) object of each attribute in the group.

The following procedure shows how to set permissions that apply to a group of object properties.

**To set permissions that apply to a group of object properties**

1.  Set the [**IADsAccessControlEntry.AccessMask**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) property to **ADS\_RIGHT\_DS\_READ\_PROP**, **ADS\_RIGHT\_DS\_WRITE\_PROP** or both values combined.
2.  Set the [**IADsAccessControlEntry.AceType**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) property to either **ADS\_ACETYPE\_ACCESS\_ALLOWED\_OBJECT** or **ADS\_ACETYPE\_ACCESS\_DENIED\_OBJECT**.
3.  Set the [**IADsAccessControlEntry.ObjectType**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) property to the GUID of the property set. This is the [**rightsGUID**](/windows/desktop/ADSchema/a-rightsguid) property of the [**controlAccessRight**](/windows/desktop/ADSchema/c-controlaccessright) object that identifies the property set. This GUID is also set as the [**attributeSecurityGUID**](/windows/desktop/ADSchema/a-attributesecurityguid) in the attributeSchema object of each property in the group.
4.  Set the [**IADsAccessControlEntry.Flags**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) property to **ADS\_FLAG\_OBJECT\_TYPE\_PRESENT**.

Be aware that you should not set the **ADS\_RIGHT\_DS\_CONTROL\_ACCESS** flag in the [**IADsAccessControlEntry.AccessMask**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) property. This flag is only used to specify a control access right.

For more information and a code example that can be used to set access rights for a property set, see [Example Code for Setting Permissions on a Group of Properties](example-code-for-setting-permissions-on-a-group-of-properties.md).

For more information about creating an ACE, see [Setting Access Rights on an Object](setting-access-rights-on-an-object.md).

For more information and a code example that can be used to set an ACE for a property set, see [Example Code for Setting an ACE on a Directory Object](example-code-for-setting-an-ace-on-a-directory-object.md).

 

 