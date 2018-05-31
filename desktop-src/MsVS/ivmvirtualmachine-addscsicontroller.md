---
title: IVMVirtualMachine AddSCSIController method
description: The AddSCSIController method adds a new SCSI controller to the virtual machine.
ms.assetid: 8b123fb0-ba99-4bf0-8c1c-b6d099d186b7
keywords:
- AddSCSIController method Virtual Server
- AddSCSIController method Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , AddSCSIController method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.AddSCSIController
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMVirtualMachine::AddSCSIController method

The **AddSCSIController** method adds a new SCSI controller to the virtual machine.

## Syntax


```C++
HRESULT AddSCSIController(
  [out] IVMSCSIController **controller
);
```



## Parameters

<dl> <dt>

*controller* \[out\]
</dt> <dd>

A new [**IVMSCSIController**](ivmscsicontroller.md) object.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                        | Description                                                                  |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>              | The operation was successful.<br/>                                     |
| <dl> <dt> **E\_POINTER**</dt> </dl>         | The *controller* parameter is **NULL**.<br/>                           |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | The maximum amount of SCSI controllers have already been created.<br/> |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>  | The configuration is unknown.<br/>                                     |
| <dl> <dt> **VM\_E\_VM\_RUNNING**</dt> </dl> | Virtual machine is running or saved.<br/>                              |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error has occurred.<br/>                                 |



 

## Remarks

You can only add a new SCSI controller to a stopped virtual machine.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





