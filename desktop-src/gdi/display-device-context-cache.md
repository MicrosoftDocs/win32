---
description: The system maintains a cache of display device contexts that it uses for common, parent, and window device contexts.
ms.assetid: b017453a-c2c5-4bb1-ae46-f303d5e200ca
title: Display Device Context Cache
ms.topic: article
ms.date: 05/31/2018
---

# Display Device Context Cache

The system maintains a cache of display device contexts that it uses for common, parent, and window device contexts. The system retrieves a device context from the cache whenever an application calls the [**GetDC**](/windows/desktop/api/Winuser/nf-winuser-getdc) or [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint) function; the system returns the DC to the cache when the application subsequently calls the [**ReleaseDC**](/windows/desktop/api/Winuser/nf-winuser-releasedc) or [**EndPaint**](/windows/desktop/api/Winuser/nf-winuser-endpaint) function.

There is no predetermined limit on the amount of device contexts that a cache can hold; the system creates a new display device context for the cache if none is available. Given this, an application can have more than five active device contexts from the cache at a time. However, the application must continue to release these device contexts after use. Because new display device contexts for the cache are allocated in the application's heap space, failing to release the device contexts eventually consumes all available heap space. The system indicates this failure by returning an error when it cannot allocate space for the new device context. Other functions unrelated to the cache may also return errors.

 

 



