---
Description: IProvisioningDomain
ms.assetid: 72f2daac-d773-4474-af26-cf0302cd992b
title: IProvisioningDomain
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IProvisioningDomain

> [!Note]  
> Wireless Provisioning Services (WPS) is no longer available as of Windows Vista.

 

The **IProvisioningDomain** interface is the public interface to the WPS provisioning store on the client. The **IProvisioningDomain**interface is used to do the following:

-   Add WPS XML files for pre-provisioning in the provisioning store. Files can only be added if the domain does not currently exist within the provisioning store.

    For more information about pre-provisioning, see [Wireless Network Provisioning](https://www.bing.com/search?q=Wireless+Network+Provisioning).

-   Query the WPS provisioning store for XML data. Queries can be made for any or all domains within the store. Queries can also be made for any or all language versions of the XML data.

WPS manages XML files in the provisioning store based on a WISP domain. The domain and its parameters are defined through the [Master schema](https://www.bing.com/search?q=Master+schema).

### Methods

The following methods are listed in vtable order:



| IUnknown method               | Description                                         |
|-------------------------------|-----------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces<br/> |
| **AddRef**<br/>         | Increments the reference count<br/>           |
| **Release**<br/>        | Decrements the reference count<br/>           |



 



| IProvisioningDomain method                            | Description                                                                                             |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**Add**](/windows/desktop/api/netprov/nf-netprov-iprovisioningdomain-add)<br/>     | Adds XML files to the WPS provisioning store for a WISP domain<br/>                               |
| [**Query**](/windows/desktop/api/netprov/nf-netprov-iprovisioningdomain-query)<br/> | Queries the WPS provisioning store for XML data from any WISP domain and/or language version<br/> |



 

### Headers

Defined in *netprov.h*. Include *netprov.h*.

### Comments

The **IProvisioningDomain** interface supports the [Wireless Network Provisioning](https://www.bing.com/search?q=Wireless+Network+Provisioning)method.

The XML data used in this interface is based on the following schemas:

-   [Master schema](https://www.bing.com/search?q=Master+schema)

-   [Configuration schemas](https://www.bing.com/search?q=Configuration+schemas)

-   [Connection property schemas](https://www.bing.com/search?q=Connection+property+schemas)

E\_NOTIMPL is not a valid return type for any of the **IProvisioningDomain** interface's methods.

> [!Note]  
> This interface is not available for use beginning with Windows Vista.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20IProvisioningDomain%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




