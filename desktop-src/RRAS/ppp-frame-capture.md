---
title: Writing a Driver to Capture PPP Frames
description: This document explains how to develop a driver that can capture PPP frames in Windows Vista before they are compressed/encrypted in the send path or after they are decompressed/decrypted in the receive path.
ms.assetid: 1b3fe1b8-2b11-4aed-98e1-464b8c0821ec
ms.topic: article
ms.date: 05/31/2018
---

# Writing a Driver to Capture PPP Frames

When Point-to-Point Protocol (PPP) frames are sent through a Point-to-Point Tunneling Protocol (PPTP) tunnel with encryption turned on, or through a Layer 2 Tunneling Protocol (L2TP) tunnel that uses IPSec for encryption, the typical PPP frame capture utility can only capture PPP frames that have an encrypted protocol identity field. This document explains how to develop a driver that can capture PPP frames in Windows Vista before they are compressed/encrypted in the send path or after they are decompressed/decrypted in the receive path.

1.  Write an NDIS protocol driver. For details, see [NDIS 6.0 Protocol Drivers](https://msdn.microsoft.com/library/ms795570.aspx) or [NDIS Protocol Drivers (NDIS 5.1)](https://msdn.microsoft.com/library/ms801145.aspx).
2.  Install the driver with a hardware identity of "ms\_netmon". For detailed instructions on how to install the driver with a specific hardware identity, see [INF Models Section](https://msdn.microsoft.com/library/ms794357.aspx).
    > [!Note]  
    > Each Windows Vista machine permits the installation of only one driver entity that has the "ms\_netmon" hardware identity. To install another driver with this identity, the first driver must be uninstalled. A driver that is installed without using the "ms\_netmon" hardware identity cannot perform the binding needed to capture PPP frames.

     

3.  The protocol driver should specify "ndiswanbh" as the binding interface for capturing PPP frames. For detailed instructions, see [Specifying Binding Interfaces](https://msdn.microsoft.com/library/aa937923.aspx).
4.  The [ProtocolBindAdapter](https://msdn.microsoft.com/library/ms797311.aspx) implementation in the driver should support "NdisMediumWan" as a part of the medium array, so that it can open the ndiswanbh miniport edge using the [NdisOpenAdapter](https://msdn.microsoft.com/library/ms804862.aspx) function.
5.  If the [ProtocolOpenAdapterComplete](https://msdn.microsoft.com/library/ms797287.aspx) function is called with status NDIS\_STATUS\_SUCCESS, the protocol driver should set the [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/bb314089.aspx) OID with the flags [NDIS\_PACKET\_TYPE\_PROMISCUOUS](https://msdn.microsoft.com/library/bb314089.aspx) and [NDIS\_PACKET\_TYPE\_ALL\_LOCAL](https://msdn.microsoft.com/library/bb314089.aspx) over this binding. Once this is done, the protocol driver will receive the decrypted PPP frames from the PPP framing layer in its [ProtocolReceive](https://msdn.microsoft.com/library/ms797274.aspx) function.

> [!Note]  
> This information only applies to drivers on a Windows Vista machine.

 

 

 




