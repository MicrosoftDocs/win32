---
Description: IEnumNetCfgComponent
ms.assetid: fb890d4f-a635-45eb-9534-3a542eb27868
title: IEnumNetCfgComponent
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IEnumNetCfgComponent

## 

The **IEnumNetCfgComponent** interface provides methods that enumerate the [**INetCfgComponent**](inetcfgcomponent.md)interfaces for network components of a particular type installed on the operating system. Types of network components include network cards, protocols, services, and clients.

The interface identifier (IID) for this interface is IID\_IEnumNetCfgComponent.

### When to Implement

It is not necessary to implement the methods of this interface. They are implemented in *Netcfgx.dll*.

### When to Use

Use this interface to retrieve the INetCfgComponent interfaces for network components of a particular type.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments the reference count.<br/>           |
| **Release**<br/>        | Decrements the reference count.<br/>           |



 



| IEnumNetCfgComponent method                            | Description                                                                           |
|--------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**Next**](/windows/desktop/api/netcfgx/nf-netcfgx-ienumnetcfgcomponent-next)<br/>   | Retrieves the next specified number of items in the enumeration sequence.<br/>  |
| [**Skip**](/windows/desktop/api/netcfgx/nf-netcfgx-ienumnetcfgcomponent-skip)<br/>   | Skips over the next specified number of items in the enumeration sequence.<br/> |
| [**Reset**](/windows/desktop/api/Netcfgx/nf-netcfgx-ienumnetcfgcomponent-reset)<br/> | Resets the enumeration sequence to the beginning item.<br/>                     |
| [**Clone**](/windows/desktop/api/Netcfgx/nf-netcfgx-ienumnetcfgcomponent-clone)<br/> | The **Clone**method is not implemented. Do not use it in your driver.<br/>      |



 

### Comments

The **IEnumNetCfgComponent**interface is a standard COM enumerator. To locate more information about COM enumerators and their methods, see the IEnum*XXXX* topic in the Microsoft Windows SDK.

Notify objects call the [**INetCfgClass::EnumComponents**](/windows/desktop/api/netcfgx/nf-netcfgx-inetcfgclass-enumcomponents)method to obtain a pointer to **IEnumNetCfgComponent**.

### See Also

[**INetCfgClass::EnumComponents**](/windows/desktop/api/netcfgx/nf-netcfgx-inetcfgclass-enumcomponents), [**INetCfgComponent**](inetcfgcomponent.md)


## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Netcfgx.h (include Netcfgx.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20IEnumNetCfgComponent%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





