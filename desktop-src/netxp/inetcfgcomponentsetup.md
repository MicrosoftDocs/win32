---
Description: INetCfgComponentSetup
ms.assetid: 'e561759a-876a-4eb0-befb-2864e6426740'
title: INetCfgComponentSetup
---

# INetCfgComponentSetup

## 

The **INetCfgComponentSetup** interface, an optional interface, provides methods that inform the notify object of the network component that the network configuration subsystem must install or remove the component.

The interface identifier (IID) for this interface is IID\_INetCfgComponentSetup.

### When to Implement

Implement the methods of this interface to perform operations required to install, upgrade, and remove a network component. This interface is optional.

### When to Use

The network configuration subsystem calls the methods of **INetCfgComponentSetup** to install and remove a network component.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments the reference count.<br/>           |
| **Release**<br/>        | Decrements the reference count.<br/>           |



 



| INetCfgComponentSetup method                                              | Description                                                                                           |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**Install**](inetcfgcomponentsetup-install.md)<br/>               | Performs operations required to install the network component that owns the notify object.<br/> |
| [**Upgrade**](inetcfgcomponentsetup-upgrade.md)<br/>               | Modifies the network component, if required, when the operating system upgrades.<br/>           |
| [**ReadAnswerFile**](inetcfgcomponentsetup-readanswerfile.md)<br/> | Retrieves parameters from a file to configure the network component.<br/>                       |
| [**Removing**](inetcfgcomponentsetup-removing.md)<br/>             | Performs operations required to remove the network component that owns the notify object.<br/>  |



 

### Comments

A network component can use the **INetCfgComponentSetup** interface to examine a file for unattended setup and determine what section contains the component's parameters.

E\_NOTIMPL is not a valid return type for any of this interface's methods.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Netcfgn.h (include Netcfgn.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20INetCfgComponentSetup%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




