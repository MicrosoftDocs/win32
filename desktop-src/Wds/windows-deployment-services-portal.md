---
title: Windows Deployment Services
description: Deploy Windows operating systems. Set up new clients with a network-based installation without requiring that administrators visit each computer or install directly from CD or DVD media.
ms.assetid: 790abc27-03cc-4f93-bf04-a4eb37e614bb
keywords:
- Windows Deployment Services Windows Deployment Services
- Windows Deployment Services Windows Deployment Services , home page
- deployment services Windows Deployment Services
- WDS Windows Deployment Services See Windows Deployment Services
- Remote Installation Services Windows Deployment Services See Windows Deployment Services
- RIS Windows Deployment Services See Windows Deployment Services
ms.topic: article
ms.date: 05/31/2018
---

# Windows Deployment Services

## Purpose

Windows Deployment Services (WDS) is the revised version of Remote Installation Services (RIS). WDS enables the deployment of Windows operating systems. You can use WDS to set up new clients with a network-based installation without requiring that administrators visit each computer or install directly from CD or DVD media.

## Developer audience

The primary developer audience of the WDS API is for groups that develop custom tools and processes for IT and other computer administration groups. In environments where the standard Windows Deployment Services (WDS) solution cannot be used, the WDS API enables programmatic access to some WDS components.

Original Equipment Manufacturers (OEMs), system builders, and corporate IT professionals looking for information on how to deploy Windows onto new computers, should see the information about the standard Windows Deployment Services (WDS) solution in the [Windows Deployment Services Update Step-by-Step Guide](/previous-versions/windows/it-pro/windows-vista/cc766320(v=ws.10)) and the [Windows Automated Installation Kit (WAIK)](https://www.microsoft.com/download/details.aspx?id=10333).

## Run-time requirements

WDS is available as an add-on for Windows Server 2003 with Service Pack 1 (SP1) and is included in the operating system starting with Windows Server 2003 with Service Pack 2 (SP2) and Windows Server 2008. The WDS PXE Server API requires the WDS server role on the server to implement custom PXE providers. The WDS Client API requires the Microsoft Windows Preinstallation Environment (Windows PE 2.0) phase of setup processing. A RAMDISK bootable image of Windows PE 2.0 in the .WIM format must be downloaded as part of the network boot process to implement custom WDS clients.

## In this section



| Topic                                                                                                 | Description                                                                    |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [About the Windows Deployment Services API](about-the-windows-deployment-services-api.md)<br/> | General information about the WDS Server API and WDS Client API.<br/>    |
| [Windows Deployment Services Reference](windows-deployment-services-reference.md)<br/>         | Describes the Windows Deployment Services functions and structures.<br/> |



 

 

