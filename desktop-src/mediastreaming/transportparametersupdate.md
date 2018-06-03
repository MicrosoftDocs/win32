---
title: TransportParametersUpdate event
description: Occurs whenever any of a set of transport parameters are updated on the DMR.
ms.assetid: 34D11925-387B-414F-A176-336BBCF87821
keywords:
- TransportParametersUpdate event Media Streaming API
topic_type:
- apiref
api_name:
- TransportParametersUpdate
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TransportParametersUpdate event

Occurs whenever any of a set of transport parameters are updated on the DMR.

## Syntax


```C++
void TransportParametersUpdate();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

To handle notifications from this event, register a [**TransportParametersUpdateHandler**](/windows/desktop/api/mfidl/) event handler function using the [**add\_TransportParametersUpdate**](https://www.bing.com/search?q=**add\_TransportParametersUpdate**) method. To unregister the event handler, use the [**remove\_TransportParametersUpdate**](https://www.bing.com/search?q=**remove\_TransportParametersUpdate**) method.

 

 




