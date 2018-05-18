---
Description: INetCfgLock
ms.assetid: '659bc92c-ed56-41e8-9a24-3bb11fc7c018'
title: INetCfgLock
---

# INetCfgLock

## 

The **INetCfgLock** interface provides methods that are used to obtain a lock on network configuration so a client can safely configure network components and binding paths.

The interface identifier (IID) for this interface is IID\_INetCfgLock.

### When to Implement

It is not necessary to implement the methods of this interface. They are implemented in *Netcfgx.dll*.

### When to Use

Use this interface to obtain an operating system-wide lock on network configuration.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments the reference count.<br/>           |
| **Release**<br/>        | Decrements the reference count.<br/>           |



 



| INetCfgLock method                                                  | Description                                                                                |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**AcquireWriteLock**](inetcfglock-acquirewritelock.md)<br/> | Requests a lock on network configuration for a particular client.<br/>               |
| [**ReleaseWriteLock**](inetcfglock-releasewritelock.md)<br/> | Releases a previously obtained lock on network configuration.<br/>                   |
| [**IsWriteLocked**](inetcfglock-iswritelocked.md)<br/>       | Indicates the name of the client that currently controls network configuration.<br/> |



 

### Comments

There can only be one write lock per operating system.

Applications call the **QueryInterface** method of the [**INetCfg**](inetcfg.md)interface to obtain a pointer to **INetCfgLock**.

### See Also

[**INetCfg**](inetcfg.md)


## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Netcfgx.h (include Netcfgx.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20INetCfgLock%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





