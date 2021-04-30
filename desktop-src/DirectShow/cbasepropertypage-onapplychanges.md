---
description: The OnApplyChanges method is called when the user applies changes to the property page.
ms.assetid: 15a55644-b7bf-4c72-8e26-18fc4fb714b9
title: CBasePropertyPage.OnApplyChanges method (Cprop.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.OnApplyChanges
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePropertyPage.OnApplyChanges method

The `OnApplyChanges` method is called when the user applies changes to the property page.

## Syntax


```C++
virtual HRESULT OnApplyChanges();
```



## Parameters

This method has no parameters.

## Return value

The base-class implementation returns S\_OK.

## Remarks

The [**CBasePropertyPage::Apply**](cbasepropertypage-apply.md) method calls `OnApplyChanges` if the [**CBasePropertyPage::m\_bDirty**](cbasepropertypage-m-bdirty.md) flag is **TRUE**. Override `OnApplyChanges` to process the changes and reset **m\_bDirty** to **FALSE**.

## Examples


```C++
HRESULT CMyProp::OnApplyChanges(void)
{
    ASSERT(m_pOwningFilter != NULL);
    return m_pOwningFilter->SetSomeProperty(&m_lNewVal);
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

 

 




