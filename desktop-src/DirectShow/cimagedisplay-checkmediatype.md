---
description: The CheckMediaType method determines whether a proposed media type is compatible with the display format.
ms.assetid: 567663cf-c79f-4549-9fa9-b16da957d2b1
title: CImageDisplay.CheckMediaType method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageDisplay.CheckMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImageDisplay.CheckMediaType method

The `CheckMediaType` method determines whether a proposed media type is compatible with the display format.

## Syntax


```C++
HRESULT CheckMediaType(
   const CMediaType *pmtIn
);
```



## Parameters

<dl> <dt>

*pmtIn* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that contains the media type.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                  | Description                              |
|----------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Invalid media type.<br/>           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Invalid media type.<br/>           |
| <dl> <dt>**S\_OK**</dt> </dl>         | The media type is compatible.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageDisplay Class**](cimagedisplay.md)
</dt> </dl>

 

 




