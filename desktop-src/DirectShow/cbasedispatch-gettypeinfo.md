---
description: The GetTypeInfo method retrieves the type information for the object, which can then be used to get the type information for an interface.
ms.assetid: aa06b97c-541b-44fc-bdef-97fd1f014e85
title: CBaseDispatch.GetTypeInfo method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseDispatch.GetTypeInfo
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseDispatch.GetTypeInfo method

The `GetTypeInfo` method retrieves the type information for the object, which can then be used to get the type information for an interface.

## Syntax


```C++
HRESULT GetTypeInfo(
   REFIID    riid,
   UINT      itinfo,
   LCID      lcid,
   ITypeInfo **pptinfo
);
```



## Parameters

<dl> <dt>

*riid* 
</dt> <dd>

Reference to an interface identifier (IID) that specifies the interface.

</dd> <dt>

*itinfo* 
</dt> <dd>

Type information to return. Must be zero.

</dd> <dt>

*lcid* 
</dt> <dd>

Locale identifier.

</dd> <dt>

*pptinfo* 
</dt> <dd>

Address of a variable that receives an **ITypeInfo** pointer.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                             | Description                                    |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Success.<br/>                            |
| <dl> <dt>**E\_POINTER**</dt> </dl>               | **NULL** pointer argument.<br/>          |
| <dl> <dt>**TYPE\_E\_ELEMENTNOTFOUND**</dt> </dl> | The *itinfo* parameter is not zero.<br/> |



 

## Remarks

This method behaves like the **IDispatch::GetTypeInfo** method. However, it includes an additional parameter, *riid*, which specifies the interface for which to retrieve type information.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseDispatch Class**](cbasedispatch.md)
</dt> </dl>

 

 




