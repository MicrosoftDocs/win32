---
title: To Load a System Profile
description: To Load a System Profile
ms.assetid: 2398a44d-c5c7-4fa2-b0ed-1cfb75d8822c
keywords:
- profiles,system
- system profiles,loading
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Load a System Profile

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To make changes to a system profile, you must load it into a profile object. The profile manager provides two options for loading system profiles: by identifier, and by index.

A system profile identifier is a GUID value assigned to the system profile when it was created. For a list of the GUID constants associated with the version 8 system profiles, see [System Profiles](system-profiles.md). You can find the GUID constants for previous versions in the header file WMSysPrf.h. For more information about this and other header files included with the Windows Media Format SDK, see [Library Files and Compiler Settings](library-files-and-compiler-settings.md).

The following example code demonstrates how to load a system profile using the system profile identifier. For this code to work, you must include WMSysPrf.h and stdio.h. For more information about using this code, see [Using the Code Examples](using-the-code-examples.md).


```C++
IWMProfileManager* pProfileMgr = NULL;
IWMProfile*        pProfile    = NULL;

HRESULT hr = S_OK;

// Initialize COM.
hr = CoInitialize(NULL);

// Create a profile manager.
hr = WMCreateProfileManager(&pProfileMgr);

// Retrieve the data for the general-purpose broadband video profile.
hr = pProfileMgr->LoadProfileByID(WMProfile_V80_100Video, &pProfile);

// TODO: Perform whatever customizations are needed. For details about
// editing profiles, see Using Custom Profiles.

// Clean up.
pProfile->Release();
pProfile = NULL;
pProfileMgr->Release();
pProfileMgr = NULL;
```



If you do not know which profile you want to use, you can iterate through all of the system profiles of a particular version using the [**GetSystemProfileCount**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-getsystemprofilecount) and [**LoadSystemProfile**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-loadsystemprofile) methods of the [**IWMProfileManager**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofilemanager) interface. These methods only deal with one version of the system profiles at a time. For more information about changing the system profile version, see [To Change System Profile Versions](to-change-system-profile-versions.md).

## Related topics

<dl> <dt>

[**Using System Profiles**](using-system-profiles.md)
</dt> </dl>

 

 




