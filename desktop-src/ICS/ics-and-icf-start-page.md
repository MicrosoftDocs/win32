---
title: Internet Connection Sharing and Internet Connection Firewall
description: Internet Connection Sharing (ICS) makes it possible for home and small office users to share a single connection to the Internet.
ms.assetid: a9f46f63-a905-48c9-bfbe-a6cec5b6edcf
keywords:
- Internet Connection Sharing and Internet Connection Firewall ICS/ICF
- Internet Connection Sharing and Internet Connection Firewall ICS/ICF , start page
- sharing
- firewall
- ICS ICS/ICF
- ICS ICS/ICF , start page
- ICF
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Internet Connection Sharing and Internet Connection Firewall

## Purpose

Internet Connection Sharing (ICS) makes it possible for home and small office users to share a single connection to the Internet. The Internet Connection Firewall (ICF) protects connections on which it is running from unsolicited network traffic. The ICS/ICF API makes it possible to programmatically manage the features of ICS/ICF, making it possible to create, enable, and disable ICS or ICF port-mappings on a network connection.

## Where applicable

The ICS/ICF API is intended for situations in which a software application or setup program needs to make adjustments to the configuration of the home networking environment in which it runs. For example, a service that is connected to the Internet through a local Network Address Translator (NAT) and that needs to receive unsolicited traffic can create port mappings on that NAT through the NAT traversal API.

Another example would be: An application that provides advanced firewall or NAT capabilities can use the ICS/ICF API to disable ICS on specific connections with a user's permission.

ICS is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. ICF will be altered or unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).

## Developer audience

The ICS/ICF API is designed for use by programmers using C/C++, Microsoft Visual Basic development system, Visual Basic Scripting Edition, and JScript development software. Programmers should be familiar with networking concepts such as stateful packet filtering and network address translation (NAT).

## Run-time requirements

The ICS/ICF API is supported on Windows XP.

## In this section



| Topic                                                                                              | Description                                                                                                                                |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [Overview](displaying-all-properties.md)<br/>                                               | General information about Internet Connection Sharing and Internet Connection Firewall.<br/>                                         |
| [Reference](internet-connection-sharing-and-internet-connection-firewall-reference.md)<br/> | Documentation for Internet Connection Sharing and Internet Connection Firewall interfaces, structures, and other code elements.<br/> |
| [Samples](using-internet-connection-sharing-and-internet-connection-firewall.md)<br/>       | Sample code that demonstrates how to use Internet Connection Sharing and Internet Connection Firewall interfaces.<br/>               |



 

## Related topics

<dl> <dt>

[Routing and Remote Access Service](https://msdn.microsoft.com/library/windows/desktop/bb545679)
</dt> <dt>

[Windows Firewall](windows-firewall-start-page.md)
</dt> </dl>

 

 





