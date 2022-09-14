---
description: The VTrackGetCount method retrieves the number of virtual tracks contained in the composition.
ms.assetid: a8117b06-4f42-45da-9b93-f547cb70aa5d
title: IAMTimelineComp::VTrackGetCount method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineComp.VTrackGetCount
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineComp::VTrackGetCount method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `VTrackGetCount` method retrieves the number of virtual tracks contained in the composition.

## Syntax


```C++
HRESULT VTrackGetCount(
   long *pVal
);
```



## Parameters

<dl> <dt>

*pVal* 
</dt> <dd>

Receives the number of virtual tracks.

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
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




