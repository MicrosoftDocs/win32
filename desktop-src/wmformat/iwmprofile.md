---
title: IWMProfile interface
description: The IWMProfile interface is the primary interface for a profile object.
ms.assetid: 00f28d6b-d27d-4268-960e-c8ea25e5359e
keywords:
- IWMProfile interface windows Media Format
- IWMProfile interface windows Media Format , described
topic_type:
- apiref
api_name:
- IWMProfile
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location:
- wmsdkidl.h
ms.custom: UpdateFrequency5
---

# IWMProfile interface

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **IWMProfile** interface is the primary interface for a [*profile*](wmformat-glossary.md) object. A profile object is used to configure custom profiles. You can use **IWMProfile** to create, delete, or modify stream configuration objects and mutual exclusion objects. You can also set and retrieve general information about the profile. To access all the features of the profile object, you should use [**IWMProfile3**](/previous-versions/windows/desktop/api/Wmsdkidl/nn-wmsdkidl-iwmprofile3), which inherits from **IWMProfile** and [**IWMProfile2**](/previous-versions/windows/desktop/api/Wmsdkidl/nn-wmsdkidl-iwmprofile2).

**IWMProfile** is also accessible through the reader object, where you can use it to get information about the streams of a file that is loaded in the reader. When accessing **IWMProfile** from the reader, you can make changes to the profile, but none of the changes can be saved to the file. It is often handy to use the profile of an existing file as the foundation of a new profile. The synchronous reader supports **IWMProfile** in the same way as the reader.

The profile information obtained through the reader or synchronous reader does not come from a .prx file. The reader uses the information in the ASF file to assemble the stream configurations. Thus certain profile information, like the name and description, are not available through the reader.

There are several ways to obtain a pointer to an **IWMProfile** interface. The profile manager has methods to create a new profile and to access existing profiles. All of these methods set an **IWMProfile** pointer. When reading a file, a pointer to **IWMProfile** can be obtained by calling the **QueryInterface** method of any reader interface. Likewise, any interface of the synchronous reader object can obtain a pointer with a call to **QueryInterface**[**IWMProfile3**](/previous-versions/windows/desktop/api/Wmsdkidl/nn-wmsdkidl-iwmprofile3).

## Members

The **IWMProfile** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWMProfile** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMProfile** interface has these methods.



| Method                                                                  | Description                                                                                 |
|:------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| [**AddMutualExclusion**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-addmutualexclusion)             | Adds a mutual exclusion object to the profile.<br/>                                   |
| [**AddStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-addstream)                               | Adds a stream to the profile.<br/>                                                    |
| [**CreateNewMutualExclusion**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewmutualexclusion) | Creates a mutual exclusion object for the profile.<br/>                               |
| [**CreateNewStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewstream)                   | Creates a stream configuration object for the profile.<br/>                           |
| [**GetDescription**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getdescription)                     | Retrieves the description of the profile.<br/>                                        |
| [**GetMutualExclusion**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getmutualexclusion)             | Retrieves a mutual exclusion object from the profile.<br/>                            |
| [**GetMutualExclusionCount**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getmutualexclusioncount)   | Retrieves the number of mutual exclusion objects in the profile.<br/>                 |
| [**GetName**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getname)                                   | Retrieves the name of the profile.<br/>                                               |
| [**GetStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstream)                               | Retrieves a stream, using an index number, from the profile.<br/>                     |
| [**GetStreamByNumber**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstreambynumber)               | Retrieves a stream, using the number of the stream, from the profile.<br/>            |
| [**GetStreamCount**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstreamcount)                     | Retrieves the number of streams in the profile.<br/>                                  |
| [**GetVersion**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getversion)                             | Retrieves the version number of Microsoft Windows Media Services in the profile.<br/> |
| [**ReconfigStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-reconfigstream)                     | Enables changes made to a stream configuration to be included in the profile.<br/>    |
| [**RemoveMutualExclusion**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-removemutualexclusion)       | Removes a mutual exclusion object from the profile.<br/>                              |
| [**RemoveStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-removestream)                         | Removes a stream from the profile.<br/>                                               |
| [**RemoveStreamByNumber**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-removestreambynumber)         | Removes a stream from the profile.<br/>                                               |
| [**SetDescription**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-setdescription)                     | Specifies the description of the profile.<br/>                                        |
| [**SetName**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-setname)                                   | Specifies the name of the profile.<br/>                                               |





For information about which interfaces can be obtained by using the QueryInterface method of this interface, see the topic for the object on which this interface is implemented.

## See also

<dl> <dt>

[**Interfaces**](interfaces.md)
</dt> <dt>

[**IWMProfileManager Interface**](/previous-versions/windows/desktop/api/Wmsdkidl/nn-wmsdkidl-iwmprofilemanager)
</dt> <dt>

[**Profile Manager Object**](profile-manager-object.md)
</dt> <dt>

[**Reader Object**](reader-object.md)
</dt> <dt>

[**Synchronous Reader Object**](synchronous-reader-object.md)
</dt> <dt>

[**Working with Profiles**](working-with-profiles.md)
</dt> </dl>
