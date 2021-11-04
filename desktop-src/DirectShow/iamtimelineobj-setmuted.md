---
description: The SetMuted method sets the object's muted state. A muted object is not rendered, but it remains in the timeline.
ms.assetid: 5dcd8533-8e58-4553-ac01-928723485f5d
title: IAMTimelineObj::SetMuted method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineObj.SetMuted
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineObj::SetMuted method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetMuted` method sets the object's muted state. A muted object is not rendered, but it remains in the timeline.

## Syntax


```C++
HRESULT SetMuted(
   BOOL newVal
);
```



## Parameters

<dl> <dt>

*newVal* 
</dt> <dd>

Flag that specifies the muted state. If **TRUE**, the object and all of its children are muted.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Muting an object also mutes any children contained in the object. For example, if you mute a track, the transitions, sources, and effects in that track are also muted. Once the object is no longer muted, its children revert to their previous state, which might be muted or unmuted.

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

[**IAMTimelineObj Interface**](iamtimelineobj.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




