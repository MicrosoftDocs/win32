---
Description: INetCfgComponentPropertyUi
ms.assetid: 882e68d7-c736-4c0f-a41e-2d4ecc408e55
title: INetCfgComponentPropertyUi
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INetCfgComponentPropertyUi

## 

The **INetCfgComponentPropertyUi** interface provides methods that inform a notify object of a user's request to display the properties of the network component that owns the object. These methods also inform the notify object that the network configuration subsystem must apply changes to the component's properties.

The interface identifier (IID) for this interface is IID\_INetCfgComponentPropertyUi.

### When to Implement

Implement the methods of this interface to display custom property pages for the network component that owns this notify object. This interface is optional.

### When to Use

The network configuration subsystem calls the **INetCfgComponentPropertyUi** methods to inform a notify object of a user's request to display the properties of the network component that owns the object, and whether the network configuration subsystem must apply changes to the component's properties.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments the reference count.<br/>           |
| **Release**<br/>        | Decrements the reference count.<br/>           |



 



| INetCfgComponentPropertyUi method                                                      | Description                                                                                                                                    |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**QueryPropertyUi**](inetcfgcomponentpropertyui-querypropertyui.md)<br/>       | Determines if the given context is appropriate for displaying properties for the component that owns the notify object.<br/>             |
| [**SetContext**](inetcfgcomponentpropertyui-setcontext.md)<br/>                 | Directs the component's notify object to display the component's properties in the context of a particular binding path or adapter.<br/> |
| [**MergePropPages**](inetcfgcomponentpropertyui-mergeproppages.md)<br/>         | Creates custom property pages and merges them into the component's default set.<br/>                                                     |
| [**ValidateProperties**](inetcfgcomponentpropertyui-validateproperties.md)<br/> | Checks proposed changes for the component's properties.<br/>                                                                             |
| [**ApplyProperties**](inetcfgcomponentpropertyui-applyproperties.md)<br/>       | Stores, in memory, proposed changes for the component's properties.<br/>                                                                 |
| [**CancelProperties**](inetcfgcomponentpropertyui-cancelproperties.md)<br/>     | Disregards proposed changes for the component's properties.<br/>                                                                         |



 

### Comments

If a network component does not supply custom property pages that users can use to modify the component's properties, the **INetCfgComponentPropertyUi** interface does not need to be implemented for the component's notify object.

E\_NOTIMPL is not a valid return type for any of the methods of **INetCfgComponentPropertyUi**.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Netcfgn.h (include Netcfgn.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20INetCfgComponentPropertyUi%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




