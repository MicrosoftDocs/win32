---
description: The Step method advances the DVD-Video stream by the specified number of frames.
ms.assetid: '6f67335e-51c7-4b81-8ab3-86a3d70ac871'
title: Step Method
ms.topic: article
ms.date: 05/31/2018
---

# Step Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `Step` method advances the DVD-Video stream by the specified number of frames.

``` syntax
MSWebDVD.Step(iFrames)
```

## Parameters

<dl> <dt>

<span id="iFrames"></span><span id="iframes"></span><span id="IFRAMES"></span>*iFrames*
</dt> <dd>

Specifies the number of frames to step as an Integer.

</dd> </dl>

## Return Value

No return value.

## Remarks

Before calling this method, call [**CanStep**](canstep-method.md) to determine whether the decoder supports frame stepping.

If the DVD-Video is playing in reverse mode when this method is called, and the decoder supports reverse frame stepping, then the frame stepping is done in reverse.

 

 



