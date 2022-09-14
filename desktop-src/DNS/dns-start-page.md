---
title: Domain Name System
description: Domain Name System (DNS), a locator service in Microsoft Windows, is an industry-standard protocol that locates computers on an IP-based network.
ms.assetid: 4d1c2151-3995-4e7f-881b-4466bd7b7bb7
keywords:
- DNS
- DNS, (See Domain Name System)
- Domain Name System
- Domain Name System, start page
ms.topic: article
ms.date: 05/31/2018
---

# Domain Name System

## Purpose

Domain Name System (DNS), a locator service in Microsoft Windows, is an industry-standard protocol that locates computers on an IP-based network. IP networks, such as the Internet and Windows networks, rely on number-based addresses to process data. Users however, can more easily remember name addresses, so it is necessary to translate user-friendly names (such as `www.microsoft.com`) into addresses that the network can recognize (such as 207.46.131.137).

## Where applicable

Windows and Active Directory use DNS. DNS is the primary locator service for the Internet and Active Directory, and therefore, DNS is considered a base service for Windows and Active Directory.

## Developer audience

Windows provides functions that enable application programmers to use DNS, such as programmatic DNS query, record compare, and name lookup.

Programmable DNS components are designed for use by C/C++ programmers. Familiarity with networking and DNS is required. Programmers should be familiar with the IP-protocol suite, as well as the DNS protocol and DNS operations.

## Run-time requirements

DNS is used on all IP networks that require an Internet-compatible locator service. However, the DNS API requires Windows 2000 or later.

## In this section



| Topic                                                             | Description                                                                          |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [DNS Standards Documents](dns-standards-documents.md)<br/> | Links to public DNS standards documents.<br/>                                  |
| [About DNS](about-dns.md)<br/>                             | General information about DNS.<br/>                                            |
| [DNS Reference](dns-reference.md)<br/>                     | Reference documentation for DNS.<br/>                                          |
| [DNS WMI Provider](dns-wmi-provider.md)<br/>               | General information and reference documentation for the DNS WMI provider.<br/> |
| [Glossary](glossary-gly.md)<br/>                           | Glossary of DNS terms and definitions.<br/>                                    |



 

## Related topics

<dl> <dt>

[DHCP](/previous-versions/windows/desktop/dhcp/dhcp-start-page)
</dt> <dt>

[Internet Protocol Helper](/windows/desktop/IpHlp/ip-helper-start-page)
</dt> <dt>

[Directory Services](https://msdn.microsoft.com/library/Dd425378(v=VS.85).aspx)
</dt> </dl>

 

