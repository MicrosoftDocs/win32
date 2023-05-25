---
title: The LaunchPage Method
description: The LaunchPage Method
ms.assetid: f0f93535-5afc-4777-9188-5bbac63ddc6b
keywords:
- Windows Media Player plug-ins,LaunchPage method
- plug-ins,LaunchPage method
- user interface plug-ins,LaunchPage method
- UI plug-ins,LaunchPage method
- LaunchPage method
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# The LaunchPage Method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The LaunchPage method provides the primary functionality of the plug-in, which is to launch a search page containing information about the artist of the media item passed to the method.

This method is called by the OnSearch method using the current **Media** object.

The following code is used to implement this method:


```C++
void LaunchPage(IWMPMedia *pMedia)
{
    USES_CONVERSION;

    HRESULT hr;
    CComBSTR bstrType;
    CComBSTR bstrArtist;

    // Get the name of the artist.
    bstrType = _T("artist");
    hr = pMedia->getItemInfo(bstrType, &bstrArtist);
    if (SUCCEEDED(hr)) 
    {
        // Create the search URL.
        TCHAR szSearch[MAX_PATH];
        _stprintf_s(szSearch, MAX_PATH, _T("https://search.msn.com/results.asp?q=%s"), OLE2T(bstrArtist));
        CComBSTR bstrURL = szSearch;

        // Launch the search page.
        m_pPlugin->m_spCore->launchURL(bstrURL);
    }
    else
    {
        MessageBox(_T("Failed to get artist information from media."), _T("Warn"), MB_OK | MB_ICONWARNING);
    }
}

```



## Related topics

<dl> <dt>

[**Implementing CPluginWindow**](implementing-cpluginwindow.md)
</dt> </dl>

 

 




