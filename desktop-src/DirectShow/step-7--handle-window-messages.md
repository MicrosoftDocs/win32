---
description: Step 7.
ms.assetid: 12bb1288-e764-4bc1-bea5-196e17cf3557
title: Step 7. Handle Window Messages
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Step 7. Handle Window Messages

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Override the [**CBasePropertyPage::OnReceiveMessage**](cbasepropertypage-onreceivemessage.md) method to update the dialog controls in response to user input. If you don't handle a particular message, call the **OnReceiveMessage** method on the parent class. Whenever the user changes a property, do the following:

-   Set the **m\_bDirty** variable of the property page to **TRUE**.
-   Call the **IPropertyPageSite::OnStatusChange** method of the property frame with the PROPPAGESTATUS\_DIRTY flag. This flag informs the property frame that it should enable the **Apply** button. The [**CBasePropertyPage::m\_pPageSite**](cbasepropertypage-m-ppagesite.md) member holds a pointer to the **IPropertyPageSite** interface.

To simplify this step, you can add the following helper function to your property page:


```C++
private:
    void SetDirty()
    {
        m_bDirty = TRUE;
        if (m_pPageSite)
        {
            m_pPageSite->OnStatusChange(PROPPAGESTATUS_DIRTY);
        }
    }
```



Call this private method inside **OnReceiveMessage** whenever a user action changes a property, as shown in the following example:


```C++
BOOL CGrayProp::OnReceiveMessage(HWND hwnd,
    UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
    case WM_COMMAND:
        if (LOWORD(wParam) == IDC_DEFAULT)
        {
            // User clicked the 'Revert to Default' button.
            m_lNewVal = SATURATION_DEFAULT;
            m_pGray->SetSaturation(m_lNewVal);

            // Update the slider control.
            SendDlgItemMessage(m_Dlg, IDC_SLIDER1, TBM_SETPOS, 1,
                m_lNewVal);
            SetDirty();
            return (LRESULT) 1;
        }
        break;

    case WM_HSCROLL:
        {
            // User moved the slider.
            switch(LOWORD(wParam))
            {
            case TB_PAGEDOWN:
            case SB_THUMBTRACK:
            case TB_PAGEUP:
                m_lNewVal = SendDlgItemMessage(m_Dlg, IDC_SLIDER1,
                    TBM_GETPOS, 0, 0);
                m_pGray->SetSaturation(m_lNewVal);
                SetDirty();
            }
            return (LRESULT) 1;
        }
    } // Switch.
    
    // Let the parent class handle the message.
    return CBasePropertyPage::OnReceiveMessage(hwnd,uMsg,wParam,lParam);
} 
```



The property page in this example has two controls, a slider bar and a **Revert to Default** button. If the user scrolls the slider bar, the property page sets the saturation value on the filter. If the user clicks the button, the property page restores the filter's default saturation value. In each case, m\_lNewVal holds the current value and m\_lVal holds the original value. The value of m\_lVal is not updated until the user commits the change, which happens when the user clicks the **OK** or **Apply** button on the property frame.

Next: [Step 8. Apply Property Changes](step-8--apply-property-changes.md).

## Related topics

<dl> <dt>

[Creating a Filter Property Page](creating-a-filter-property-page.md)
</dt> </dl>

 

 



