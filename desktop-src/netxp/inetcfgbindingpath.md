---
Description: INetCfgBindingPath
ms.assetid: c7dc6589-7934-4a2c-b4f2-6be873b400cb
title: INetCfgBindingPath
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INetCfgBindingPath

## 

The **INetCfgBindingPath** interface provides methods that control and retrieve information about a binding path.

The interface identifier (IID) for this interface is IID\_INetCfgBindingPath.

### When to Implement

It is not necessary to implement the methods of this interface. They are implemented in *Netcfgx.dll*.

### When to Use

Use this interface to control and retrieve information about a binding path.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments the reference count.<br/>           |
| **Release**<br/>        | Decrements the reference count.<br/>           |



 



| INetCfgBindingPath method                                                            | Description                                                                                            |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**IsSamePathAs**](inetcfgbindingpath-issamepathas.md)<br/>                   | Verifies if the specified binding path is the same as this binding path.<br/>                    |
| [**IsSubPathOf**](inetcfgbindingpath-issubpathof.md)<br/>                     | Verifies if this binding path is a subpath of the specified binding path.<br/>                   |
| [**IsEnabled**](inetcfgbindingpath-isenabled.md)<br/>                         | Retrieves the current state of a binding path.<br/>                                              |
| [**Enable**](inetcfgbindingpath-enable.md)<br/>                               | Sets the state of a binding path to enabled or disabled.<br/>                                    |
| [**GetPathToken**](inetcfgbindingpath-getpathtoken.md)<br/>                   | Retrieves the identifier of a binding path that is unique across operating system reboots.<br/>  |
| [**GetOwner**](inetcfgbindingpath-getowner.md)<br/>                           | Retrieves the network component that owns a binding path.<br/>                                   |
| [**GetDepth**](inetcfgbindingpath-getdepth.md)<br/>                           | Retrieves the number of network components contained in a binding path.<br/>                     |
| [**EnumBindingInterfaces**](inetcfgbindingpath-enumbindinginterfaces.md)<br/> | Retrieves an enumeration of a collection of binding interfaces contained in a binding path.<br/> |



 

### Comments

A binding path consists of a string of network components that are connected together by binding interfaces. The component at the top of the binding path owns the path.

Starting with Windows 10, there is a change in how a binding path is reported as enabled or disabled. Prior to Windows 10, for a binding path such as C → B → A, disabling B → A by calling [**INetCfgBindingPath::Enable(FALSE)**](inetcfgbindingpath-enable.md) would not report C → B → A as disabled by **INetCfgBindingPath::Enable**. To have it reported as disabled, you must also call [**INetCfg::Apply**](inetcfg-apply.md). Starting with Windows 10, you call **INetCfgBindingPath::Enable(FALSE)** to disable B → A, which results in C → B → A being reported as disabled.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Netcfgx.h (include Netcfgx.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20INetCfgBindingPath%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




