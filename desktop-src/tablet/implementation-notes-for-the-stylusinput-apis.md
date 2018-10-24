---
Description: The RealTimeStylus, GestureRecognizer, and DynamicRenderer classes are implemented as COM wrappers and are available only in managed code.
ms.assetid: db8f0f25-3650-4843-92e4-af5460841e7e
title: Implementation Notes for the StylusInput APIs
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Implementation Notes for the StylusInput APIs

The [**RealTimeStylus**](realtimestylus-class.md), [GestureRecognizer](https://msdn.microsoft.com/library/ms575185(v=VS.90).aspx), and [DynamicRenderer](https://msdn.microsoft.com/library/ms575176(v=VS.90).aspx) classes are implemented as COM wrappers and are available only in managed code.

When the [**RealTimeStylus**](realtimestylus-class.md), [GestureRecognizer](https://msdn.microsoft.com/library/ms575185(v=VS.90).aspx), or [DynamicRenderer](https://msdn.microsoft.com/library/ms575176(v=VS.90).aspx) object is added as a plug-in to a **RealTimeStylus** object, the underlying COM objects interact on the COM level. Therefore, directly calling the methods of the [IStylusSyncPlugin](https://msdn.microsoft.com/library/ms575201(v=VS.90).aspx) or [IStylusAsyncPlugin](https://msdn.microsoft.com/library/ms575194(v=VS.90).aspx) interfaces are not supported. Adding the **RealTimeStylus**, GestureRecognizer, or DynamicRenderer object to the **RealTimeStylus** object is the only way to access these features.

 

 



