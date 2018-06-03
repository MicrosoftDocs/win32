---
Description: The IWiaUIExtension interface provides methods that replace the default system user interface, provide a custom device bitmap logo, and provide a custom device icon.
ms.assetid: e3c69019-0e07-44ad-b48b-ea7e3daed2b7
title: IWiaUIExtension interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IWiaUIExtension interface

The **IWiaUIExtension** interface provides methods that replace the default system user interface, provide a custom device bitmap logo, and provide a custom device icon.

## Members

The **IWiaUIExtension** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/windows/desktop/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IWiaUIExtension** also has these types of members:

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
| [IUnknown::QueryInterface](https://msdn.microsoft.com/windows/desktop/54d5ff80-18db-43f2-b636-f93ac053146d) | Returns pointers to supported interfaces. |
| [IUnknown::AddRef](https://msdn.microsoft.com/windows/desktop/b4316efd-73d4-4995-b898-8025a316ba63)                 | Increments reference count.               |
| [IUnknown::Release](https://msdn.microsoft.com/windows/desktop/4b494c6f-f0ee-4c35-ae45-ed956f40dc7a)               | Decrements reference count.               |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wiadevd.h</dt> </dl> |



 

 




