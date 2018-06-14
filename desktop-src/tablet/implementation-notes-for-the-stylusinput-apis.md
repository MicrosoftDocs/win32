---
Description: The RealTimeStylus, GestureRecognizer, and DynamicRenderer classes are implemented as COM wrappers and are available only in managed code.
ms.assetid: db8f0f25-3650-4843-92e4-af5460841e7e
title: Implementation Notes for the StylusInput APIs
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Implementation Notes for the StylusInput APIs

The [**RealTimeStylus**](https://msdn.microsoft.com/en-us/library/ms704918(v=VS.85).aspx), [GestureRecognizer](https://www.bing.com/search?q=GestureRecognizer), and [DynamicRenderer](https://www.bing.com/search?q=DynamicRenderer) classes are implemented as COM wrappers and are available only in managed code.

When the [**RealTimeStylus**](https://msdn.microsoft.com/en-us/library/ms704918(v=VS.85).aspx), [GestureRecognizer](https://www.bing.com/search?q=GestureRecognizer), or [DynamicRenderer](https://www.bing.com/search?q=DynamicRenderer) object is added as a plug-in to a **RealTimeStylus** object, the underlying COM objects interact on the COM level. Therefore, directly calling the methods of the [IStylusSyncPlugin](https://www.bing.com/search?q=IStylusSyncPlugin) or [IStylusAsyncPlugin](https://www.bing.com/search?q=IStylusAsyncPlugin) interfaces are not supported. Adding the **RealTimeStylus**, GestureRecognizer, or DynamicRenderer object to the **RealTimeStylus** object is the only way to access these features.

 

 



