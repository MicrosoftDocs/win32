---
Description: INetCfgComponentBindings
ms.assetid: 78f00f08-bcfc-4f0e-a975-48e0209cd756
title: INetCfgComponentBindings
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# INetCfgComponentBindings

## 

The **INetCfgComponentBindings** interface provides methods that control and retrieve information about how the network configuration subsystem binds a network component with other network components.

The interface identifier (IID) for this interface is IID\_INetCfgComponentBindings.

### When to Implement

It is not necessary to implement the methods of this interface. They are implemented in *Netcfgx.dll*.

### When to Use

Use this interface to control binding and to retrieve binding information for a network component.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments the reference count.<br/>           |
| **Release**<br/>        | Decrements the reference count.<br/>           |



 



| INetCfgComponentBindings method                                                                  | Description                                                                                            |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**BindTo**](/windows/desktop/api/netcfgx/nf-netcfgx-inetcfgcomponentbindings-bindto)<br/>                                     | Activates all binding paths that are shared with a specific component.<br/>                      |
| [**UnbindFrom**](/windows/desktop/api/netcfgx/nf-netcfgx-inetcfgcomponentbindings-unbindfrom)<br/>                             | Inactivates all binding paths that are shared with a specific component.<br/>                    |
| [**SupportsBindingInterface**](/windows/desktop/api/netcfgx/nf-netcfgx-inetcfgcomponentbindings-supportsbindinginterface)<br/> | Verifies whether a component supports either an upper-edge or lower-edge binding interface.<br/> |
| [**IsBoundTo**](/windows/desktop/api/netcfgx/nf-netcfgx-inetcfgcomponentbindings-isboundto)<br/>                               | Verifies whether at least one binding path shared with a specific component is activated.<br/>   |
| [**IsBindableTo**](/windows/desktop/api/netcfgx/nf-netcfgx-inetcfgcomponentbindings-isbindableto)<br/>                         | Verifies whether at least one binding path shared with a specific component exists.<br/>         |
| [**EnumBindingPaths**](/windows/desktop/api/netcfgx/nf-netcfgx-inetcfgcomponentbindings-enumbindingpaths)<br/>                 | Retrieves an enumeration of a collection of the component's binding paths.<br/>                  |
| [**MoveBefore**](/windows/desktop/api/netcfgx/nf-netcfgx-inetcfgcomponentbindings-movebefore)<br/>                             | Sets the order of two binding paths so one comes before the other.<br/>                          |
| [**MoveAfter**](/windows/desktop/api/netcfgx/nf-netcfgx-inetcfgcomponentbindings-moveafter)<br/>                               | Sets the order of two binding paths so one comes after the other.<br/>                           |



 

### Comments

Notify objects call the **QueryInterface** method of the [**INetCfgComponent**](inetcfgcomponent.md)interface to obtain a pointer to **INetCfgComponentBindings**

### See Also

[**INetCfgComponent**](inetcfgcomponent.md)


## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Netcfgx.h (include Netcfgx.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20INetCfgComponentBindings%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





