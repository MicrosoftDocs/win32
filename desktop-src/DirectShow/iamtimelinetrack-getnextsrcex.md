---
description: The GetNextSrcEx method retrieves the next source after the specified source.
ms.assetid: cda3d079-eeb5-42a9-8854-5c90ae0e2c07
title: IAMTimelineTrack::GetNextSrcEx method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrack.GetNextSrcEx
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTrack::GetNextSrcEx method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetNextSrcEx` method retrieves the next source after the specified source.

## Syntax


```C++
HRESULT GetNextSrcEx(
        IAMTimelineObj *pLast,
  [out] IAMTimelineObj **ppNext
);
```



## Parameters

<dl> <dt>

*pLast* 
</dt> <dd>

Pointer to the previous source object, or **NULL** to retrieve the first source in the track.

</dd> <dt>

*ppNext* \[out\]
</dt> <dd>

Receives a pointer to the next source object's [**IAMTimelineObj**](iamtimelineobj.md) interface.

</dd> </dl>

## Return value

Returns S\_OK if the method retrieves a source, or S\_FALSE otherwise.

## Remarks

If the method returns S\_OK, the **IAMTimelineObj** interface that it returns has an outstanding reference count. Be sure to release the interface when you are finished using it.

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

[**IAMTimelineTrack Interface**](iamtimelinetrack.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




