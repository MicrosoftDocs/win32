---
Description: IProvisioningProfileWireless
ms.assetid: 54901ff0-4293-4bee-a6eb-df112529c20a
title: IProvisioningProfileWireless
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IProvisioningProfileWireless

> [!Note]  
> Wireless Provisioning Services (WPS) is no longer available as of Windows Vista.

 

The **IProvisioningProfileWireless** interface is used to add a wireless profile to the preferred profile list managed by the Wireless Zero Configuration service.

> [!Note]  
> This method should only be used for private networks that do not provide a subscription service.

 

### Methods

The following methods are listed in vtable order:



| IUnknown method               | Description                                         |
|-------------------------------|-----------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces<br/> |
| **AddRef**<br/>         | Increments the reference count<br/>           |
| **Release**<br/>        | Decrements the reference count<br/>           |



 



| IProvisioningProfileWireless method                                            | Description                                                                                                                 |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| [**CreateProfile**](/windows/desktop/api/netprov/nf-netprov-iprovisioningprofilewireless-createprofile)<br/> | Enables the dynamic configuration of a new profile in the preferred profile list using XML-formatted information<br/> |



 

### Comments

The **IProvisioningProfileWireless** interface supports the [preferred profile provisioning](https://www.bing.com/search?q=preferred+profile+provisioning)method.

The XML data used in this interface is based on the [WirelessProfile schema](https://www.bing.com/search?q=WirelessProfile+schema).

E\_NOTIMPL is not a valid return type for any of the **IProvisioningProfileWireless** interface's methods.

## Requirements



|                    |                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------|
| Version<br/> | Not available beginning with Windows Vista.<br/>                                                   |
| Header<br/>  | <dl> <dt>Netprov.h (include Netprov.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20IProvisioningProfileWireless%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




