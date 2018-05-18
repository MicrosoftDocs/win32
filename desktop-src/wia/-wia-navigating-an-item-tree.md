---
Description: 'An application navigates a Windows Image Acquisition (WIA) device''s item tree to find and select images on that device. Using this technique, an application selects and acquires an image without presenting a dialog box to the user.'
ms.assetid: '1f124b4a-45fb-4181-b45a-e810a61ac37d'
title: Navigating an Item Tree
---

# Navigating an Item Tree

An application navigates a Windows Image Acquisition (WIA) device's item tree to find and select images on that device. Using this technique, an application selects and acquires an image without presenting a dialog box to the user.

A WIA device is represented as the root item in a tree of [**IWiaItem**](-wia-iwiaitem.md) or [**IWiaItem2**](-wia-iwiaitem2.md) objects. The child items in the tree represent images for a camera or scan beds for a scanner.

After a WIA device is selected, an application calls the [**IWiaItem::EnumChildItems**](-wia-iwiaitem-enumchilditems.md) method of the [**IWiaItem**](-wia-iwiaitem.md) or [**IWiaItem2**](-wia-iwiaitem2.md) interface of the device to enumerate the child items (the images or scan beds) of the device. For instructions, see [Selecting a Device](-wia-selecting-a-device.md).

The [**IWiaItem::EnumChildItems**](-wia-iwiaitem-enumchilditems.md) method creates an enumeration object for the child items of the device, and returns a pointer to that object's [**IEnumWiaItem**](-wia-ienumwiaitem.md) interface. The application can then use the methods of the **IEnumWiaItem** interface to obtain pointers to the items in the device's item tree.

 

 



