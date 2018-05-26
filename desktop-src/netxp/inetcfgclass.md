---
Description: INetCfgClass
ms.assetid: 45b0ba0a-3f4f-497e-955f-92428b21aafa
title: INetCfgClass
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INetCfgClass

## 

The **INetCfgClass** interface provides methods that retrieve network components from a group containing a specified type of network component.

The interface identifier (IID) for this interface is IID\_INetCfgClass.

### When to Implement

It is not necessary to implement the methods of this interface. They are implemented in *Netcfgx.dll*.

### When to Use

Use this interface to retrieve a network component of a specific type.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments reference count.<br/>               |
| **Release**<br/>        | Decrements reference count.<br/>               |



 



| INetCfgClass method                                              | Description                                                                                             |
|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**FindComponent**](inetcfgclass-findcomponent.md)<br/>   | Retrieves a network component belonging to a particular type.<br/>                                |
| [**EnumComponents**](inetcfgclass-enumcomponents.md)<br/> | Retrieves an enumeration containing a collection of network components of a particular type.<br/> |



 

### Comments

Notify objects call the [**INetCfg::QueryNetCfgClass**](inetcfg-querynetcfgclass.md) method to obtain a pointer to a **INetCfgClass** interface.

The classes of network components that notify objects can obtain are:



| Class                       | Represented by                        |
|-----------------------------|---------------------------------------|
| Network cards<br/>    | GUID\_DEVCLASS\_NET<br/>        |
| Transports<br/>       | GUID\_DEVCLASS\_NETTRANS<br/>   |
| Network services<br/> | GUID\_DEVCLASS\_NETSERVICE<br/> |
| Network clients<br/>  | GUID\_DEVCLASS\_NETCLIENT<br/>  |



 

> [!Note]  
> **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later.

 

### See Also

[**INetCfg::QueryNetCfgClass**](inetcfg-querynetcfgclass.md)


## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Netcfgx.h (include Netcfgx.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20INetCfgClass%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





