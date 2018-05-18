---
title: Using Custom Mutual Exclusion Types
description: Using Custom Mutual Exclusion Types
ms.assetid: '9a4d760c-80af-4c67-823d-6da2732671ff'
keywords: ["IWMMutualExclusion", "mutual exclusion,IWMMutualExclusion interface", "mutual exclusion,custom types", "profiles,custom mutual exclusion types"]
---

# Using Custom Mutual Exclusion Types

You can use mutual exclusion objects in a profile to meet the needs of custom scenarios. By passing the GUID value CLSID\_WMMUTEX\_Unknown to [**IWMMutualExclusion::SetType**](iwmmutualexclusion-settype.md), you inform the mutual exclusion object that you are using a custom scenario.

You must manually control stream selection when you read a file with a custom mutual exclusion value. The reader object will use the first stream you add to the mutual exclusion as the default.

Use the following steps to create a custom mutual exclusion object and add it to a profile:

1.  Create a profile manager by calling the [**WMCreateProfileManager**](wmcreateprofilemanager.md) function.
2.  Either start with an existing profile, or create an entirely new one.
    -   If you are using an existing profile, call one of the load methods of the [**IWMProfileManager**](iwmprofilemanager.md) interface. Then skip to step 4.
    -   If you are creating an entirely new profile, call [**IWMProfileManager::CreateEmptyProfile**](iwmprofilemanager-createemptyprofile.md).
3.  Add streams to the new profile by calling [**IWMProfile::CreateNewStream**](iwmprofile-createnewstream.md). Configure the streams as needed using the methods of [**IWMStreamConfig**](iwmstreamconfig.md). You can also call **QueryInterface** to access other interfaces in the stream configuration object.

    **CreateNewStream** creates only a stream configuration object, and does not affect the profile. After a stream is configured properly, you must call [**IWMProfile::AddStream**](iwmprofile-addstream.md) to add the stream to the profile.

4.  Create a mutual exclusion object by calling [**IWMProfile::CreateNewMutualExclusion**](iwmprofile-createnewmutualexclusion.md).
5.  Add the desired streams to the mutual exclusion object by calling [**IWMStreamList::AddStream**](iwmstreamlist-addstream.md) (available directly from [**IWMMutualExclusion**](iwmmutualexclusion.md), which inherits from [**IWMStreamList**](iwmstreamlist.md)).
6.  Set the type of mutual exclusion to custom by calling [**IWMMutualExclusion::SetType**](iwmmutualexclusion-settype.md). Pass the CLSID\_WMMUTEX\_Unknown as the type GUID.
7.  Add the configured mutual exclusion object to the profile by calling [**IWMProfile::AddMutualExclusion**](iwmprofile-addmutualexclusion.md).

## Related topics

<dl> <dt>

[**IWMMutualExclusion Interface**](iwmmutualexclusion.md)
</dt> <dt>

[**IWMProfile Interface**](iwmprofile.md)
</dt> <dt>

[**IWMProfileManager Interface**](iwmprofilemanager.md)
</dt> <dt>

[**IWMStreamConfig Interface**](iwmstreamconfig.md)
</dt> <dt>

[**IWMStreamList Interface**](iwmstreamlist.md)
</dt> <dt>

[**Using Mutual Exclusion**](using-mutual-exclusion.md)
</dt> <dt>

[**WMCreateProfileManager**](wmcreateprofilemanager.md)
</dt> </dl>

 

 




