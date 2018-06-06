---
Description: INetCfgComponentSysPrep
ms.assetid: 803242e2-8c1a-4167-a923-ede9cf532681
title: INetCfgComponentSysPrep
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# INetCfgComponentSysPrep

The **INetCfgComponentSysPrep** interface provides methods that inform a notify object to manage parameters for a specific network adapter.

The interface identifier (IID) for this interface is IID\_INetCfgComponentSysPrep.

### When to Implement

This interface should only be implemented by system components and is not recommended for vendor components.

### When to Use

The network configuration subsystem calls the methods of **INetCfgComponentSysPrep**to inform a notify object to manage parameters for a specific network adapter.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments the reference count.<br/>           |
| **Release**<br/>        | Decrements the reference count.<br/>           |



 



| INetCfgComponentSysPrep method                                                                  | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [**SaveAdapterParameters**](/windows/desktop/api/Netcfgn/nf-netcfgn-inetcfgcomponentsysprep-saveadapterparameters)<br/>       | Saves parameters for a network adapter in the registry.<br/> |
| [**RestoreAdapterParameters**](/windows/desktop/api/Netcfgn/nf-netcfgn-inetcfgcomponentsysprep-restoreadapterparameters)<br/> | Restores parameters for a network adapter.<br/>              |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20INetCfgComponentSysPrep%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




