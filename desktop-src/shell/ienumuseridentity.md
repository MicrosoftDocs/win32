---
description: IEnumUserIdentity is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: df4b6235-e66a-4187-b1f9-33c042cae2f2
title: IEnumUserIdentity interface (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEnumUserIdentity
api_type: 
- COM
api_location: 
- Msident.dll
---

# IEnumUserIdentity interface

\[**IEnumUserIdentity** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Provides enumeration of all user identities present on the system.

## Members

The **IEnumUserIdentity** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IEnumUserIdentity** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumUserIdentity** interface has these methods.



| Method                                         | Description                                                                                                                  |
|:-----------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| [**Clone**](ienumuseridentity-clone.md)       | Deprecated. Gets a copy of the current enumeration.<br/>                                                               |
| [**GetCount**](ienumuseridentity-getcount.md) | Deprecated. Gets the count of user identities currently on the system.<br/>                                            |
| [**Next**](ienumuseridentity-next.md)         | Deprecated. Retrieves an array of user identity interfaces from the enumeration.<br/>                                  |
| [**Reset**](ienumuseridentity-reset.md)       | Deprecated. Resets the internal count of retrieved interfaces in the enumeration.<br/>                                 |
| [**Skip**](ienumuseridentity-skip.md)         | Deprecated. Skips a given number of user identity interfaces in the enumeration. Used when retrieving interfaces.<br/> |



 

## Remarks

To retrieve information about user identities present on the system, you can use this interface. From a [**IUserIdentityManager**](iuseridentitymanager.md) interface, you can call [**IUserIdentityManager::EnumIdentities**](iuseridentitymanager-enumidentities.md) to retrieve this interface.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows XP<br/>                                                                  |
| End of server support<br/>    | Windows Server 2003<br/>                                                         |
| Header<br/>                   | <dl> <dt>Msident.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msident.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msident.dll</dt> </dl> |



## See also

<dl> <dt>

[**IUserIdentityManager**](iuseridentitymanager.md)
</dt> </dl>

 

 
