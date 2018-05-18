---
title: IVMRCClientControl Connect method
description: The Connect method disconnects the control from the current VMRC server (if necessary) and connects to a new VMRC server.
ms.assetid: 'bf0cd929-d90b-4199-bd2c-71b092a7cb90'
keywords: ["Connect method Virtual Server", "Connect method Virtual Server , IVMRCClientControl interface", "IVMRCClientControl interface Virtual Server , Connect method", "Connect method Virtual Server , VMRCClientControl interface", "VMRCClientControl interface Virtual Server , Connect method"]
topic_type:
- apiref
api_name:
- IVMRCClientControl.Connect
- VMRCClientControl.Connect
api_location:
- VMRCClientControl.lib
- VMRCClientControl.dll
api_type:
- COM
---

# IVMRCClientControl::Connect method

The **Connect** method disconnects the control from the current VMRC server (if necessary) and connects to a new VMRC server.

## Syntax


```C++
HRESULT Connect();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code                                                                          | Description                              |
|--------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The operation was successful.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VMRCClientControl.h</dt> </dl>    |
| Library<br/>  | <dl> <dt>VMRCClientControl.lib</dt> </dl>  |



## See also

<dl> <dt>

[**IVMRCClientControl**](ivmrcclientcontrol.md)
</dt> </dl>

 

 





