---
title: Windows Firewall for Windows XP with SP2
description: Microsoft Windows Firewall helps to protect computers from unsolicited network traffic.
ms.assetid: '4043a85f-ebdc-424c-acf5-9097d1472773'
keywords: ["Windows Firewall", "Windows Firewall,start page", "firewall"]
---

# Windows Firewall for Windows XP with SP2

## Purpose

Microsoft Windows Firewall helps to protect computers from unsolicited network traffic. The Windows Firewall APIs make it possible to programmatically manage the features of Windows Firewall by allowing applications to create, enable, and disable firewall exceptions.

> [!Note]  
> For Windows Vista and later, use of the [Windows Firewall with Advanced Security](windows-firewall-advanced-security-start-page.md) API is recommended.

 

## Where applicable

The Windows Firewall API is intended for situations in which a software application or setup program must operate with adjustments to the configuration of the networking environment in which it runs. For example, a service that needs to receive unsolicited traffic can use this API to create exceptions that allow the unsolicited traffic.

## Developer audience

The Windows Firewall API is designed for use by programmers using C/C++, Microsoft Visual Basic development system, Visual Basic Scripting Edition, and JScript development software. Programmers should be familiar with networking concepts such as stateful packet filtering, TCP/IP protocol concepts, and network address translation (NAT).

## Run-time requirements

The Windows Firewall API is supported on Windows XP with Service Pack 2 (SP2). (For Windows Vista and later, use of the [Windows Firewall with Advanced Security](windows-firewall-advanced-security-start-page.md) API is recommended.) For more specific information about which operating systems support a particular programming element, refer to the Requirements sections in the documentation.

## In this section



| Topic                                                  | Description                                                                                    |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [Overview](about-windows-firewall.md)<br/>      | General information about the Windows Firewall API for Windows XP with SP2.<br/>         |
| [Using](using-windows-firewall.md)<br/>         | Usage examples for Windows Firewall API for Windows XP with SP2.<br/>                    |
| [Reference](windows-firewall-reference.md)<br/> | Documentation for Windows Firewall interfaces, structures, and other code elements.<br/> |



 

 

 





