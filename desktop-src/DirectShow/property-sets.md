---
description: Property Sets
ms.assetid: 4b8a917f-7a6c-4433-83f4-b83ef6d26115
title: Property Sets (DirectShow)
ms.topic: article
ms.date: 05/31/2018
---

# Property Sets (DirectShow)

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

 

 



