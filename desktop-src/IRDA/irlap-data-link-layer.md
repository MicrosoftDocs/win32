---
title: IrLAP Data Link Layer
description: Data rates are negotiated and changed during IrLAP connection establishment. The negotiation is transparent to applications.
ms.assetid: 5ada1314-3a32-4346-a2bc-d35be1daf00c
keywords:
- Infrared Data Association IrDA , described, IrLAP data link layer
- IrLAP IrDA
- architecture IrDA , data link layer
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IrLAP Data Link Layer

Data rates are negotiated and changed during IrLAP connection establishment. The negotiation is transparent to applications.

IrLAP defines two protocols: a [*discovery protocol*](https://www.bing.com/search?q=*discovery protocol*) and a data link protocol.

## IrLAP Discovery Protocol

The discovery protocol is used directly by an application to learn about currently visible devices, their nicknames, and device (MAC) addresses. In its discovery protocol, IrDA differs from other common bus or networking protocols. Clients are not expected to have advance knowledge of the device addresses of servers — they simply ask for a list of which devices are visible, and select one.

The information returned from discovery is a list of device MAC addresses, human-readable device nicknames, and a bitmask of hints that suggest the nature of peer devices. MAC addresses are randomly generated 32-bit values.

## IrLAP Data Link Protocol

The data link protocol is based on the widely implemented High Level Data Link Control (HDLC) data link protocol. As such, IrLAP provides a simple and reliable connection between two devices. If the HDLC connection is broken, an error is quickly reported back to applications.

 

 




