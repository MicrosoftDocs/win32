---
description: When an application connects to a Windows Image Acquisition (WIA) hardware device, WIA creates an item tree (a hierarchical tree of IWiaItem or IWiaItem2 interfaces) that represents the device and its images, folders, and scanning beds.
ms.assetid: 2a7bcfd4-4075-48a4-9eff-5210b9a635e3
title: Selecting a Device (WIA)
ms.topic: article
ms.date: 05/31/2018
---

# Selecting a Device (WIA)

When an application connects to a Windows Image Acquisition (WIA) hardware device, WIA creates an item tree (a hierarchical tree of [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) or [**IWiaItem2**](-wia-iwiaitem2.md) interfaces) that represents the device and its images, folders, and scanning beds. An application can select and connect to a device without user input, or it can display a dialog box that allows a user to select a device.

-   [Selecting a Device Without the UI](#selecting-a-device-without-the-ui)
-   [Selecting a Device With the UI](#selecting-a-device-with-the-ui)

## Selecting a Device Without the UI

Perform the following steps to select and connect to a WIA hardware device.

-   Call [CoCreateInstance](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to retrieve a pointer to the [**IWiaDevMgr**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadevmgr) or [**IWiaDevMgr2**](-wia-iwiadevmgr2.md) interface.
-   Use the [**IWiaDevMgr::EnumDeviceInfo**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadevmgr-enumdeviceinfo) method of the [**IWiaDevMgr**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadevmgr) or [**IWiaDevMgr2**](-wia-iwiadevmgr2.md) interface to obtain a pointer to the [**IEnumWIA\_DEV\_INFO**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwia_dev_info) interface. For instructions on how to enumerate devices, see [Enumerating System Devices](-wia-enumerating-system-devices.md).
-   Use [**IEnumWIA\_DEV\_INFO**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwia_dev_info) interface to obtain [**IWiaPropertyStorage**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiapropertystorage) interface pointers for each WIA device enumerated.
-   Use [**IWiaPropertyStorage**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiapropertystorage) interface to inspect the device information properties of each device and save the WIA\_DIP\_DEV\_ID property from the desired device.
-   Use the DeviceID property with the [**IWiaDevMgr::CreateDevice**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadevmgr-createdevice) method in the [**IWiaDevMgr**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadevmgr) or [**IWiaDevMgr2**](-wia-iwiadevmgr2.md) interface to create a WIA device object. The **IWiaDevMgr::CreateDevice** method provides the application with the pointer to the [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) or [**IWiaItem2**](-wia-iwiaitem2.md) interface of the root item of the specified device.

For an example of how to do this in an application, see [Creating a Device](-wia-creating-a-device.md) in the tutorial section of this guide.

## Selecting a Device With the UI

After retrieving a pointer to [**IWiaDevMgr**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadevmgr), an application can allow a user to select a device by skipping the rest of the above steps and calling [**IWiaDevMgr::SelectDeviceDlg**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadevmgr-selectdevicedlg). The **IWiaDevMgr::SelectDeviceDlg** displays a dialog box in which the user can select a WIA device.

It is recommended that applications make device and image selection available through a menu item named **From scanner** on the **File** menu.

 

 
