---
title: Windows Filtering Platform
description: Windows Filtering Platform (WFP) is a set of API and system services that provide a platform for creating network filtering applications.
ms.assetid: 0436f559-20e6-4199-8391-10eb7d85df23
keywords:
- Windows Filtering Platform
- Windows Filtering Platform Start Page,start page
ms.topic: article
ms.date: 05/31/2018
---

# Windows Filtering Platform

## Purpose

Windows Filtering Platform (WFP) is a set of API and system services that provide a platform for creating network filtering applications. The WFP API allows developers to write code that interacts with the packet processing that takes place at several layers in the networking stack of the operating system. Network data can be filtered and also modified before it reaches its destination.

By providing a simpler development platform, WFP is designed to replace previous packet filtering technologies such as Transport Driver Interface (TDI) filters, Network Driver Interface Specification (NDIS) filters, and Winsock Layered Service Providers (LSP). Starting in Windows Server 2008 and Windows Vista, the firewall hook and the filter hook drivers are not available; applications that were using these drivers should use WFP instead.

With the WFP API, developers can implement firewalls, intrusion detection systems, antivirus programs, network monitoring tools, and parental controls. WFP integrates with and provides support for firewall features such as authenticated communication and dynamic firewall configuration based on applications' use of sockets API (application-based policy). WFP also provides infrastructure for IPsec policy management, change notifications, network diagnostics, and stateful filtering.

Windows Filtering Platform is a development platform and not a firewall itself. The firewall application that is built into Windows Vista, Windows Server 2008, and later operating systems   Windows Firewall with Advanced Security (WFAS)   is implemented using WFP. Therefore, applications developed with the WFP API or the [WFAS API](/previous-versions/windows/desktop/ics/windows-firewall-with-advanced-security-reference) use the common filtering arbitration logic that is built into WFP.

The WFP API consists of a user-mode API and a kernel-mode API. This section provides an overview of the entire WFP and describes in detail only the user-mode portion of the WFP API. For a detailed description of the kernel-mode WFP API, see the [Windows Driver Kit](/windows-hardware/drivers/network/windows-filtering-platform-callout-drivers2) online help.

## Developer audience

The Windows Filtering Platform API is designed for use by programmers using C/C++ development software. Programmers should be familiar with networking concepts and design of systems using user-mode and kernel-mode components.

## Run-time requirements

The Windows Filtering Platform is supported on clients running Windows Vista and later, and on servers running Windows Server 2008 and later. For information about the run-time requirements for a specific programming element, see the Requirements section of the reference page for that element.





 

## In this section



| Topic                                                                                               | Description                                                                                       |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [What's New in Windows Filtering Platform](what-s-new-in-windows-filtering-platform.md)<br/> | Information on new features and APIs in Windows Filtering Platform.<br/>                    |
| [About Windows Filtering Platform](about-windows-filtering-platform.md)<br/>                 | An overview of Windows Filtering Platform.<br/>                                             |
| [Using Windows Filtering Platform](using-windows-filtering-platform.md)<br/>                 | Example code using the Windows Filtering Platform API. <br/>                                |
| [Windows Filtering Platform API Reference](fwp-reference.md)<br/>                            | Documentation for the Windows Filtering Platform functions, structures, and constants.<br/> |



 

## Additional resources

To ask questions and have discussions about using the WFP API, visit the [Windows Filtering Platform Forum](https://social.msdn.microsoft.com/forums/wfp/threads/).

## Related topics

<dl> <dt>

[Kernel-Mode Windows Filtering Platform API - Design Guide](/windows-hardware/drivers/network/windows-filtering-platform-callout-drivers2)
</dt> <dt>

[Kernel-Mode Windows Filtering Platform API - Reference](/windows-hardware/drivers/ddi/_netvista/)
</dt> <dt>

[Windows Firewall with Advanced Security](/previous-versions/windows/desktop/ics/windows-firewall-advanced-security-start-page)
</dt> <dt>

[WFP Diagnostics Extensible Helper Class](/windows/desktop/NDF/windows-filtering-platform-extensible-helper-class)
</dt> <dt>

[Winsock Secure Socket Extensions](/windows/desktop/WinSock/winsock-secure-socket-extensions)
</dt> </dl>

 

