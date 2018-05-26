---
Description: The Skip method skips over a specified number of media types. This method implements the IEnumMediaTypesSkip method.
ms.assetid: a01fb084-b227-4ca6-b5ca-c57d56e8b1aa
title: CEnumMediaTypes.Skip method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CEnumMediaTypes.Skip method

The `Skip` method skips over a specified number of media types. This method implements the [**IEnumMediaTypes::Skip**](/windows/win32/Strmif/nf-strmif-ienummediatypes-skip?branch=master) method.

## Syntax


```C++
HRESULT Skip(
   ULONG cMediaTypes
);
```



## Parameters

<dl> <dt>

*cMediaTypes* 
</dt> <dd>

Number of media types to skip.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                                | Description                                                                         |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>                    | Skipped past the end of the sequence.<br/>                                    |
| <dl> <dt>**S\_OK**</dt> </dl>                       | Success.<br/>                                                                 |
| <dl> <dt>**VFW\_E\_ENUM\_OUT\_OF\_SYNC**</dt> </dl> | The pin's state has changed and is now inconsistent with the enumerator.<br/> |



 

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CEnumMediaTypes Class**](cenummediatypes.md)
</dt> </dl>

 

 




