---
description: The RealTimeStylus, GestureRecognizer, and DynamicRenderer classes are implemented as COM wrappers and are available only in managed code.
ms.assetid: db8f0f25-3650-4843-92e4-af5460841e7e
title: Implementation Notes for the StylusInput APIs
ms.topic: article
ms.date: 05/31/2018
---

# Implementation Notes for the StylusInput APIs

The [**RealTimeStylus**](realtimestylus-class.md), [GestureRecognizer](/previous-versions/ms575185(v=vs.100)), and [DynamicRenderer](/previous-versions/ms575176(v=vs.100)) classes are implemented as COM wrappers and are available only in managed code.

When the [**RealTimeStylus**](realtimestylus-class.md), [GestureRecognizer](/previous-versions/ms575185(v=vs.100)), or [DynamicRenderer](/previous-versions/ms575176(v=vs.100)) object is added as a plug-in to a **RealTimeStylus** object, the underlying COM objects interact on the COM level. Therefore, directly calling the methods of the [IStylusSyncPlugin](/previous-versions/ms575201(v=vs.100)) or [IStylusAsyncPlugin](/previous-versions/ms575194(v=vs.100)) interfaces are not supported. Adding the **RealTimeStylus**, GestureRecognizer, or DynamicRenderer object to the **RealTimeStylus** object is the only way to access these features.

 

 
