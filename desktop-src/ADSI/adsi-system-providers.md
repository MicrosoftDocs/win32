---
title: ADSI Service Providers
description: This topic gives an overview of the ADSI service providers that are provided in the server.
ms.assetid: 419d7953-a879-4d6c-be74-173d76c3f932
ms.tgt_platform: multiple
keywords:
- ADSI ADSI , Service Providers
- Service Providers ADSI
ms.topic: article
ms.date: 05/31/2018
---

# ADSI Service Providers

ADSI includes the service providers listed in the following table.



| Service provider | Description                                                                                | For more information                                      |
|------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| LDAP<br/>  | Namespace implementation compatible with Lightweight Directory Access Protocol.<br/> | [ADSI LDAP Provider](adsi-ldap-provider.md)<br/>   |
| WinNT<br/> | Namespace implementation compatible with Windows.<br/>                               | [ADSI WinNT Provider](adsi-winnt-provider.md)<br/> |



 

Other service providers are included as part of products other than ADSI. The following are the ADSI service providers implemented by Microsoft.



| Service provider | For more information                                                                        |
|------------------|---------------------------------------------------------------------------------------------|
| IIS<br/>   | [IIS ADSI Provider Architecture](/previous-versions/iis/6.0-sdk/ms525929(v=vs.90))<br/> |



 

The methods and property methods exposed by ADSI interfaces are not supported by every service provider. Because different directory services vary in the types of objects and properties stored, use different protocols, and authentication, ADSI is designed to work seamlessly with supported service providers. Thus, there are interfaces, methods, and property methods that work with one service provider, such as LDAP, that may not work on another, such as WinNT.

This section contains provider-specific information, such as the ADsPath format, a listing of ADSI objects used for that service provider, and data type and syntax information for the service providers included with ADSI. There is also a summary description of ADSI interfaces supported by each provider included with ADSI.

In ADSI, different providers are associated with different DLLs. The LDAP provider is associated with Adsldp.dll, Adsldpc.dll, and Adsmsext.dll. The WinNT provider is associated with Adsnt.dll. The ROUTER provider is associated with Activeds.dll.

> [!Note]  
> Do not assume that default ADSI providers are thread-safe. Multithreaded application developers should coordinate access between threads through the proper use of synchronization objects such as semaphores, mutexes, critical sections, and so on.

 

For more information about ADSI service providers, see [ADSI Router](adsi-router.md) and [Provider Support of ADSI interfaces](provider-support-of-adsi-interfaces.md).

 

