---
title: RenderingParametersUpdate event
description: Occurs whenever any of a set of rendering control parameters are updated on the DMR.
ms.assetid: 3CEED740-19EA-4CC6-B3F8-F9DE9C6DCC58
keywords:
- RenderingParametersUpdate event Media Streaming API
topic_type:
- apiref
api_name:
- RenderingParametersUpdate
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RenderingParametersUpdate event

Occurs whenever any of a set of rendering control parameters are updated on the DMR.

## Syntax


```C++
void RenderingParametersUpdate();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

To handle notifications from this event, register a [**RenderingParametersUpdateHandler**](https://msdn.microsoft.com/en-us/library/Hh828994(v=VS.85).aspx) event handler function using the [**add\_RenderingParametersUpdate**](https://msdn.microsoft.com/en-us/library/Hh828928(v=VS.85).aspx) method. To unregister the event handler, use the [**remove\_RenderingParametersUpdate**](https://msdn.microsoft.com/en-us/library/Hh828940(v=VS.85).aspx) method.

 

 




