---
description: The IWiaItem2 interface provides applications with the same functionality as the IWiaItem interface (the ability to query devices to discover their capabilities, to access data transfer interfaces and item properties, and to control the device).
ms.assetid: 4e29ea54-1ee7-4150-b26c-f8c7f41a3f08
title: IWiaItem2 interface (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaItem2
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaItem2 interface

The **IWiaItem2** interface provides applications with the same functionality as the [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) interface (the ability to query devices to discover their capabilities, to access data transfer interfaces and item properties, and to control the device). It also provides application with the ability to dynamically create and use image processing filters that can come as extensions of the Windows Image Acquisition (WIA) 2.0 device drivers provided in Windows Vista.

## Members

The **IWiaItem2** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IWiaItem2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWiaItem2** interface has these methods.



| Method                                                                  | Description                                                                                                                                                                                                  |
|:------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CheckExtension**](-wia-iwiaitem2-checkextension.md)                 | Checks whether a specified extension is available on the machine and can be used by the [**IWiaItem2::GetExtension**](-wia-iwiaitem2-getextension.md) method. <br/>                                   |
| [**CreateChildItem**](-wia-iwiaitem2-createchilditem.md)               | Create a new child item. Adds **IWiaItem2** objects to a device's **IWiaItem2** tree. <br/>                                                                                                            |
| [**DeleteItem**](-wia-iwiaitem2-deleteitem.md)                         | Removes the current **IWiaItem2** object from the device's object tree. <br/>                                                                                                                          |
| [**DeviceCommand**](-wia-iwiaitem2-devicecommand.md)                   | Issues a command to a WIA 2.0 hardware device. <br/>                                                                                                                                                   |
| [**DeviceDlg**](-wia-iwiaitem2-devicedlg.md)                           | Displays a dialog box to the user to prepare for image acquisition. <br/>                                                                                                                              |
| [**Diagnostic**](-wia-iwiaitem2-diagnostic.md)                         | Not currently supported.<br/>                                                                                                                                                                          |
| [**EnumChildItems**](-wia-iwiaitem2-enumchilditems.md)                 | Creates an enumerator object and passes back a pointer to its [**IEnumWiaItem2**](-wia-ienumwiaitem2.md) interface for folders with items in the **IWiaItem2** tree of a WIA 2.0 device. <br/>        |
| [**EnumDeviceCapabilities**](-wia-iwiaitem2-enumdevicecapabilities.md) | Creates an enumerator that is used to ascertain the commands and events a WIA 2.0 device supports. <br/>                                                                                               |
| [**EnumRegisterEventInfo**](-wia-iwiaitem2-enumregistereventinfo.md)   | The [**IWiaItem2::EnumRegisterEventInfo**](-wia-iwiaitem2-enumregistereventinfo.md) method creates an enumerator used to obtain information about events for which an application is registered.<br/> |
| [**FindItemByName**](-wia-iwiaitem2-finditembyname.md)                 | Searches an item's tree of subitems using the name as the search key. <br/>                                                                                                                            |
| [**GetExtension**](-wia-iwiaitem2-getextension.md)                     | Gets the extension interfaces that might come with a WIA 2.0 device driver. <br/>                                                                                                                      |
| [**GetItemCategory**](-wia-iwiaitem2-getitemcategory.md)               | Gets an item's category information. <br/>                                                                                                                                                             |
| [**GetItemType**](-wia-iwiaitem2-getitemtype.md)                       | Gets an item's type information. <br/>                                                                                                                                                                 |
| [**GetParentItem**](-wia-iwiaitem2-getparentitem.md)                   | Gets the parent item in the tree that represents a WIA 2.0 hardware device. <br/>                                                                                                                      |
| [**GetPreviewComponent**](-wia-iwiaitem2-getpreviewcomponent.md)       | Gets the WIA 2.0 preview component.<br/>                                                                                                                                                               |
| [**GetRootItem**](-wia-iwiaitem2-getrootitem.md)                       | Gets the root item of a tree of item objects used to represent a WIA 2.0 hardware device. <br/>                                                                                                        |



 

## Remarks

The WIA 2.0 item tree that an application can see is separate from the tree that is created and maintained by a WIA 2.0 minidriver. When a minidriver creates a tree of items, the WIA 2.0 Service uses this WIA 2.0 item tree as a guide to create identical copies that can be viewed by imaging applications. Items in the copied tree are called application items. Items in the tree created by a minidriver are called driver items. In Windows Vista the WIA 2.0 item trees are built of **IWiaItem2** objects, each one of which implements the **IWiaItem2** interface).

The **IWiaItem2** interface, like all Component Object Model (COM) interfaces, inherits the [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface methods.



| IUnknown Methods                                        | Description                               |
|---------------------------------------------------------|-------------------------------------------|
| [IUnknown::QueryInterface](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) | Returns pointers to supported interfaces. |
| [IUnknown::AddRef](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref)                 | Increments reference count.               |
| [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release)               | Decrements reference count.               |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 
