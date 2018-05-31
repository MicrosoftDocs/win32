---
title: IVMVirtualNetworkCollection interface
description: The IVMVirtualNetworkCollection interface defines a collection of IVMVirtualNetwork objects. An IVMVirtualNetworkCollection object is returned from the IVMVirtualServer VirtualNetworks property.
ms.assetid: 9bfee725-db47-41b2-8967-3712f62f7827
keywords:
- IVMVirtualNetworkCollection interface Virtual Server
- IVMVirtualNetworkCollection interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMVirtualNetworkCollection
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IVMVirtualNetworkCollection interface

The **IVMVirtualNetworkCollection** interface defines a collection of [**IVMVirtualNetwork**](ivmvirtualnetwork.md) objects. An **IVMVirtualNetworkCollection** object is returned from the [**IVMVirtualServer::VirtualNetworks**](ivmvirtualserver-virtualnetworks.md) property.

## Members

The **IVMVirtualNetworkCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMVirtualNetworkCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMVirtualNetworkCollection** interface has these properties.



| Property                                                             | Access type          | Description                                                                                            |
|:---------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmvirtualnetworkcollection--newenum.md)<br/> | Read-only<br/> | An **IEnumVariant** enumerator for the collection.<br/>                                          |
| [**Count**](ivmvirtualnetworkcollection-count.md)<br/>        | Read-only<br/> | The number of virtual networks in this collection.<br/>                                          |
| [**Item**](ivmvirtualnetworkcollection-item.md)<br/>          | Read-only<br/> | The [**IVMVirtualNetwork**](ivmvirtualnetwork.md) object at a given index (1-based index).<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





