---
description: .
ms.assetid: 94ac6a91-1e00-45f3-9374-3ac48ac63765
title: Remote Desktop Services (Windows 7 and Windows Server 2008 R2 Application Quality Cookbook)
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Services (Windows 7 and Windows Server 2008 R2 Application Quality Cookbook)

## Affected Platforms

**Servers** – Windows Server 2008 \| Windows Server 2008 R2  

## Description

Remote Desktop Services (formerly known as Terminal Services) allows multiple concurrent users to access Windows Server in order to provide application and data hosting services using Microsoft "Presentation Virtualization" technology.

While most 32-bit and 64-bit applications run as is on Windows Remote Desktop Services, several others do not perform as expected due to the difference in the platform (multi-user environment, concurrent access by multiple users, and so on).

For further information regarding application quality, please read the *Application Readiness for Terminal Services* white paper. Visit the Remote Desktop Services product page and the TS TechNet websites learn more about Remote Desktop Services. To learn more about developing applications for Remote Desktop Services, review the *Terminal Services Programming Guidelines*. (These resources may not be available in some languages and countries/regions.)

## Manifestation of Impacts and Their Mitigations

Three changes in Windows 7 affect applications on Remote Desktop Services:

-   Windows Server 2008 R2 is 64-bit only
-   Per-session IP Virtualization
-   MSI-based deployments – User-specific keys

**64-bit Only Windows Server 2008 R2**

Applications written for 32-bit server will run in WoW mode and not natively on the Windows Server 2008 R2 or, hence, on Remote Desktop Services. See the Windows 7 64-Bit Only topic for details.

*Mitigations for 64-bit only Windows Server 2008 R2*

Most applications written for 32-bit will continue to work as normal in WoW mode. Any new applications written for Windows 7 Remote Desktop Services should be developed and tested for deployment on 64-bit platforms.

**IP Virtualization**

Remote Desktop IP Virtualization allows the user to assign IP addresses to remote desktop connections on a per-session or per-program basis:

-   If you assign IP addresses on a per-session basis, all of the applications will use the session IP address.
-   If you assign IP addresses on a per-program basis, only the specified applications will use the session IP address and the remaining applications in the session will not be affected.
-   If you assign IP addresses for multiple programs, they will share a session IP address.
-   If you have more than one network adapter on the computer, you must also choose one of them for Remote Desktop IP Virtualization.

*Mitigations for IP Virtualization*

Some programs require a unique IP address for each instance of the application. Prior to Windows Server 2008 R2, every session on a remote desktop server shared the same IP address, resulting in compatibility issues for these applications. Remote Desktop IP Virtualization allows these applications to run on a Remote Desktop Server.

**MSI-based Deployments**

Microsoft Installer RDS Compatibility is a new feature included with Remote Desktop Services in Windows Server 2008 R2. With Remote Desktop Services in Windows Server 2008 R2, per-user application installations are queued by the Remote Desktop Server and then handled by the Microsoft Installer.

In Windows Server 2008 R2, you can install a program on the Remote Desktop Server just as you would install the program on a local desktop. Ensure, however, that you install the program for all users and install all components of the program locally on the Remote Desktop Server.

*Mitigations for MSI based Deployments*

Prior to the Windows Server 2008 R2 version of Remote Desktop Services, Windows supported only one Windows Installer installation at a time. For applications that required per-user configurations, such as Microsoft Office Word, an administrator needed to pre-install the application, and application developers needed to test these applications on both the remote desktop client and the Remote Desktop Session Host. Windows Installer RDS Compatibility feature allows identifying and installing missing per-user configurations for multiple users simultaneously and makes the application installation experience on Remote Desktop Server similar to that on a local desktop.

**Windows Server 2008 R2 with the [Remote Desktop Services](../termserv/terminal-services-portal.md) role enabled:** Not supported. A multiple package installation using the [MsiEmbeddedChainer table](../msi/msiembeddedchainer-table.md) fails if the [Remote Desktop Services](../termserv/terminal-services-portal.md) role is enabled.

## Links to Other Resources

-   [Terminal Services Programming Guidelines](../termserv/terminal-services-programming-guidelines.md)
-   [Terminal Services product home page](https://www.microsoft.com/windowsserver2008/en/us/rds-product-home.aspx)
-   [Application Readiness for Terminal Services white paper](/collaborate/connect-redirect)

> [!Note]  
> These resources may not be available in some languages and countries/regions.

 

 

 
