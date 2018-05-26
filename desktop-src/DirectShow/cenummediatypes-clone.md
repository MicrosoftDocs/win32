---
Description: The Clone method makes a copy of the enumerator with the same enumeration state. This method implements the IEnumMediaTypesClone method.
ms.assetid: 3b4eb29e-48fc-4f00-a5f3-597b9aa94ce1
title: CEnumMediaTypes.Clone method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CEnumMediaTypes.Clone method

The `Clone` method makes a copy of the enumerator with the same enumeration state. This method implements the [**IEnumMediaTypes::Clone**](/windows/win32/Strmif/nf-strmif-ienummediatypes-clone?branch=master) method.

## Syntax


```C++
HRESULT Clone(
   IEnumMediaTypes **ppEnum
);
```



## Parameters

<dl> <dt>

*ppEnum* 
</dt> <dd>

Address of a variable that receives a pointer to the [**IEnumMediaTypes**](/windows/win32/Strmif/nn-strmif-ienummediatypes?branch=master) interface of the new enumerator.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                                | Description                                                                         |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Success.<br/>                                                                 |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>              | Insufficient memory.<br/>                                                     |
| <dl> <dt>**E\_POINTER**</dt> </dl>                  | **NULL** pointer argument.<br/>                                               |
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

 

 




