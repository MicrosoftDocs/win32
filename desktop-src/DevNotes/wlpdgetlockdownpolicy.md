---
description: Calls the library to get the security state relative to the host, and script or msi to be used.
ms.assetid: 4CCDA3B7-7661-47F6-A015-720BDEAEDBB1
title: WldpGetLockdownPolicy function (Wldp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WldpGetLockdownPolicy
api_type: 
- DllExport
api_location: 
- wldp.dll
---

# WldpGetLockdownPolicy function

Calls the library to get the security state relative to the host, and script or msi to be used. The function has no associated import library. You must use the LoadLibrary and GetProcAddress functions to dynamically link to wldp.dll.

## Syntax


```C++
HRESULT WINAPI WldpGetLockdownPolicy(
  _In_opt_ PWLDP_HOST_INFORMATION hostInformation,
  _Out_    PDWORD                 lockdownState,
  _In_     DWORD                  lockdownFlags
);
```



## Parameters

<dl> <dt>

*hostInformation* \[in, optional\]
</dt> <dd>

A [**WLDP\_HOST\_INFORMATION**](wldp-host-information.md) structure identifying the host and source file to be evaluated.

</dd> <dt>

*lockdownState* \[out\]
</dt> <dd>

Provides the resulting policy secure value. If !WLDP_LOCKDOWN_IS_OFF, then UMCI is enabled. You can also check WLDP_LOCKDOWN_IS_AUDIT and WLDP_LOCKDOWN_IS_ENFORCE to determine if a policy is in audit or enforce mode.
</dd> <dt>

*lockdownFlags* \[in\]
</dt> <dd>

The following flag values are defined WLDP\_FLAGS\_SKIPSIGNATUREVALIDATION 0x00000100 – when set, skip the SaferIdentifyLevel validation, which will ignore whether a script is signed.

</dd> </dl>

## Return value

This method returns S\_OK if successful or a failure code otherwise.

## Remarks

When called with WLDP\_HOST\_INFORMATION.szSource = NULL, the generic policy for the host is returned.

When called with WLDP\_HOST\_INFORMATION.dwHostId = WLDP\_HOST\_ID\_GLOBAL, WLDP\_HOST\_INFORMATION.szSource must be NULL, and the function will return the global system policy.

The dwFlag WLDP\_FLAGS\_SKIPSIGNATUREVALIDATION can be used to skip the SaferIdentifyLevel() validation, which will ignore whether a script is signed.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wldp.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Wldp.dll</dt> </dl> |



 

 




