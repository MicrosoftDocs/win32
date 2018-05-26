---
Description: IEnumNetCfgBindingPath
ms.assetid: 8f918136-9649-4009-acc1-ffd9b95acad8
title: IEnumNetCfgBindingPath
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IEnumNetCfgBindingPath

## 

The [**INetCfgBindingPath**](inetcfgbindingpath.md) interface provides methods that enumerate the **INetCfgBindingPath**interfaces for binding paths that contain a particular network component.

The interface identifier (IID) for this interface is IID\_IEnumNetCfgBindingPath.

### When to Implement

It is not necessary to implement the methods of this interface. They are implemented in *Netcfgx.dll*.

### When to Use

Use this interface to retrieve the [**INetCfgBindingPath**](inetcfgbindingpath.md) interfaces for binding paths that contain a particular network component.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments reference count.<br/>               |
| **Release**<br/>        | Decrements reference count.<br/>               |



 



| IEnumNetCfgBindingPath method                            | Description                                                                           |
|----------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**Next**](ienumnetcfgbindingpath-next.md)<br/>   | Retrieves the next specified number of items in the enumeration sequence.<br/>  |
| [**Skip**](ienumnetcfgbindingpath-skip.md)<br/>   | Skips over the next specified number of items in the enumeration sequence.<br/> |
| [**Reset**](ienumnetcfgbindingpath-reset.md)<br/> | Resets the enumeration sequence to the beginning item.<br/>                     |
| [**Clone**](ienumnetcfgbindingpath-clone.md)<br/> | The **Clone**method is not implemented. Do not use it in your driver.<br/>      |



 

### Comments

The [**INetCfgBindingPath**](inetcfgbindingpath.md)interface is a standard COM enumerator. To locate more information about COM enumerators and their methods, see the IEnum*XXXX* topic in the Microsoft Windows SDK.

To obtain a pointer to [**INetCfgBindingPath**](inetcfgbindingpath.md), notify objects call the [**INetCfgComponentBindings::EnumBindingPaths**](inetcfgcomponentbindings-enumbindingpaths.md)method.

### See Also

[**INetCfgBindingPath**](inetcfgbindingpath.md), [**INetCfgComponentBindings::EnumBindingPaths**](inetcfgcomponentbindings-enumbindingpaths.md)


## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Netcfgx.h (include Netcfgx.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20IEnumNetCfgBindingPath%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





