---
Description: INetCfgBindingInterface
ms.assetid: '414e7a36-58e9-41fd-9174-7e7410072991'
title: INetCfgBindingInterface
---

# INetCfgBindingInterface

## 

The **INetCfgBindingInterface** interface provides methods that retrieve information about a binding interface.

The interface identifier (IID) for this interface is IID\_INetCfgBindingInterface.

### When to Implement

It is not necessary to implement the methods of this interface. They are implemented in *Netcfgx.dll*.

### When to Use

Use this interface to retrieve information about a binding interface.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments the reference count.<br/>           |
| **Release**<br/>        | Decrements the reference count.<br/>           |



 



| INetCfgBindingInterface method                                                    | Description                                                                                    |
|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**GetName**](inetcfgbindinginterface-getname.md)<br/>                     | Retrieves the name of a binding interface.<br/>                                          |
| [**GetUpperComponent**](inetcfgbindinginterface-getuppercomponent.md)<br/> | Retrieves the network component connected to the upper part of a binding interface.<br/> |
| [**GetLowerComponent**](inetcfgbindinginterface-getlowercomponent.md)<br/> | Retrieves the network component connected to the lower part of a binding interface.<br/> |



 

### Comments

A binding interface binds two network components together, and the components communicate through this binding interface. Binding interfaces include TDI and NDIS5.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Netcfgx.h (include Netcfgx.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20INetCfgBindingInterface%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




