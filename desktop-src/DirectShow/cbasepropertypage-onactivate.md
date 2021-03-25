---
description: The OnActivate method is called when the property page is activated.
ms.assetid: aff843d4-cfb2-4255-a59c-0579f1cd24bd
title: CBasePropertyPage.OnActivate method (Cprop.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.OnActivate
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePropertyPage.OnActivate method

The `OnActivate` method is called when the property page is activated.

## Syntax


```C++
virtual HRESULT OnActivate();
```



## Parameters

This method has no parameters.

## Return value

The base-class implementation returns S\_OK.

## Remarks

The [**CBasePropertyPage::Activate**](cbasepropertypage-activate.md) method calls the `OnActivate` method. In your derived class, override `OnActivate` to initialize the dialog box.

## Examples

The following example initializes a trackbar control. This example assumes that **m\_pOwningFilter** is a pointer to a custom interface on the filter associated with the property page. (Use the [**CBasePropertyPage::OnConnect**](cbasepropertypage-onconnect.md) method to initialize such pointers.)


```C++
HRESULT CMyProp::OnActivate(void)
{
    ASSERT(m_pOwningFilter != NULL);
    m_pOwningFilter->GetSomeProperty(&m_lOldVal);
    
    SendDlgItemMessage(m_Dlg, IDC_SLIDER1, TBM_SETRANGE, 0, MAKELONG(0, 100));
    SendDlgItemMessage(m_Dlg, IDC_SLIDER1, TBM_SETTICFREQ, 10, 0);
    SendDlgItemMessage(m_Dlg, IDC_SLIDER1, TBM_SETPOS, 1, m_lOldVal);
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

 

 




