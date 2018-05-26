---
Description: INetCfgClassSetup
ms.assetid: 46b78781-8ff3-466b-86ee-af604071daf3
title: INetCfgClassSetup
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INetCfgClassSetup

## 

The **INetCfgClassSetup** interface provides methods that install or remove network components of a specified type.

The interface identifier (IID) for this interface is IID\_INetCfgClassSetup.

### When to Implement

It is not necessary to implement the methods of this interface. They are implemented in *Netcfgx.dll*.

### When to Use

Use this interface to either install or remove network components.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments the reference count.<br/>           |
| **Release**<br/>        | Decrements the reference count.<br/>           |



 



| INetCfgClassSetup method                                                  | Description                                                                                                            |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**SelectAndInstall**](inetcfgclasssetup-selectandinstall.md)<br/> | Displays a dialog that a user can use to select a network component of a particular class for installation.<br/> |
| [**Install**](inetcfgclasssetup-install.md)<br/>                   | Informs a class of network components to install the component specified by an identifier.<br/>                  |
| [**DeInstall**](inetcfgclasssetup-deinstall.md)<br/>               | Removes the specified network component from the registry.<br/>                                                  |



 

### Comments

If an application did not already call [**INetCfgLock::AcquireWriteLock**](inetcfglock-acquirewritelock.md) to provide a client control over network configuration, the methods of INetCfgClassSetup return NETCFG\_E\_NO\_WRITE\_LOCK.

Calls to any **INetCfgClassSetup** methods within a notify object's implementation of any of the following interface methods could return E\_FAIL:

<dl>

[**INetCfgComponentSetup**](inetcfgcomponentsetup.md)  
[**INetCfgComponentNotifyGlobal**](inetcfgcomponentnotifyglobal.md)  
[**INetCfgComponentPropertyUi**](inetcfgcomponentpropertyui.md)  
[INetCfgComponentNotifyBinding](inetcfgcomponentnotifybinding.md)  
</dl>

These **INetCfgClassSetup** methods return E\_FAIL if an implemented method of one of the interfaces in the preceding list is not also passed change flags containing one of the following values:

-   NCN\_ADD

-   NCN\_REMOVE

-   NCN\_UPDATE

Notify objects call the **QueryInterface** method of the [**INetCfgClass**](inetcfgclass.md) interface to obtain a pointer to **INetCfgClassSetup**.

### See Also

[**INetCfgClass**](inetcfgclass.md), [INetCfgComponentNotifyBinding](inetcfgcomponentnotifybinding.md), [**INetCfgComponentNotifyGlobal**](inetcfgcomponentnotifyglobal.md), [**INetCfgComponentPropertyUi**](inetcfgcomponentpropertyui.md), [**INetCfgComponentSetup**](inetcfgcomponentsetup.md), [**INetCfgLock::AcquireWriteLock**](inetcfglock-acquirewritelock.md)


## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Netcfgx.h (include Netcfgx.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20INetCfgClassSetup%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





