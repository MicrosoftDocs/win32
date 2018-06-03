---
Description: The AreYouBlank method determines whether the track is blank (contains no source objects).
ms.assetid: 05d02753-6e40-4307-9445-c3cbc835f75e
title: IAMTimelineTrack::AreYouBlank method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAMTimelineTrack::AreYouBlank method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `AreYouBlank` method determines whether the track is blank (contains no source objects).

## Syntax


```C++
HRESULT AreYouBlank(
   long *pVal
);
```



## Parameters

<dl> <dt>

*pVal* 
</dt> <dd>

Receives a Boolean value specifying whether the track is blank. If the value is **TRUE**, the track is blank and contains no source objects. If **FALSE**, the track is not blank.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](http://go.microsoft.com/fwlink/p/?linkid=129787). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IAMTimelineTrack Interface**](iamtimelinetrack.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




