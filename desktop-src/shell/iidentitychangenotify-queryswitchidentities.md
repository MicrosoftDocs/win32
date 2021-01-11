---
description: Called when the current user has requested that their user identity be switched, but before the switch occurs.
ms.assetid: f159b829-623c-4348-9692-7317663811a7
title: IIdentityChangeNotify::QuerySwitchIdentities method (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IIdentityChangeNotify.QuerySwitchIdentities
api_type: 
- COM
api_location: 
- Msoe.dll
---

# IIdentityChangeNotify::QuerySwitchIdentities method

\[**QuerySwitchIdentities** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Called when the current user has requested that their user identity be switched, but before the switch occurs.

## Syntax


```C++
HRESULT QuerySwitchIdentities();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Result of the switch query. If the switch should proceed, return S\_OK. Otherwise, return E\_PROCESS\_CANCELLED\_SWITCH to indicate that the user identity switch should be aborted.

## Remarks

You may implement this method to provide custom behavior for your application when a user requests that identities be switched. You can stop the pending identity switch by returning the value E\_PROCESS\_CANCELLED\_SWITCH.

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



## See also

<dl> <dt>

[**IIdentityChangeNotify**](iidentitychangenotify.md)
</dt> <dt>

[**IIdentityChangeNotify::SwitchIdentities**](iidentitychangenotify-switchidentities.md)
</dt> </dl>

 

 




