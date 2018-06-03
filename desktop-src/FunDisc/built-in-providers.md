---
Description: The built-in Function Discovery providers enumerate discoverable resources, manage property stores, and respond to queries for enumerated resources.
ms.assetid: 45caf8f6-3173-4b1a-bbbe-66637ac1f7bc
title: Built-in Providers
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Built-in Providers

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

The built-in Function Discovery providers enumerate discoverable resources, manage property stores, and respond to queries for enumerated resources.

Function Discovery providers are implemented as simple in-process COM objects. Each provider implements the [**IFunctionDiscoveryProvider**](/windows/desktop/api/FunctionDiscoveryProvider/nn-functiondiscoveryprovider-ifunctiondiscoveryprovider) interface so that the provider can respond to function instance queries.

Function Discovery supports the following built-in providers.



| Provider                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="NetBIOS_provider"></span><span id="netbios_provider"></span><span id="NETBIOS_PROVIDER"></span>[NetBIOS provider](netbios-provider.md)<br/>                                             | The NetBIOS provider enumerates NetBIOS discoverable devices using the WNet functions.<br/>                                                                                                                                                                                                         |
| <span id="Plug_and_Play__PnP__provider"></span><span id="plug_and_play__pnp__provider"></span><span id="PLUG_AND_PLAY__PNP__PROVIDER"></span>[Plug and Play (PnP) provider](pnp-provider.md)<br/> | The PnP provider constructs a function instance for each functional device object (FDO) installed on the system. The PnP provider also discovers network connected devices (NCD) that have been associated with the system through the PnP-X architecture.<br/>                                     |
| <span id="Registry_provider"></span><span id="registry_provider"></span><span id="REGISTRY_PROVIDER"></span>[Registry provider](registry-provider.md)<br/>                                        | The registry provider persists function instances based on resources registered through the system registry.<br/>                                                                                                                                                                                   |
| <span id="SSDP_provider"></span><span id="ssdp_provider"></span><span id="SSDP_PROVIDER"></span>[SSDP provider](ssdp-provider.md)<br/>                                                            | The Simple Service Discovery Protocol (SSDP) provider provides Function Discovery with information regarding the presence of SSDP devices on the network. The SSDP provider discovers devices on the local subnet and, optionally, any other discoverable devices or local network resources. <br/> |
| <span id="WS-Discovery__WSD__provider"></span><span id="ws-discovery__wsd__provider"></span><span id="WS-DISCOVERY__WSD__PROVIDER"></span>[WS-Discovery (WSD) provider](wsd-provider.md)<br/>     | The Function Discovery WS-Discovery provider provides Function Discovery with information regarding the presence of Web services devices on the network. The WS-Discovery provider discovers devices across subnets.<br/>                                                                           |
| <span id="WCN_provider"></span><span id="wcn_provider"></span><span id="WCN_PROVIDER"></span>WCN provider<br/>                                                                                     | The Windows Connect Now provider.<br/>                                                                                                                                                                                                                                                              |



 

 

 




