---
Description: INetCfgComponentNotifyBinding
ms.assetid: e256a777-7bfa-4a28-bdb5-44dd20fe80f5
title: INetCfgComponentNotifyBinding
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# INetCfgComponentNotifyBinding

## 

The **INetCfgComponentNotifyBinding** interface provides methods that inform a notify object about changes in binding that affect its network component. These changes relate to how the network configuration subsystem binds other network components to the notify object's network component.

The interface identifier (IID) for this interface is IID\_INetCfgComponentNotifyBinding.

### When to Implement

Implement the methods of this interface so the notify object can accept, reject, or process changes in binding that affect its network component. These changes relate to how the network configuration subsystem binds other network components to the network component that owns this notify object. This interface is optional.

### When to Use

The network configuration subsystem calls the methods of **INetCfgComponentNotifyBinding** to inform a notify object about changes to the way the subsystem binds other network components to the network component that owns this notify object.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments the reference count.<br/>           |
| **Release**<br/>        | Decrements the reference count.<br/>           |



 



| INetCfgComponentNotifyBinding method                                                    | Description                                                                                                                |
|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**QueryBindingPath**](/windows/desktop/api/netcfgn/nf-netcfgn-inetcfgcomponentnotifybinding-querybindingpath)<br/>   | Evaluates a pending change in the binding path to which the notify object's component belongs.<br/>                  |
| [**NotifyBindingPath**](/windows/desktop/api/netcfgn/nf-netcfgn-inetcfgcomponentnotifybinding-notifybindingpath)<br/> | Performs operations resulting from a change in the binding path to which the notify object's component belongs.<br/> |



 

### Headers

Defined in *Netcfgn.h*. Include *Netcfgn.h*.

### Comments

If a notify object does not need to accept, reject, or process changes to the way the network component that owns it binds to other network components, the **INetCfgComponentNotifyBinding** interface does not need to be implemented for that notify object.

E\_NOTIMPL is not a valid return type for any of the methods of **INetCfgComponentNotifyBinding**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20INetCfgComponentNotifyBinding%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




