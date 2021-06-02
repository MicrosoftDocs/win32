---
description: Not supported. Call the IAMTimelineComp::GetRecursiveLayerOfType method instead.
ms.assetid: 857f57e2-6123-43c3-bb74-62afd0fc0b52
title: IAMTimelineComp::GetRecursiveLayerOfTypeI method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineComp.GetRecursiveLayerOfTypeI
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineComp::GetRecursiveLayerOfTypeI method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

Not supported. Call the [**IAMTimelineComp::GetRecursiveLayerOfType**](iamtimelinecomp-getrecursivelayeroftype.md) method instead.

## Syntax


```C++
HRESULT GetRecursiveLayerOfTypeI(
   IAMTimelineObj      **ppVirtualTrack,
   long                **pWhichLayer,
   TIMELINE_MAJOR_TYPE Type
);
```



## Parameters

<dl> <dt>

*ppVirtualTrack* 
</dt> <dd>

Reserved.

</dd> <dt>

*pWhichLayer* 
</dt> <dd>

Reserved.

</dd> <dt>

*Type* 
</dt> <dd>

Reserved.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

[**IAMTimelineComp Interface**](iamtimelinecomp.md)
</dt> </dl>

 

 




