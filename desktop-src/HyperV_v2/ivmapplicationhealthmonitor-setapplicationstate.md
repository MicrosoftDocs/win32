---
description: Sets the health state of an application that is running in a virtual machine.
ms.assetid: 012190CA-9CBF-47B6-9C5D-F75D73B0499B
title: IVmApplicationHealthMonitor::SetApplicationState method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IVmApplicationHealthMonitor.SetApplicationState
api_type: 
- COM
api_location: 
- VmApplicationHealthMonitor.idl
---

# IVmApplicationHealthMonitor::SetApplicationState method

Sets the health state of an application that is running in a virtual machine.

## Syntax


```C++
HRESULT SetApplicationState(
  [in] BSTR              Id,
  [in] BSTR              Name,
  [in] APPLICATION_STATE State
);
```



## Parameters

<dl> <dt>

*Id* \[in\]
</dt> <dd>

A **BSTR** representation of the **GUID** that identifies the application. It is the calling application's responsibility to create and maintain the identifiers it uses for the applications being monitored.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The display name of the application. This name is used in an informational event log entry for the state change.

</dd> <dt>

*State* \[in\]
</dt> <dd>

A value of the [**APPLICATION\_STATE**](application-state.md) enumeration that specifies the new health state of the application.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The state of the applications running in the virtual machine are reflected in the **OperationalStatus**\[1\] property value of the [**Msvm\_HeartbeatComponent**](msvm-heartbeatcomponent.md) class.

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

 

 




