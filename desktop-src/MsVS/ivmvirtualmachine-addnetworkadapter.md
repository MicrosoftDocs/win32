---
title: IVMVirtualMachine AddNetworkAdapter method
description: The AddNetworkAdapter method adds a network interface to the virtual machine.
ms.assetid: '4bf423e2-172b-43fc-bbf5-dae132ae670b'
keywords: ["AddNetworkAdapter method Virtual Server", "AddNetworkAdapter method Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , AddNetworkAdapter method"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.AddNetworkAdapter
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::AddNetworkAdapter method

The **AddNetworkAdapter** method adds a network interface to the virtual machine.

## Syntax


```C++
HRESULT AddNetworkAdapter(
  [out] IVMNetworkAdapter **networkAdapter
);
```



## Parameters

<dl> <dt>

*networkAdapter* \[out\]
</dt> <dd>

A new [**IVMNetworkAdapter**](ivmnetworkadapter.md) object.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                        | Description                                            |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>              | The operation was successful.<br/>               |
| <dl> <dt> **E\_POINTER**</dt> </dl>         | The *networkAdapter* parameter is **NULL**.<br/> |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>  | The configuration is unknown.<br/>               |
| <dl> <dt> **VM\_E\_VM\_RUNNING**</dt> </dl> | Virtual machine is running or saved.<br/>        |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error has occurred.<br/>           |



 

## Remarks

You can only add a new network interface to a stopped virtual machine. The newly created network adapter is not connected to a virtual network.

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

 

 





