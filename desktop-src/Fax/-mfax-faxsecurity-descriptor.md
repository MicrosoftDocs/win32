---
Description: The Descriptor property represents the security descriptor for a FaxServer object.
ms.assetid: 66911dcd-2c46-4ef3-ae77-cb94249e92e3
title: FaxSecurity.Descriptor property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxSecurity.Descriptor property

The **Descriptor** property represents the security descriptor for a [**FaxServer**](-mfax-faxserver.md) object.

This property is read/write.

## Syntax


```VB
Property Descriptor As Variant
```



## Property value

A **Variant** that specifies or receives the security descriptor. The security descriptor is a [SECURITY\_DESCRIPTOR](http://msdn.microsoft.com/library/en-us/secauthz/security/security_descriptor.asp) structure and is represented as a variant safe array of unsigned characters (**VT\_ARRAY** \| **Integer**).

## Remarks

The **Descriptor** property represents the security descriptor, which contains the rights explicitly granted to a user by the fax administrator. The [**GrantedRights**](-mfax-faxsecurity-grantedrights-vb.md) property reflects the user rights that the fax server grants based on the descriptor. Specifically, if a user has the access right [****farSUBMIT\_HIGH****](-mfax-fax-access-rights-enum.md), the user can send high-priority, normal-priority and low-priority faxes. If a user has the access right [****farSUBMIT\_NORMAL****](-mfax-fax-access-rights-enum.md), the user can send normal-priority and low-priority faxes.

To read this property, a user must have the [****farQUERY\_CONFIG****](-mfax-fax-access-rights-enum.md) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxSecurity**](-mfax-faxsecurity.md)
</dt> <dt>

[**IFaxSecurity::Descriptor**](-mfax-faxsecurity-descriptor-cpp.md)
</dt> </dl>

 

 




