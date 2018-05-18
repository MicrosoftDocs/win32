---
Description: 'WIA provides several interfaces for enumerating various capabilities, properties, and information.'
ms.assetid: 'd46d4c18-79cc-4f3c-9745-522ab2635068'
title: Using WIA Enumerators
---

# Using WIA Enumerators

WIA provides several interfaces for enumerating various capabilities, properties, and information. The Windows Image Acquisition (WIA) enumeration interfaces are all specific implementations of the standard Component Object Model (COM) enumeration interface. For details, see [IEnumXXXX](http://msdn.microsoft.com/en-us/library/ms680089(VS.85).aspx).

The following table provides information about the WIA enumeration interfaces. 

| Interface                                                   | How to Obtain a Pointer                                                                                                                                                                                    | Used For                                                                                                                             |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumWIA\_DEV\_CAPS**](-wia-ienumwia-dev-caps.md)       | Call a [**IWiaItem::EnumDeviceCapabilities**](-wia-iwiaitem-enumdevicecapabilities.md) or [**IWiaItem2::EnumDeviceCapabilities**](-wia-iwiaitem2-enumdevicecapabilities.md) method of a WIA root item's. | Enumerates the capabilities of a WIA hardware device, such as device commands and events.                                            |
| [**IEnumWIA\_DEV\_INFO**](-wia-ienumwia-dev-info.md)       | Call the [**IWiaDevMgr::EnumDeviceInfo**](-wia-iwiadevmgr-enumdeviceinfo.md) or [**IWiaDevMgr2::EnumDeviceInfo**](-wia-iwiadevmgr2-enumdeviceinfo.md) method.                                            | Enumerates available WIA devices, and provides pointers to their [**IWiaPropertyStorage**](-wia-iwiapropertystorage.md) interfaces. |
| [**IEnumWIA\_FORMAT\_INFO**](-wia-ienumwia-format-info.md) | Call an [**IWiaDataTransfer::idtEnumWIA\_FORMAT\_INFO**](-wia-iwiadatatransfer-idtenumwia-format-info.md) method of an item.                                                                              | Enumerates all image format information that a WIA item provides.                                                                    |
| [**IEnumWiaItem**](-wia-ienumwiaitem.md)                   | Call a [**IWiaItem::EnumChildItems**](-wia-iwiaitem-enumchilditems.md) or [**IWiaItem2::EnumChildItems**](-wia-iwiaitem2-enumchilditems.md) method of WIA item.                                          | Enumerates the child items of a WIA item that represents either a device or a folder.                                                |



 

 

 



