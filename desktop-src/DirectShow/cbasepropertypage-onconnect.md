---
description: The OnConnect method provides an IUnknown pointer to the object associated with the property page.
ms.assetid: 74cae8e1-5347-4e3d-ba5f-6a4efec2ddae
title: CBasePropertyPage.OnConnect method (Cprop.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.OnConnect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePropertyPage.OnConnect method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `OnConnect` method provides an **IUnknown** pointer to the object associated with the property page.

## Syntax


```C++
virtual HRESULT OnConnect(
   IUnknown *pUnknown
);
```



## Parameters

<dl> <dt>

*pUnknown* 
</dt> <dd>

Pointer to the **IUnknown** interface of the object.

</dd> </dl>

## Return value

The base-class implementation returns S\_OK.

## Remarks

The [**CBasePropertyPage::SetObjects**](cbasepropertypage-setobjects.md) method calls the `OnConnect` method. Override this method to store a pointer to the object specified by *pUnknown*. You can either store the *pUnknown* pointer itself, or query that pointer for other interfaces. If you store the *pUnknown* pointer, call **AddRef** before `OnConnect` returns.

In the [**CBasePropertyPage::OnActivate**](cbasepropertypage-onactivate.md) method, use the stored pointer (or pointers) to retrieve initial values for the dialog properties. In the [**CBasePropertyPage::OnApplyChanges**](cbasepropertypage-onapplychanges.md) method, apply any changes back to the object. Release all pointers in the [**CBasePropertyPage::OnDisconnect**](cbasepropertypage-ondisconnect.md) method.

## Examples


```C++
HRESULT CMyProp::OnConnect(IUnknown *pUnk)
{
    ASSERT(m_pOwningFilter == NULL);
    HRESULT hr;
    // Query pUnk for the filter's custom interface.
    hr = pUnk->QueryInterface(IID_ISomeCustomInterface,
             reinterpret_cast<void**>(&m_pOwningFilter));
    return hr;
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

 

 




