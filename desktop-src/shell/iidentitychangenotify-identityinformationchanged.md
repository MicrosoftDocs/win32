---
description: IdentityInformationChanged is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: 3aca8a98-3d12-482d-9991-d6b53adde522
title: IIdentityChangeNotify::IdentityInformationChanged method (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IIdentityChangeNotify.IdentityInformationChanged
api_type: 
- COM
api_location: 
- Msoe.dll
---

# IIdentityChangeNotify::IdentityInformationChanged method

\[**IdentityInformationChanged** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Called when information about a user identity has changed, or when a user identity has been added or deleted.

## Syntax


```C++
HRESULT IdentityInformationChanged(
   DWORD dwType
);
```



## Parameters

<dl> <dt>

*dwType* 
</dt> <dd>

Type: **DWORD**

A value that specifies the type of information changed, or the operation performed on an identity. Can be a combination of the following values.

<dt>



 (IIC\_CURRENT\_IDENTITY\_CHANGED)


</dt> <dd>

The current identity has been modified.

</dd> <dt>



 (IIC\_IDENTITY\_CHANGED)


</dt> <dd>

An identity has been modified.

</dd> <dt>



 (IIC\_IDENTITY\_DELETED)


</dt> <dd>

An identity has been deleted.

</dd> <dt>



 (IIC\_IDENTITY\_ADDED)


</dt> <dd>

A new identity has been added.

</dd> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

You may implement this method to provide custom behavior for your application when the list of user identities on the system has been modified.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows 2000 Professional<br/>                                                   |
| End of server support<br/>    | Windows 2000 Server<br/>                                                         |
| Header<br/>                   | <dl> <dt>Msident.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msident.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msoe.dll</dt> </dl>    |



 

 




