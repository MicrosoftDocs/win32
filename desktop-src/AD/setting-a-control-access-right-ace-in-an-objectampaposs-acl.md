---
title: Setting a Control Access Right ACE in an Object's ACL
description: Using ADSI, you set a control access right ACE just as you would a property-specific ACE, except that the IADsAccessControlEntry.ObjectType property is the rightsGUID of the control access right.
ms.assetid: 454dc372-47b0-457d-8660-644fcfa59be8
ms.tgt_platform: multiple
keywords:
- Setting a Control Access Right ACE in an Object's ACL
ms.topic: article
ms.date: 05/31/2018
---

# Setting a Control Access Right ACE in an Object's ACL

Using ADSI, you set a control access right ACE just as you would a property-specific ACE, except that the [**IADsAccessControlEntry.ObjectType**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) property is the **rightsGUID** of the control access right. Be aware that you can also use the Win32 security APIs to set ACLs on directory objects.

The following table lists the [**IADsAccessControlEntry**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrolentry) properties for control access rights that can be used to set properties for an ACE.



| Property                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AccessMask**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) | For control access rights that control extended rights access to special operations, AccessMask must contain the **ADS\_RIGHT\_DS\_CONTROL\_ACCESS** flag. For control access rights that define a property set, AccessMask contains **ADS\_RIGHT\_DS\_READ\_PROP** and/or **ADS\_RIGHT\_DS\_WRITE\_PROP**.<br/> For control access rights that control validated writes, [**AccessMask**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) contains **ADS\_RIGHT\_DS\_SELF**.<br/> |
| [**Flags**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods)      | This value must include the **ADS\_FLAG\_OBJECT\_TYPE\_PRESENT** flag.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**ObjectType**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) | This value must be the [**StringFromGUID2**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromguid2) format of the **rightsGUID** attribute of the control access right. Be aware that, in an ACE, the GUID string must include the starting and terminating curly braces even though the **rightsGUID** attribute of the **controlAccessRight** object does not include the curly braces.                                                                                                                                     |
| [**AceType**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods)    | Either **ADS\_ACETYPE\_ACCESS\_ALLOWED\_OBJECT** to grant the trustee the access control right or **ADS\_ACETYPE\_ACCESS\_DENIED\_OBJECT** to deny the trustee the control access right.                                                                                                                                                                                                                                                                                                     |
| [**Trustee**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods)    | The security principal, for example user, group, computer, and so on, to which the ACE applies.                                                                                                                                                                                                                                                                                                                                                                                              |



 

For more information about creating an ACE, see [Setting Access Rights on an Object](setting-access-rights-on-an-object.md).

For more information and a code example for setting an ACE, see [Example Code for Setting an ACE on a Directory Object](example-code-for-setting-an-ace-on-a-directory-object.md).

 

