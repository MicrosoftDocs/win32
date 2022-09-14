---
description: The Connect method completes a connection to the output pin.
ms.assetid: fb20ef5d-e00a-4154-a6da-25bef663c0e7
title: CPullPin.Connect method (Pullpin.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPullPin.Connect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPullPin.Connect method

The `Connect` method completes a connection to the output pin.

## Syntax


```C++
HRESULT Connect(
   IUnknown      *pUnk,
   IMemAllocator *pAlloc,
   BOOL          bSync
);
```



## Parameters

<dl> <dt>

*pUnk* 
</dt> <dd>

Pointer to the **IUnknown** interface of the output pin.

</dd> <dt>

*pAlloc* 
</dt> <dd>

Pointer to the [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) interface of the input pin's preferred allocator, or **NULL**.

</dd> <dt>

*bSync* 
</dt> <dd>

Boolean value that specifies whether to use synchronous reads. If **TRUE**, the pin performs synchronous read operations on the output pin. If **FALSE**, the pin makes asynchronous read requests.

</dd> </dl>

## Return value

Returns an **HRESULT**. Possible values include the following.



| Return code                                                                                               | Description                                                                     |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Success.<br/>                                                             |
| <dl> <dt>**VFW\_E\_ALREADY\_CONNECTED**</dt> </dl> | The input pin is already connected.<br/>                                  |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl>             | The output pin does not expose [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader).<br/> |



 

## Remarks

Call this method during the input pin's connection process. If the method fails, the pin should fail the connection.

This method queries the output pin for the **IAsyncReader** interface. If successful, it calls [**CPullPin::DecideAllocator**](cpullpin-decideallocator.md) to negotiate the allocator for the connection. If your input pin has a preferred allocator, specify it in the *pAlloc* parameter; the **DecideAllocator** method passes this pointer to the output pin's [**IAsyncReader::RequestAllocator**](/windows/desktop/api/Strmif/nf-strmif-iasyncreader-requestallocator) method. Otherwise, set *pAlloc* to **NULL**.

If the value of *bSync* is **TRUE**, the **CPullPin** object makes synchronous read requests, by calling the output pin's [**IAsyncReader::SyncReadAligned**](/windows/desktop/api/Strmif/nf-strmif-iasyncreader-syncreadaligned). Otherwise, it calls the [**IAsyncReader::Request**](/windows/desktop/api/Strmif/nf-strmif-iasyncreader-request) method to make overlapping read requests.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pullpin.h</dt> </dl>                                                                                                       |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPullPin Class**](cpullpin.md)
</dt> </dl>

 

 




