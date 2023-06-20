---
description: Property Sets
ms.assetid: 4b8a917f-7a6c-4433-83f4-b83ef6d26115
title: Property Sets (DirectShow)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Property Sets (DirectShow)

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Microsoft DirectShow uses property sets to support extended services offered by hardware and its associated drivers and filters. Hardware and filter vendors can define new capabilities as properties, arrange them in property sets, and publish the specification for these property sets. As the application developer, you can use the methods of the [**IKsPropertySet**](ikspropertyset.md) interface to determine whether a driver or filter supports a particular set of properties, and retrieve or set those properties.

All the methods exposed by **IKsPropertySet** require a **GUID** that identifies the property set (the *guidPropSet* parameter) and a **DWORD** that identifies the property within the property set (the *dwPropID* parameter). The *dwPropID* parameter is typically a member of an enumerated data type.

Individual properties can have associated data that you specify in the *pPropData* parameter in the [**IKsPropertySet::Set**](ikspropertyset-set.md) and [**IKsPropertySet::Get**](ikspropertyset-get.md) methods. In these methods, the property data is typed as a pointer to `void`. The data type and the meaning of the data are specified in the definition of the property set.

The following sections provide information about the property sets supported in DirectShow:

-   [**DVD Copy Protection Property Set**](dvd-copy-protection-property-set.md)
-   [**DVD Karaoke Property Set**](dvd-karaoke-property-set.md)
-   [**DVD Subpicture Property Set**](dvd-subpicture-property-set.md)
-   [External Device Transport Property Set](external-device-transport-property-set.md)
-   [Frame Stepping Property Set](frame-stepping-property-set.md)
-   [Pin Property Set](pin-property-set.md)
-   [**Rate Change Property Set**](rate-change-property-set.md)

 

 



