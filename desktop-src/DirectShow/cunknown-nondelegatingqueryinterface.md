---
description: Retrieves an interface pointer and increments the reference count. This method implements the INonDelegatingUnknown::NonDelegatingQueryInterface method.
ms.assetid: 451ca350-f40b-4cbf-ac39-e86dadb48a24
title: CUnknown.NonDelegatingQueryInterface method (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CUnknown.NonDelegatingQueryInterface
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CUnknown.NonDelegatingQueryInterface method

Retrieves an interface pointer and increments the reference count. This method implements the **INonDelegatingUnknown::NonDelegatingQueryInterface** method.

## Syntax


```C++
HRESULT NonDelegatingQueryInterface(
   REFIID riid,
   void   **ppv
);
```



## Parameters

<dl> <dt>

*riid* 
</dt> <dd>

Identifier of the interface.

</dd> <dt>

*ppv* 
</dt> <dd>

Address of a pointer to receive the interface.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                   | Description                                        |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                                |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | Object does not support this interface.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | **NULL** pointer argument.<br/>              |



 

## Remarks

The **CUnknown** class exposes only the **IUknown** interface. Override this method to expose additional interfaces. For information on how to override this method, see [How to Implement IUnknown](how-to-implement-iunknown.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




