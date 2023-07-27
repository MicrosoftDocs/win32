---
description: The SetDelayTime method sets the delay time for the ToolTip associated with the MSWebDVD object.
ms.assetid: bb1086e1-57e2-495a-9b7b-2d349a516e72
title: SetDelayTime
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SetDelayTime

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `SetDelayTime` method sets the delay time for the ToolTip associated with the **MSWebDVD** object.

``` syntax
MSWebDVD.SetDelayTime(iDelayType, iNewVal)
```

## Parameters

<dl> <dt>

<span id="iDelayType"></span><span id="idelaytype"></span><span id="IDELAYTYPE"></span>*iDelayType*
</dt> <dd>

Specifies the type of delay as an Integer.



| Value | Description                                                                                                                                                                                                                                      |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -1    | To reset the autopop delay time to its default value, set *iNewVal* to -1.                                                                                                                                                                       |
| 0     | Set the length of time a ToolTip window remains visible if the pointer is stationary within a tool's bounding rectangle.                                                                                                                         |
| 1     | Set the length of time a pointer must remain stationary within a tool's bounding rectangle before the ToolTip window appears.                                                                                                                    |
| 2     | Set the length of time it takes for subsequent ToolTip windows to appear as the pointer moves from one tool to another.                                                                                                                          |
| 3     | Set all delay times to default proportions. The autopop time is ten times the initial time and the reshow time is one-fifth the initial time. If this flag is set, use a positive value of iNewVal to specify the initial time, in milliseconds. |



 

</dd> <dt>

<span id="iNewVal"></span><span id="inewval"></span><span id="INEWVAL"></span>*iNewVal*
</dt> <dd>

Specifies the delay, in milliseconds, as an Integer.



| Value                    | Description                                                   |
|--------------------------|---------------------------------------------------------------|
| -1                       | Sets the delay specified in *iDelayType* to its default value |
| any other negative value | Sets all delay types to their default value.                  |



 

</dd> </dl>

## Return Value

No return value.

 

 



