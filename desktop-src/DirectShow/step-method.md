---
Description: The Step method advances the DVD-Video stream by the specified number of frames.
ms.assetid: 21721722-0bf4-4cc7-a0e4-96b353888948
title: Step Method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

 

 



