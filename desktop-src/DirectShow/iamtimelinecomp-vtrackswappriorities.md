---
description: The VTrackSwapPriorities method switches the priority levels of two tracks.
ms.assetid: 87085060-5165-4c32-b5b0-895ae487e7ef
title: IAMTimelineComp::VTrackSwapPriorities method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineComp.VTrackSwapPriorities
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineComp::VTrackSwapPriorities method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `VTrackSwapPriorities` method switches the priority levels of two tracks.

Given two priority levels, this method switches the virtual tracks at those priorities. When the method returns, the track that was at the first priority level is now at the second priority level, and vice versa.

## Syntax


```C++
HRESULT VTrackSwapPriorities(
   long VirtualTrackA,
   long VirtualTrackB
);
```



## Parameters

<dl> <dt>

*VirtualTrackA* 
</dt> <dd>

First priority level at which to swap virtual tracks.

</dd> <dt>

*VirtualTrackB* 
</dt> <dd>

Second priority level at which to swap virtual tracks.

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

 

 




