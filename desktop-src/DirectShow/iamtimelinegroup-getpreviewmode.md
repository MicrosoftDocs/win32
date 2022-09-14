---
description: The GetPreviewMode method retrieves the preview mode for the group.
ms.assetid: 635354e5-5cb2-4045-8a7f-21d31005c5f3
title: IAMTimelineGroup::GetPreviewMode method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineGroup.GetPreviewMode
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineGroup::GetPreviewMode method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetPreviewMode` method retrieves the preview mode for the group.

## Syntax


```C++
HRESULT GetPreviewMode(
   BOOL *pfPreview
);
```



## Parameters

<dl> <dt>

*pfPreview* 
</dt> <dd>

Receives a Boolean value indicating the preview mode. If **TRUE**, the group is in preview mode. If **FALSE**, the group is in authoring mode.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

In preview mode, frames are dropped during slow effects or transitions to keep the video synchronized with the audio. The video might look choppy as a result. In authoring mode, every frame is rendered. Authoring mode is appropriate for writing files; for on-screen preview, the video might become out of sync with the audio.

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IAMTimelineGroup Interface**](iamtimelinegroup.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




