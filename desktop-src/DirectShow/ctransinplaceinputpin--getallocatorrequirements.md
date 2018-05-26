---
Description: The GetAllocatorRequirements method retrieves the allocator properties requested by the pin. This method implements the IMemInputPinGetAllocatorRequirements method.
ms.assetid: 1355facc-f863-44b2-9284-8f06f62d39a2
title: CTransInPlaceInputPin.GetAllocatorRequirements method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransInPlaceInputPin.GetAllocatorRequirements method

The `GetAllocatorRequirements` method retrieves the allocator properties requested by the pin. This method implements the [**IMemInputPin::GetAllocatorRequirements**](/windows/win32/Strmif/nf-strmif-imeminputpin-getallocatorrequirements?branch=master) method.

## Syntax


```C++
HRESULT GetAllocatorRequirements(
   ALLOCATOR_PROPERTIES *pProps
);
```



## Parameters

<dl> <dt>

*pProps* 
</dt> <dd>

Pointer to an [**ALLOCATOR\_PROPERTIES**](/windows/win32/strmif/ns-strmif-_allocatorproperties?branch=master) structure, which is filled in with the requirements.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                               | Description                                                                                          |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Success<br/>                                                                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The output pin is not connected, or the downstream input pin does not support the method.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument<br/>                                                                 |



 

## Remarks

If the output pin is connected, this method passes the call to the downstream input pin. Otherwise, it returns E\_NOTIMPL.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceInputPin Class**](ctransinplaceinputpin.md)
</dt> </dl>

 

 




