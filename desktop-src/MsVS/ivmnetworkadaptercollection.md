---
title: IVMNetworkAdapterCollection interface
description: The IVMNetworkAdapterCollection interface defines a collection of IVMNetworkAdapter objects.
ms.assetid: 590bedbd-1c6c-4b0c-8ef3-8af2e808d30c
keywords:
- IVMNetworkAdapterCollection interface Virtual Server
- IVMNetworkAdapterCollection interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMNetworkAdapterCollection
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

# IVMNetworkAdapterCollection interface

The **IVMNetworkAdapterCollection** interface defines a collection of [**IVMNetworkAdapter**](ivmnetworkadapter.md) objects. An **IVMNetworkAdapterCollection** object is returned from the [**IVMVirtualMachine::NetworkAdapters**](ivmvirtualmachine-networkadapters.md), [**IVMVirtualNetwork::NetworkAdapters**](ivmvirtualnetwork-networkadapters.md), and [**IVMVirtualServer::UnconnectedNetworkAdapters**](ivmvirtualserver-unconnectednetworkadapters.md) properties.

## Members

The **IVMNetworkAdapterCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMNetworkAdapterCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMNetworkAdapterCollection** interface has these properties.



| Property                                                             | Access type          | Description                                                                                                                  |
|:---------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmnetworkadaptercollection--newenum.md)<br/> | Read-only<br/> | An [**IEnumVariant**](139e3c93-faef-4003-9079-e0e94494db3e) enumerator for the collection<br/>                         |
| [**Count**](ivmnetworkadaptercollection-count.md)<br/>        | Read-only<br/> | The number of network interfaces in the collection.<br/>                                                               |
| [**Item**](ivmnetworkadaptercollection-item.md)<br/>          | Read-only<br/> | The [**IVMNetworkAdapter**](ivmnetworkadapter.md) object that corresponds to the given index in this collection.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





