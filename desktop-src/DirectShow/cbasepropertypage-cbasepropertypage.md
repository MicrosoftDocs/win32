---
description: CBasePropertyPage.CBasePropertyPage constructor - Constructor method.
ms.assetid: 5d9863e7-fdd9-4df2-a603-34a240a2286c
title: CBasePropertyPage.CBasePropertyPage constructor (Cprop.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.CBasePropertyPage
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePropertyPage.CBasePropertyPage constructor

Constructor method.

## Syntax


```C++
CBasePropertyPage(
   TCHAR     *pName,
   LPUNKNOWN pUnk,
   int       DialogId,
   int       TitleId
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

String that contains the name of the object, for debugging purposes. For more information, see [**CBaseObject::CBaseObject**](cbaseobject-cbaseobject.md).

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the aggregating **IUnknown** interface.

</dd> <dt>

*DialogId* 
</dt> <dd>

Resource ID for the dialog box.

</dd> <dt>

*TitleId* 
</dt> <dd>

Resource ID for the string that contains the dialog box title.

</dd> </dl>

## Examples


```C++
CMyProp::CMyProp(IUnknown *pUnk) : 
    CBasePropertyPage(NAME("MyPropPage"), pUnk, IDD_PROPPAGE, IDS_TITLE),
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> </dl>

 

 




