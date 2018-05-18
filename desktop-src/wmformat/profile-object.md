---
title: Profile Object
description: Profile Object
ms.assetid: 'ec42889e-580e-4a65-9fe6-4a5f15c97eb0'
keywords: ["Windows Media Format SDK,profile objects", "Advanced Systems Format (ASF),profile objects", "ASF (Advanced Systems Format),profile objects", "objects,profile objects", "profiles,objects"]
---

# Profile Object

A profile object manages the settings of a profile. Profile objects can be created for existing profile data or can be created empty, ready to receive new data. A profile object is also created by the reader object (and the synchronous reader object) when a file is loaded for reading. In this case the object is populated with the profile information stored in the header of the file.

To save the contents of a profile object, you must call [**IWMProfileManager::SaveProfile**](iwmprofilemanager-saveprofile.md).

A profile contains multiple objects that control various aspects of the profile (such as streams). All of these objects are subordinate to the profile object. You do not create these objects with creation functions as you would with the major objects of this SDK. Instead, the interfaces of the profile object contain methods that create the subordinate objects.

To create a profile object, call one of the following methods.



| Method                                                                                | Description                                                                                                                                                     |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMProfileManager::CreateEmptyProfile**](iwmprofilemanager-createemptyprofile.md) | Creates a profile object without any profile data.                                                                                                              |
| [**IWMProfileManager::LoadProfileByData**](iwmprofilemanager-loadprofilebydata.md)   | Creates a profile object populated with data from a profile saved as a string. This is the only way to create a profile object with data from a custom profile. |
| [**IWMProfileManager::LoadProfileByID**](iwmprofilemanager-loadprofilebyid.md)       | Creates a profile object populated with data from a system profile. Uses the GUID to identify the desired system profile.                                       |
| [**IWMProfileManager::LoadSystemProfile**](iwmprofilemanager-loadsystemprofile.md)   | Creates a profile object populated with data from a system profile. Uses the profile index to identify the desired system profile.                              |



 

All of the methods in the preceding table set a pointer to an **IWMProfile** interface. The other interfaces of the profile object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by every profile object.



| Interface                                  | Description                                                                                                                                       |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMLanguageList**](iwmlanguagelist.md) | Manages a list of languages supported by an ASF file.                                                                                             |
| [**IWMPacketSize**](iwmpacketsize.md)     | Controls the maximum size of packets in a file.                                                                                                   |
| [**IWMPacketSize2**](iwmpacketsize2.md)   | Controls the minimum size of packets in a file. Inherits all of the methods of **IWMPacketSize**.                                                 |
| [**IWMProfile**](iwmprofile.md)           | Controls the basic settings and objects included in a profile.                                                                                    |
| [**IWMProfile2**](iwmprofile2.md)         | Retrieves the globally unique identifier (GUID) associated with the profile. Inherits all of the methods of **IWMProfile**.                       |
| [**IWMProfile3**](iwmprofile3.md)         | Controls bandwidth sharing and stream prioritization information in a profile. Inherits all of the methods of **IWMProfile** and **IWMProfile2**. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Profile Manager Object**](profile-manager-object.md)
</dt> <dt>

[**Profiles**](profiles.md)
</dt> </dl>

 

 




