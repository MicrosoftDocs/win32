---
title: IVMVirtualMachine RemoveNetworkAdapter method
description: The RemoveNetworkAdapter method removes a network interface from the virtual machine.
ms.assetid: '6c0cd513-7425-4be5-a81c-723124042d90'
keywords: ["RemoveNetworkAdapter method Virtual Server", "RemoveNetworkAdapter method Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , RemoveNetworkAdapter method"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.RemoveNetworkAdapter
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::RemoveNetworkAdapter method

The **RemoveNetworkAdapter** method removes a network interface from the virtual machine.

## Syntax


```C++
HRESULT RemoveNetworkAdapter(
  [in] IVMNetworkAdapter *networkAdapter
);
```



## Parameters

<dl> <dt>

*networkAdapter* \[in\]
</dt> <dd>

The network adapter to be removed.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                         | Description                                                                                   |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>              | The operation was successful.<br/>                                                      |
| <dl> <dt> **E\_POINTER**</dt> </dl>          | The *networkAdapter* parameter is **NULL**.<br/>                                        |
| <dl> <dt> **VM\_E\_VM\_RUNNING** </dt> </dl> | This operation cannot be performed while this virtual machine is running or saved.<br/> |
| <dl> <dt> **VM\_E\_VM\_UNKNOWN** </dt> </dl> | The configuration is unknown.<br/>                                                      |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl> | An unexpected error has occurred.<br/>                                                  |



 

## Remarks

You can only remove an existing network interface from a stopped virtual machine.

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

 

 





