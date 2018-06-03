---
title: Windows IrDA Architecture
description: Many Microsoft operating systems support IrDA.
ms.assetid: 5f6f94d0-97f3-481e-8b3d-48a05c8495d5
keywords:
- Infrared Data Association IrDA , described, architecture
- architecture IrDA
- networking IrDA , architecture
- infrared networking IrDA , Windows architecture
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows IrDA Architecture

Many Microsoft operating systems support IrDA. Recent operating systems provide better performance and nonserialized data transmission using IrDA. The following table defines the support and capabilities of IrDA on the Windows Server and Windows operating systems.



| Operating system                         | IrDA functionality                                                                                                                                                                                                                                                                                       |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Server 2003Windows XP<br/> | Provides the most extensive IrDA functionality of all Windows operating systems. Capable of nonserialized data transmission of up to 16Mbps. Includes support for IrCOMM telephones, but does not support the IrCOMM programming model.                                                                  |
| Windows 2000                             | Provides IrDA functionality. Capable of nonserialized data transmission. Includes support for IrCOMM telephones, but does not support the IrCOMM programming model.                                                                                                                                      |
| Windows Me                               | Includes IrDA functionality in the form of serialized data transmissions. Supports IrCOMM as the primary programming model, which has been replaced in later versions of Windows. Windows Sockets calls explained in this document work properly, but under the constraints of serialized communication. |
| Windows 98                               | Includes IrDA functionality in the form of serialized data transmissions. Supports IrCOMM as the primary programming model, which has been replaced in later versions of Windows. Windows Sockets calls explained in this document work properly, but under the constraints of serialized communication. |
| Windows CE                               | Includes IrDA functionality in the form of serialized data transmissions. Windows Sockets calls explained in this document, and available on Windows CE, work properly, but under the constraints of serialized communication.                                                                           |



 

The following sections explain various aspects of Windows IrDA architecture. For more information, see [IrDA Core Protocols and Services](irda-core-protocols-and-services.md).

 

 





