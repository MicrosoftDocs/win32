---
description: The IsClassID method determines whether a CLSID matches this class template.
ms.assetid: de560f7a-2ccb-44e2-ac32-3b0fea0d80b8
title: CFactoryTemplate.IsClassID method (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CFactoryTemplate.IsClassID
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CFactoryTemplate.IsClassID method

The `IsClassID` method determines whether a CLSID matches this class template.

## Syntax


```C++
BOOL IsClassID(
   REFCLSID rclsid
);
```



## Parameters

<dl> <dt>

*rclsid* 
</dt> <dd>

Reference to a CLSID.

</dd> </dl>

## Return value

Returns **TRUE** if the *rclsid* parameter is the same CLSID as the [**CFactoryTemplate::m\_ClsID**](cfactorytemplate-m-clsid.md) member variable, or else returns **FALSE**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CFactoryTemplate Class**](cfactorytemplate.md)
</dt> </dl>

 

 




