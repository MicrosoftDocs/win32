---
title: Resource URIs
description: A resource URI is an identifier for a distinct type of management operation or value used by management services that implement the WS-Management protocol.
ms.assetid: 478a6e5d-0675-462e-b2fd-fd2b5379e298
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Resource URIs

A [*resource URI*](windows-remote-management-glossary.md) is an identifier for a distinct type of management operation or value used by management services that implement the WS-Management protocol. A management value could be the temperature inside a computer. An example of a management operation is starting a stopped service or setting a disk volume user quota.

## Resource URI Format

A URI consists of a prefix and a path to a resource as is shown in the following example:

"http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32\_LogicalDisk"

This schema specification indicates that the URI is based on version 1 of the official WS-Management protocol and that the resource is a [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) in the "root\\cimv2" namespace of the WMI repository. URI prefixes contain a schema specification, such as "schemas.microsoft.com/wbem/wsman/1/wmi" and a specific type of resource, such as **Win32\_LogicalDisk**. For more information about identifying a specific instance of a WMI class, see [Windows Remote Management and WMI](windows-remote-management-and-wmi.md).

For more information, see [URI Prefixes](uri-prefixes.md).

## Types of Resource URIs

While [*Windows Management Instrumentation (WMI)*](windows-remote-management-glossary.md) is the primary source of management data for Windows-based operating systems, other sources of management schema also exist.

The following list describes several types of resource URIs used by Windows Remote Management:

-   WMI URIs

    This group of URIs represent a [*Common Information Model*](/windows/desktop/WmiSdk/gloss-c) class path which includes namespace and class.

    WMI URIs can be used in:

    -   [**Session**](session.md) methods
    -   [**IWSManSession**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmansession) methods
    -   [**WSMan.CreateResourceLocator**](wsman-createresourcelocator.md) or [**IWSMan.CreateResourceLocator**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex-createresourcelocator) methods
    -   [**ResourceLocator**](resourcelocator.md) or [**IWSManResourceLocator**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmanresourcelocator) methods

-   IPMI URIs

    This group of URIs represent industry standard URIs based upon CIM version 2.9. IPMI URIs can be used in [**Session**](session.md) methods [**Get**](session-get.md), [**Put**](session-put.md), [**Enumerate**](session-enumerate.md) , and [**Invoke**](session-invoke.md).

    An example is https://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/CIM_NumericSensor.xsd. This resource is defined according to the [DMTF.org](https://www.dmtf.org/home) CIM schema.

-   WinRM configuration URIs

    This group of URIs are configuration operations for the WinRM[*listener*](windows-remote-management-glossary.md) configuration.

    `https://schemas.microsoft.com/wbem/wsman/1/config/listener` can be used in [**Session**](session.md) methods [**Get**](session-get.md), [**Put**](session-put.md), [**Create**](session-create.md), [**Delete**](session-delete.md), and [**Enumerate**](session-enumerate.md).

-   [*System Event Log*](windows-remote-management-glossary.md) (SEL) URIs

    This group of URIs subscribes to Event Collector events from the BMC. You can subscribe to these events using the **Wevtutil** command-line tool.

## Case Sensitivity

The [*WMI plug-in*](windows-remote-management-glossary.md) preserves the case of the resource URI received in a request. However, to ensure interoperability with other implementations of WS-Management protocol, use the correct case for the requested resource in resource URI. The correct case is the spelling defined by the resource provider.

While resource URIs do not require case-sensitivity, [*fragment*](windows-remote-management-glossary.md) XML does. A fragment specifies just one property, rather than the entire set of properties for a resource. In the case of WMI resources, fragment syntax gets one property from a resource instance. For example, getting only the **Version** property from [**Win32\_OperatingSystem**](/windows/desktop/CIMWin32Prov/win32-operatingsystem) requires using a fragment. For more information about fragments, see "Adding a selector to a ResourceLocator or IWSManResourceLocator object" in [Windows Remote Management and WMI](windows-remote-management-and-wmi.md).

Following XML and [*XPath*](windows-remote-management-glossary.md) standards, the [*WMI plug-in*](windows-remote-management-glossary.md) enforces case-sensitivity for fragments and XML that defines the input parameters for a method. Case-sensitivity is required to support the XPath 1.0/Level 1 standard. To get WMI data through WinRM, case-sensitivity means that the names of WMI classes, properties, and methods must match the case of the name found in the WMI repository.

For more information, see [XPath Syntax](/previous-versions/dotnet/netframework-4.0/ms256471(v=vs.100)).

## Case Sensitivity Examples

For example, a script that obtains the **SECURITY\_DESCRIPTOR** property from an instance of the WMI [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service) class cannot use upper-case for the names in the fragment path, only the URI. The WinRM [*WMI plug-in*](windows-remote-management-glossary.md) returns an error for the following VBScript example because the XPath XML supplied for the **FragmentPath** does not use the correct case. In the WMI repository, the class is spelled "Win32\_Service".


```VB
RResourceUri = "http://schemas.microsoft.com/wbem/wsman/1/"_& "wmi/root/cimv2/Win32_Service?Name=winrm"
Set WSMan = CreateObject("WSMan.Automation")
Set Locator = WSMan.CreateResourceLocator(Resourceuri)
Locator.FragmentPath = "/Win32_SERVICE/Name"
Set Session = WSMan.Createsession
xml = Session.Get(Locator)
WScript.Echo xml
```



The following version of the same example shows the correct use of case for the [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service) class and **SECURITY\_DESCRIPTOR** property.


```VB
ResourceUri = "http://schemas.microsoft.com/wbem/wsman/1/"_
    & "wmi/root/cimv2/Win32_Service?Name=winrm"
Set WSMan = CreateObject("WSMan.Automation")
Set Locator = WSMan.CreateResourceLocator(Resourceuri)
Locator.FragmentPath = "/Win32_Service/Name"
Set Session = WSMan.Createsession
xml = Session.Get(Locator)
WScript.Echo xml
```



## Related topics

<dl> <dt>

[About Windows Remote Management](about-windows-remote-management.md)
</dt> <dt>

[Remote Hardware Management](remote-hardware-management.md)
</dt> <dt>

[**ResourceLocator**](resourcelocator.md)
</dt> </dl>

 

 
