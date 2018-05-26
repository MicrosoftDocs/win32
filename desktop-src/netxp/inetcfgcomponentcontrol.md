---
Description: INetCfgComponentControl
ms.assetid: a656a146-7353-4471-850c-e5ba605d0892
title: INetCfgComponentControl
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INetCfgComponentControl

## 

The **INetCfgComponentControl** interface is a required interface which provides methods that are called by the network configuration subsystem to initialize the notify object of the network component and to apply changes to the component.

The interface identifier (IID) for this interface is IID\_INetCfgComponentControl.

### When to Implement

The methods of this interface must be implemented so the network configuration subsystem can initialize the notify object of the network component and can apply changes to the component. This interface is required.

### When to Use

The network configuration subsystem calls the methods of **INetCfgComponentControl** to initialize the notify object of the network component and to apply changes to the component.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments the reference count.<br/>           |
| **Release**<br/>        | Decrements the reference count.<br/>           |



 



| INetCfgComponentControl method                                                          | Description                                                                                                 |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**Initialize**](inetcfgcomponentcontrol-initialize.md)<br/>                     | Initializes the network component's notify object.<br/>                                               |
| [**ApplyRegistryChanges**](inetcfgcomponentcontrol-applyregistrychanges.md)<br/> | Applies to the registry changes made to the network component's configuration.<br/>                   |
| [**ApplyPnpChanges**](inetcfgcomponentcontrol-applypnpchanges.md)<br/>           | Informs the notify object of the network component that it can configure its component's driver.<br/> |
| [**CancelChanges**](inetcfgcomponentcontrol-cancelchanges.md)<br/>               | Disregards proposed changes for the network component's configuration.<br/>                           |



 

### Comments

E\_NOTIMPL is not a valid return type for any of the **INetCfgComponentControl** interface's methods.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Netcfgn.h (include Netcfgn.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20INetCfgComponentControl%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




