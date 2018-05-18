---
title: IWMProfile interface
description: The IWMProfile interface is the primary interface for a profile object.
ms.assetid: '00f28d6b-d27d-4268-960e-c8ea25e5359e'
keywords: ["IWMProfile interface windows Media Format", "IWMProfile interface windows Media Format , described"]
topic_type:
- apiref
api_name:
- IWMProfile
api_type:
- COM
---

# IWMProfile interface

The **IWMProfile** interface is the primary interface for a [*profile*](wmformat-glossary.md#wmformat-profile) object. A profile object is used to configure custom profiles. You can use **IWMProfile** to create, delete, or modify stream configuration objects and mutual exclusion objects. You can also set and retrieve general information about the profile. To access all the features of the profile object, you should use [**IWMProfile3**](iwmprofile3.md), which inherits from **IWMProfile** and [**IWMProfile2**](iwmprofile2.md).

**IWMProfile** is also accessible through the reader object, where you can use it to get information about the streams of a file that is loaded in the reader. When accessing **IWMProfile** from the reader, you can make changes to the profile, but none of the changes can be saved to the file. It is often handy to use the profile of an existing file as the foundation of a new profile. The synchronous reader supports **IWMProfile** in the same way as the reader.

The profile information obtained through the reader or synchronous reader does not come from a .prx file. The reader uses the information in the ASF file to assemble the stream configurations. Thus certain profile information, like the name and description, are not available through the reader.

There are several ways to obtain a pointer to an **IWMProfile** interface. The profile manager has methods to create a new profile and to access existing profiles. All of these methods set an **IWMProfile** pointer. When reading a file, a pointer to **IWMProfile** can be obtained by calling the **QueryInterface** method of any reader interface. Likewise, any interface of the synchronous reader object can obtain a pointer with a call to **QueryInterface**[**IWMProfile3**](iwmprofile3.md).

## Members

The **IWMProfile** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IWMProfile** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMProfile** interface has these methods.



| Method                                                                  | Description                                                                                 |
|:------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| [**AddMutualExclusion**](iwmprofile-addmutualexclusion.md)             | Adds a mutual exclusion object to the profile.<br/>                                   |
| [**AddStream**](iwmprofile-addstream.md)                               | Adds a stream to the profile.<br/>                                                    |
| [**CreateNewMutualExclusion**](iwmprofile-createnewmutualexclusion.md) | Creates a mutual exclusion object for the profile.<br/>                               |
| [**CreateNewStream**](iwmprofile-createnewstream.md)                   | Creates a stream configuration object for the profile.<br/>                           |
| [**GetDescription**](iwmprofile-getdescription.md)                     | Retrieves the description of the profile.<br/>                                        |
| [**GetMutualExclusion**](iwmprofile-getmutualexclusion.md)             | Retrieves a mutual exclusion object from the profile.<br/>                            |
| [**GetMutualExclusionCount**](iwmprofile-getmutualexclusioncount.md)   | Retrieves the number of mutual exclusion objects in the profile.<br/>                 |
| [**GetName**](iwmprofile-getname.md)                                   | Retrieves the name of the profile.<br/>                                               |
| [**GetStream**](iwmprofile-getstream.md)                               | Retrieves a stream, using an index number, from the profile.<br/>                     |
| [**GetStreamByNumber**](iwmprofile-getstreambynumber.md)               | Retrieves a stream, using the number of the stream, from the profile.<br/>            |
| [**GetStreamCount**](iwmprofile-getstreamcount.md)                     | Retrieves the number of streams in the profile.<br/>                                  |
| [**GetVersion**](iwmprofile-getversion.md)                             | Retrieves the version number of Microsoft Windows Media Services in the profile.<br/> |
| [**ReconfigStream**](iwmprofile-reconfigstream.md)                     | Enables changes made to a stream configuration to be included in the profile.<br/>    |
| [**RemoveMutualExclusion**](iwmprofile-removemutualexclusion.md)       | Removes a mutual exclusion object from the profile.<br/>                              |
| [**RemoveStream**](iwmprofile-removestream.md)                         | Removes a stream from the profile.<br/>                                               |
| [**RemoveStreamByNumber**](iwmprofile-removestreambynumber.md)         | Removes a stream from the profile.<br/>                                               |
| [**SetDescription**](iwmprofile-setdescription.md)                     | Specifies the description of the profile.<br/>                                        |
| [**SetName**](iwmprofile-setname.md)                                   | Specifies the name of the profile.<br/>                                               |



 

For information about which interfaces can be obtained by using the QueryInterface method of this interface, see the topic for the object on which this interface is implemented.

## See also

<dl> <dt>

[**Interfaces**](interfaces.md)
</dt> <dt>

[**IWMProfileManager Interface**](iwmprofilemanager.md)
</dt> <dt>

[**Profile Manager Object**](profile-manager-object.md)
</dt> <dt>

[**Reader Object**](reader-object.md)
</dt> <dt>

[**Synchronous Reader Object**](synchronous-reader-object.md)
</dt> <dt>

[**Working with Profiles**](working-with-profiles.md)
</dt> </dl>

 

 





