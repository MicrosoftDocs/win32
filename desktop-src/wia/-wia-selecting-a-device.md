---
Description: When an application connects to a Windows Image Acquisition (WIA) hardware device, WIA creates an item tree (a hierarchical tree of IWiaItem or IWiaItem2 interfaces) that represents the device and its images, folders, and scanning beds.
ms.assetid: 2a7bcfd4-4075-48a4-9eff-5210b9a635e3
title: Selecting a Device
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Selecting a Device

When an application connects to a Windows Image Acquisition (WIA) hardware device, WIA creates an item tree (a hierarchical tree of [**IWiaItem**](/windows/win32/wia_xp/nn-wia_xp-iwiaitem?branch=master) or [**IWiaItem2**](-wia-iwiaitem2.md) interfaces) that represents the device and its images, folders, and scanning beds. An application can select and connect to a device without user input, or it can display a dialog box that allows a user to select a device.

-   [Selecting a Device Without the UI](#selecting-a-device-without-the-ui)
-   [Selecting a Device With the UI](#selecting-a-device-with-the-ui)

## Selecting a Device Without the UI

Perform the following steps to select and connect to a WIA hardware device.

-   Call [CoCreateInstance](com.cocreateinstance) to retrieve a pointer to the [**IWiaDevMgr**](/windows/win32/wia_xp/nn-wia_xp-iwiadevmgr?branch=master) or [**IWiaDevMgr2**](-wia-iwiadevmgr2.md) interface.
-   Use the [**IWiaDevMgr::EnumDeviceInfo**](/windows/win32/wia_xp/nf-wia_xp-iwiadevmgr-enumdeviceinfo?branch=master) method of the [**IWiaDevMgr**](/windows/win32/wia_xp/nn-wia_xp-iwiadevmgr?branch=master) or [**IWiaDevMgr2**](-wia-iwiadevmgr2.md) interface to obtain a pointer to the [**IEnumWIA\_DEV\_INFO**](/windows/win32/wia_xp/nn-wia_xp-ienumwia_dev_info?branch=master) interface. For instructions on how to enumerate devices, see [Enumerating System Devices](-wia-enumerating-system-devices.md).
-   Use [**IEnumWIA\_DEV\_INFO**](/windows/win32/wia_xp/nn-wia_xp-ienumwia_dev_info?branch=master) interface to obtain [**IWiaPropertyStorage**](/windows/win32/wia_xp/nn-wia_xp-iwiapropertystorage?branch=master) interface pointers for each WIA device enumerated.
-   Use [**IWiaPropertyStorage**](/windows/win32/wia_xp/nn-wia_xp-iwiapropertystorage?branch=master) interface to inspect the device information properties of each device and save the WIA\_DIP\_DEV\_ID property from the desired device.
-   Use the DeviceID property with the [**IWiaDevMgr::CreateDevice**](/windows/win32/wia_xp/nf-wia_xp-iwiadevmgr-createdevice?branch=master) method in the [**IWiaDevMgr**](/windows/win32/wia_xp/nn-wia_xp-iwiadevmgr?branch=master) or [**IWiaDevMgr2**](-wia-iwiadevmgr2.md) interface to create a WIA device object. The **IWiaDevMgr::CreateDevice** method provides the application with the pointer to the [**IWiaItem**](/windows/win32/wia_xp/nn-wia_xp-iwiaitem?branch=master) or [**IWiaItem2**](-wia-iwiaitem2.md) interface of the root item of the specified device.

For an example of how to do this in an application, see [Creating a Device](-wia-creating-a-device.md) in the tutorial section of this guide.

## Selecting a Device With the UI

After retrieving a pointer to [**IWiaDevMgr**](/windows/win32/wia_xp/nn-wia_xp-iwiadevmgr?branch=master), an application can allow a user to select a device by skipping the rest of the above steps and calling [**IWiaDevMgr::SelectDeviceDlg**](/windows/win32/wia_xp/nf-wia_xp-iwiadevmgr-selectdevicedlg?branch=master). The **IWiaDevMgr::SelectDeviceDlg** displays a dialog box in which the user can select a WIA device.

It is recommended that applications make device and image selection available through a menu item named **From scanner** on the **File** menu.

 

 



