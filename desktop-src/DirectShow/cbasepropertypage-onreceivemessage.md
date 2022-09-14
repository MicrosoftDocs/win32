---
description: The OnReceiveMessage method is called when the dialog box receives a message.
ms.assetid: ea93500d-fd0f-4820-a54a-a186c40899ad
title: CBasePropertyPage.OnReceiveMessage method (Cprop.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.OnReceiveMessage
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePropertyPage.OnReceiveMessage method

The `OnReceiveMessage` method is called when the dialog box receives a message.

## Syntax


```C++
virtual INT_PTR OnReceiveMessage(
   HWND   hwnd,
   UINT   uMsg,
   WPARAM wParam,
   LPARAM lParam
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

Handle to the window.

</dd> <dt>

*uMsg* 
</dt> <dd>

Message.

</dd> <dt>

*wParam* 
</dt> <dd>

First message parameter.

</dd> <dt>

*lParam* 
</dt> <dd>

Second message parameter.

</dd> </dl>

## Return value

Returns a Boolean value. The dialog procedure returns this value; for more information, see the Platform SDK documentation.

## Remarks

The base-class implementation calls **DefWindowProc**. Override this method to handle messages that relate to the dialog controls. If the overriding method does not handle a particular message, it should call the base-class method.

If the user changes any properties via the dialog controls, set the [**CBasePropertyPage::m\_bDirty**](cbasepropertypage-m-bdirty.md) flag to **TRUE**. Then call the **IPropertyPageSite::OnStatusChange** method on the [**CBasePropertyPage::m\_pPageSite**](cbasepropertypage-m-ppagesite.md) pointer to inform the frame.

## Examples

The following example responds to a button click by updating a member variable, which is assumed to be defined in the derived class. This example also shows a helper function for setting the property page's dirty status.


```C++
INT_PTR CMyProp::OnReceiveMessage(HWND hwnd,
  UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
    case WM_COMMAND:
        if (LOWORD(wParam) == IDC_BUTTON1)
        {
            m_lNewVal = GetDlgItemInt(m_Dlg, IDC_EDIT1, 0, TRUE);
            SetDirty();
            return (INT_PTR)TRUE;
        }
        break;
    } // switch

    // Did not handle the message.
    return CBasePropertyPage::OnReceiveMessage(hwnd, uMsg, wParam, lParam);
}

// Helper function to update the dirty status.
void CMyProp::SetDirty()
{
    m_bDirty = TRUE;
    if (m_pPageSite)
    {
        m_pPageSite->OnStatusChange(PROPPAGESTATUS_DIRTY);
    }
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

 

 




