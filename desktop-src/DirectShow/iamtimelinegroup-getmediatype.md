---
description: The GetMediaType method retrieves the uncompressed media type for the group.
ms.assetid: 129ed688-0f03-4ccb-b65f-d61f02cb94b2
title: IAMTimelineGroup::GetMediaType method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineGroup.GetMediaType
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineGroup::GetMediaType method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetMediaType` method retrieves the uncompressed media type for the group.

## Syntax


```C++
HRESULT GetMediaType(
  [out] AM_MEDIA_TYPE *pmt
);
```



## Parameters

<dl> <dt>

*pmt* \[out\]
</dt> <dd>

Pointer to an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure that is filled with the media type.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The caller must free the returned media type's format block, given in the **pbFormat** member of the returned AM\_MEDIA\_TYPE structure. You can use the helper function [**FreeMediaType**](freemediatype.md) from the base class library.

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

 

 




