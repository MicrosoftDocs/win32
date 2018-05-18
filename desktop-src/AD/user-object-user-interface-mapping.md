---
title: User Object User Interface Mapping
description: The following tables identify the property pages supplied by the Active Directory Users and Computers snap-in.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'f309c139-c957-40c4-b369-f527aa87157c'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["User Object User Interface Mapping AD", "User Interface Mapping AD , User Object"]
---

# User Object User Interface Mapping

The following tables identify the property pages supplied by the Active Directory Users and Computers snap-in. Each table identifies the user interface elements of the property page and the attribute associated with that user interface element. Because the property pages that are displayed by the Active Directory Users and Computers snap-in can be extended, it is not possible to provide this data for all of the pages displayed in a property sheet.

## General Property Page

The following table lists UI labels of the **General** property page.



| UI label         | Attribute in Active Directory Domain Services                           |
|------------------|-------------------------------------------------------------------------|
| First Name       | [**givenName**](https://msdn.microsoft.com/library/ms675719)                                   |
| Last Name        | [**sn**](https://msdn.microsoft.com/library/ms679872)                                                 |
| Initials         | [**initials**](https://msdn.microsoft.com/library/ms676202)                                     |
| Display Name     | [**displayName**](https://msdn.microsoft.com/library/ms675514)                               |
| Description      | [**description**](https://msdn.microsoft.com/library/ms675492)                               |
| Office           | [**physicalDeliveryOfficeName**](https://msdn.microsoft.com/library/ms679117) |
| Telephone Number | [**telephoneNumber**](https://msdn.microsoft.com/library/ms680027)                       |
| Telephone: Other | [**otherTelephone**](https://msdn.microsoft.com/library/ms679094)                         |
| E-Mail           | [**E-mail-Addresses**](https://msdn.microsoft.com/library/ms676855)                                 |
| Web Page         | [**wWWHomePage**](https://msdn.microsoft.com/library/ms680927)                               |
| Web Page: Other  | [**url**](https://msdn.microsoft.com/library/ms680541)                                               |



 

## Account Property Page

The following table lists the UI labels of the **Account** property page.



| UI label                                | Attribute in Active Directory Domain Services                                                   | Comment                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UserLogon Name                          | [**userPrincipalName**](https://msdn.microsoft.com/library/ms680857)                                           | This field is taken from everything in the [**userPrincipalName**](https://msdn.microsoft.com/library/ms680857) attribute that precedes the last '@' character. The last '@' character and everything after it is placed in the suffix combo box.                                                                                                                                                      |
| User logon name (pre-Windows 2000)      | [**sAMAccountname**](https://msdn.microsoft.com/library/ms679635)                                                 | No comment.                                                                                                                                                                                                                                                                                                                                                                             |
| Logon Hours                             | [**logonHours**](https://msdn.microsoft.com/library/ms676846)                                                         | No comment.                                                                                                                                                                                                                                                                                                                                                                             |
| Log On To                               | [**logonWorkstation**](https://msdn.microsoft.com/library/ms676847)                                             | No comment.                                                                                                                                                                                                                                                                                                                                                                             |
| Account is locked out                   | [**lockoutTime**](https://msdn.microsoft.com/library/ms676843) and [**lockoutDuration**](https://msdn.microsoft.com/library/ms676840) | If the [**lockoutTime**](https://msdn.microsoft.com/library/ms676843) attribute is not zero, the [**lockoutDuration**](https://msdn.microsoft.com/library/ms676840) attribute is added to **lockoutTime** and compared to the current date and time to determine if the account is locked out.                                                                                                                                |
| User must change password at next logon | [**pwdLastSet**](https://msdn.microsoft.com/library/ms679430)                                                         | No comment.                                                                                                                                                                                                                                                                                                                                                                             |
| User cannot change password             | N/A                                                                                             | This is the Change Password control in the ACL.                                                                                                                                                                                                                                                                                                                                         |
| Other Account Options                   | [**userAccountControl**](https://msdn.microsoft.com/library/ms680832)                                         | The remaining items in Account Options toggle bits in the [**userAccountControl**](https://msdn.microsoft.com/library/ms680832) attribute bitmask (flags in a DWORD).                                                                                                                                                                                                                                 |
| Account Expires                         | [**accountExpires**](https://msdn.microsoft.com/library/ms675098)                                                 | The **Account Expires** control displays the date that the account will expire at the end of. The [**accountExpires**](https://msdn.microsoft.com/library/ms675098) attribute is stored as the date that the account expires on. Because of this, the date displayed in the **Account Expires** control will be displayed as one day earlier than the date contained in the **accountExpires** attribute. |



 

## Address Property Page

The following table lists the UI labels of the **Address** property page.



| UI label        | Attribute in Active Directory Domain Services                                                 | Comment                                                   |
|-----------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Street          | [**streetAddress**](https://msdn.microsoft.com/library/ms679886)                                                 | No comment.                                               |
| P.O.Box         | [**postOfficeBox**](https://msdn.microsoft.com/library/ms679367)                                                 | No comment.                                               |
| City            | [**l**](https://msdn.microsoft.com/library/ms676817)                                                                         | The **l** attribute name is a lowercase "L" as in Locale. |
| State/Province  | [**st**](https://msdn.microsoft.com/library/ms679880)                                                                       | No comment.                                               |
| Zip/Postal Code | [**postalCode**](https://msdn.microsoft.com/library/ms679366)                                                       | No comment.                                               |
| Country/Region  | [**c**](https://msdn.microsoft.com/library/ms675432), [**co**](https://msdn.microsoft.com/library/ms675450), and [**countryCode**](https://msdn.microsoft.com/library/ms675466) | No comment.                                               |



 

## Member Of Property Page

The following table lists UI labels of the **Member Of** property page.



| UI label          | Attribute in Active Directory Domain Services   | Comment                                                                                                                                                                    |
|-------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Member of         | [**memberOf**](https://msdn.microsoft.com/library/ms677099)             | Includes all of the groups in the UI list, except the primary group, which is represented in the AD through the [**primaryGroupId**](https://msdn.microsoft.com/library/ms679375) attribute. |
| Set Primary Group | [**primaryGroupID**](https://msdn.microsoft.com/library/ms679375) | LDAP: Tied to [**primaryGroupToken**](https://msdn.microsoft.com/library/ms679376) of the primary group.                                                                                  |



 

## Organization Property Page

The following table shows the UI labels of the **Organization** property page.



| UI label       | Attribute in Active Directory Domain Services | Comment     |
|----------------|-----------------------------------------------|-------------|
| Title          | [**title**](https://msdn.microsoft.com/library/ms680037)                 | No comment. |
| Department     | [**department**](https://msdn.microsoft.com/library/ms675490)       | No comment. |
| Company        | [**company**](https://msdn.microsoft.com/library/ms675457)             | No comment. |
| Manager:Name   | [**manager**](https://msdn.microsoft.com/library/ms676859)             | No comment. |
| Direct Reports | [**directReports**](https://msdn.microsoft.com/library/ms675513) | No comment. |



 

## Profile Property Page

The following table lists the UI labels of the **Profile** property page.



| UI label                | Attribute in Active Directory Domain Services | Comment                                                                                                                 |
|-------------------------|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Profile Path            | [**profilePath**](https://msdn.microsoft.com/library/ms679422)     | No comment.                                                                                                             |
| Logon Script            | [**scriptPath**](https://msdn.microsoft.com/library/ms679656)       | No comment.                                                                                                             |
| Home Folder: Local Path | [**homeDirectory**](https://msdn.microsoft.com/library/ms676190) | If **Local path** is selected, the local path is stored in the [**homeDirectory**](https://msdn.microsoft.com/library/ms676190) attribute. |
| Home Folder: Connect    | [**homeDrive**](https://msdn.microsoft.com/library/ms676191)         | If **Connect** is selected, the mapped drive is stored in the [**homeDrive**](https://msdn.microsoft.com/library/ms676191) attribute.          |
| Home Folder: To         | [**homeDirectory**](https://msdn.microsoft.com/library/ms676190) | If **Connect** is selected, the path is stored in the [**homeDirectory**](https://msdn.microsoft.com/library/ms676190) attribute.          |



 

## Telephones Property Page

The following table lists the UI elements of the **Telephones** property page and their corresponding Active Directory attributes.



| UI label        | Attribute in Active Directory Domain Services                                 |
|-----------------|-------------------------------------------------------------------------------|
| Home            | [**homePhone**](https://msdn.microsoft.com/library/ms676192)                                         |
| Home: Other     | [**otherHomePhone**](https://msdn.microsoft.com/library/ms679088)                               |
| Pager           | [**pager**](https://msdn.microsoft.com/library/ms679102)                                                 |
| Pager: Other    | [**otherPager**](https://msdn.microsoft.com/library/ms679093)                                       |
| Mobile          | [**mobile**](https://msdn.microsoft.com/library/ms677119)                                               |
| Mobile: Other   | [**otherMobile**](https://msdn.microsoft.com/library/ms679092)                                     |
| Fax             | [**facsimileTelephoneNumber**](https://msdn.microsoft.com/library/ms675675)           |
| Fax: Other      | [**otherFacsimileTelephoneNumber**](https://msdn.microsoft.com/library/ms679087) |
| IP phone        | [**ipPhone**](https://msdn.microsoft.com/library/ms676213)                                             |
| IP phone: Other | [**otherIpPhone**](https://msdn.microsoft.com/library/ms679089)                                   |
| Notes           | [**info**](https://msdn.microsoft.com/library/ms676199)                                                   |



 

## Environment, Sessions, Remote Control, and Terminal Services Profile Property Pages

The **Environment**, **Sessions**, **Remote Control**, and **Terminal Services Profile** pages are supplied for a user object to support terminal services. The UI elements for these pages do not correspond to individual attributes. Instead, the settings are stored in private data within Active Directory Domain Services. The terminal services settings can be accessed with the [**IADsTsUserEx**](https://msdn.microsoft.com/library/aa380823) interface.

 

 




