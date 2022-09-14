---
title: Mutual Exclusion Object
description: Mutual Exclusion Object
ms.assetid: dd1f7865-e409-4bf9-9fa0-769a29eaed60
keywords:
- Windows Media Format SDK,mutual exclusion objects
- Advanced Systems Format (ASF),mutual exclusion objects
- ASF (Advanced Systems Format),mutual exclusion objects
- objects,mutual exclusion objects
- mutual exclusion,objects
ms.topic: article
ms.date: 05/31/2018
---

# Mutual Exclusion Object

A mutual exclusion object is used to specify a number of streams, of which only one can be delivered at a time. This can be used in several ways, such as providing an audio stream in several languages as the soundtrack for one video stream.

Mutual exclusion is an optional part of a profile. Mutual exclusion objects can be created for existing mutual exclusion information in a profile or can be created empty, ready to receive new data. Mutual exclusion objects cannot exist independently of a profile object. To save the contents of a mutual exclusion object, you must call [**IWMProfile::AddMutualExclusion**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-addmutualexclusion).

To create a mutual exclusion object, use one of the following methods.



| Method                                                                              | Description                                                                                                                                                 |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMProfile::CreateNewMutualExclusion**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewmutualexclusion) | Creates a mutual exclusion object without any data.                                                                                                         |
| [**IWMProfile::GetMutualExclusion**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getmutualexclusion)             | Creates a mutual exclusion object populated with data from a profile. Uses the mutual exclusion index to identify the desired mutual exclusion information. |



 

Both methods in the preceding table set a pointer to an **IWMMutualExclusion** interface. The **IWMStreamList** interface is inherited by **IWMMutualExclusion** and never needs to be accessed directly. The other interface of the mutual exclusion object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by every mutual exclusion object.



| Interface                                          | Description                                                                                                                                            |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMMutualExclusion**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmutualexclusion)   | Sets and retrieves the type of mutual exclusion to be used.                                                                                            |
| [**IWMMutualExclusion2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmutualexclusion2) | Organizes streams into records, which can be used to create complex mutual exclusion scenarios. Inherits all of the methods of **IWMMutualExclusion**. |
| [**IWMStreamList**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamlist)             | Manages the list of mutually exclusive streams.                                                                                                        |



 

## Related topics

<dl> <dt>

[**Mutual Exclusion**](mutual-exclusion.md)
</dt> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Profile Manager Object**](profile-manager-object.md)
</dt> </dl>

 

 




