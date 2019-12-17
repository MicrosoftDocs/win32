---
Description: The IWiaUIExtension2 interface provides methods that replace the default, system-supplied user interface with a custom user interface, and that provide a custom device icon.
ms.assetid: 1a747ea3-2476-438b-baf0-903b86cbbb16
title: IWiaUIExtension2 interface (Wiadevd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaUIExtension2
api_type: 
- COM
api_location: 
- Wiadevd.h
---

# IWiaUIExtension2 interface

The IWiaUIExtension2 interface provides methods that replace the default, system-supplied user interface with a custom user interface, and that provide a custom device icon. Device vendors can implement this interface to provide custom user interfaces for their devices.

## Members

The **IWiaUIExtension2** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/ms680509(v=VS.85).aspx) interface. **IWiaUIExtension2** also has these types of members:

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
| [IUnknown::QueryInterface](https://msdn.microsoft.com/library/ms682521(v=VS.85).aspx) | Returns pointers to supported interfaces. |
| [IUnknown::AddRef](https://msdn.microsoft.com/library/ms691379(v=VS.85).aspx)                 | Increments reference count.               |
| [IUnknown::Release](https://msdn.microsoft.com/library/ms682317(v=VS.85).aspx)               | Decrements reference count.               |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wiadevd.h</dt> </dl> |



 

 




