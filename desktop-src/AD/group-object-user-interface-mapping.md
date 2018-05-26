---
title: Group Object User Interface Mapping
description: This topic describes the Group object property sheets in the Active Directory Users and Computers snap-in.General Property SheetMember Of Property SheetMembers Property SheetManaged By Property Sheet
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c0cd73f0-f09f-4645-966d-6149888ce482
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Group Object User Interface Mapping AD
- User Interface Mapping,Group Object AD
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Group Object User Interface Mapping

This topic describes the Group object property sheets in the Active Directory Users and Computers snap-in.

-   [General Property Sheet](#general-property-sheet)
-   [Member Of Property Sheet](#member-of-property-sheet)
-   [Members Property Sheet](#members-property-sheet)
-   [Managed By Property Sheet](#managed-by-property-sheet)

## General Property Sheet

The following table shows the UI labels of the **General** property sheet.



| UI label                      | Attribute in Active Directory Domain Services     |
|-------------------------------|---------------------------------------------------|
| Group Name (pre-Windows 2000) | [**SAM-Account-Name**](https://msdn.microsoft.com/library/ms679635) |
| Description                   | [**Description**](https://msdn.microsoft.com/library/ms675492)         |
| E-Mail                        | [**E-mail-Addresses**](https://msdn.microsoft.com/library/ms676855)           |
| Group Scope                   | [**Group-Type**](https://msdn.microsoft.com/library/ms675935)            |
| Group Type                    | [**Group-Type**](https://msdn.microsoft.com/library/ms675935)            |
| Notes                         | [**Comment**](https://msdn.microsoft.com/library/ms676199)                    |



 

## Member Of Property Sheet

The following table shows the UI labels of the **Member Of** property sheet.



| UI label  | Attribute in Active Directory Domain Services | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Member of | [**Is-Member-Of-DL**](https://msdn.microsoft.com/library/ms677099)    | Contains the distinguished names of the groups to which this group belongs. The member attribute of each of the groups in this list contains the distinguished name of this group object.The user interface does not directly modify the [**Is-Member-Of-DL**](https://msdn.microsoft.com/library/ms677099) attribute. It modifies the [**Member**](https://msdn.microsoft.com/library/ms677097) attribute on the group object of which this object is made a member of. The Active Directory server maintains the **Is-Member-Of-DL** attribute.<br/> |



 

## Members Property Sheet

The following table shows the UI labels of the **Members** property sheet.



| UI label | Attribute in Active Directory Domain Services | Description                                                           |
|----------|-----------------------------------------------|-----------------------------------------------------------------------|
| Members  | [**Member**](https://msdn.microsoft.com/library/ms677097)               | Contains the distinguished names of the members of this group object. |



 

## Managed By Property Sheet

The following table shows the UI labels of the **Managed By** property sheet.



| UI label                           | Attribute in Active Directory Domain Services                                                                                   |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Name                               | [**Managed-By**](https://msdn.microsoft.com/library/ms676857)                                                                                          |
| Manager can update membership list | None. An ACE with the "Allow - Write Members" permission is added to the account identified by **Name**.                        |
| Office                             | The [**Physical-Delivery-Office-Name**](https://msdn.microsoft.com/library/ms679117) attribute of the account identified by **Name**. |
| Street                             | The [**Street-Address**](https://msdn.microsoft.com/library/ms679882) attribute of the account identified by **Name**.                                    |
| City                               | The [**Locality-Name**](https://msdn.microsoft.com/library/ms676817) attribute of the account identified by **Name**.                                          |
| State/province                     | The [**State-Or-Province-Name**](https://msdn.microsoft.com/library/ms679880) attribute of the account identified by **Name**.                                |
| Country/region                     | The [**Country-Name**](https://msdn.microsoft.com/library/ms675432) attribute of the account identified by **Name**.                                           |
| Telephone number                   | The [**Telephone-Number**](https://msdn.microsoft.com/library/ms680027) attribute of the account identified by **Name**.                         |
| Fax number                         | The [**Facsimile-Telephone-Number**](https://msdn.microsoft.com/library/ms675675) attribute of the account identified by **Name**.      |



 

 

 





