---
description: Specifies the health state of an application.
ms.assetid: CA06AA34-A549-4CFC-9B52-D2E0B200C3E9
title: APPLICATION_STATE enumeration
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- APPLICATION_STATE
api_type: 
- IDLDef
api_location: 
- VmApplicationHealthMonitor.idl
---

# APPLICATION\_STATE enumeration

Specifies the health state of an application.

## Syntax


```C++
typedef enum _APPLICATION_STATE { 
  ApplicationStateHealthy   = 0,
  ApplicationStateCritical
} APPLICATION_STATE, *PAPPLICATION_STATE;
```



## Constants

<dl> <dt>

<span id="ApplicationStateHealthy"></span><span id="applicationstatehealthy"></span><span id="APPLICATIONSTATEHEALTHY"></span>**ApplicationStateHealthy**
</dt> <dd>

The application state is healthy.

</dd> <dt>

<span id="ApplicationStateCritical"></span><span id="applicationstatecritical"></span><span id="APPLICATIONSTATECRITICAL"></span>**ApplicationStateCritical**
</dt> <dd>

The application state is critical.

</dd> </dl>

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

[**SetApplicationState**](ivmapplicationhealthmonitor-setapplicationstate.md)
</dt> </dl>

 

 




