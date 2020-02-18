---
title: To Change System Profile Versions
description: To Change System Profile Versions
ms.assetid: 66bf4041-47b5-41b4-abb4-eb08d05e3b28
keywords:
- profiles,system
- system profiles,versions
- system profiles,changing versions
ms.topic: article
ms.date: 05/31/2018
---

# To Change System Profile Versions

Whenever you create a profile manager object, it parses the system profiles. You can iterate through the system profiles using the [**IWMProfileManager::GetSystemProfileCount**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-getsystemprofilecount) and [**IWMProfileManager::LoadSystemProfile**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-loadsystemprofile) methods, but the profile manager will count and list only the profiles of a single version at a time. If you want to use this method of finding system profiles, you need to ensure that the profile manger deals with the version you want. Use the methods of the [**IWMProfileManager2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofilemanager2) interface to set and retrieve the system profile version used by the profile manager.

Versions are specified using the members of the [**WMT\_VERSION**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_version) enumeration type. If you set the system profile version to WMT\_VER\_9\_0, the call will succeed, but the system profile count will be zero. This is because no predefined system profiles use the Windows Media Audio and Video 9 Series codecs. For more information about updating profiles to use the newest codecs, see [Reusing Stream Configurations](reusing-stream-configurations.md).

If you load a system profile by its GUID identifier, it does not matter which system profile version the profile manager is using. For more information about loading system profiles, see [To Load a System Profile](to-load-a-system-profile.md).

The following example code shows how to set and retrieve the system profile version. This example uses printf for console output and requires stdio.h to be included. For more information about using this code, see [Using the Code Examples](using-the-code-examples.md).


```C++
int main(void)
{
    HRESULT hr = S_OK;

    IWMProfileManager*  pProfileMgr  = NULL;
    IWMProfileManager2* pProfileMgr2 = NULL;

    WMT_VERSION         profileVersion;

    // Initialize COM.
    hr = CoInitialize(NULL);
    if(FAILED(hr))
    {
        printf("Could not initialize COM.");
        return 0;
    }

    // Create a profile manager object.
    hr = WMCreateProfileManager(&pProfileMgr);
    if(FAILED(hr))
    {
        printf("Could not create a profile manager object.");
        return 0;
    }

    // Get the IWMProfileManager2 interface.
    hr = pProfileMgr->QueryInterface(IID_IWMProfileManager2, 
                                     (void**) &pProfileMgr2);
    if(FAILED(hr))
    {
        printf("Could not get the IWMProfileManager2 interface.");
        SAFE_RELEASE(pProfileMgr);
        return 0;
    }

    // Release the old interface.
    SAFE_RELEASE(pProfileMgr);

    // Get the current system profile version.
    hr = pProfileMgr2->GetSystemProfileVersion(&profileVersion);
    if(FAILED(hr))
    {
        printf("Could not retrieve profile version.");
        printf("\nError code: 0x%X\n", hr);
        SAFE_RELEASE(pProfileMgr2);
        return 0;
    }
    
    // Display the current version.
    printf("Current version: ");
    switch(profileVersion)
    {
    case WMT_VER_4_0:
        printf("WMT_VER_4_0\n");
        break;
    case WMT_VER_7_0:
        printf("WMT_VER_7_0\n");
        break;
    case WMT_VER_8_0:
        printf("WMT_VER_8_0\n");
        break;
    case WMT_VER_9_0:
        printf("WMT_VER_9_0\n");
        break;
    }

    // Set the system profile version to 8.
    profileVersion = WMT_VER_8_0;

    hr = pProfileMgr2->SetSystemProfileVersion(profileVersion);
    if(FAILED(hr))
    {
        printf("Could not change profile version.");
        printf("\nError code: 0x%X\n", hr);
        SAFE_RELEASE(pProfileMgr2);
        return 0;
    }

    // Print verification.
    printf("Successfully set version to ");
    switch(profileVersion)
    {
    case WMT_VER_4_0:
        printf("WMT_VER_4_0\n");
        break;
    case WMT_VER_7_0:
        printf("WMT_VER_7_0\n");
        break;
    case WMT_VER_8_0:
        printf("WMT_VER_8_0\n");
        break;
    case WMT_VER_9_0:
        printf("WMT_VER_9_0\n");
        break;
    }

    // Clean up.
    SAFE_RELEASE(pProfileMgr2);
}
```



## Related topics

<dl> <dt>

[**Using System Profiles**](using-system-profiles.md)
</dt> </dl>

 

 




