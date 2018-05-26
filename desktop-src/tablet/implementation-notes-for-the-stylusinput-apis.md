---
Description: The RealTimeStylus, GestureRecognizer, and DynamicRenderer classes are implemented as COM wrappers and are available only in managed code.
ms.assetid: db8f0f25-3650-4843-92e4-af5460841e7e
title: Implementation Notes for the StylusInput APIs
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implementation Notes for the StylusInput APIs

The [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master), [GestureRecognizer](T:Microsoft.StylusInput.GestureRecognizer), and [DynamicRenderer](T:Microsoft.StylusInput.DynamicRenderer) classes are implemented as COM wrappers and are available only in managed code.

When the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master), [GestureRecognizer](T:Microsoft.StylusInput.GestureRecognizer), or [DynamicRenderer](T:Microsoft.StylusInput.DynamicRenderer) object is added as a plug-in to a **RealTimeStylus** object, the underlying COM objects interact on the COM level. Therefore, directly calling the methods of the [IStylusSyncPlugin](T:Microsoft.StylusInput.IStylusSyncPlugin) or [IStylusAsyncPlugin](T:Microsoft.StylusInput.IStylusAsyncPlugin) interfaces are not supported. Adding the **RealTimeStylus**, GestureRecognizer, or DynamicRenderer object to the **RealTimeStylus** object is the only way to access these features.

 

 



