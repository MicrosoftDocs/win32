---
Description: The AllocFormatBuffer method allocates memory for the format block.
ms.assetid: 5ff716c7-f9cf-4b1c-9d3a-62ab955c1392
title: CMediaType.AllocFormatBuffer method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMediaType.AllocFormatBuffer method

The `AllocFormatBuffer` method allocates memory for the format block.

## Syntax


```C++
BYTE* AllocFormatBuffer(
   ULONG length
);
```



## Parameters

<dl> <dt>

*length* 
</dt> <dd>

Size required for the format block, in bytes.

</dd> </dl>

## Return value

Returns a pointer to the new block if successful. Otherwise, returns **NULL**.

## Remarks

If the method successfully allocates a new format block, it frees the existing format block. If the allocation fails, the method leaves the existing format block.

The method updates the **cbFormat** and **pbFormat** members of the **AM\_MEDIA\_TYPE** structure.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




