---
description: The GetMediaLength method retrieves the media length of this source object.
ms.assetid: 70298d8f-67e7-4774-a7ae-f0b48e4afda7
title: IAMTimelineSrc::GetMediaLength method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.GetMediaLength
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineSrc::GetMediaLength method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetMediaLength` method retrieves the media length of this source object.

## Syntax


```C++
HRESULT GetMediaLength(
   REFERENCE_TIME *pLength
);
```



## Parameters

<dl> <dt>

*pLength* 
</dt> <dd>

Receives the media length in 100-nanosecond units.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                                     | Description                                        |
|-------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>            | Success.<br/>                                |
| <dl> <dt>**E\_NOTDETERMINED**</dt> </dl> | Media times are not set on this object.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>       | **NULL** pointer argument.<br/>              |



 

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

[**IAMTimelineSrc Interface**](iamtimelinesrc.md)
</dt> <dt>

[**IAMTimelineSrc::SetMediaLength**](iamtimelinesrc-setmedialength.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




