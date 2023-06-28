---
title: Using Custom Mutual Exclusion Types
description: Using Custom Mutual Exclusion Types
ms.assetid: 9a4d760c-80af-4c67-823d-6da2732671ff
keywords:
- IWMMutualExclusion
- mutual exclusion,IWMMutualExclusion interface
- mutual exclusion,custom types
- profiles,custom mutual exclusion types
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using Custom Mutual Exclusion Types

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can use mutual exclusion objects in a profile to meet the needs of custom scenarios. By passing the GUID value CLSID\_WMMUTEX\_Unknown to [**IWMMutualExclusion::SetType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmutualexclusion-settype), you inform the mutual exclusion object that you are using a custom scenario.

You must manually control stream selection when you read a file with a custom mutual exclusion value. The reader object will use the first stream you add to the mutual exclusion as the default.

Use the following steps to create a custom mutual exclusion object and add it to a profile:

1.  Create a profile manager by calling the [**WMCreateProfileManager**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager) function.
2.  Either start with an existing profile, or create an entirely new one.
    -   If you are using an existing profile, call one of the load methods of the [**IWMProfileManager**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofilemanager) interface. Then skip to step 4.
    -   If you are creating an entirely new profile, call [**IWMProfileManager::CreateEmptyProfile**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-createemptyprofile).
3.  Add streams to the new profile by calling [**IWMProfile::CreateNewStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewstream). Configure the streams as needed using the methods of [**IWMStreamConfig**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig). You can also call **QueryInterface** to access other interfaces in the stream configuration object.

    **CreateNewStream** creates only a stream configuration object, and does not affect the profile. After a stream is configured properly, you must call [**IWMProfile::AddStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-addstream) to add the stream to the profile.

4.  Create a mutual exclusion object by calling [**IWMProfile::CreateNewMutualExclusion**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewmutualexclusion).
5.  Add the desired streams to the mutual exclusion object by calling [**IWMStreamList::AddStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamlist-addstream) (available directly from [**IWMMutualExclusion**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmutualexclusion), which inherits from [**IWMStreamList**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamlist)).
6.  Set the type of mutual exclusion to custom by calling [**IWMMutualExclusion::SetType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmutualexclusion-settype). Pass the CLSID\_WMMUTEX\_Unknown as the type GUID.
7.  Add the configured mutual exclusion object to the profile by calling [**IWMProfile::AddMutualExclusion**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-addmutualexclusion).

## Related topics

<dl> <dt>

[**IWMMutualExclusion Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmutualexclusion)
</dt> <dt>

[**IWMProfile Interface**](iwmprofile.md)
</dt> <dt>

[**IWMProfileManager Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofilemanager)
</dt> <dt>

[**IWMStreamConfig Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig)
</dt> <dt>

[**IWMStreamList Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamlist)
</dt> <dt>

[**Using Mutual Exclusion**](using-mutual-exclusion.md)
</dt> <dt>

[**WMCreateProfileManager**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager)
</dt> </dl>

 

 




