---
title: IVMNetworkAdapter AttachToVirtualNetwork method
description: The AttachToVirtualNetwork method attaches the virtual NIC to the specified virtual network.
ms.assetid: '415a0446-8609-4eca-9c32-404da99b0731'
keywords: ["AttachToVirtualNetwork method Virtual Server", "AttachToVirtualNetwork method Virtual Server , IVMNetworkAdapter interface", "IVMNetworkAdapter interface Virtual Server , AttachToVirtualNetwork method", "AttachToVirtualNetwork method Virtual Server , VMNetworkAdapter interface", "VMNetworkAdapter interface Virtual Server , AttachToVirtualNetwork method"]
topic_type:
- apiref
api_name:
- IVMNetworkAdapter.AttachToVirtualNetwork
- VMNetworkAdapter.AttachToVirtualNetwork
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMNetworkAdapter::AttachToVirtualNetwork method

The **AttachToVirtualNetwork** method attaches the virtual NIC to the specified virtual network.

## Syntax


```C++
HRESULT AttachToVirtualNetwork(
  [in] IVMVirtualNetwork *virtualNetwork
);
```



## Parameters

<dl> <dt>

*virtualNetwork* \[in\]
</dt> <dd>

The virtual network to which this virtual NIC will be connected.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                                           | Description                                                                         |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>                                | The operation was successful.<br/>                                            |
| <dl> <dt>**E\_POINTER**</dt> </dl>                             | The *virtualNetwork* parameter is **NULL**.<br/>                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                          | The *virtualNetwork* parameter does not contain a valid virtual network.<br/> |
| <dl> <dt>**E\_ACCESS\_DENIED**</dt> </dl>                      | Access was denied to the requested virtual network.<br/>                      |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>                     | The virtual machine is invalid or no longer exists.<br/>                      |
| <dl> <dt> **VM\_E\_INVALID\_VIRTUAL\_NETWORK\_ID** </dt> </dl> | The *virtualNetwork* parameter is not an existing virtual network.<br/>       |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl>                   | An unexpected error has occurred.<br/>                                        |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMNetworkAdapter**](ivmnetworkadapter.md)
</dt> </dl>

 

 





