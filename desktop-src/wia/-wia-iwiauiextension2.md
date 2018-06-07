---
Description: The IWiaUIExtension2 interface provides methods that replace the default, system-supplied user interface with a custom user interface, and that provide a custom device icon.
ms.assetid: 1a747ea3-2476-438b-baf0-903b86cbbb16
title: IWiaUIExtension2 interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IWiaUIExtension2 interface

The IWiaUIExtension2 interface provides methods that replace the default, system-supplied user interface with a custom user interface, and that provide a custom device icon. Device vendors can implement this interface to provide custom user interfaces for their devices.

## Members

The **IWiaUIExtension2** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IWiaUIExtension2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWiaUIExtension2** interface has these methods.



| Method                                                       | Description                                                                                  |
|:-------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**DeviceDialog**](-wia-iwiauiextension2-devicedialog.md)   | Provides a custom user interface that replaces the default system user interface.<br/> |
| [**GetDeviceIcon**](-wia-iwiauiextension2-getdeviceicon.md) | Gets a custom device icon.<br/>                                                        |



 

## Remarks



| IUnknown Methods                                        | Description                               |
|---------------------------------------------------------|-------------------------------------------|
| [IUnknown::QueryInterface](https://msdn.microsoft.com/54d5ff80-18db-43f2-b636-f93ac053146d) | Returns pointers to supported interfaces. |
| [IUnknown::AddRef](https://msdn.microsoft.com/b4316efd-73d4-4995-b898-8025a316ba63)                 | Increments reference count.               |
| [IUnknown::Release](https://msdn.microsoft.com/4b494c6f-f0ee-4c35-ae45-ed956f40dc7a)               | Decrements reference count.               |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wiadevd.h</dt> </dl> |



 

 




