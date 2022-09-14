---
description: The ChangeStop method is called when the stop position changes.
ms.assetid: 3d4a73a4-68e6-449c-9637-62cad937c4b4
title: CSourceSeeking.ChangeStop method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceSeeking.ChangeStop
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceSeeking.ChangeStop method

The `ChangeStop` method is called when the stop position changes.

## Syntax


```C++
virtual HRESULT ChangeStop() = 0;
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value.

## Remarks

The [**CSourceSeeking::SetPositions**](csourceseeking-setpositions.md) method calls this method if the stop position changes. This method is pure virtual; the derived class must implement it. The following example shows a possible implementation:


```C++
HRESULT CMyStream::ChangeStop( )
{
    UpdateFromSeek();
    return S_OK;
}
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




