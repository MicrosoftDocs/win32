---
title: Creating Profiles
description: Creating Profiles
ms.assetid: af4a8efe-d797-4d19-961d-b917e4c7c81a
keywords:
- Windows Media Format SDK,profiles
- profiles,creating
- profiles,IWMProfileManager interface
- IWMProfileManager,creating profiles
- profiles,WMCreateProfileManager function
- WMCreateProfileManager
ms.topic: article
ms.date: 05/31/2018
---

# Creating Profiles

In many cases, you will want to create an empty profile to configure for your needs. In other cases it is easier to edit an existing profile, like a system profile. For more information about using system profiles, see [Using System Profiles](using-system-profiles.md).

Creating an empty profile, ready for you to configure, requires a profile manager object. To get the [**IWMProfileManager**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofilemanager) interface of a profile manager object, call the [**WMCreateProfileManager**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager) function.

To create an empty profile, call [**IWMProfileManager::CreateEmptyProfile**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-createemptyprofile). When you create an empty profile, the only thing you specify is the version of the Windows Media Format SDK with which the profile complies. Unless you have a specific need to use a previous version, you should always use the latest version. The version dictates the structure of the profile; previous versions did not support some properties.

The following example code shows how to create a new profile. To compile this code in your application, include stdio.h. For more information about using this code, see [Using the Code Examples](using-the-code-examples.md).


```C++
HRESULT CreateProfile(IWMProfileManager* pProfileMgr, IWMProfile** ppProfile)
{
    HRESULT hr = S_OK;

    // Create the empty profile.
    hr = pProfileMgr->CreateEmptyProfile(WMT_VER_9_0, ppProfile);
    if(FAILED(hr))
    {
        printf("Could not create the profile.\n");
        return hr;
    }

    return S_OK;
}
```



## Related topics

<dl> <dt>

[**IWMProfile Interface**](iwmprofile.md)
</dt> <dt>

[**IWMProfileManager Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofilemanager)
</dt> <dt>

[**Working with Profiles**](working-with-profiles.md)
</dt> </dl>

 

 




