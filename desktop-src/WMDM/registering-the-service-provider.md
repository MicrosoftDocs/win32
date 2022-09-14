---
title: Registering the Service Provider
description: Registering the Service Provider
ms.assetid: 556d6519-bc24-446b-a360-e3d83b40d541
keywords:
- Windows Media Device Manager,registering service providers
- Device Manager,registering service providers
- programming guide,registering service providers
- service providers,registering service providers
- creating service providers,registering service providers
- registering service providers
ms.topic: article
ms.date: 05/31/2018
---

# Registering the Service Provider

In addition to being registered as a COM object, a service provider must be registered as a plug-in to Windows Media Device Manager. To register, a service provider must create the following registry key:

`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Media Device Manager\Plugins\SP\<             `

In this key, < *your service provider name* > is the name of your DLL; for example, the sample service provider uses MsHDSP. The ProgID key should have a string value that corresponds to the CLSID of your service provider. For instance, the sample service provider has the value "MDServiceProviderHD.MDServiceProviderHD".

The sample service provider's implementation of DLLRegisterServer in Mdsp.cpp adds this registry key when you register the sample service provider DLL.

## Related topics

<dl> <dt>

[**Creating a Service Provider**](creating-a-service-provider.md)
</dt> </dl>

 

 




