---
Description: Notify Object Interfaces
ms.assetid: 'b7ae68d8-6a71-40d3-beed-25c0637bb738'
title: Notify Object Interfaces
---

# Notify Object Interfaces

## 

A *notify object* for a network component implements the following interfaces to control networking setup and configuration, and to create custom property pages used for modifying a component's properties:

<dl>

[**INetCfgComponentControl**](inetcfgcomponentcontrol.md) initializes a component's notify object. (Required)  
[**INetCfgComponentSetup**](inetcfgcomponentsetup.md) performs operations for installing and removing a component. (Optional)  
[**INetCfgComponentPropertyUi**](inetcfgcomponentpropertyui.md) displays custom property pages for a component. (Optional)  
[INetCfgComponentNotifyBinding](inetcfgcomponentnotifybinding.md) evaluates changes to how the network configuration subsystem binds a component to other network components. (Optional)  
[**INetCfgComponentNotifyGlobal**](inetcfgcomponentnotifyglobal.md) evaluates changes to network configuration that might affect a component. (Optional)  
[**INetCfgComponentSysPrep**](inetcfgcomponentsysprep.md) should only be implemented by system components and is not recommended for vendor components.  
[**INetCfgComponentUpperEdge**](inetcfgcomponentupperedge.md) should only be implemented by system components and is not recommended for vendor components.  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20Notify%20Object%20Interfaces%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



