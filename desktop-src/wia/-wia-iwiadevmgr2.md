---
description: The IWiaDevMgr2 interface is used to create and manage image acquisition devices and to register to receive device events.
ms.assetid: 0e9fb3a1-bbe3-4dba-ba8c-b79f202d5a38
title: IWiaDevMgr2 interface (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaDevMgr2
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaDevMgr2 interface

The **IWiaDevMgr2** interface is used to create and manage image acquisition devices and to register to receive device events.

## Members

The **IWiaDevMgr2** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IWiaDevMgr2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWiaDevMgr2** interface has these methods.



| Method                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                  |
|:------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateDevice**](-wia-iwiadevmgr2-createdevice.md)                                     | Creates a hierarchical tree of [**IWiaItem2**](-wia-iwiaitem2.md) objects for a WIA 2.0 device. <br/>                                                                                                                                                                                                                                                                                                 |
| [**EnumDeviceInfo**](-wia-iwiadevmgr2-enumdeviceinfo.md)                                 | Creates an enumerator of property information for each available WIA 2.0 device. <br/>                                                                                                                                                                                                                                                                                                                 |
| [**GetImageDlg**](-wia-iwiadevmgr2-getimagedlg.md)                                       | The [**IWiaDevMgr2::GetImageDlg**](-wia-iwiadevmgr2-getimagedlg.md) method displays one or more dialog boxes that enable a user to acquire an image from a WIA 2.0 device and write the image to a specified file. This method extends the functionality of [**IWiaDevMgr2::SelectDeviceDlg**](-wia-iwiadevmgr2-selectdevicedlg.md) to encapsulate image acquisition within a single API call. <br/> |
| [**RegisterEventCallbackCLSID**](-wia-iwiadevmgr2-registereventcallbackclsid.md)         | The [**IWiaDevMgr2::RegisterEventCallbackCLSID**](-wia-iwiadevmgr2-registereventcallbackclsid.md) method registers an application to receive events even if the application is not running.<br/>                                                                                                                                                                                                      |
| [**RegisterEventCallbackInterface**](-wia-iwiadevmgr2-registereventcallbackinterface.md) | Registers a running application for WIA 2.0 event notification. <br/>                                                                                                                                                                                                                                                                                                                                  |
| [**RegisterEventCallbackProgram**](-wia-iwiadevmgr2-registereventcallbackprogram.md)     | The [**IWiaDevMgr2::RegisterEventCallbackProgram**](-wia-iwiadevmgr2-registereventcallbackprogram.md) method registers an application to receive device events. It is primarily provided for backward compatibility with applications that were not written for WIA 2.0.<br/>                                                                                                                         |
| [**SelectDeviceDlg**](-wia-iwiadevmgr2-selectdevicedlg.md)                               | Displays a dialog box that enables the user to select a hardware device for image acquisition. <br/>                                                                                                                                                                                                                                                                                                   |
| [**SelectDeviceDlgID**](-wia-iwiadevmgr2-selectdevicedlgid.md)                           | Displays a dialog box that enables the user to select a hardware device for image acquisition. <br/>                                                                                                                                                                                                                                                                                                   |



 

## Remarks

The **IWiaDevMgr2** interface, like all Component Object Model (COM) interfaces, inherits the [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface methods.



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



 

 
