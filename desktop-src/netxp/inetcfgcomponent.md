---
Description: INetCfgComponent
ms.assetid: f3233a14-74e9-4c51-8883-7ca526752f96
title: INetCfgComponent
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INetCfgComponent

## 

The **INetCfgComponent** interface provides methods that control and retrieve information about a network component.

The interface identifier (IID) for this interface is IID\_INetCfgComponent.

### When to Implement

It is not necessary to implement the methods of this interface. They are implemented in *Netcfgx.dll*.

### When to Use

Use this interface to control and retrieve information about a network component.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments the reference count.<br/>           |
| **Release**<br/>        | Decrements the reference count.<br/>           |



 



| INetCfgComponent method                                                      | Description                                                                                            |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**GetDisplayName**](inetcfgcomponent-getdisplayname.md)<br/>         | Retrieves the name of a component that displays in a network connection's property sheet.<br/>   |
| [**SetDisplayName**](inetcfgcomponent-setdisplayname.md)<br/>         | Sets the name of a component that displays in a network connection's property sheet.<br/>        |
| [**GetHelpText**](inetcfgcomponent-gethelptext.md)<br/>               | Retrieves a component's description that displays in a network connection's property sheet.<br/> |
| [**GetId**](inetcfgcomponent-getid.md)<br/>                           | Retrieves a component's identifier.<br/>                                                         |
| [**GetCharacteristics**](inetcfgcomponent-getcharacteristics.md)<br/> | Retrieves a component's characteristics.<br/>                                                    |
| [**GetInstanceGuid**](inetcfgcomponent-getinstanceguid.md)<br/>       | Retrieves a component's instance GUID.<br/>                                                      |
| [**GetPnpDevNodeId**](inetcfgcomponent-getpnpdevnodeid.md)<br/>       | Retrieves the identifier of a component's Plug and Play device node.<br/>                        |
| [**GetClassGuid**](inetcfgcomponent-getclassguid.md)<br/>             | Retrieves the class GUID for a component's type.<br/>                                            |
| [**GetBindName**](inetcfgcomponent-getbindname.md)<br/>               | Retrieves a component's description for binding operations.<br/>                                 |
| [**GetDeviceStatus**](inetcfgcomponent-getdevicestatus.md)<br/>       | Retrieves the status of a network card.<br/>                                                     |
| [**OpenParamKey**](inetcfgcomponent-openparamkey.md)<br/>             | Opens and retrieves the registry key that contains parameters for a network component.<br/>      |
| [**RaisePropertyUi**](inetcfgcomponent-raisepropertyui.md)<br/>       | Displays a component's property sheet so users can modify the component's properties.<br/>       |



 

### Comments

When notify objects initialize, they receive a pointer to INetCfgComponent. Notify objects use this pointer to access and configure the network components that own them.

A notify object can call the **QueryInterface** method of **INetCfgComponent** to obtain a pointer to the [**INetCfgComponentBindings**](inetcfgcomponentbindings.md)interface for the network component. The notify object can use this interface to control binding and to retrieve binding information for the network component.

A notify object can call the following methods to retrieve binding paths to which the network component belongs:

-   [**INetCfgComponentBindings::EnumBindingPaths**](inetcfgcomponentbindings-enumbindingpaths.md)

-   Methods of the [**IEnumNetCfgBindingPath**](ienumnetcfgbindingpath.md) interface that enumerate the [**INetCfgBindingPath**](inetcfgbindingpath.md) interfaces

### See Also

[**IEnumNetCfgBindingPath**](ienumnetcfgbindingpath.md), [**INetCfgBindingPath**](inetcfgbindingpath.md), [**INetCfgComponentBindings**](inetcfgcomponentbindings.md)


## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Netcfgx.h (include Netcfgx.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20INetCfgComponent%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





