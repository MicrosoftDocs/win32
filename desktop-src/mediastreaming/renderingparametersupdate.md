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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

To handle notifications from this event, register a [**RenderingParametersUpdateHandler**](/windows/win32/mfidl/?branch=master) event handler function using the [**add\_RenderingParametersUpdate**](imediarenderer-add-renderingparametersupdate.md) method. To unregister the event handler, use the [**remove\_RenderingParametersUpdate**](imediarenderer-remove-renderingparametersupdate.md) method.

 

 




