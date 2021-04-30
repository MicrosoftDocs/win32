---
description: The WiaAddDevice function invokes the Scanner and Camera Installation Wizard UI. It is equivalent to running &\#0034;rundll32.exe sti\_ci.dll AddDevice&\#0034; from the command prompt.
ms.assetid: 83a1e22c-d751-4c8e-8f39-ec987042c745
title: WiaAddDevice function (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WiaAddDevice
api_type: 
- LibDef
api_location: 
- Wiaguid.lib
- Wiaguid.dll
---

# WiaAddDevice function

The **WiaAddDevice** function invokes the Scanner and Camera Installation Wizard UI. It is equivalent to running "rundll32.exe sti\_ci.dll AddDevice" from the command prompt.

## Syntax


```C++
void WINAPI WiaAddDevice(void);
```



## Parameters

This function has no parameters.

## Return value

This function does not return a value.

## Remarks

This function should be called with administrator credentials. When running under User Account Control (LUA), the process should be elevated.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>       |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



## See also

<dl> <dt>

[**InstallWiaDevice**](-wia-installwiadevice.md)
</dt> </dl>

 

 




