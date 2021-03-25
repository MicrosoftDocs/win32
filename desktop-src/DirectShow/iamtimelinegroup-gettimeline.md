---
description: The GetTimeline method retrieves the timeline to which this group belongs.
ms.assetid: a57d75c9-6e2e-426f-9403-ad32188b2211
title: IAMTimelineGroup::GetTimeline method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineGroup.GetTimeline
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineGroup::GetTimeline method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetTimeline` method retrieves the timeline to which this group belongs.

## Syntax


```C++
HRESULT GetTimeline(
  [out] IAMTimeline **ppTimeline
);
```



## Parameters

<dl> <dt>

*ppTimeline* \[out\]
</dt> <dd>

Receives the timeline's [**IAMTimeline**](iamtimeline.md) interface. If the group is not part of a timeline, the value is set to **NULL**.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If the value returned in *ppTimeline* is not **NULL**, the **IAMTimeline** interface has an outstanding reference count. Be sure to release the interface when you are finished using it.

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

[**IAMTimelineGroup Interface**](iamtimelinegroup.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




