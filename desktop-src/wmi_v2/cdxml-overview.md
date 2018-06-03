---
title: CDXML definition and terms
description: This topic defines CDXML and its terms and lists resources for further reading.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 98514EC3-4D88-4B26-881F-01DD3DDFE996
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CDXML definition and terms

This topic defines CDXML and its terms and lists resources for further reading.

## What is CDXML?

A cmdlet definition XML, or CDXML, file defines the mapping between PowerShell cmdlets and CIM class operations or methods. PowerShell cmdlet developers use CDXML files to define cmdlets that call a CIM Object Manager (CIMOM) server (such as WMI in Windows) to manage the server. Cmdlets defined by using CDXML communicate with remote CIM servers by using the WsMan protocol (implemented by the WinRM service in Windows). This enables management of end-points that don't have PowerShell installed on them; for example, a computer running Windows Server with PowerShell remoting disabled, or a computer that is running on server software other than Windows Server; for example, a CIM server like the [Open Management Infrastructure (OMI)](http://go.microsoft.com/fwlink/p/?linkid=257489).

## CDXML glossary

This section lists the various terms and their definitions that are commonly used when using CDXML.



| Terms        | Description                                                                                                                                                                                                                                                                                                                            |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PowerShell   | A task automation framework consisting of a command-line shell and associated scripting language built on top of, and integrated with, the .NET Framework.                                                                                                                                                                             |
| cmdlet       | A single-feature command that manipulates objects in PowerShell. The names of cmdlets follow a verb-noun format with a predefined set of recommended common verbs.                                                                                                                                                                     |
| Verb         | The first element of the cmdlet name separated with a hyphen (-) from the second element (the noun).                                                                                                                                                                                                                                   |
| Noun         | The second element of the cmdlet name that represents the entity to take action (the verb) against.                                                                                                                                                                                                                                    |
| WMI          | [Windows Management Infrastructure](windows-management-infrastructure.md) (WMI) is the infrastructure for managing Windows operating system resources. WMI implements the DMTF management standards, CIM and WS-Man. WMI is a Microsoft implementation of a CIM Object Manager (CIMOM).                                               |
| CIM          | [Common Information Model](https://msdn.microsoft.com/library/aa389234) (CIM) is the DMTF standard \[DSP0004\] for describing the structure and behavior of the managed resources such as storage, network, or software components. Declarations for CIM resources are encoded in one of two languages: Management Object Framework (MOF) or CIM-XML. |
| CIM provider | An executable that can return or set information about a given managed resource object, as described in \[DMTF-DSP0004\].                                                                                                                                                                                                              |
| WQL query    | The [WMI Query Language](https://msdn.microsoft.com/library/aa394606) (WQL) is a subset of the ANSI Structured Query Language (ANSI SQL) that is used by WMI to query for managed resources.                                                                                                                                                                   |
| WS-Man/WinRM | [Windows Remote Management](https://msdn.microsoft.com/library/aa384426) (WinRM) is the Microsoft implementation of WS-Management (WS-Man) protocol, a standard Simple Object Access Protocol (SOAP)-based, firewall-friendly protocol that allows hardware and operating systems, from different vendors, to interoperate.                                           |



 

The following terms are defined in the [Windows Protocols Master Glossary](http://go.microsoft.com/fwlink/p/?linkid=257493).

-   Common Information Model (CIM)
-   Common Information Model (CIM) class
-   Common Information Model (CIM) instance
-   Common Information Model (CIM) method
-   Common Information Model (CIM) namespace
-   Common Information Model (CIM) object
-   Common Information Model (CIM) path
-   Common Information Model (CIM) property
-   Common Information Model (CIM) relative path

## CDXML resources

The following topics define and illustrate many of the technologies used by and associated with CDXML.

-   [Getting Started with Windows PowerShell](http://go.microsoft.com/fwlink/p/?linkid=257852)
-   [Windows PowerShell SDK](http://go.microsoft.com/fwlink/p/?linkid=257853)
-   [WMI Glossary](http://go.microsoft.com/fwlink/p/?linkid=257800)
-   [Querying with WQL](http://go.microsoft.com/fwlink/p/?linkid=257801)
-   [Windows Protocols Master Glossary](http://go.microsoft.com/fwlink/p/?linkid=257806)
-   [DMTF Generic CIM Operations Specification DSP0223](http://dmtf.org/sites/default/files/standards/documents/DSP0223_1.0.0_1.pdf)

 

 




