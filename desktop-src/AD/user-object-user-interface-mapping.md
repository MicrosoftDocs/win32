---
title: User Object User Interface Mapping
description: The following tables identify the property pages supplied by the Active Directory Users and Computers snap-in.
ms.assetid: f309c139-c957-40c4-b369-f527aa87157c
ms.tgt_platform: multiple
keywords:
- User Object User Interface Mapping AD
- User Interface Mapping AD , User Object
ms.topic: article
ms.date: 05/31/2018
---

# User Object User Interface Mapping

The following tables identify the property pages supplied by the Active Directory Users and Computers snap-in. Each table identifies the user interface elements of the property page and the attribute associated with that user interface element. Because the property pages that are displayed by the Active Directory Users and Computers snap-in can be extended, it is not possible to provide this data for all of the pages displayed in a property sheet.

## General Property Page

The following table lists UI labels of the **General** property page.



| UI label         | Attribute in Active Directory Domain Services                           |
|------------------|-------------------------------------------------------------------------|
| First Name       | [**givenName**](/windows/desktop/ADSchema/a-givenname)                                   |
| Last Name        | [**sn**](/windows/desktop/ADSchema/a-sn)                                                 |
| Initials         | [**initials**](/windows/desktop/ADSchema/a-initials)                                     |
| Display Name     | [**displayName**](/windows/desktop/ADSchema/a-displayname)                               |
| Description      | [**description**](/windows/desktop/ADSchema/a-description)                               |
| Office           | [**physicalDeliveryOfficeName**](/windows/desktop/ADSchema/a-physicaldeliveryofficename) |
| Telephone Number | [**telephoneNumber**](/windows/desktop/ADSchema/a-telephonenumber)                       |
| Telephone: Other | [**otherTelephone**](/windows/desktop/ADSchema/a-othertelephone)                         |
| E-Mail           | [**E-mail-Addresses**](/windows/desktop/ADSchema/a-mail)                                 |
| Web Page         | [**wWWHomePage**](/windows/desktop/ADSchema/a-wwwhomepage)                               |
| Web Page: Other  | [**url**](/windows/desktop/ADSchema/a-url)                                               |



 

## Account Property Page

The following table lists the UI labels of the **Account** property page.



| UI label                                | Attribute in Active Directory Domain Services                                                   | Comment                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UserLogon Name                          | [**userPrincipalName**](/windows/desktop/ADSchema/a-userprincipalname)                                           | This field is taken from everything in the [**userPrincipalName**](/windows/desktop/ADSchema/a-userprincipalname) attribute that precedes the last '@' character. The last '@' character and everything after it is placed in the suffix combo box.                                                                                                                                                      |
| User logon name (pre-Windows 2000)      | [**sAMAccountname**](/windows/desktop/ADSchema/a-samaccountname)                                                 | No comment.                                                                                                                                                                                                                                                                                                                                                                             |
| Logon Hours                             | [**logonHours**](/windows/desktop/ADSchema/a-logonhours)                                                         | No comment.                                                                                                                                                                                                                                                                                                                                                                             |
| Log On To                               | [**logonWorkstation**](/windows/desktop/ADSchema/a-logonworkstation)                                             | No comment.                                                                                                                                                                                                                                                                                                                                                                             |
| Account is locked out                   | [**lockoutTime**](/windows/desktop/ADSchema/a-lockouttime) and [**lockoutDuration**](/windows/desktop/ADSchema/a-lockoutduration) | If the [**lockoutTime**](/windows/desktop/ADSchema/a-lockouttime) attribute is not zero, the [**lockoutDuration**](/windows/desktop/ADSchema/a-lockoutduration) attribute is added to **lockoutTime** and compared to the current date and time to determine if the account is locked out.                                                                                                                                |
| User must change password at next logon | [**pwdLastSet**](/windows/desktop/ADSchema/a-pwdlastset)                                                         | No comment.                                                                                                                                                                                                                                                                                                                                                                             |
| User cannot change password             | N/A                                                                                             | This is the Change Password control in the ACL.                                                                                                                                                                                                                                                                                                                                         |
| Other Account Options                   | [**userAccountControl**](/windows/desktop/ADSchema/a-useraccountcontrol)                                         | The remaining items in Account Options toggle bits in the [**userAccountControl**](/windows/desktop/ADSchema/a-useraccountcontrol) attribute bitmask (flags in a DWORD).                                                                                                                                                                                                                                 |
| Account Expires                         | [**accountExpires**](/windows/desktop/ADSchema/a-accountexpires)                                                 | The **Account Expires** control displays the date that the account will expire at the end of. The [**accountExpires**](/windows/desktop/ADSchema/a-accountexpires) attribute is stored as the date that the account expires on. Because of this, the date displayed in the **Account Expires** control will be displayed as one day earlier than the date contained in the **accountExpires** attribute. |



 

## Address Property Page

The following table lists the UI labels of the **Address** property page.



