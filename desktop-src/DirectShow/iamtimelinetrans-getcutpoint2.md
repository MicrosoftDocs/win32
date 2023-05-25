---
description: The GetCutPoint2 method retrieves the cut point. This method is equivalent to IAMTimelineTrans::GetCutPoint, but takes a REFTIME value.
ms.assetid: bf2b7cac-6740-44d8-a889-8c745a23db19
title: IAMTimelineTrans::GetCutPoint2 method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrans.GetCutPoint2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineTrans::GetCutPoint2 method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetCutPoint2` method retrieves the cut point. This method is equivalent to [**IAMTimelineTrans::GetCutPoint**](iamtimelinetrans-getcutpoint.md), but takes a [**REFTIME**](reftime.md) value.

## Syntax


```C++
HRESULT GetCutPoint2(
   REFTIME *pTLTime
);
```



## Parameters

<dl> <dt>

*pTLTime* 
</dt> <dd>

Receives the cut point, relative to the start time of the transition, in seconds.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                               | Description                                                                    |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>   | The cut point was not set. The value returned is the default value.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>      | The cut point was set to a value other than the default.<br/>            |
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument.<br/>                                          |



 

## Remarks

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

[**IAMTimelineTrans Interface**](iamtimelinetrans.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




