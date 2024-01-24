---
title: Security (Windows 7 Developer Guide)
description: Windows 7 includes new and improved security features that make it easier for developers to improve, use, and manage the security of their applications.
ms.assetid: c3f19338-8ada-4ded-82a9-ca0869ad469d
ms.topic: article
ms.date: 05/31/2018
---

# Security (Windows 7 Developer Guide)

Windows 7 includes new and improved security features that make it easier for developers to improve, use, and manage the security of their applications. It comes with a variety of new security features that not only help protect against threats but also limit the damage that attackers can do if they gain access to a computer.

Enhancements to the Windows Filtering Platform allow developers to create applications that interact with the packet processing in the networking stack of the operating system. Network data can be filtered and also modified before it reaches its destination.

Also, due to changes to the Windows privilege model, system security is more manageable by both developers and their end users. New improvements make it easy to identify critical prompts to ensure that users can access the applications and features they need without compromising their systems. (See the [MSDN Security Developer Center](https://msdn.microsoft.com/security/default.aspx).)

## Windows Filtering Platform

In Windows 7, the Windows Filtering Platform has been enhanced to give developers more control over firewall functionality. The level of filtering has been increased and *ISVs* can now plug in custom protection and detection at lower levels. In addition, firewall developers can selectively turn parts of the Windows Firewall on or off.

Using Windows Filtering Platform, developers can build firewalls, intrusion detection systems, antivirus programs, network monitoring tools, and parental controls into their applications. Windows Filtering Platform integrates with and provides support for a wide variety of firewall features, including authenticated communication and dynamic firewall configuration based on applications' use of sockets API (application-based policy). Windows Filtering Platform also provides infrastructure for policy management, change notifications, network diagnostics, and stateful filtering.

The initial architecture of Windows Filtering Platform in Windows Vista provided capabilities for IP-based traffic. Other non-IP protocols--such as such as Address Resolution Protocol (ARP) and media access control (*MAC*)-layer protocols for network management and authentication--also require filtering, inspection, or logging. In Windows 7, an *NDIS* inspection layer that supports *MAC* and *ETHERNET* filtering has been provided to satisfy this need. (See [Windows Filtering Platform](../fwp/windows-filtering-platform-start-page.md).)

## User Account Control

User account control (UAC) is a security component in Windows 7 that allows developers to build applications that enable users to perform common tasks as non-administrators. Developers can reduce security risks by running applications under a standard user token, reducing the risks of mistakes or attacks.

User accounts that are members of the local *Administrators* group will run most applications as a standard user. By separating user and administrator functions while enabling productivity, UAC gives developers greater control over the level of access that users have over protected areas of an application. UAC requests credentials in a *Secure Desktop* mode, where the entire screen is protected to prevent spoofing of the user interface or the mouse. (See [User Account Control Dialog Updates](../win7appqual/user-interface---user-account-control-dialog-updates.md) and [User Account Control and WMI](../wmisdk/user-account-control-and-wmi.md).)

 

 
