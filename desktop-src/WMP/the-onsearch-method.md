---
title: The OnSearch Method
description: The OnSearch Method
ms.assetid: 709bb428-1a5e-4b8d-8622-5fcc816f0a1a
keywords:
- Windows Media Player plug-ins,OnSearch method
- plug-ins,OnSearch method
- user interface plug-ins,OnSearch method
- UI plug-ins,OnSearch method
- OnSearch method
ms.topic: article
ms.date: 05/31/2018
---

# The OnSearch Method

The OnSearch method is called by Windows Media Player when the **Search** button is clicked. This method retrieves the current **Media** object and passes it to the LaunchPage method.

The following code is used to implement this method:


```C++
LRESULT OnSearch(WORD wNotifyCode, WORD wID, HWND hwndCtl, BOOL& fHandled)
{
    HRESULT hr;
    CComPtr<IWMPMedia> spMedia;

    if( m_pPlugin && m_pPlugin->m_spCore )
    {
        // Get a pointer to the current media item.
        hr = m_pPlugin->m_spCore->get_currentMedia(&spMedia);
        if (SUCCEEDED(hr) && spMedia)
        {
            LaunchPage(spMedia);
        }
    else
        {
            MessageBox(_T("There is no media loaded."), _T("Warn"), MB_OK | MB_ICONWARNING);
        }
    }
    return 0;
}

```



## Related topics

<dl> <dt>

[**Implementing CPluginWindow**](implementing-cpluginwindow.md)
</dt> </dl>

 

 




