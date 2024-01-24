---
description: The IWiaUIExtension interface provides methods that replace the default system user interface, provide a custom device bitmap logo, and provide a custom device icon.
ms.assetid: e3c69019-0e07-44ad-b48b-ea7e3daed2b7
title: IWiaUIExtension interface (Wiadevd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaUIExtension
api_type: 
- COM
api_location: 
- Wiadevd.h
---

# IWiaUIExtension interface

The **IWiaUIExtension** interface provides methods that replace the default system user interface, provide a custom device bitmap logo, and provide a custom device icon.

## Members

The **IWiaUIExtension** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IWiaUIExtension** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWiaUIExtension** interface has these methods.



| Method                                                                  | Description                                                                                  |
|:------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**DeviceDialog**](-wia-iwiauiextension-devicedialog.md)               | Provides a custom user interface that replaces the default system user interface.<br/> |
| [**GetDeviceBitmapLogo**](-wia-iwiauiextension-getdevicebitmaplogo.md) | Gets a custom bitmap logo for the device.<br/>                                         |
| [**GetDeviceIcon**](-wia-iwiauiextension-getdeviceicon.md)             | Gets a custom device icon.<br/>                                                        |



 

## Remarks



| IUnknown Methods                                        | Description                               |
|---------------------------------------------------------|-------------------------------------------|
| [IUnknown::QueryInterface](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) | Returns pointers to supported interfaces. |
| [IUnknown::AddRef](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref)                 | Increments reference count.               |
| [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release)               | Decrements reference count.               |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wiadevd.h</dt> </dl> |



 

 
