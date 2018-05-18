---
Description: 'The IWiaUIExtension2 interface provides methods that replace the default, system-supplied user interface with a custom user interface, and that provide a custom device icon.'
ms.assetid: '1a747ea3-2476-438b-baf0-903b86cbbb16'
title: IWiaUIExtension2 interface
---

# IWiaUIExtension2 interface

The IWiaUIExtension2 interface provides methods that replace the default, system-supplied user interface with a custom user interface, and that provide a custom device icon. Device vendors can implement this interface to provide custom user interfaces for their devices.

## Members

The **IWiaUIExtension2** interface inherits from the [**IUnknown**](com.iunknown) interface. **IWiaUIExtension2** also has these types of members:

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
| [IUnknown::QueryInterface](com.iunknown_queryinterface) | Returns pointers to supported interfaces. |
| [IUnknown::AddRef](com.iunknown_addref)                 | Increments reference count.               |
| [IUnknown::Release](com.iunknown_release)               | Decrements reference count.               |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wiadevd.h</dt> </dl> |



 

 




