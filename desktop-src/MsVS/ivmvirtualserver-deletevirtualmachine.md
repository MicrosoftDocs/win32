---
title: IVMVirtualServer DeleteVirtualMachine method
description: The DeleteVirtualMachine method deletes a virtual machine configuration.
ms.assetid: 3b3ffb6c-6955-4b60-ac95-b3870d67c516
keywords:
- DeleteVirtualMachine method Virtual Server
- DeleteVirtualMachine method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , DeleteVirtualMachine method
topic_type:
- apiref
api_name:
- IVMVirtualServer.DeleteVirtualMachine
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::DeleteVirtualMachine method

The **DeleteVirtualMachine** method deletes a virtual machine configuration.

## Syntax


```C++
HRESULT DeleteVirtualMachine(
  [in] IVMVirtualMachine *virtualMachine
);
```



## Parameters

<dl> <dt>

*virtualMachine* \[in\]
</dt> <dd>

Pointer to a [**IVMVirtualMachine**](ivmvirtualmachine.md) object representing the virtual machine configuration to delete.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                       | Description                                                |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | The operation was successful.<br/>                   |
| <dl> <dt>**S\_FALSE**</dt> </dl>           | The specified configuration could not be found.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | The *virtualMachine* parameter was **NULL**.<br/>    |
| <dl> <dt>**VM\_E\_VM\_RUNNING**</dt> </dl> | The virtual machine is running.<br/>                 |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error occurred.<br/>                   |



 

## Remarks

Only stopped virtual machines can be deleted. Note that any existing saved state or undo drive data for this configuration will be deleted in addition to the configuration file.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





