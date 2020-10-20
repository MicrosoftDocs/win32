---
title: URI prefixes
description: The resource URI prefix is different depending on which XML schema describes the resource.
ms.assetid: 47c32da6-98c9-4f66-82ac-647976127cb7
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# URI prefixes

The [*resource URI*](windows-remote-management-glossary.md) prefix is different depending on which XML schema describes the resource.

## Prefixes

If you access a [*CIM*](windows-remote-management-glossary.md) 2.1 class, such as [**CIM\_DataFile**](/windows/desktop/CIMWin32Prov/cim-datafile), the prefix of the URI differs from the prefix for a CIM 2.9 class, such as **CIM\_AdminDomain**. CIM 2.1 classes are documented in the [CIM Classes](/windows/desktop/WmiSdk/cimclas) section of Windows Management Instrumentation (WMI).

Most [WMI classes](/windows/desktop/WmiSdk/wmi-classes) are in the **root\\cimv2** WMI namespace. Classes for the Microsoft Intelligent Platform Management Interface ([IPMI](/previous-versions/windows/desktop/ipmiprv/ipmi-provider)) provider are in **root\\hardware**.

The following list contains the resource URI prefixes for these schemas:

-   WMI or CIM 2.1 classes in the **root\\cimv2** namespace

    "http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/"

-   CIM 2.9 classes or IPMI classes

    "https://schemas.dmtf.org/wbem/wscim/1/cim-schema/2"

-   Alternate way to access IPMI provider classes

    "http://schemas.microsoft.com/wbem/wsman/1/wmi/root/hardware/"

For more information, see [Resource URIs](resource-uris.md) and [UrlPrefix Strings](/windows/desktop/Http/urlprefix-strings). For more information about generating a URI for a WMI class or method, see [Windows Remote Management and WMI](windows-remote-management-and-wmi.md).

## Prefix Aliases

A prefix alias is a shortcut that represents the long resource URI prefix. You can also use aliases in the **Winrm** command-line. To view a list of available aliases, type **Winrm help aliases**.

Be aware that an alias cannot be used inside an endpoint reference (EPR) when specifying a resource URI. Windows Remote Management is unable to expand the alias when it is embedded in XML.

In the following code example, the winrm alias is used in an EPR instead of the complete resource URI, which is `http://schemas.microsoft.com/wbem/wsman/1/config/Listener`. In this case, WinRM returns an error that indicates the service cannot process the request.


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

`http://schemas.microsoft.com/wbem/wsman/1/wmi`

</dd> <dt>

<span id="wmicimv2"></span><span id="WMICIMV2"></span>wmicimv2
</dt> <dd>

`http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2`

</dd> <dt>

<span id="cimv2"></span><span id="CIMV2"></span>cimv2
</dt> <dd>

`https://schemas.dmtf.org/wbem/wscim/1/cim-schema/2`

</dd> <dt>

<span id="winrm"></span><span id="WINRM"></span>winrm
</dt> <dd>

`http://schemas.microsoft.com/wbem/wsman/1`

</dd> <dt>

<span id="wsman"></span><span id="WSMAN"></span>wsman
</dt> <dd>

`http://schemas.microsoft.com/wbem/wsman/1`

</dd> <dt>

<span id="shell"></span><span id="SHELL"></span>shell
</dt> <dd>

`http://schemas.microsoft.com/wbem/wsman/1/windows/shell`

</dd> </dl>

## Related topics

<dl> <dt>

[About Windows Remote Management](about-windows-remote-management.md)
</dt> <dt>

[Windows Remote Management and WMI](windows-remote-management-and-wmi.md)
</dt> <dt>

[Resource URIs](resource-uris.md)
</dt> </dl>
