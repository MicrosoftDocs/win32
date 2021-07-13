---
description: CBaseControlWindow.CBaseControlWindow constructor - Constructor method.
ms.assetid: 575f7f94-5f55-4834-bdb6-0db877187388
title: CBaseControlWindow.CBaseControlWindow constructor (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.CBaseControlWindow
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.CBaseControlWindow constructor

Constructor method.

## Syntax


```C++
CBaseControlWindow(
   CBaseMediaFilter *pFilter,
   CCritSec         *pInterfaceLock,
   TCHAR            *pName,
   LPUNKNOWN        pUnk,
   HRESULT          *phr
);
```



## Parameters

<dl> <dt>

*pFilter* 
</dt> <dd>

Pointer to the owning media filter object.

</dd> <dt>

*pInterfaceLock* 
</dt> <dd>

Pointer to the critical section to use for locking.

</dd> <dt>

*pName* 
</dt> <dd>

Pointer to the object description.

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the controlling **IUnknown** interface, if the object is part of an aggregate; otherwise, must be **NULL**.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to a variable that receives an HRESULT value indicating the success or failure of the constructor method.

</dd> </dl>

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




