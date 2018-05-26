---
Description: The GetMediaTime method retrieves the time stamps on the current sample.
ms.assetid: 13710373-04fd-4c1d-ba97-78be5cf27e7d
title: CRendererPosPassThru.GetMediaTime method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CRendererPosPassThru.GetMediaTime method

The `GetMediaTime` method retrieves the time stamps on the current sample.

## Syntax


```C++
HRESULT GetMediaTime(
   LONGLONG *pStartTime,
   LONGLONG *pEndTime
);
```



## Parameters

<dl> <dt>

*pStartTime* 
</dt> <dd>

Pointer to a variable that receives the start time, in units of the current time format.

</dd> <dt>

*pEndTime* 
</dt> <dd>

Pointer to a variable that receives the end time, in units of the current time format. Can be **NULL**.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                                  | Description                                            |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Conversion to this format is not supported.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | **NULL** pointer argument.<br/>                  |



 

## Remarks

This method overrides the [**CPosPassThru::GetMediaTime**](cpospassthru-getmediatime.md) method. The time-stamp values are converted to the current time format by calling the [**CPosPassThru::ConvertTimeFormat**](cpospassthru-converttimeformat.md) method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




