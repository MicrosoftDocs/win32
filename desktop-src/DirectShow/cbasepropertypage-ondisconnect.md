---
description: The OnDisconnect method is called when the property page should release the associated object.
ms.assetid: 55bab0ca-587e-405c-9025-f391cf08a620
title: CBasePropertyPage.OnDisconnect method (Cprop.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.OnDisconnect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePropertyPage.OnDisconnect method

The `OnDisconnect` method is called when the property page should release the associated object.

## Syntax


```C++
virtual HRESULT OnDisconnect();
```



## Parameters

This method has no parameters.

## Return value

The base-class implementation returns S\_OK.

## Remarks

The [**CBasePropertyPage::SetObjects**](cbasepropertypage-setobjects.md) method calls the `OnDisconnect` method. Override `OnDisconnect` to release any pointers that were obtained in the [**CBasePropertyPage::OnConnect**](cbasepropertypage-onconnect.md) method.

## Examples


```C++
HRESULT CMyProp::OnDisconnect(void)
{
    if (m_pOwningFilter)
    {
        m_pOwningFilter->Release();
        m_pOwningFilter = NULL;
    }
    return S_OK;
}
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

 

 




