---
description: The IsNormalRate method indicates whether the clip will play at the normal playback rate; that is, the playback rate of the original file.
ms.assetid: 4a8fe415-f9eb-450d-9a75-e528577050d9
title: IAMTimelineSrc::IsNormalRate method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.IsNormalRate
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineSrc::IsNormalRate method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IsNormalRate` method indicates whether the clip will play at the normal playback rate; that is, the playback rate of the original file.

## Syntax


```C++
HRESULT IsNormalRate(
   BOOL *pVal
);
```



## Parameters

<dl> <dt>

*pVal* 
</dt> <dd>

Receives a Boolean value indicating how the clip will render. If the value is **TRUE**, the clip will play at the normal rate. Otherwise, it will play faster or slower than normal.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

A clip's playback rate is determined by its media start and stop times, relative to its timeline times:


```C++
Playback rate = (Media Stop <entity type="mdash"/> Media Start) / (Timeline Stop <entity type="mdash"/> Timeline Start)
```



If this ratio is equal to 1, the clip plays at the authored speed. Otherwise, it plays faster or slower. For more information, see [Time in DirectShow Editing Services](time-in-directshow-editing-services.md).

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

[**IAMTimelineSrc Interface**](iamtimelinesrc.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