| UI label        | Attribute in Active Directory Domain Services                                                 | Comment                                                   |
|-----------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Street          | [**streetAddress**](/windows/desktop/ADSchema/a-streetaddress)                                                 | No comment.                                               |
| P.O.Box         | [**postOfficeBox**](/windows/desktop/ADSchema/a-postofficebox)                                                 | No comment.                                               |
| City            | [**l**](/windows/desktop/ADSchema/a-l)                                                                         | The **l** attribute name is a lowercase "L" as in Locale. |
| State/Province  | [**st**](/windows/desktop/ADSchema/a-st)                                                                       | No comment.                                               |
| Zip/Postal Code | [**postalCode**](/windows/desktop/ADSchema/a-postalcode)                                                       | No comment.                                               |
| Country/Region  | [**c**](/windows/desktop/ADSchema/a-c), [**co**](/windows/desktop/ADSchema/a-co), and [**countryCode**](/windows/desktop/ADSchema/a-countrycode) | No comment.                                               |



 

## Member Of Property Page

The following table lists UI labels of the **Member Of** property page.



| UI label          | Attribute in Active Directory Domain Services   | Comment                                                                                                                                                                    |
|-------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Member of         | [**memberOf**](/windows/desktop/ADSchema/a-memberof)             | Includes all of the groups in the UI list, except the primary group, which is represented in the AD through the [**primaryGroupId**](/windows/desktop/ADSchema/a-primarygroupid) attribute. |
| Set Primary Group | [**primaryGroupId**](/windows/desktop/ADSchema/a-primarygroupid) | LDAP: Tied to [**primaryGroupToken**](/windows/desktop/ADSchema/a-primarygrouptoken) of the primary group.                                                                                  |



 

## Organization Property Page

The following table shows the UI labels of the **Organization** property page.



| UI label       | Attribute in Active Directory Domain Services | Comment     |
|----------------|-----------------------------------------------|-------------|
| Title          | [**title**](/windows/desktop/ADSchema/a-title)                 | No comment. |
| Department     | [**department**](/windows/desktop/ADSchema/a-department)       | No comment. |
| Company        | [**company**](/windows/desktop/ADSchema/a-company)             | No comment. |
| Manager:Name   | [**manager**](/windows/desktop/ADSchema/a-manager)             | No comment. |
| Direct Reports | [**directReports**](/windows/desktop/ADSchema/a-directreports) | No comment. |



 

## Profile Property Page

The following table lists the UI labels of the **Profile** property page.



| UI label                | Attribute in Active Directory Domain Services | Comment                                                                                                                 |
|-------------------------|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Profile Path            | [**profilePath**](/windows/desktop/ADSchema/a-profilepath)     | No comment.                                                                                                             |
| Logon Script            | [**scriptPath**](/windows/desktop/ADSchema/a-scriptpath)       | No comment.                                                                                                             |
| Home Folder: Local Path | [**homeDirectory**](/windows/desktop/ADSchema/a-homedirectory) | If **Local path** is selected, the local path is stored in the [**homeDirectory**](/windows/desktop/ADSchema/a-homedirectory) attribute. |
| Home Folder: Connect    | [**homeDrive**](/windows/desktop/ADSchema/a-homedrive)         | If **Connect** is selected, the mapped drive is stored in the [**homeDrive**](/windows/desktop/ADSchema/a-homedrive) attribute.          |
| Home Folder: To         | [**homeDirectory**](/windows/desktop/ADSchema/a-homedirectory) | If **Connect** is selected, the path is stored in the [**homeDirectory**](/windows/desktop/ADSchema/a-homedirectory) attribute.          |



 

## Telephones Property Page

The following table lists the UI elements of the **Telephones** property page and their corresponding Active Directory attributes.



| UI label        | Attribute in Active Directory Domain Services                                 |
|-----------------|-------------------------------------------------------------------------------|
| Home            | [**homePhone**](/windows/desktop/ADSchema/a-homephone)                                         |
| Home: Other     | [**otherHomePhone**](/windows/desktop/ADSchema/a-otherhomephone)                               |
| Pager           | [**pager**](/windows/desktop/ADSchema/a-pager)                                                 |
| Pager: Other    | [**otherPager**](/windows/desktop/ADSchema/a-otherpager)                                       |
| Mobile          | [**mobile**](/windows/desktop/ADSchema/a-mobile)                                               |
| Mobile: Other   | [**otherMobile**](/windows/desktop/ADSchema/a-othermobile)                                     |
| Fax             | [**facsimileTelephoneNumber**](/windows/desktop/ADSchema/a-facsimiletelephonenumber)           |
| Fax: Other      | [**otherFacsimileTelephoneNumber**](/windows/desktop/ADSchema/a-otherfacsimiletelephonenumber) |
| IP phone        | [**ipPhone**](/windows/desktop/ADSchema/a-ipphone)                                             |
| IP phone: Other | [**otherIpPhone**](/windows/desktop/ADSchema/a-otheripphone)                                   |
| Notes           | [**info**](/windows/desktop/ADSchema/a-info)                                                   |



 

## Environment, Sessions, Remote Control, and Terminal Services Profile Property Pages

The **Environment**, **Sessions**, **Remote Control**, and **Terminal Services Profile** pages are supplied for a user object to support terminal services. The UI elements for these pages do not correspond to individual attributes. Instead, the settings are stored in private data within Active Directory Domain Services. The terminal services settings can be accessed with the [**IADsTsUserEx**](/windows/desktop/api/tsuserex/nn-tsuserex-iadstsuserex) interface.

 

 