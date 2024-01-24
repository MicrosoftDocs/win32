---
description: Checks that the online user profile is loaded.
ms.assetid: 4391664E-44D0-461D-84FF-E2B2410511BC
title: OnProfileLoaded function (Lsaidprov.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OnProfileLoaded
api_type: 
- HeaderDef
api_location: 
- Lsaidprov.h
---

# OnProfileLoaded function

Checks that the online user profile is loaded.

## Syntax


```C++
SEC_ENTRY OnProfileLoaded(
  _In_ PVOID   ProviderHandle,
  _In_ HANDLE  UserToken,
  _In_ BOOLEAN Loaded
);
```



## Parameters

<dl> <dt>

*ProviderHandle* \[in\]
</dt> <dd>

The provider handle.

</dd> <dt>

*UserToken* \[in\]
</dt> <dd>

Token of the user whose profile is being loaded or unloaded.

</dd> <dt>

*Loaded* \[in\]
</dt> <dd>

**TRUE** if the profile has been loaded.

</dd> </dl>

## Return value

If the function succeeds, the function returns STATUS\_SUCCESS.

If the function fails, the function returns a nonzero error code that is a provider-specific error for diagnostic purposes.

## Remarks

This function is called each time the [**LoadUserProfile**](/windows/win32/api/userenv/nf-userenv-loaduserprofilea) function is called. It is not synchronized with **LoadUserProfile**; that is, **LoadUserProfile** might have returned and the profile might have been unloaded by the time the function was called. This function can be called more than once even when the profile has been loaded. The identity provider must not assume that a call to this function with *Loaded* equal to TRUE will be followed by a call with *Loaded* equal to FALSE.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Lsaidprov.h</dt> </dl> |



 

 
