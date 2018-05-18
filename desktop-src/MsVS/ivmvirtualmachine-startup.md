---
title: IVMVirtualMachine Startup method
description: The Startup method starts up the virtual machine.
ms.assetid: 'b2e439b3-a0ab-4cda-9228-39739d9a0d16'
keywords: ["Startup method Virtual Server", "Startup method Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , Startup method"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Startup
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::Startup method

The **Startup** method starts up the virtual machine.

## Syntax


```C++
HRESULT Startup(
  [out] IVMTask **startupTask
);
```



## Parameters

<dl> <dt>

*startupTask* \[out\]
</dt> <dd>

A task that is used to track the completion progress of the virtual machine's startup sequence.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                              | Description                                                                               |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                    | The operation was successful.<br/>                                                  |
| <dl> <dt>**E\_POINTER**</dt> </dl>                | The *startupTask* parameter is **NULL**.<br/>                                       |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>           | The caller must have execute access permissions to start this virtual machine.<br/> |
| <dl> <dt> **VM\_E\_OUT\_OF\_RESOURCE**</dt> </dl> | Not enough host resources.<br/>                                                     |
| <dl> <dt> **VM\_E\_TOO\_MANY\_VMS**</dt> </dl>    | Too many active virtual machines.<br/>                                              |
| <dl> <dt>**VM\_E\_VM\_RUNNING**</dt> </dl>        | The virtual machine is already running.<br/>                                        |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>       | An unexpected error has occurred.<br/>                                              |



 

## Remarks

If the virtual machine is saved, it will be restored from the saved state.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





