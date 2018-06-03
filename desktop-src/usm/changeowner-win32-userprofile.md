---
title: ChangeOwner method of the Win32\_UserProfile class
description: Changes a user profile's owner.
ms.assetid: b073a403-9850-4a4d-ba64-320cad5d8fed
keywords:
- ChangeOwner method User State Manageability API
- ChangeOwner method User State Manageability API , Win32_UserProfile class
- Win32_UserProfile class User State Manageability API , ChangeOwner method
topic_type:
- apiref
api_name:
- Win32_UserProfile.ChangeOwner
api_location:
- Root\CIMv2
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ChangeOwner method of the Win32\_UserProfile class

Changes a user profile's owner.

## Syntax


```mof
uint32 ChangeOwner(
  [in] string NewOwnerSID,
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*NewOwnerSID* \[in\]
</dt> <dd>

The new owner's [security identifier](https://msdn.microsoft.com/library/windows/desktop/aa379571) (SID).

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Flag values that control what happens to the new owner's existing profile, if such a profile exists.



| Flag value                                                                                                                                                                                                                                                                                       | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ReplaceNewOwnerProfile"></span><span id="replacenewownerprofile"></span><span id="REPLACENEWOWNERPROFILE"></span><dl> <dt>**ReplaceNewOwnerProfile**</dt> <dt>0x00000001</dt> </dl> | If this flag is set and the new owner already has a profile, the new owner's existing profile will be replaced.<br/> If this flag is not set and the new owner already has a profile, the call to **ChangeOwner** will fail with `HRESULT_FROM_WIN32(ERROR_ALREADY_EXISTS)`.<br/> If the new owner doesn't already have a profile, this flag has no effect.<br/>                                         |
| <span id="DeleteReplacedProfile"></span><span id="deletereplacedprofile"></span><span id="DELETEREPLACEDPROFILE"></span><dl> <dt>**DeleteReplacedProfile**</dt> <dt>0x00000002</dt> </dl>     | If the **ReplaceNewOwnerProfile** flag is not set, this flag has no effect. <br/> Otherwise, if this flag is set and the new owner already has a profile, the new owner's existing profile will be deleted when it is replaced.<br/> If this flag is not set, the existing profile is replaced but not deleted. The replaced profile will not be enumerated, and no user will automatically use it.<br/> |



 

</dd> </dl>

## Requirements



|                                     |                                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                  |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                |
| MOF<br/>                      | <dl> <dt>UserProfileWmiProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_UserProfile**](win32-userprofile.md)
</dt> </dl>

 

 





