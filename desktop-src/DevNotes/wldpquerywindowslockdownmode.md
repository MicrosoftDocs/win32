---
Description: 'Retrieves the current Windows secure mode. Windows can be in locked mode, unlocked normal mode, or trial mode.'
ms.assetid: 'FD280818-C6DE-4CEA-A772-E239A8DB891F'
title: WldpQueryWindowsLockdownMode function
---

# WldpQueryWindowsLockdownMode function

Retrieves the current Windows secure mode. Windows can be in locked mode, unlocked normal mode, or trial mode.

## Syntax


```C++
 WINAPI WldpQueryWindowsLockdownMode(
  _Out_ PWLDP_WINDOWS_LOCKDOWN_MODE lockdownMode
);
```



## Parameters

<dl> <dt>

*lockdownMode* \[out\]
</dt> <dd>

On success, returns a [**PWLDP\_WINDOWS\_LOCKDOWN\_MODE**](wldp-windows-lockdown-mode.md) that indicates the secure mode for the current Windows 10 device.

</dd> </dl>

## Return value

This method returns **S\_OK** if successful or a failure code otherwise.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1803 \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wldp.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Wldp.dll</dt> </dl> |



 

 




