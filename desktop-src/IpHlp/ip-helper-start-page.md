---
description: The Internet Protocol Helper (IP Helper) API enables the retrieval and modification of network configuration settings for the local computer.
ms.assetid: 4896a9f8-0486-4380-bf49-d1c9ef114acc
title: IP Helper
ms.topic: article
ms.date: 05/31/2018
---

# IP Helper

## Purpose

The Internet Protocol Helper (IP Helper) API enables the retrieval and modification of network configuration settings for the local computer.

## Where applicable

The IP Helper API is applicable in any computing environment where programmatically manipulating network and TCP/IP configuration is useful. Typical applications include IP routing protocols and Simple Network Management Protocol (SNMP) agents.

## Developer audience

The IP Helper API is designed for use by C/C++ programmers. Programmers should also be familiar with Windows networking and TCP/IP networking concepts.

## Run-time requirements

The IP Helper API can be used on all Windows platforms. Not all operating systems support all functions. Where certain implementations or capabilities of Windows Sockets 2 platform restrictions do exist, they are clearly noted in the documentation. If an IP Helper function is called on a platform that does not support the function, ERROR\_NOT\_SUPPORTED is returned. For more specific information about which operating systems support a particular function, refer to the Requirements sections in the documentation.

## In this section



| Topic                                                              | Description                                                                                                                                                                                                       |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [What's New in IP Helper](what-s-new-in-ip-helper.md)<br/>  | Information on new features for IP Helper.<br/>                                                                                                                                                             |
| [About IP Helper](about-ip-helper.md)<br/>                  | General information about IP Helper programming considerations and capabilities available to developers.<br/>                                                                                               |
| [Using IP Helper](using-ip-helper.md)<br/>                  | Procedures and programming techniques used with IP Helper. This section includes basic IP Helper programming techniques, such as [Getting Started With IP Helper](getting-started-with-ip-helper.md).<br/> |
| [IP Helper reference](ip-helper-function-reference.md)<br/> | Reference documentation for the IP Helper functions, structures, and enumerations.<br/>                                                                                                                     |



 

## Related topics

<dl> <dt>

[Windows Sockets 2](/windows/desktop/WinSock/windows-sockets-start-page-2)
</dt> <dt>

[Routing and Remote Access Service](../rras/routing-start-page.md)
</dt> </dl>

 

