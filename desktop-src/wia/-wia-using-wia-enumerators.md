---
description: WIA provides several interfaces for enumerating various capabilities, properties, and information.
ms.assetid: d46d4c18-79cc-4f3c-9745-522ab2635068
title: Using WIA Enumerators
ms.topic: article
ms.date: 05/31/2018
---

# Using WIA Enumerators

WIA provides several interfaces for enumerating various capabilities, properties, and information. The Windows Image Acquisition (WIA) enumeration interfaces are all specific implementations of the standard Component Object Model (COM) enumeration interface. For details, see [IEnumXXXX](/previous-versions//ms680089(v=vs.85)).

The following table provides information about the WIA enumeration interfaces. 

| Interface                                                   | How to Obtain a Pointer                                                                                                                                                                                    | Used For                                                                                                                             |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumWIA\_DEV\_CAPS**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwia_dev_caps)       | Call a [**IWiaItem::EnumDeviceCapabilities**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiaitem-enumdevicecapabilities) or [**IWiaItem2::EnumDeviceCapabilities**](-wia-iwiaitem2-enumdevicecapabilities.md) method of a WIA root item's. | Enumerates the capabilities of a WIA hardware device, such as device commands and events.                                            |
| [**IEnumWIA\_DEV\_INFO**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwia_dev_info)       | Call the [**IWiaDevMgr::EnumDeviceInfo**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadevmgr-enumdeviceinfo) or [**IWiaDevMgr2::EnumDeviceInfo**](-wia-iwiadevmgr2-enumdeviceinfo.md) method.                                            | Enumerates available WIA devices, and provides pointers to their [**IWiaPropertyStorage**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiapropertystorage) interfaces. |
| [**IEnumWIA\_FORMAT\_INFO**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwia_format_info) | Call an [**IWiaDataTransfer::idtEnumWIA\_FORMAT\_INFO**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadatatransfer-idtenumwia_format_info) method of an item.                                                                              | Enumerates all image format information that a WIA item provides.                                                                    |
| [**IEnumWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwiaitem)                   | Call a [**IWiaItem::EnumChildItems**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiaitem-enumchilditems) or [**IWiaItem2::EnumChildItems**](-wia-iwiaitem2-enumchilditems.md) method of WIA item.                                          | Enumerates the child items of a WIA item that represents either a device or a folder.                                                |



 

 

 
