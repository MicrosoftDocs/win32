---
description: Removal of UDDI Services from Server Operating System
ms.assetid: 5ebc8c4c-acee-4658-8d36-30fbb17b1ef1
title: Removal of UDDI Services from Server Operating System
ms.topic: article
ms.date: 05/31/2018
---

# Removal of UDDI Services from Server Operating System

## Affected Platform

**Servers** - Windows Server 2008 R2  



## Feature Impact

**Severity** - Medium  
**Frequency** - Low  

## Description

Microsoft has removed the UDDI (Universal Description, Discovery, and Integration) Services server role from Windows Server 2008 R2. Future releases of UDDI Services will be part of the Microsoft BizTalk product. This product realignment and consolidation positions Microsoft to better serve the services-oriented architecture (SOA) market.

The first post-Windows Server 2008 release of UDDI Services will be UDDI v3.0 standards compliant. It will ship as part of the BizTalk Server 2009 release. To meet our commitment to provide a satisfactory user experience, we will offer a UDDI Services v3 installation package for Windows Server 2008 R2.

## Manifestation

The presence of previous versions of UDDI Services components on the system blocks an upgrade to Windows Server 2008 R2.

## Mitigation of Impact

Users who have deployed a UDDI Services site from Windows Server 2003 or Windows Server 2008 can choose not to upgrade the servers running the UDDI Services to Windows Server 2008 R2. They can also move the UDDI Services to dedicated Windows Server 2003 or Windows Server 2008 boxes if they have to upgrade the current UDDI Services boxes.

## Solution

The recommended solution is to deploy UDDI Services v3.0 from BizTalk Server 2009 onto a Windows Server 2008 R2 machine, and then to migrate the old site to the new site. UDDI Services v3.0 provides backward compatibility with UDDI Services 2.0, so any applications that are using UDDI Services will be unaffected.

To do this, follow these steps:

1.  Set up a new UDDI Services v3.0 site on a machine already loaded with Windows Server 2008 R2. (Note: In a distributed setup, a UDDI v3.0 site can consist of more than one Windows Server 2008 R2 machines.)
2.  Use the UDDI data migration tool to migrate the data from the old UDDI Services database to the new database.
3.  Back up the old UDDI Services database to ensure rollback capability.
4.  Uninstall the old UDDI Services software and then upgrade those boxes to Windows Server 2008 R2.

## Links to Other Resources

-   [Microsoft UDDI Services website](https://msdn.microsoft.com/biztalk/dd789428.aspx)
-   [UDDI specifications](http://uddi.xml.org/specification)
-   [UDDI Services v3.0 download for Windows Server 2008 R2](https://www.microsoft.com/downloads/details.aspx?FamilyID=e4761835-70f0-4e8d-96c5-64818d54e06e)

 

 



