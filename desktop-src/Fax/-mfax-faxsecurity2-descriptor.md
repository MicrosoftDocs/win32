---
Description: Represents the security descriptor for a IFaxServer2 interface.
ms.assetid: 9fda9779-6688-431c-8f06-8420d0263e0d
title: FaxSecurity2.Descriptor property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxSecurity2.Descriptor property

Represents the security descriptor for a [**IFaxServer2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxserver2) interface.

This property is read/write.

## Syntax


```VB
Property Descriptor As Variant
```



## Property value

A **Variant** that specifies or receives the security descriptor. The security descriptor is a [SECURITY\_DESCRIPTOR](http://msdn.microsoft.com/library/en-us/secauthz/security/security_descriptor.asp) structure and is represented as a variant safe array of unsigned characters (**VT\_ARRAY** \| **Integer**).

## Remarks

The **Descriptor** property represents the security descriptor, which contains the rights explicitly granted to a user by the fax administrator. The [**GrantedRights**](-mfax-faxsecurity2-grantedrights-vb.md) property reflects the user rights that the fax server grants based on the descriptor. Specifically, if a user has the access right [****far2SUBMIT\_HIGH****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum_2), the user can send high-priority, normal-priority and low-priority faxes. If a user has the access right [****far2SUBMIT\_NORMAL****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum_2), the user can send normal-priority and low-priority faxes.

To read and write this property, the user must have the [****far2MANAGE\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum_2) access right. Users with the [****far2QUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum_2) access right can read this property.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxSecurity2**](-mfax-faxsecurity2.md)
</dt> <dt>

[**IFaxSecurity2::Descriptor**](/previous-versions/windows/desktop/api/FaxComex/nf-faxcomex-ifaxsecurity2-get_descriptor)
</dt> </dl>

 

 




