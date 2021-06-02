---
description: Windows Management Instrumentation (WMI) is the Microsoft implementation of Web-Based Enterprise Management (WBEM), which is an industry initiative to develop a standard technology for accessing management information in an enterprise environment.
ms.assetid: d745cf25-a139-439d-9ac5-e7720b640516
ms.tgt_platform: multiple
title: About WMI
ms.topic: article
ms.date: 05/31/2018
---

# About WMI

Windows Management Instrumentation (WMI) is the Microsoft implementation of Web-Based Enterprise Management (WBEM), which is an industry initiative to develop a standard technology for accessing management information in an enterprise environment. WMI uses the Common Information Model (CIM) industry standard to represent systems, applications, networks, devices, and other managed components. CIM is developed and maintained by the Distributed Management Task Force ([DMTF](https://www.dmtf.org/standards/wsman)).

> [!Note]  
> The next-generation of WMI, known as the Windows Management Infrastructure (MI), is currently available. MI is fully compatible with previous versions of WMI, and provides a host of features and benefits that make designing and developing providers and clients easier than ever. For example, many newer providers are written using the MI framework, but can be accessed using WMI scripts and applications. For more information about the differences between the two technologies, see [Why Use MI?](/previous-versions/windows/desktop/wmi_v2/why-use-mi-)

 

## Managing Remote Computer Systems with WMI

The ability to obtain management data from remote computers is what makes WMI useful. Remote WMI connections are made through DCOM. An alternative is to use Windows Remote Management ([WinRM](/windows/desktop/WinRM/portal)), which obtains remote WMI management data using the WS-Management SOAP-based protocol.

## Programming with WMI

Management applications or scripts can get data or perform operations through WMI in a variety of languages. For more information, see the Developer Audience section at [Windows Management Instrumentation](wmi-start-page.md).

Many Windows features have associated WMI providers, like the [Boot Configuration Data (BCD) Provider](/previous-versions/windows/desktop/bcd/boot-configuration-data-portal) or the [Storage Volume Provider](/previous-versions/windows/desktop/vdswmi/storage-volume-provider). WMI Providers implement the functionality described by WMI classes methods and properties to manage associated Windows features. For more information, see [WMI Providers](wmi-providers.md) and [WMI Classes](wmi-classes.md).

For more information about how to write a provider to supply data from new hardware or applications, see [Providing Data to WMI](providing-data-to-wmi.md).

For more information about how to implement this technology, see [Using WMI](using-wmi.md).

The following table lists topics included in this section.



| Section                                                                                                | Description                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [What's New in WMI](what-s-new-in-wmi.md)                                                             | New features in WMI.                                                                                                                                                                                                                              |
| [Operating System Availability of WMI Components](operating-system-availability-of-wmi-components.md) | Some components are no longer available or are available as an optional installation.                                                                                                                                                             |
| [WMI Architecture](wmi-architecture.md)                                                               | A management application communicates with WMI by using a variety of interfaces, such as Visual Basic, C++, ODBC, and ActiveX. All the WMI interfaces are based on the Component Object Model (COM).                                              |
| [Common Information Model](common-information-model.md)                                               | A language independent programming model that uses object oriented techniques to describe an enterprise.                                                                                                                                          |
| [Managed Object Format](managed-object-format--mof-.md)                                               | A format that enables you to create human-readable code, which the operating system can translate into a set of CIM classes. You can use the new classes to model and control new technologies for an enterprise.                                 |
| [User Account Control and WMI](user-account-control-and-wmi.md)                                       | User Account Control (UAC) affects what WMI data is returned, remote access, and how scripts must be run. For more information, see [Getting Started with User Account Control on Windows Vista](https://support.microsoft.com/help/922708/how-to-use-user-account-control-uac-in-windows-vista). |
| [Access to WMI Securable Objects](access-to-wmi-securable-objects.md)                                 | WMI uses standard Windows security objects and procedures to control and protect access to securable objects like WMI namespaces, printers, services, and DCOM applications.                                                                      |
| [Performance Libraries and WMI](performance-libraries-and-wmi.md)                                     | Data from the system performance counters is available in WMI classes.                                                                                                                                                                            |
| [IPv6 and IPv4 Support in WMI](ipv6-and-ipv4-support-in-wmi.md)                                       | WMI [IP Route Provider](/previous-versions/windows/desktop/wmiiprouteprov/ip-route-provider) and network classes supply data for IPv4 addresses. Starting with Windows Vista, WMI also provides limited support for IPv6 network capabilities.                                       |
| [Date and Time Format](date-and-time-format.md)                                                       | WMI uses the date and time formats defined by the Distributed Management Task Force CIM specification. For more information, see [DMTF](https://www.dmtf.org/).                                                          |
| [Scripting Access to WMI](scripting-access-to-wmi.md)                                                 | Write WMI scripts to perform management tasks.                                                                                                                                                                                                    |
| [WMI Troubleshooting](wmi-troubleshooting.md)                                                         | When accessing WMI local or remote data in an application or script, you may receive errors ranging from missing classes to access denied. Providers also have debugging options and troubleshooting classes available.                           |
| [Further Information](further-information.md)                                                         | Websites, books, and articles about WMI.                                                                                                                                                                                                          |



 

## Related topics

<dl> <dt>

[Using WMI](using-wmi.md)
</dt> <dt>

[WMI Reference](wmi-reference.md)
</dt> </dl>

 

 
