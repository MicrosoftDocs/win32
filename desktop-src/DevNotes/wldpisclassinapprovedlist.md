---
description: Calls the library to validate if a particular CLSID is safe to be called.
ms.assetid: 94C8731B-88FD-4240-BF5D-2CD67C41B063
title: WldpIsClassInApprovedList function (Wldp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WldpIsClassInApprovedList
api_type: 
- DllExport
api_location: 
- wldp.dll
---

# WldpIsClassInApprovedList function

Calls the library to validate if a particular **CLSID** is safe to be called. The function has no associated import library. You must use the LoadLibrary and GetProcAddress functions to dynamically link to wldp.dll.

## Syntax


```C++
HRESULT WINAPI WldpIsClassInApprovedList(
        REFCLSID               classID,
  _In_  PWLDP_HOST_INFORMATION hostInformation,
  _Out_ PBOOL                  isApproved,
        DWORD                  optionalFlags
);
```



## Parameters

<dl> <dt>

*classID* 
</dt> <dd>

The COM class ID to check for approval.

</dd> <dt>

*hostInformation* \[in\]
</dt> <dd>

A [**WLDP\_HOST\_INFORMATION**](wldp-host-information.md) structure identifying the host to be evaluated.

</dd> <dt>

*isApproved* \[out\]
</dt> <dd>

On successful completion, contains **TRUE** if the class ID is approved; otherwise, **FALSE**.

</dd> <dt>

*optionalFlags* 
</dt> <dd>

This parameter is reserved and must be set to zero.

</dd> </dl>

## Return value

This method returns **S\_OK** if successful or a failure code otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wldp.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Wldp.dll</dt> </dl> |



 

 




