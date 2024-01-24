---
description: Resets the health state for all applications in a virtual machine.
ms.assetid: DB0B2FB3-87EB-44B2-9C4E-849BCE594E89
title: IVmApplicationHealthMonitor::ResetAllApplicationState method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IVmApplicationHealthMonitor.ResetAllApplicationState
api_type: 
- COM
api_location: 
- VmApplicationHealthMonitor.idl
---

# IVmApplicationHealthMonitor::ResetAllApplicationState method

Resets the health state for all applications in a virtual machine. If successful, the health state for all monitored applications will be set to **ApplicationStateHealthy**.

## Syntax


```C++
HRESULT ResetAllApplicationState();
```



## Parameters

This method has no parameters.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

To use this programming element, the Windows 8 integration components must be installed on the virtual machine that the application is running in.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                      |
| Version<br/>                  | Integration components for Windows 8<br/>                                                           |
| IDL<br/>                      | <dl> <dt>VmApplicationHealthMonitor.idl</dt> </dl> |



## See also

<dl> <dt>

[**IVmApplicationHealthMonitor**](ivmapplicationhealthmonitor.md)
</dt> </dl>

 

 




