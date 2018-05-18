---
title: IVMVirtualMachine TurnOff method
description: The TurnOff method turns off the virtual machine.
ms.assetid: 'cfe35294-4e49-43c2-84a7-835182359a46'
keywords: ["TurnOff method Virtual Server", "TurnOff method Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , TurnOff method"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.TurnOff
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::TurnOff method

The **TurnOff** method turns off the virtual machine.

## Syntax


```C++
HRESULT TurnOff(
  [out] IVMTask **turnOffTask
);
```



## Parameters

<dl> <dt>

*turnOffTask* \[out\]
</dt> <dd>

A task that is used to track the completion progress of the virtual machine's turnoff sequence.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                             | Description                                                                                  |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                   | The operation was successful.<br/>                                                     |
| <dl> <dt>**E\_POINTER**</dt> </dl>               | The *turnOffTask* parameter is **NULL**.<br/>                                          |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>          | The caller must have execute access permissions to turn off this virtual machine.<br/> |
| <dl> <dt> **VM\_E\_VM\_NOT\_RUNNING**</dt> </dl> | The virtual machine is not running.<br/>                                               |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>      | An unexpected error has occurred.<br/>                                                 |



 

## Remarks

This method turns off the virtual machine in the same manner as turning the power off on a real machine.

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

 

 





