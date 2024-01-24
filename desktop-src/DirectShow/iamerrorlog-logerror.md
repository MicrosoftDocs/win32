---
description: The LogError method logs an error. Applications do not need to call this method. It is called internally in response to rendering errors.
ms.assetid: 08765c8a-21ca-4c40-84a8-d13da87d9c5f
title: IAMErrorLog::LogError method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMErrorLog.LogError
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMErrorLog::LogError method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The **LogError** method logs an error. Applications do not need to call this method. It is called internally in response to rendering errors.

## Syntax


```C++
HRESULT LogError(
       LONG    Severity,
       BSTR    ErrorString,
       LONG    ErrorCode,
       HRESULT hresult,
  [in] VARIANT *pExtraInfo
);
```



## Parameters

<dl> <dt>

*Severity* 
</dt> <dd>

Reserved. Do not use.

</dd> <dt>

*ErrorString* 
</dt> <dd>

String value containing the text of the error.

</dd> <dt>

*ErrorCode* 
</dt> <dd>

Error code.

</dd> <dt>

*hresult* 
</dt> <dd>

The HRESULT value that was returned by the method call that caused the error.

</dd> <dt>

*pExtraInfo* \[in\]
</dt> <dd>

Pointer to a VARIANT that contains any additional information about the error.

</dd> </dl>

## Return value

Return the value of the *hresult* parameter.

## Remarks

Within this method, do not free the **VARIANT** pointed to by *pExtraInfo*. Also, the **VARIANT** becomes invalid after the method returns, so do not try to reference it later.

Implement this method to return as quickly as possible. Do not make function calls from inside this method that might block program execution. For example, do not call functions that send window messages, block on events, or otherwise might block execution. Doing so could cause the computer to stop responding.

For a list of errors defined by DES, along with the meaning and data type of the **VARIANT** pointed to by *pExtraInfo*, see [Rendering Errors](rendering-errors.md).

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

[**IAMErrorLog Interface**](iamerrorlog.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




