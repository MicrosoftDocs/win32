---
title: IVMVirtualServer DeleteVirtualNetwork method
description: The DeleteVirtualNetwork method deletes a virtual network.
ms.assetid: '647075fb-4edb-4f2d-832a-039fb145cd2e'
keywords: ["DeleteVirtualNetwork method Virtual Server", "DeleteVirtualNetwork method Virtual Server , IVMVirtualServer interface", "IVMVirtualServer interface Virtual Server , DeleteVirtualNetwork method"]
topic_type:
- apiref
api_name:
- IVMVirtualServer.DeleteVirtualNetwork
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::DeleteVirtualNetwork method

The **DeleteVirtualNetwork** method deletes a virtual network.

## Syntax


```C++
HRESULT DeleteVirtualNetwork(
  [in] IVMVirtualNetwork *virtualNetworkName
);
```



## Parameters

<dl> <dt>

*virtualNetworkName* \[in\]
</dt> <dd>

Pointer to a [**IVMVirtualNetwork**](ivmvirtualnetwork.md) object representing the virtual network configuration to delete.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                       | Description                                                  |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | The operation was successful.<br/>                     |
| <dl> <dt>**S\_FALSE**</dt> </dl>           | The specified virtual network could not be found.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | The *virtualNetwork* parameter was **NULL**.<br/>      |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error occurred.<br/>                     |



 

## Remarks

The virtual network's configuration file is deleted by this method.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





