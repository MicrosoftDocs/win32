---
Description: Retrieves a combination of the fax server access rights granted to the user referencing this property.
ms.assetid: 3b75a295-31fd-4381-b97d-1847d842ec6c
title: FaxSecurity2.GrantedRights property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxSecurity2.GrantedRights property

Retrieves a combination of the fax server access rights granted to the user referencing this property. For example, some users have permission to submit fax jobs with high priority while others have permission to submit jobs with normal or low priority only.

This property is read-only.

## Syntax


```VB
Property GrantedRights As Long
```



## Property value

A **Long** that receives the bitwise combination of access rights granted to the user. For possible values, see [**FAX\_ACCESS\_RIGHTS\_ENUM\_2**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum_2?branch=master).

## Remarks

The **GrantedRights** property reflects rights granted by the fax server, while the [**Descriptor**](-mfax-faxsecurity2-descriptor.md) property represents the security descriptor, which contains the rights explicitly granted to a user by the fax administrator.

To read this property, a user must have the [****far2QUERY\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum_2?branch=master) access right.

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

[**IFaxSecurity2**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxsecurity2?branch=master)
</dt> </dl>

 

 




