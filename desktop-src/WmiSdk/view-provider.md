---
Description: The View provider is an instance and method provider that creates new classes based on instances of other classes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e1992e10-647b-4747-8f3d-b437ef7f3770
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: View Provider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# View Provider

The View provider is an instance and method provider that creates new classes based on instances of other classes. You can use the View provider to take properties from different source classes, different namespaces, or different computers and combine the properties as a single class.

As an instance and method provider, the View provider supports the standard [**IWbemProviderInit**](/windows/win32/Wbemprov/nn-wbemprov-iwbemproviderinit?branch=master) interface and the following [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) methods:

-   [**CreateInstanceEnumAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-createinstanceenumasync?branch=master)
-   [**ExecMethodAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execmethodasync?branch=master)
-   [**ExecQueryAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execqueryasync?branch=master)
-   [**GetObjectAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-getobjectasync?branch=master)
-   [**PutInstanceAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync?branch=master)

For more information about the qualifiers use to define View provider classes, see [Qualifiers Specific to the View Provider](qualifiers-specific-to-the-view-provider.md).

For more information about views, see [Linking Classes Together](linking-classes-together.md).

Two versions of the View provider are available on 64-bit platforms. For more information, see [Getting and Providing Data on a 64-bit Computer](getting-and-providing-data-on-a-64-bit-computer.md).

The View provider is implemented in ViewProv.dll.

## Related topics

<dl> <dt>

[WMI Providers](wmi-providers.md)
</dt> </dl>

 

 



