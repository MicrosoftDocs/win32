---
title: Active Directory
description: Introduces active directory technology.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1291af94-e600-42f1-93a6-07a84ca6da45'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Active Directory

Active Directory Service Interfaces (ADSI) is the primary API for directory services based on Active Directory technology. Active Directory provides the following:

<dl> <dt>

<span id="Location_transparency"></span><span id="location_transparency"></span><span id="LOCATION_TRANSPARENCY"></span>Location transparency
</dt> <dd>

Finding information about a user, group, networked service, or resource, without knowing addressing information.

</dd> <dt>

<span id="Information_on_people_and_services"></span><span id="information_on_people_and_services"></span><span id="INFORMATION_ON_PEOPLE_AND_SERVICES"></span>Information on people and services
</dt> <dd>

Storing user, group, organization, or service information in a structured hierarchical tree.

</dd> <dt>

<span id="Rich_query"></span><span id="rich_query"></span><span id="RICH_QUERY"></span>Rich query
</dt> <dd>

Locating objects of interest by querying for properties of the objects.

</dd> <dt>

<span id="High_availability"></span><span id="high_availability"></span><span id="HIGH_AVAILABILITY"></span>High availability
</dt> <dd>

Locating a replica of the directory at a location that is the most efficient for a read/write operation.

</dd> </dl>

Snap-in developers can use ADSI to gain access to objects stored in the directory as COM objects. Active Directory adds a powerful component to distributed application management by providing a way to transparently access objects on the enterprise network.

 

 




