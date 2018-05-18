---
title: URI Prefixes
description: The resource URI prefix is different depending on which XML schema describes the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '47c32da6-98c9-4f66-82ac-647976127cb7'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-remote-management'
ms.tgt_platform: multiple
---

# URI Prefixes

The [*resource URI*](windows-remote-management-glossary.md#winrm-gloss-resource-uri) prefix is different depending on which XML schema describes the resource.

## Prefixes

If you access a [*CIM*](windows-remote-management-glossary.md#winrm-gloss-cim) 2.1 class, such as [**CIM\_DataFile**](https://msdn.microsoft.com/library/aa387236), the prefix of the URI differs from the prefix for a CIM 2.9 class, such as **CIM\_AdminDomain**. CIM 2.1 classes are documented in the [CIM Classes](https://msdn.microsoft.com/library/aa386179) section of Windows Management Instrumentation (WMI).

Most [WMI classes](https://msdn.microsoft.com/library/aa394554) are in the **root\\cimv2** WMI namespace. Classes for the Microsoft Intelligent Platform Management Interface ([IPMI](https://msdn.microsoft.com/library/aa391402)) provider are in **root\\hardware**.

The following list contains the resource URI prefixes for these schemas:

-   WMI or CIM 2.1 classes in the **root\\cimv2** namespace

    "http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/"

-   CIM 2.9 classes or IPMI classes

    "http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2"

-   Alternate way to access IPMI provider classes

    "http://schemas.microsoft.com/wbem/wsman/1/wmi/root/hardware/"

For more information, see [Resource URIs](resource-uris.md) and [UrlPrefix Strings](https://msdn.microsoft.com/library/windows/desktop/aa364698). For more information about generating a URI for a WMI class or method, see [Windows Remote Management and WMI](windows-remote-management-and-wmi.md).

## Prefix Aliases

A prefix alias is a shortcut that represents the long resource URI prefix. You can also use aliases in the **Winrm** command-line. To view a list of available aliases, type **Winrm help aliases**.

Be aware that an alias cannot be used inside an endpoint reference (EPR) when specifying a resource URI. Windows Remote Management is unable to expand the alias when it is embedded in XML.

In the following code example, the winrm alias is used in an EPR instead of the complete resource URI, which is http://schemas.microsoft.com/wbem/wsman/1/config/Listener. In this case, WinRM returns an error that indicates the service cannot process the request.


```XML
ResourceUri = "</wxf:ResourceCreated>.....
<w:ResourceURI>winrm/config/listener</w:ResourceURI>...
</w:SelectorSet></a:ReferenceParameters></wxf:ResourceCreated>"

Set ResourceLocator = WSManObj.CreateResourceLocator(resourceUri)
ResponseStr = Session.Get(ResourceLocator, 0)
```



The following lists defined aliases and resource URIs for which they substitute.

<dl> <dt>

<span id="wmi"></span><span id="WMI"></span>wmi
</dt> <dd>

http://schemas.microsoft.com/wbem/wsman/1/wmi

</dd> <dt>

<span id="wmicimv2"></span><span id="WMICIMV2"></span>wmicimv2
</dt> <dd>

http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2

</dd> <dt>

<span id="cimv2"></span><span id="CIMV2"></span>cimv2
</dt> <dd>

http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2

</dd> <dt>

<span id="winrm"></span><span id="WINRM"></span>winrm
</dt> <dd>

http://schemas.microsoft.com/wbem/wsman/1

</dd> <dt>

<span id="wsman"></span><span id="WSMAN"></span>wsman
</dt> <dd>

http://schemas.microsoft.com/wbem/wsman/1

</dd> <dt>

<span id="shell"></span><span id="SHELL"></span>shell
</dt> <dd>

http://schemas.microsoft.com/wbem/wsman/1/windows/shell

</dd> </dl>

## Related topics

<dl> <dt>

[About Windows Remote Management](about-windows-remote-management.md)
</dt> <dt>

[Windows Remote Management and WMI](windows-remote-management-and-wmi.md)
</dt> <dt>

[Resource URIs](resource-uris.md)
</dt> </dl>

 

 




