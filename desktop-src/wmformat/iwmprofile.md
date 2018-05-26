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
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWMProfile interface

The **IWMProfile** interface is the primary interface for a [*profile*](wmformat-glossary.md#wmformat-profile) object. A profile object is used to configure custom profiles. You can use **IWMProfile** to create, delete, or modify stream configuration objects and mutual exclusion objects. You can also set and retrieve general information about the profile. To access all the features of the profile object, you should use [**IWMProfile3**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmprofile3?branch=master), which inherits from **IWMProfile** and [**IWMProfile2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmprofile2?branch=master).

**IWMProfile** is also accessible through the reader object, where you can use it to get information about the streams of a file that is loaded in the reader. When accessing **IWMProfile** from the reader, you can make changes to the profile, but none of the changes can be saved to the file. It is often handy to use the profile of an existing file as the foundation of a new profile. The synchronous reader supports **IWMProfile** in the same way as the reader.

The profile information obtained through the reader or synchronous reader does not come from a .prx file. The reader uses the information in the ASF file to assemble the stream configurations. Thus certain profile information, like the name and description, are not available through the reader.

There are several ways to obtain a pointer to an **IWMProfile** interface. The profile manager has methods to create a new profile and to access existing profiles. All of these methods set an **IWMProfile** pointer. When reading a file, a pointer to **IWMProfile** can be obtained by calling the **QueryInterface** method of any reader interface. Likewise, any interface of the synchronous reader object can obtain a pointer with a call to **QueryInterface**[**IWMProfile3**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmprofile3?branch=master).

## Members

The **IWMProfile** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IWMProfile** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMProfile** interface has these methods.



| Method                                                                  | Description                                                                                 |
|:------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| [**AddMutualExclusion**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-addmutualexclusion?branch=master)             | Adds a mutual exclusion object to the profile.<br/>                                   |
| [**AddStream**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-addstream?branch=master)                               | Adds a stream to the profile.<br/>                                                    |
| [**CreateNewMutualExclusion**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewmutualexclusion?branch=master) | Creates a mutual exclusion object for the profile.<br/>                               |
| [**CreateNewStream**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewstream?branch=master)                   | Creates a stream configuration object for the profile.<br/>                           |
| [**GetDescription**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-getdescription?branch=master)                     | Retrieves the description of the profile.<br/>                                        |
| [**GetMutualExclusion**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-getmutualexclusion?branch=master)             | Retrieves a mutual exclusion object from the profile.<br/>                            |
| [**GetMutualExclusionCount**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-getmutualexclusioncount?branch=master)   | Retrieves the number of mutual exclusion objects in the profile.<br/>                 |
| [**GetName**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-getname?branch=master)                                   | Retrieves the name of the profile.<br/>                                               |
| [**GetStream**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstream?branch=master)                               | Retrieves a stream, using an index number, from the profile.<br/>                     |
| [**GetStreamByNumber**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstreambynumber?branch=master)               | Retrieves a stream, using the number of the stream, from the profile.<br/>            |
| [**GetStreamCount**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstreamcount?branch=master)                     | Retrieves the number of streams in the profile.<br/>                                  |
| [**GetVersion**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-getversion?branch=master)                             | Retrieves the version number of Microsoft Windows Media Services in the profile.<br/> |
| [**ReconfigStream**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-reconfigstream?branch=master)                     | Enables changes made to a stream configuration to be included in the profile.<br/>    |
| [**RemoveMutualExclusion**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-removemutualexclusion?branch=master)       | Removes a mutual exclusion object from the profile.<br/>                              |
| [**RemoveStream**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-removestream?branch=master)                         | Removes a stream from the profile.<br/>                                               |
| [**RemoveStreamByNumber**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-removestreambynumber?branch=master)         | Removes a stream from the profile.<br/>                                               |
| [**SetDescription**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-setdescription?branch=master)                     | Specifies the description of the profile.<br/>                                        |
| [**SetName**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-setname?branch=master)                                   | Specifies the name of the profile.<br/>                                               |



 

For information about which interfaces can be obtained by using the QueryInterface method of this interface, see the topic for the object on which this interface is implemented.

## See also

<dl> <dt>

[**Interfaces**](interfaces.md)
</dt> <dt>

[**IWMProfileManager Interface**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmprofilemanager?branch=master)
</dt> <dt>

[**Profile Manager Object**](profile-manager-object.md)
</dt> <dt>

[**Reader Object**](reader-object.md)
</dt> <dt>

[**Synchronous Reader Object**](synchronous-reader-object.md)
</dt> <dt>

[**Working with Profiles**](working-with-profiles.md)
</dt> </dl>

 

 





