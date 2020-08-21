---
title: Group Object User Interface Mapping
description: This topic describes the Group object property sheets in the Active Directory Users and Computers snap-in.General Property SheetMember Of Property SheetMembers Property SheetManaged By Property Sheet
ms.assetid: c0cd73f0-f09f-4645-966d-6149888ce482
ms.tgt_platform: multiple
keywords:
- Group Object User Interface Mapping AD
- User Interface Mapping,Group Object AD
ms.topic: article
ms.date: 05/31/2018
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
| Group Name (pre-Windows 2000) | [**SAM-Account-Name**](/windows/desktop/ADSchema/a-samaccountname) |
| Description                   | [**Description**](/windows/desktop/ADSchema/a-description)         |
| E-Mail                        | [**E-mail-Addresses**](/windows/desktop/ADSchema/a-mail)           |
| Group Scope                   | [**Group-Type**](/windows/desktop/ADSchema/a-grouptype)            |
| Group Type                    | [**Group-Type**](/windows/desktop/ADSchema/a-grouptype)            |
| Notes                         | [**Comment**](/windows/desktop/ADSchema/a-info)                    |



 

## Member Of Property Sheet

The following table shows the UI labels of the **Member Of** property sheet.



| UI label  | Attribute in Active Directory Domain Services | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Member of | [**Is-Member-Of-DL**](/windows/desktop/ADSchema/a-memberof)    | Contains the distinguished names of the groups to which this group belongs. The member attribute of each of the groups in this list contains the distinguished name of this group object.The user interface does not directly modify the [**Is-Member-Of-DL**](/windows/desktop/ADSchema/a-memberof) attribute. It modifies the [**Member**](/windows/desktop/ADSchema/a-member) attribute on the group object of which this object is made a member of. The Active Directory server maintains the **Is-Member-Of-DL** attribute.<br/> |



 

## Members Property Sheet

The following table shows the UI labels of the **Members** property sheet.



| UI label | Attribute in Active Directory Domain Services | Description                                                           |
|----------|-----------------------------------------------|-----------------------------------------------------------------------|
| Members  | [**Member**](/windows/desktop/ADSchema/a-member)               | Contains the distinguished names of the members of this group object. |



 

## Managed By Property Sheet

The following table shows the UI labels of the **Managed By** property sheet.



| UI label                           | Attribute in Active Directory Domain Services                                                                                   |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Name                               | [**Managed-By**](/windows/desktop/ADSchema/a-managedby)                                                                                          |
| Manager can update membership list | None. An ACE with the "Allow - Write Members" permission is added to the account identified by **Name**.                        |
| Office                             | The [**Physical-Delivery-Office-Name**](/windows/desktop/ADSchema/a-physicaldeliveryofficename) attribute of the account identified by **Name**. |
| Street                             | The [**Street-Address**](/windows/desktop/ADSchema/a-street) attribute of the account identified by **Name**.                                    |
| City                               | The [**Locality-Name**](/windows/desktop/ADSchema/a-l) attribute of the account identified by **Name**.                                          |
| State/province                     | The [**State-Or-Province-Name**](/windows/desktop/ADSchema/a-st) attribute of the account identified by **Name**.                                |
| Country/region                     | The [**Country-Name**](/windows/desktop/ADSchema/a-c) attribute of the account identified by **Name**.                                           |
| Telephone number                   | The [**Telephone-Number**](/windows/desktop/ADSchema/a-telephonenumber) attribute of the account identified by **Name**.                         |
| Fax number                         | The [**Facsimile-Telephone-Number**](/windows/desktop/ADSchema/a-facsimiletelephonenumber) attribute of the account identified by **Name**.      |



 

 

