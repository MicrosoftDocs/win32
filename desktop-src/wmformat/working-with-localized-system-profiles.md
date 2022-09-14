---
title: Working with Localized System Profiles
description: Working with Localized System Profiles
ms.assetid: d911baf6-0731-4f02-9001-d04464a03f56
keywords:
- profiles,system
- system profiles,localized
- system profiles,IWMProfileManagerLanguage interface
- localized system profiles,about
- IWMProfileManagerLanguage
ms.topic: article
ms.date: 05/31/2018
---

# Working with Localized System Profiles

The Windows Media Format SDK includes system profiles with names and descriptions in several languages. The localized system profile .prx files are installed into the \[SDKRoot\]\\WMSDK\\WMFSDK9\\LocalizedProfiles folder. To access a particular file with the **IWMProfileManagerLanguage** methods, you must move it into the system root directory along with the other system profile files. For a list of the localized system profile files, see [Localized System Profiles](localized-system-profiles.md).

You can set or retrieve the system profile language using the methods of the [**IWMProfileManagerLanguage**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofilemanagerlanguage) interface. The language is specified as a LANGID value, which consists of a primary language identifier and a secondary language identifier. The following code demonstrates how to retrieve the current language. The default language is U.S. English (0x409). For more information about using this code, see [Using the Code Examples](using-the-code-examples.md).


```C++
HRESULT GetCurrentSystemProfileLanguage(IMWProfilManager* pProfileMgr)
{
    HRESULT hr = S_OK;

    IWMProfileManagerLanguage* pProfileMgrLang = NULL;

    // Get the profile manager language interface.
    hr = pProfileMgr->QueryInterface(IID_IWMProfileManagerLanguage,
                                     (void **) &pProfileMgrLang);
    if(FAILED(hr))
    {
        printf("Couldn't get IWMProfileManagerLanguage.\n");
        SAFE_RELEASE(pProfileMgrLang);
        return hr;
    }

    // Retrieve the current language (as a LANGID value)
    WORD wLangID = 0;
    hr = pProfileMgrLang->GetUserLanguageID(&wLangID);
    if(FAILED(hr))
    {
        printf("Could not get the current language.\n");
        SAFE_RELEASE(pProfileMgrLang);
        return hr;
    }

    printf("The current language ID is 0x%X\n", wLangID);

    SAFE_RELEASE(pProfileMgrLang);
    return S_OK;
}
```



## Related topics

<dl> <dt>

[**Using System Profiles**](using-system-profiles.md)
</dt> </dl>

 

 




