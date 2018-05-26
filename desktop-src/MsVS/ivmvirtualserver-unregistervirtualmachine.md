---
title: IVMVirtualServer UnregisterVirtualMachine method
description: The UnregisterVirtualMachine method unregisters a virtual machine configuration without deleting the configuration file.
ms.assetid: 55eb9b5d-8a7f-40cf-aa93-badb1bde91a7
keywords:
- UnregisterVirtualMachine method Virtual Server
- UnregisterVirtualMachine method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , UnregisterVirtualMachine method
- UnregisterVirtualMachine method Virtual Server , VMVirtualServer interface
- VMVirtualServer interface Virtual Server , UnregisterVirtualMachine method
topic_type:
- apiref
api_name:
- IVMVirtualServer.UnregisterVirtualMachine
- VMVirtualServer.UnregisterVirtualMachine
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMVirtualServer::UnregisterVirtualMachine method

The **UnregisterVirtualMachine** method unregisters a virtual machine configuration without deleting the configuration file.

## Syntax


```C++
HRESULT UnregisterVirtualMachine(
  [in] IVMVirtualMachine *virtualMachine
);
```



## Parameters

<dl> <dt>

*virtualMachine* \[in\]
</dt> <dd>

Pointer to a [**IVMVirtualMachine**](ivmvirtualmachine.md) object representing the virtual machine configuration to unregister.

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

Only stopped virtual machines can be unregistered. Existing saved state or undo drive data for this configuration will be retained when a virtual machine is unregistered.

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

 

 





