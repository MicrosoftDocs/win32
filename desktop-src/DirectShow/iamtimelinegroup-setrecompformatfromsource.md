---
description: The SetRecompFormatFromSource method sets the video recompression format using the compression format from a source file.
ms.assetid: 2d42876a-524b-454d-b4f1-353afe3a4d28
title: IAMTimelineGroup::SetRecompFormatFromSource method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineGroup.SetRecompFormatFromSource
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineGroup::SetRecompFormatFromSource method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetRecompFormatFromSource` method sets the video recompression format using the compression format from a source file.

## Syntax


```C++
HRESULT SetRecompFormatFromSource(
   IAMTimelineSrc *pSource
);
```



## Parameters

<dl> <dt>

*pSource* 
</dt> <dd>

Pointer to the [**IAMTimelineSrc**](iamtimelinesrc.md) interface of the source object.

</dd> </dl>

## Return value

Returns an **HRESULT** values. Possible values include the following.



| Return code                                                                                             | Description                                                                                            |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Success.<br/>                                                                                    |
| <dl> <dt>**E\_NO\_TIMELINE**</dt> </dl>          | The group is not within a timeline.<br/>                                                         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>           | Insufficient memory.<br/>                                                                        |
| <dl> <dt>**E\_POINTER**</dt> </dl>               | **NULL** pointer argument.<br/>                                                                  |
| <dl> <dt>**VFW\_E\_INVALIDMEDIATYPE**</dt> </dl> | Invalid media type. The group is not a video group, or the source file has no video stream.<br/> |



 

## Remarks

This method finds the source file associated with *pSource*, retrieves the media type of the first video stream in the file, and sets the group compression format using that type. For more information about compression formats, see [**IAMTimelineGroup::SetSmartRecompressFormat**](iamtimelinegroup-setsmartrecompressformat.md).

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

 

 




