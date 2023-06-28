---
description: The GetDefaultTransitionB method retrieves the default transition. This method is equivalent to IAMTimeline::GetDefaultTransition, but receives a BSTR value, rather than a GUID.
ms.assetid: ed743766-e970-4bd9-a9a0-8b5d9fec2d80
title: IAMTimeline::GetDefaultTransitionB method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.GetDefaultTransitionB
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimeline::GetDefaultTransitionB method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetDefaultTransitionB` method retrieves the default transition. This method is equivalent to [**IAMTimeline::GetDefaultTransition**](iamtimeline-getdefaulttransition.md), but receives a BSTR value, rather than a GUID.

## Syntax


```C++
HRESULT GetDefaultTransitionB(
  [out, retval] BSTR *pGuid
);
```



## Parameters

<dl> <dt>

*pGuid* \[out, retval\]
</dt> <dd>

Receives a **BSTR** value representing the GUID of the default transition.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The method allocates memory for the string. The application must call **SysFreeString** to free the memory.

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

[**IAMTimeline Interface**](iamtimeline.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




