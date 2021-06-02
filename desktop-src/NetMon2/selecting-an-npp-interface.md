---
description: Network packet providers (NPPs) expose the IDelaydC, IESP, IRTC, and IStats interfaces.
ms.assetid: 269b26f5-b794-4920-98da-505eda83c990
title: Selecting an NPP Interface
ms.topic: article
ms.date: 05/31/2018
---

# Selecting an NPP Interface

Network packet providers (NPPs) expose the [**IDelaydC**](idelaydc.md), [**IESP**](iesp.md), [**IRTC**](irtc.md), and [**IStats**](istats.md) interfaces. Each of these interfaces provides similar methods for connecting the NPP to the network, capturing network traffic, and collecting statistical information about the captured data. To choose which interface to use, refer to the following table.

> [!Note]  
> When you connect an NPP to the network with one of these interfaces, you can only use the methods provided by that interface. For example, if you connect to the network using the [**IRTC**](irtc.md) interface and then try to start a capture with [**IDelaydC**](idelaydc.md), your call to start the capture will fail, and an error code will be returned.

 



| Interface                    | When to use                                                                                                                                                                                                                                                                                                                                     |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IDelaydC**](idelaydc.md) | Use to capture network traffic and store it in a capture file. This interface is used by the Network Monitor UI and other NPP applications, which require storing captured network information.<br/>                                                                                                                                      |
| [**IESP**](iesp.md)         | Used to provide enhanced statistics in a special ESP file format. This interface is used by NPP applications that require the enhanced statistics provided by the ESP format.<br/>                                                                                                                                                        |
| [**IRTC**](irtc.md)         | Use to capture real-time network traffic and to trigger events when they occur. This interface is used by NPP applications that require run-time captures. Note that this interface does not provide the statistics that the other NPP interfaces provide, nor does it allow you to insert frames into the captured network traffic.<br/> |
| [**IStats**](istats.md)     | Use to retrieve capture statistics but not the captured frames.                                                                                                                                                                                                                                                                                 |



 

 

 




