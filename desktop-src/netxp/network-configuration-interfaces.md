---
Description: Network Configuration Interfaces
ms.assetid: f19cc518-a5b5-409b-9416-970ce990cb1a
title: Network Configuration Interfaces
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Network Configuration Interfaces

## 

The following sections document the interfaces that a notify object for a network component can use to control networking setup and configuration. Most of these interfaces provide access to the network configuration subsystem.

The network configuration interfaces are described in the following topics:

<dl>

[**INetCfg**](inetcfg.md)  
[**INetCfgLock**](inetcfglock.md)  
[**INetCfgClass**](inetcfgclass.md)  
[**INetCfgClassSetup**](inetcfgclasssetup.md)  
[**INetCfgBindingPath**](inetcfgbindingpath.md)  
[**INetCfgBindingInterface**](inetcfgbindinginterface.md)  
[**INetCfgComponent**](inetcfgcomponent.md)  
[**INetCfgComponentBindings**](inetcfgcomponentbindings.md)  
[**INetCfgPnpReconfigCallback**](inetcfgpnpreconfigcallback.md)  
[**IEnumNetCfgComponent**](ienumnetcfgcomponent.md)  
[**IEnumNetCfgBindingInterface**](ienumnetcfgbindinginterface.md)  
[**IEnumNetCfgBindingPath**](ienumnetcfgbindingpath.md)  
[**INetLanConnectionUiInfo**](inetlanconnectionuiinfo.md)  
</dl>

The **INetLanConnectionUiInfo** interface does not provide access to the network configuration subsystem. A notify object can use this interface to retrieve the context in which to display properties for the network component that owns the object.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20Network%20Configuration%20Interfaces%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



