---
description: Network packet providers (NPPs) provide COM interfaces that are called by NPP applications, and Network Monitor.
ms.assetid: 101ce722-3101-4f50-b492-dad8b68a7aaf
title: NPP Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# NPP Interfaces

Network packet providers (NPPs) provide COM interfaces that are called by NPP applications, and Network Monitor. When you call [CreateNPPInterface](createnppinterface.md), remember that each NPP is represented as a single in-process COM object. Applications can instantiate any number of NPP objects. However, each instantiated object must use one—and only one—of the five NPP interfaces.

Note also that different NPP interfaces provide network data in various forms. For example, Network Monitor uses the **IDelaydC** interface to capture network traffic and save it to a capture file; while monitors use the **IRTC** interface to capture real time network traffic. The following table describes Network Monitor NPP interfaces.



| Interface                | Description                                                                                                                                                         |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IDelaydC](idelaydc.md) | Captures network traffic that is stored in a capture file. This interface is used by Network Monitor and NPP applications.                                          |
| [IESP](iesp.md)         | Captures network traffic that is stored in a capture file and provides enhanced statistics in a special ESP file format. This interface is used by NPP applications |
| [IRTC](irtc.md)         | Captures real time network traffic and triggers events when they occur. This interface is used by [*monitors*](m.md) and NPP applications.     |
| [IStats](istats.md)     | Retrieves statistics as raw data rather than frames. This interface is used by NPP applications such as [*Perfmon*](p.md).                     |



 

 

 



