---
Description: The CreateInstance method creates a new instance of the CMemAllocator class.
ms.assetid: 87a831a4-2414-4240-8448-c5d90f130470
title: CMemAllocator.CreateInstance method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMemAllocator.CreateInstance method

The `CreateInstance` method creates a new instance of the **CMemAllocator** class.

## Syntax


```C++
static CUnknown* CreateInstance(
   LPUNKNOWN pUnk,
   HRESULT   *phr
);
```



## Parameters

<dl> <dt>

*pUnk* 
</dt> <dd>

Pointer to the owner of this object. If the object is aggregated, pass a pointer to the aggregating object's **IUnknown** interface. Otherwise, set this parameter to **NULL**.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to a variable that receives an **HRESULT** value indicating the success or failure of the method.

</dd> </dl>

## Return value

Returns a pointer to a new **CMemAllocator** object, typed as a **CUnknown** object.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMemAllocator Class**](cmemallocator.md)
</dt> </dl>

 

 




