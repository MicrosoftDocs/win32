---
title: IVMNetworkAdapter DetachFromVirtualNetwork method
description: The DetachFromVirtualNetwork method detaches the virtual NIC from its virtual network.
ms.assetid: 814f6ea4-48e6-4d15-a657-52f88e7fd389
keywords:
- DetachFromVirtualNetwork method Virtual Server
- DetachFromVirtualNetwork method Virtual Server , IVMNetworkAdapter interface
- IVMNetworkAdapter interface Virtual Server , DetachFromVirtualNetwork method
- DetachFromVirtualNetwork method Virtual Server , VMNetworkAdapter interface
- VMNetworkAdapter interface Virtual Server , DetachFromVirtualNetwork method
topic_type:
- apiref
api_name:
- IVMNetworkAdapter.DetachFromVirtualNetwork
- VMNetworkAdapter.DetachFromVirtualNetwork
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

# IVMNetworkAdapter::DetachFromVirtualNetwork method

The **DetachFromVirtualNetwork** method detaches the virtual NIC from its virtual network.

## Syntax


```C++
HRESULT DetachFromVirtualNetwork();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code                                                                                         | Description                                  |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>              | The operation was successful.<br/>     |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl> | An unexpected error has occurred.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMNetworkAdapter**](ivmnetworkadapter.md)
</dt> </dl>

 

 





