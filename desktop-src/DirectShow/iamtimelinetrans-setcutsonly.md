---
description: The SetCutsOnly method specifies whether the transition is rendered as a cut. If so, the transition occurs instantly at the cut point. If a transition takes a long time to render, you might want to preview it as a cut to speed preview.
ms.assetid: 9ccff624-e37b-422e-9cb2-c472e6c8b2bb
title: IAMTimelineTrans::SetCutsOnly method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrans.SetCutsOnly
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTrans::SetCutsOnly method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetCutsOnly` method specifies whether the transition is rendered as a cut. If so, the transition occurs instantly at the cut point. If a transition takes a long time to render, you might want to preview it as a cut to speed preview.

## Syntax


```C++
HRESULT SetCutsOnly(
   BOOL Val
);
```



## Parameters

<dl> <dt>

*Val* 
</dt> <dd>

Specifies whether to render the transition as a cut. If **TRUE**, the transition is rendered as an instantaneous cut. If **FALSE**, the transition renders over its normal duration.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Rendering a transition as a cut is not compatible with swapping the inputs. (See [**IAMTimelineTrans::SetSwapInputs**](iamtimelinetrans-setswapinputs.md).) If you call `SetCutsOnly` with a value of **TRUE**, it temporarily overrides the **SetSwapInputs** setting. The cuts-only setting is intended for preview, however, so this limitation does not affect file output—just remember to call `SetCutsOnly` with the value **FALSE** before writing the file.

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

 

 




