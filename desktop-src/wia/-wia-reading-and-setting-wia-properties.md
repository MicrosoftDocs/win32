---
description: The IWiaPropertyStorage interface provides methods for reading and writing a Windows Image Acquisition (WIA) item's properties. Item properties include device commands, item format information, and device information.
ms.assetid: 268d2298-bc9c-479b-b078-a8180cd38bc3
title: Reading and Setting WIA Properties
ms.topic: article
ms.date: 05/31/2018
---

# Reading and Setting WIA Properties

The [**IWiaPropertyStorage**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiapropertystorage) interface provides methods for reading and writing a Windows Image Acquisition (WIA) item's properties. Item properties include device commands, item format information, and device information.

An application can obtain a pointer to an [**IWiaPropertyStorage**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiapropertystorage) interface of an item either by enumerating the item's device information or event information by calling [**IWiaItem::EnumDeviceCapabilities**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiaitem-enumdevicecapabilities) or [**IWiaItem::EnumRegisterEventInfo**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiaitem-enumregistereventinfo) or by querying the [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) interface of the item. (In WIA 2.0, do this by calling [**IWiaItem2::EnumDeviceCapabilities**](-wia-iwiaitem2-enumdevicecapabilities.md) or [**IWiaItem2::EnumRegisterEventInfo**](-wia-iwiaitem2-enumregistereventinfo.md) or by querying the [**IWiaItem2**](-wia-iwiaitem2.md) interface of the item.)

[**IWiaPropertyStorage**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiapropertystorage) inherits from [IPropertyStorage](/windows/win32/api/propidlbase/nn-propidlbase-ipropertystorage) and the inherited methods are implemented as described in the reference section of Structured Storage in the Windows Software Development Kit (SDK).

> [!Note]
>
> WIA applications should always read image data headers for accurate image information. The WIA driver can alter the WIA properties and image data headers during data transfer.
>
> If there is no image data header supplied with the specified format, the WIA application should use the WIA properties as an information source about the data transfer. The WIA application should reread the needed WIA properties after the scan or capture completes to get the updated settings.

 

The following sections describe the various WIA properties:

-   [WIA Property Validation](-wia-wia-property-validation.md)
-   [Device Information Properties](-wia-device-information-properties-wia-dip-xxxx.md)
-   [Device Properties](-wia-device-properties.md)
-   [Item Properties](-wia-item-properties.md)
-   [Additional WIA Properties](-wia-additional-wia-properties.md)
-   [Defining Custom Properties](-wia-defining-custom-properties.md)
-   [Using Custom Properties](-wia-using-custom-properties.md)
-   [Scan Profile Schema](-wia-scan-profile-schema.md)

 

 
