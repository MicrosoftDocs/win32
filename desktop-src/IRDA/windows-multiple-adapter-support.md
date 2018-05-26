---
title: Windows Multiple-adapter Support
description: The Windows IrDA stack supports the concurrent operation of several NDIS 4.0 VFIR/FIR/SIR miniport adapters. This support allows a single server to support multiple inbound connections in a way that is transparent to both client and server applications.
ms.assetid: 38ac17f8-b76e-4f74-8eca-370f911670f5
keywords:
- Infrared Data Association IrDA , described, multiple-adapter support
- miniport IrDA
- adapters IrDA
- multiple-adapter support IrDA
- networking IrDA , multiple-adapter support
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Multiple-adapter Support

The Windows IrDA stack supports the concurrent operation of several NDIS 4.0 VFIR/FIR/SIR miniport adapters. This support allows a single server to support multiple inbound connections in a way that is transparent to both client and server applications.

An adapter is defined as the hardware/software needed to support a single IrLAP connection. Since IrDA is not a routable protocol, multiple-adapter support is limited to connections to a single server by multiple clients. Peer devices cannot talk to each other through the server. Each adapter and IrLAP instance will have a unique IrDA MAC address (DeviceId).

Discovery operations are run on every idle adapter in sequence. A global list of discovered devices is returned. Cached discovery information is maintained on a per-IrLAP instance and returned for each adapter that has a connection active.

The Windows IrDA stack maintains a mapping between device address and last seen adapter. When a connection is requested to a peer device, the stack routes the connection to the correct adapter.

Incoming connections are delivered to a single, listening transport endpoint. The listening client will not receive any per-adapter information. The mapping between the new connection and the adapter is maintained by the IrDA stack.

 

 




