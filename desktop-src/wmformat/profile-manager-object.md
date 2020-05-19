---
title: Profile Manager Object
description: Profile Manager Object
ms.assetid: 8d174243-334e-418e-a1c8-77486b940de7
keywords:
- Windows Media Format SDK,profile manager objects
- Advanced Systems Format (ASF),profile manager objects
- ASF (Advanced Systems Format),profile manager objects
- objects,profile manager objects
- profiles,objects
- profiles,profile manager objects
ms.topic: article
ms.date: 05/31/2018
---

# Profile Manager Object

A profile is a set of media parameters used to create an ASF file. The profile manager object creates profile objects for editing. Profile objects can be created without any data in them or built from existing profile data. The profile manager object also provides methods for enumerating supported codecs and querying those codecs for information.

The profile manager object is created by the [**WMCreateProfileManager**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager) function, which sets a pointer to an [**IWMProfileManager**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofilemanager) interface. The other interfaces of the profile manager object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the profile manager object.



| Interface                                                      | Description                                                                                                                                  |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMCodecInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmcodecinfo)                           | Retrieves information about supported codecs and their formats.                                                                              |
| [**IWMCodecInfo2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmcodecinfo2)                         | Retrieves the names of the supported codecs and the descriptions of their formats. Inherits all of the methods of **IWMCodecInfo**.          |
| [**IWMCodecInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmcodecinfo3)                         | Retrieves codec properties and queries codecs for supported features. Inherits all of the methods of **IWMCodecInfo** and **IWMCodecInfo2**. |
| [**IWMProfileManager**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofilemanager)                 | Creates new profiles, loads existing profiles, and saves custom profiles.                                                                    |
| [**IWMProfileManager2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofilemanager2)               | Controls the version of system profiles enumerated by the profile manager. Inherits all of the methods of **IWMProfileManager**.             |
| [**IWMProfileManagerLanguage**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofilemanagerlanguage) | Controls the language of the system profiles parsed by the profile manager.                                                                  |



 

## Remarks

When a profile manager object is created, it parses all of the system profiles, which can take several seconds. Creating and releasing a profile manager every time you need to use it will adversely affect performance. You should create a profile manager once in your application and release it only when you no longer need to use it.

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Profile Object**](profile-object.md)
</dt> <dt>

[**Profiles**](profiles.md)
</dt> </dl>

 

 




