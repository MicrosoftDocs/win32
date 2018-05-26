---
Description: INetCfgPnpReconfigCallback
ms.assetid: c6a7faf0-6213-40da-baa1-88419cb69f56
title: INetCfgPnpReconfigCallback
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INetCfgPnpReconfigCallback

## 

The **INetCfgPnpReconfigCallback** interface provides a method that sends configuration information to the driver of the network component that owns a notify object.

The interface identifier (IID) for this interface is IID\_INetCfgPnpReconfigCallback.

### When to Implement

It is not necessary to implement the method of this interface. It is implemented in *Netcfgx.dll*.

### When to Use

The network configuration subsystem supplies **INetCfgPnpReconfigCallback** to a notify object when the subsystem calls the object's [**INetCfgComponentControl::ApplyPnpChanges**](inetcfgcomponentcontrol-applypnpchanges.md) method. **ApplyPnpChanges**can use the method of **INetCfgPnpReconfigCallback** to send configuration information to the driver of the network component that owns the object. A notify object is not required to use **INetCfgPnpReconfigCallback**.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments the reference count.<br/>           |
| **Release**<br/>        | Decrements the reference count.<br/>           |



 



| INetCfgPnpReconfigCallback method                                                | Description                                                                                                  |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**SendPnpReconfig**](inetcfgpnpreconfigcallback-sendpnpreconfig.md)<br/> | Sends configuration information to the driver of the network component that owns a notify object.<br/> |



 

### Comments

The network configuration subsystem calls **ApplyPnpChanges**after calling the [**INetCfgComponentControl::ApplyRegistryChanges**](inetcfgcomponentcontrol-applyregistrychanges.md)method and after drivers and services for a network component have started. The component's notify object can use the **INetCfgPnpReconfigCallback** interface that **ApplyPnpChanges**provides to send configuration information to the component's driver. This driver must be either a TDI provider or an NDIS miniport driver. Using **INetCfgPnpReconfigCallback** is optional, but recommended to avoid requiring a user to reboot the operating system to implement changes to the configuration.

### See Also

[**INetCfgComponentControl::ApplyPnpChanges**](inetcfgcomponentcontrol-applypnpchanges.md), [**INetCfgComponentControl::ApplyRegistryChanges**](inetcfgcomponentcontrol-applyregistrychanges.md)


## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Netcfgn.h (include Netcfgn.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20INetCfgPnpReconfigCallback%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





