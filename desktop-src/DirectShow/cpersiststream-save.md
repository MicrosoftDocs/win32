---
description: Saves the filter's data to the given stream.
ms.assetid: f45c8c6e-f0bb-4358-805a-da2669706d34
title: CPersistStream.Save method (Pstream.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPersistStream.Save
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPersistStream.Save method

Saves the filter's data to the given stream.

## Syntax


```C++
HRESULT Save(
   LPSTREAM pStm,
   BOOL     fClearDirty
);
```



## Parameters

<dl> <dt>

*pStm* 
</dt> <dd>

Pointer to the stream to which data is to be saved.

</dd> <dt>

*fClearDirty* 
</dt> <dd>

Flag that indicates whether to reset the current stream's dirty flag; **TRUE** means to reset it. (When the method is called as part of a Save operation, the value is typically **TRUE**; when called as part of a Save As operation, the value is typically **FALSE**.)

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function implements the **IPersistStream::Save** method. It calls **WriteInt** with the software version, calls [**CPersistStream::WriteToStream**](cpersiststream-writetostream.md) with the stream in *pStm*, and resets **mPS\_fDirty**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pstream.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPersistStream Class**](cpersiststream.md)
</dt> </dl>

 

 




