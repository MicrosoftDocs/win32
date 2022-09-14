---
title: Using Device Contexts
description: Using Device Contexts
ms.assetid: 2e8de313-6218-4401-a578-73140e7fdae1
keywords:
- visualizations,device context
- custom visualizations,device context
- visualizations,Render function
- custom visualizations,Render function
- Render function,device context
ms.topic: article
ms.date: 05/31/2018
---

# Using Device Contexts

The device context is a standard handle to a device context. You need this for many drawing functions so that Microsoft Windows knows which window to draw in. For example, to draw a rectangle, you need to specify the device context.


```C++
HDC hdc;
::Rectangle( hdc, 1, 1, 100, 100 );

```



The device context is specified by Windows Media Player through the **Render** function. If your plug-in renders using a window, you'll need to use the device context of that window. Use this device context for any drawing tool that requires a device context.

## Related topics

<dl> <dt>

[**Implementing Render**](implementing-render.md)
</dt> </dl>

 

 




