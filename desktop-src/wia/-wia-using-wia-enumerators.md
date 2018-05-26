---
Description: WIA provides several interfaces for enumerating various capabilities, properties, and information.
ms.assetid: d46d4c18-79cc-4f3c-9745-522ab2635068
title: Using WIA Enumerators
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using WIA Enumerators

WIA provides several interfaces for enumerating various capabilities, properties, and information. The Windows Image Acquisition (WIA) enumeration interfaces are all specific implementations of the standard Component Object Model (COM) enumeration interface. For details, see [IEnumXXXX](http://msdn.microsoft.com/en-us/library/ms680089(VS.85).aspx).

The following table provides information about the WIA enumeration interfaces. 

| Interface                                                   | How to Obtain a Pointer                                                                                                                                                                                    | Used For                                                                                                                             |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumWIA\_DEV\_CAPS**](/windows/win32/wia_xp/nn-wia_xp-ienumwia_dev_caps?branch=master)       | Call a [**IWiaItem::EnumDeviceCapabilities**](/windows/win32/wia_xp/nf-wia_xp-iwiaitem-enumdevicecapabilities?branch=master) or [**IWiaItem2::EnumDeviceCapabilities**](-wia-iwiaitem2-enumdevicecapabilities.md) method of a WIA root item's. | Enumerates the capabilities of a WIA hardware device, such as device commands and events.                                            |
| [**IEnumWIA\_DEV\_INFO**](/windows/win32/wia_xp/nn-wia_xp-ienumwia_dev_info?branch=master)       | Call the [**IWiaDevMgr::EnumDeviceInfo**](/windows/win32/wia_xp/nf-wia_xp-iwiadevmgr-enumdeviceinfo?branch=master) or [**IWiaDevMgr2::EnumDeviceInfo**](-wia-iwiadevmgr2-enumdeviceinfo.md) method.                                            | Enumerates available WIA devices, and provides pointers to their [**IWiaPropertyStorage**](/windows/win32/wia_xp/nn-wia_xp-iwiapropertystorage?branch=master) interfaces. |
| [**IEnumWIA\_FORMAT\_INFO**](/windows/win32/wia_xp/nn-wia_xp-ienumwia_format_info?branch=master) | Call an [**IWiaDataTransfer::idtEnumWIA\_FORMAT\_INFO**](/windows/win32/wia_xp/nf-wia_xp-iwiadatatransfer-idtenumwia_format_info?branch=master) method of an item.                                                                              | Enumerates all image format information that a WIA item provides.                                                                    |
| [**IEnumWiaItem**](/windows/win32/wia_xp/nn-wia_xp-ienumwiaitem?branch=master)                   | Call a [**IWiaItem::EnumChildItems**](/windows/win32/wia_xp/nf-wia_xp-iwiaitem-enumchilditems?branch=master) or [**IWiaItem2::EnumChildItems**](-wia-iwiaitem2-enumchilditems.md) method of WIA item.                                          | Enumerates the child items of a WIA item that represents either a device or a folder.                                                |



 

 

 



