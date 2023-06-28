---
description: Step 8.
ms.assetid: c54745ef-beeb-40b6-9db6-6e3b5da860f8
title: Step 8. Apply Property Changes
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Step 8. Apply Property Changes

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Override the [**CBasePropertyPage::OnApplyChanges**](cbasepropertypage-onapplychanges.md) method to commit any property changes. In this example, the m\_lNewVal variable is updated whenever the user scrolls the slider bar. The **OnApplyChanges** method copies this value into the m\_lVal variable, overwriting the original value:


```C++
HRESULT CGrayProp::OnApplyChanges(void)
{
    m_lVal = m_lNewVal;
    return S_OK;
} 
```



Next: [Step 9. Disconnect the Property Page](step-9--disconnect-the-property-page.md).

## Related topics

<dl> <dt>

[Creating a Filter Property Page](creating-a-filter-property-page.md)
</dt> </dl>

 

 



