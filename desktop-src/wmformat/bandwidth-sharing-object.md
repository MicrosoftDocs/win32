---
title: Bandwidth Sharing Object
description: Bandwidth Sharing Object
ms.assetid: 9dc863da-1842-41e7-b66c-c97e0140046d
keywords:
- Windows Media Format SDK,bandwidth sharing objects
- Advanced Systems Format (ASF),bandwidth sharing objects
- ASF (Advanced Systems Format),bandwidth sharing objects
- objects,bandwidth sharing objects
- bandwidth sharing,about
ms.topic: article
ms.date: 05/31/2018
---

# Bandwidth Sharing Object

A bandwidth sharing object is used to indicate that two or more streams, regardless of their individual bit rates, will never use more than a specified amount of bandwidth between them. This is a purely informational object; the bit rates set within it are not enforced programmatically by any object of this SDK.

Bandwidth sharing information is an optional part of a profile. Bandwidth sharing objects can be created for existing bandwidth sharing information in a profile or can be created empty, ready to receive new data. Bandwidth sharing objects cannot exist independently of a profile object. To save the contents of a bandwidth sharing object, you must call [**IWMProfile3::AddBandwidthSharing**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile3-addbandwidthsharing).

To create a bandwidth sharing object, call one of the following methods.



| Method                                                                                  | Description                                                                                                                                                    |
|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMProfile3::CreateNewBandwidthSharing**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile3-createnewbandwidthsharing) | Creates a bandwidth sharing object without any data.                                                                                                           |
| [**IWMProfile3::GetBandwidthSharing**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile3-getbandwidthsharing)             | Creates a bandwidth sharing object populated with data from a profile. Uses the bandwidth sharing index to identify the desired bandwidth sharing information. |



 

Both methods in the preceding table set a pointer to an **IWMBandwidthSharing** interface. The **IWMStreamList** interface is inherited by **IWMBandwidthSharing**, so there is no need to call **QueryInterface** with this object.

The following interfaces are supported by every bandwidth sharing object.



| Interface                                          | Description                                                             |
|----------------------------------------------------|-------------------------------------------------------------------------|
| [**IWMBandwidthSharing**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmbandwidthsharing) | Manages the properties of a group of streams that will share bandwidth. |
| [**IWMStreamList**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamlist)             | Manages the list of streams that will share bandwidth.                  |



 

## Related topics

<dl> <dt>

[**Bandwidth Sharing**](bandwidth-sharing.md)
</dt> <dt>

[**Profile Manager Object**](profile-manager-object.md)
</dt> <dt>

[**Profile Object**](profile-object.md)
</dt> </dl>

 

 




