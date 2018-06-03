---
Description: INetCfg
ms.assetid: 56946b55-78d6-42e1-8d30-a4ea61e95077
title: INetCfg
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# INetCfg

## 

The **INetCfg** interface is the root of all networking configuration and installation. The **INetCfg**interface provides methods that load into memory basic networking information, apply changes to network configuration, and retrieve network components and binding paths.

The interface identifier (IID) for this interface is IID\_INetCfg.

### When to Implement

It is not necessary to implement the methods of this interface. They are implemented in *Netcfgx.dll*.

### When to Use

Use this interface to retrieve network components and binding paths.

### Methods

The following methods are listed in Vtable order:



| IUnknown method               | Description                                          |
|-------------------------------|------------------------------------------------------|
| **QueryInterface**<br/> | Returns pointers to supported interfaces.<br/> |
| **AddRef**<br/>         | Increments the reference count.<br/>           |
| **Release**<br/>        | Decrements the reference count.<br/>           |



 



| INetCfg method                                                  | Description                                                                                             |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**Initialize**](/windows/desktop/api/netcfgx/nf-netcfgx-inetcfg-initialize)<br/>             | Initializes network configuration by loading into memory all basic networking information.<br/>   |
| [**Uninitialize**](/windows/desktop/api/Netcfgx/nf-netcfgx-inetcfg-uninitialize)<br/>         | Unloads from memory all basic networking information.<br/>                                        |
| [**Apply**](/windows/desktop/api/Netcfgx/nf-netcfgx-inetcfg-apply)<br/>                       | Applies all changes made to the configuration state of the network to the registry.<br/>          |
| [**Cancel**](/windows/desktop/api/Netcfgx/nf-netcfgx-inetcfg-cancel)<br/>                     | Disregards any proposed changes to the configuration state of the network.<br/>                   |
| [**EnumComponents**](/windows/desktop/api/netcfgx/nf-netcfgx-inetcfg-enumcomponents)<br/>     | Retrieves an enumeration containing a collection of network components of a particular type.<br/> |
| [**FindComponent**](/windows/desktop/api/netcfgx/nf-netcfgx-inetcfg-findcomponent)<br/>       | Retrieves the first network component that matches the specified component identifier.<br/>       |
| [**QueryNetCfgClass**](/windows/desktop/api/netcfgx/nf-netcfgx-inetcfg-querynetcfgclass)<br/> | Retrieves a pointer to a specific class of network component.<br/>                                |



 

### Comments

The **INetCfg** interface is the only network configuration interface that applications can receive after they call the COM [**CoCreateInstance**](https://msdn.microsoft.com/windows/desktop/7295a55b-12c7-4ed0-a7a4-9ecee16afdec) function to create a network configuration object. Applications must obtain all other network configuration interfaces from **INetCfg** by either enumerating the interfaces or by calling methods that return the interfaces.

When notify objects initialize, they receive a pointer to **INetCfg** that represents the current networking configuration. Notify objects can use **INetCfg** to access all aspects of networking configuration.

After an application creates a network configuration object, the application should call **Initialize**to initialize network configuration. After the application finishes with the network configuration object, the application should call **Uninitialize**before releasing the network configuration object.

### Example

The following example creates a network configuration object, accesses a specific network component, and, finally, releases the network configuration object. This example shows a typical sequence of operations.


```
INetCfg *pnetcfg = NULL;
INetCfgLock *pncfglock = NULL;
INetCfgComponent *pncfgcomp = NULL;
HRESULT hr = S_OK;
LPWSTR szwrClient = NULL;

hr = CoInitialize(NULL);
 
hr = CoCreateInstance(CLSID_CNetCfg, NULL, CLSCTX_SERVER, 
                      IID_INetCfg, (LPVOID*)&amp;pnetcfg);
hr = pnetcfg->QueryInterface(IID_INetCfgLock, (LPVOID*)&amp;pncfglock);
hr = pncfglock->AcquireWriteLock(5000, L"MY CLIENT", &amp;szwrClient);
// hr is S_FALSE if the lock could not be acquired in 5 seconds
hr = pnetcfg->Initialize(NULL);
 
hr = pnetcfg->FindComponent(L"MS_TCPIP", &amp;pncfgcomp);
// Call various methods on pncfgcomp here.
pncfgcomp->Release();
 
hr = pnetcfg->Apply();
hr = pnetcfg->Uninitialize();
hr = pncfglock->ReleaseWriteLock();
pnetcfg->Release();

CoUninitialize();
 
```



## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Netcfgx.h (include Netcfgx.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20INetCfg%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




