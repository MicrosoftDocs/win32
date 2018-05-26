---
title: Using Custom Mutual Exclusion Types
description: Using Custom Mutual Exclusion Types
ms.assetid: 9a4d760c-80af-4c67-823d-6da2732671ff
keywords:
- IWMMutualExclusion
- mutual exclusion,IWMMutualExclusion interface
- mutual exclusion,custom types
- profiles,custom mutual exclusion types
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Custom Mutual Exclusion Types

You can use mutual exclusion objects in a profile to meet the needs of custom scenarios. By passing the GUID value CLSID\_WMMUTEX\_Unknown to [**IWMMutualExclusion::SetType**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmmutualexclusion-settype?branch=master), you inform the mutual exclusion object that you are using a custom scenario.

You must manually control stream selection when you read a file with a custom mutual exclusion value. The reader object will use the first stream you add to the mutual exclusion as the default.

Use the following steps to create a custom mutual exclusion object and add it to a profile:

1.  Create a profile manager by calling the [**WMCreateProfileManager**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager?branch=master) function.
2.  Either start with an existing profile, or create an entirely new one.
    -   If you are using an existing profile, call one of the load methods of the [**IWMProfileManager**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmprofilemanager?branch=master) interface. Then skip to step 4.
    -   If you are creating an entirely new profile, call [**IWMProfileManager::CreateEmptyProfile**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-createemptyprofile?branch=master).
3.  Add streams to the new profile by calling [**IWMProfile::CreateNewStream**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewstream?branch=master). Configure the streams as needed using the methods of [**IWMStreamConfig**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmstreamconfig?branch=master). You can also call **QueryInterface** to access other interfaces in the stream configuration object.

    **CreateNewStream** creates only a stream configuration object, and does not affect the profile. After a stream is configured properly, you must call [**IWMProfile::AddStream**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-addstream?branch=master) to add the stream to the profile.

4.  Create a mutual exclusion object by calling [**IWMProfile::CreateNewMutualExclusion**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewmutualexclusion?branch=master).
5.  Add the desired streams to the mutual exclusion object by calling [**IWMStreamList::AddStream**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmstreamlist-addstream?branch=master) (available directly from [**IWMMutualExclusion**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmmutualexclusion?branch=master), which inherits from [**IWMStreamList**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmstreamlist?branch=master)).
6.  Set the type of mutual exclusion to custom by calling [**IWMMutualExclusion::SetType**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmmutualexclusion-settype?branch=master). Pass the CLSID\_WMMUTEX\_Unknown as the type GUID.
7.  Add the configured mutual exclusion object to the profile by calling [**IWMProfile::AddMutualExclusion**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-addmutualexclusion?branch=master).

## Related topics

<dl> <dt>

[**IWMMutualExclusion Interface**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmmutualexclusion?branch=master)
</dt> <dt>

[**IWMProfile Interface**](iwmprofile.md)
</dt> <dt>

[**IWMProfileManager Interface**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmprofilemanager?branch=master)
</dt> <dt>

[**IWMStreamConfig Interface**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmstreamconfig?branch=master)
</dt> <dt>

[**IWMStreamList Interface**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmstreamlist?branch=master)
</dt> <dt>

[**Using Mutual Exclusion**](using-mutual-exclusion.md)
</dt> <dt>

[**WMCreateProfileManager**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager?branch=master)
</dt> </dl>

 

 




