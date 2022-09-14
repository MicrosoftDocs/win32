---
description: The FreeMediaType function deletes the format block in an AM\_MEDIA\_TYPE structure.
ms.assetid: b7ec335e-518d-4aa6-8cde-8cb92184d0b0
title: FreeMediaType function (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FreeMediaType
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# FreeMediaType function

The **FreeMediaType** function deletes the format block in an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure.

## Syntax


```C++
void FreeMediaType(
   AM_MEDIA_TYPE &mt
);
```



## Parameters

<dl> <dt>

*mt* \[ref\]
</dt> <dd>

A reference to an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The format block is allocated on the heap. The **pbFormat** member of the [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) points to the format block. Use this function to free just the format block. To delete an allocated **AM\_MEDIA\_TYPE** structure, call [**DeleteMediaType**](deletemediatype.md).

This function is defined in the [DirectShow Base Classes](directshow-base-classes.md) library. If you prefer not to link to the base class library, you can use the following code:


```C++
// Release the format block for a media type.

void _FreeMediaType(AM_MEDIA_TYPE& mt)
{
    if (mt.cbFormat != 0)
    {
        CoTaskMemFree((PVOID)mt.pbFormat);
        mt.cbFormat = 0;
        mt.pbFormat = NULL;
    }
    if (mt.pUnk != NULL)
    {
        // pUnk should not be used.
        mt.pUnk->Release();
        mt.pUnk = NULL;
    }
}
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**DeleteMediaType**](deletemediatype.md)
</dt> <dt>

[**Media Type Functions**](media-type-functions.md)
</dt> </dl>

 

 




