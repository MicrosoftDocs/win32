---
Description: The SetOutputFPS method sets the uncompressed output frame rate for this group.
ms.assetid: 335ea106-d5db-43a1-b771-b027e25164a6
title: IAMTimelineGroupSetOutputFPS method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IAMTimelineGroup::SetOutputFPS method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetOutputFPS` method sets the uncompressed output frame rate for this group.

## Syntax


```C++
HRESULT SetOutputFPS(
   double FPS
);
```



## Parameters

<dl> <dt>

*FPS* 
</dt> <dd>

Output frame rate for this group, in frames per second. The value cannot equal zero, and cannot have more than seven digits after the decimal place.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Rendered output from this group runs at the specified frame rate, and all edits on the source material are rounded to the nearest frame boundary, as defined by the frame rate. For best performance, use the same frame rate for all groups, video and audio.

The [**IAMTimelineGroup::SetSmartRecompressFormat**](iamtimelinegroup-setsmartrecompressformat.md) method overwrites the frame rate.

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](http://go.microsoft.com/fwlink/p/?linkid=129787). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IAMTimelineGroup Interface**](iamtimelinegroup.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




