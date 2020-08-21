---
title: Computer Object User Interface Mapping
description: The following tables list elements of the Computer object property sheets in the Active Directory Users and Computers snap-in.
ms.assetid: e2a7a42d-e854-43fc-a36b-f3031c1685a7
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Computer Object User Interface Mapping

The following tables list elements of the Computer object property sheets in the Active Directory Users and Computers snap-in.

## General Property Sheet

The following table lists the UI labels of the **General** property sheet.



| UI label                         | Active Directory Domain Services attribute | Comments                                         |
|----------------------------------|--------------------------------------------|--------------------------------------------------|
| Computer Name (pre-Windows 2000) | sAMAccountName                             |                                                  |
| DNS Name                         | dNSHostName                                |                                                  |
| Role                             | userAccountControl                         | Toggles a bit in the userAccountControl bitmask. |
| Description                      | description                                |                                                  |
| Trust Computer for delegation    | userAccountControl                         | Toggles a bit in the userAccountControl bitmask. |



 

## Location Property Sheet

The following table lists the UI labels of the **Location** property sheet.



| UI label | Active Directory Domain Services attribute |
|----------|--------------------------------------------|
| Location | location                                   |



 

## Member Of Property Sheet

The following table lists the UI labels of the **Member Of** property sheet.



| UI label          | Active Directory Domain Services attribute | Comments                                                                                                                                                                   |
|-------------------|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Member of         | memberOf                                   | Includes all of the groups in the UI list, except the primary group, which is represented in the AD through the [**primaryGroupId**](/windows/desktop/ADSchema/a-primarygroupid) attribute. |
| Set Primary Group | primaryGroupID                             | LDAP: Tied to [**primaryGroupToken**](/windows/desktop/ADSchema/a-primarygrouptoken) of the primary group.                                                                                  |



 

## Operating System Property Sheet

The following table lists the UI labels of the **Operating System** property sheet.



| UI label     | Active Directory Domain Services attribute |
|--------------|--------------------------------------------|
| Name         | operatingSystem                            |
| Version      | operatingSystemVersion                     |
| Service Pack | operatingSystemServicePack                 |



 

 

 