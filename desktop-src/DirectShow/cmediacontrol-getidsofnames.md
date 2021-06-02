---
description: Maps a single member function and an optional set of parameters to a corresponding set of integer dispatch identifiers (DISPIDs), which can be used upon subsequent calls to the CMediaControl::Invoke member function.
ms.assetid: 9ce1b1aa-ea03-4a65-bff7-e46771cd0772
title: CMediaControl.GetIDsOfNames method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaControl.GetIDsOfNames
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaControl.GetIDsOfNames method

Maps a single member function and an optional set of parameters to a corresponding set of integer dispatch identifiers (DISPIDs), which can be used upon subsequent calls to the [**CMediaControl::Invoke**](cmediacontrol-invoke.md) member function.

## Syntax


```C++
HRESULT GetIDsOfNames(
   REFIID  riid,
   OLECHAR **rgszNames,
   UINT    cNames,
   LCID    lcid,
   DISPID  *rgdispid
);
```



## Parameters

<dl> <dt>

*riid* 
</dt> <dd>

Reference identifier. Reserved for future use. Must be **NULL**.

</dd> <dt>

*rgszNames* 
</dt> <dd>

Address of a pointer to a passed-in array of names to be mapped.

</dd> <dt>

*cNames* 
</dt> <dd>

Count of the names to be mapped.

</dd> <dt>

*lcid* 
</dt> <dd>

Locale context in which to interpret the names.

</dd> <dt>

*rgdispid* 
</dt> <dd>

Pointer to a caller-allocated array, each element of which contains an ID corresponding to one of the names passed in the *rgszNames* array. The first element represents the member name; the subsequent elements represent each of the member's parameters.

</dd> </dl>

## Return value

Returns one of the following values.



| Return code                                                                                            | Description                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DISP\_E\_UNKNOWN\_CLSID**</dt> </dl> | The CLSID was not recognized.<br/>                                                                                                             |
| <dl> <dt>**DISP\_E\_UNKNOWNNAME**</dt> </dl>    | One or more of the names were not known. The returned DISPIDs contain DISPID\_UNKNOWN for each entry that corresponds to an unknown name.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>          | Out of memory.<br/>                                                                                                                            |
| <dl> <dt>**S\_OK**</dt> </dl>                   | Success.<br/>                                                                                                                                  |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaControl Class**](cmediacontrol.md)
</dt> </dl>

 

 




