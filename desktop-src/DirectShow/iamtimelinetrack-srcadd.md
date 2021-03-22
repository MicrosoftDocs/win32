---
description: The SrcAdd method adds a source to the track.
ms.assetid: 71c62e92-02d6-4c6f-8121-2052d6cc832c
title: IAMTimelineTrack::SrcAdd method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrack.SrcAdd
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTrack::SrcAdd method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SrcAdd` method adds a source to the track.

## Syntax


```C++
HRESULT SrcAdd(
   IAMTimelineObj *pSrc
);
```



## Parameters

<dl> <dt>

*pSrc* 
</dt> <dd>

Pointer to the source object's [**IAMTimelineObj**](iamtimelineobj.md) interface.

</dd> </dl>

## Return value

Returns S\_OK if successful. Returns E\_NOINTERFACE if the object is not a source object. Otherwise, returns an **HRESULT** value indicating the cause of the error.

## Remarks

Set the source's start and stop times before calling this method. (Call [**IAMTimelineObj::SetStartStop**](iamtimelineobj-setstartstop.md).)

Currently, DES cannot simultaneously render more than 75 sources that were compressed with Video Compression Manager (VCM) codecs. Also, if the project as a whole contains more than 75 such sources, you must use dynamic reconnection or DES cannot preview the project. For more information, see [**IRenderEngine::SetDynamicReconnectLevel**](irenderengine-setdynamicreconnectlevel.md).

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

 

 




