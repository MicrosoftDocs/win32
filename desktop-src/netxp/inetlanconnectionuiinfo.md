---
Description: INetLanConnectionUiInfo
ms.assetid: '59a2bdf9-297b-444a-b88d-924ca05b3deb'
title: INetLanConnectionUiInfo
---

# INetLanConnectionUiInfo

## 

The **INetLanConnectionUiInfo** interface provides a method that retrieves the context in which to display properties for the network component that owns a notify object.

The interface identifier (IID) for this interface is IID\_INetLanConnectionUiInfo.

### When to Implement

It is not necessary to implement the method of this interface. It is implemented in *Netcfgx.dll*.

### When to Use

The network configuration subsystem can supply **INetLanConnectionUiInfo** to a notify object when the subsystem calls the object's [**INetCfgComponentPropertyUi::SetContext**](inetcfgcomponentpropertyui-setcontext.md) method. The network configuration subsystem supplies **INetLanConnectionUiInfo** as a pointer to an **IUnknown** interface. The notify object can call the **QueryInterface** method to determine if the supplied **IUnknown** supports **INetLanConnectionUiInfo**. **SetContext**can use the method of **INetLanConnectionUiInfo** to retrieve the context in which to display properties for the network component that owns the notify object.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments reference count.<br/>               |
| **Release**<br/>        | Decrements reference count.<br/>               |



 



| INetLanConnectionUiInfo method                                            | Description                                                  |
|---------------------------------------------------------------------------|--------------------------------------------------------------|
| [**GetDeviceGuid**](inetlanconnectionuiinfo-getdeviceguid.md)<br/> | Retrieves a pointer to the GUID for a LAN device.<br/> |



 

### See Also

[**INetCfgComponentPropertyUi::SetContext**](inetcfgcomponentpropertyui-setcontext.md)


## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Netcfgn.h (include Netcfgn.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20INetLanConnectionUiInfo%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





