---
title: IVMVirtualServer FindVirtualNetwork method
description: The FindVirtualNetwork method returns a virtual network object matching the requested name.
ms.assetid: a249d41f-a853-47eb-bcda-511004105f7e
keywords:
- FindVirtualNetwork method Virtual Server
- FindVirtualNetwork method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , FindVirtualNetwork method
topic_type:
- apiref
api_name:
- IVMVirtualServer.FindVirtualNetwork
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

# IVMVirtualServer::FindVirtualNetwork method

The **FindVirtualNetwork** method returns a virtual network object matching the requested name.

## Syntax


```C++
HRESULT FindVirtualNetwork(
  [in]  BSTR              virtualNetworkName,
  [out] IVMVirtualNetwork **virtualNetwork
);
```



## Parameters

<dl> <dt>

*virtualNetworkName* \[in\]
</dt> <dd>

The name of the virtual network to find.

</dd> <dt>

*virtualNetwork* \[out\]
</dt> <dd>

A pointer to a new [**IVMVirtualNetwork**](ivmvirtualnetwork.md) object which represents this virtual network.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                        | Description                                                                       |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | The operation was successful.<br/>                                          |
| <dl> <dt>**S\_FALSE**</dt> </dl>            | The specified virtual network could not be found.<br/>                      |
| <dl> <dt>**E\_POINTER**</dt> </dl>          | The *virtualNetwork* parameter is **NULL**.<br/>                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | The *virtualNetworkName* parameter is not valid or is an empty string.<br/> |
| <dl> <dt>**E\_FILE\_NOT\_FOUND**</dt> </dl> | The virtual network file could not be found.<br/>                           |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>  | An unexpected error has occurred.<br/>                                      |



 

## Remarks

Virtual network names are case-insensitive, for example, "MyNetwork" and "mynetwork" refer to the same virtual network.

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

 

 





