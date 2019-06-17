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
| First Name       | [**givenName**](https://docs.microsoft.com/windows/desktop/ADSchema/a-givenname)                                   |
| Last Name        | [**sn**](https://docs.microsoft.com/windows/desktop/ADSchema/a-sn)                                                 |
| Initials         | [**initials**](https://docs.microsoft.com/windows/desktop/ADSchema/a-initials)                                     |
| Display Name     | [**displayName**](https://docs.microsoft.com/windows/desktop/ADSchema/a-displayname)                               |
| Description      | [**description**](https://docs.microsoft.com/windows/desktop/ADSchema/a-description)                               |
| Office           | [**physicalDeliveryOfficeName**](https://docs.microsoft.com/windows/desktop/ADSchema/a-physicaldeliveryofficename) |
| Telephone Number | [**telephoneNumber**](https://docs.microsoft.com/windows/desktop/ADSchema/a-telephonenumber)                       |
| Telephone: Other | [**otherTelephone**](https://docs.microsoft.com/windows/desktop/ADSchema/a-othertelephone)                         |
| E-Mail           | [**E-mail-Addresses**](https://docs.microsoft.com/windows/desktop/ADSchema/a-mail)                                 |
| Web Page         | [**wWWHomePage**](https://docs.microsoft.com/windows/desktop/ADSchema/a-wwwhomepage)                               |
| Web Page: Other  | [**url**](https://docs.microsoft.com/windows/desktop/ADSchema/a-url)                                               |



 

## Account Property Page

The following table lists the UI labels of the **Account** property page.



| UI label                                | Attribute in Active Directory Domain Services                                                   | Comment                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UserLogon Name                          | [**userPrincipalName**](https://docs.microsoft.com/windows/desktop/ADSchema/a-userprincipalname)                                           | This field is taken from everything in the [**userPrincipalName**](https://docs.microsoft.com/windows/desktop/ADSchema/a-userprincipalname) attribute that precedes the last '@' character. The last '@' character and everything after it is placed in the suffix combo box.                                                                                                                                                      |
| User logon name (pre-Windows 2000)      | [**sAMAccountname**](https://docs.microsoft.com/windows/desktop/ADSchema/a-samaccountname)                                                 | No comment.                                                                                                                                                                                                                                                                                                                                                                             |
| Logon Hours                             | [**logonHours**](https://docs.microsoft.com/windows/desktop/ADSchema/a-logonhours)                                                         | No comment.                                                                                                                                                                                                                                                                                                                                                                             |
| Log On To                               | [**logonWorkstation**](https://docs.microsoft.com/windows/desktop/ADSchema/a-logonworkstation)                                             | No comment.                                                                                                                                                                                                                                                                                                                                                                             |
| Account is locked out                   | [**lockoutTime**](https://docs.microsoft.com/windows/desktop/ADSchema/a-lockouttime) and [**lockoutDuration**](https://docs.microsoft.com/windows/desktop/ADSchema/a-lockoutduration) | If the [**lockoutTime**](https://docs.microsoft.com/windows/desktop/ADSchema/a-lockouttime) attribute is not zero, the [**lockoutDuration**](https://docs.microsoft.com/windows/desktop/ADSchema/a-lockoutduration) attribute is added to **lockoutTime** and compared to the current date and time to determine if the account is locked out.                                                                                                                                |
| User must change password at next logon | [**pwdLastSet**](https://docs.microsoft.com/windows/desktop/ADSchema/a-pwdlastset)                                                         | No comment.                                                                                                                                                                                                                                                                                                                                                                             |
| User cannot change password             | N/A                                                                                             | This is the Change Password control in the ACL.                                                                                                                                                                                                                                                                                                                                         |
| Other Account Options                   | [**userAccountControl**](https://docs.microsoft.com/windows/desktop/ADSchema/a-useraccountcontrol)                                         | The remaining items in Account Options toggle bits in the [**userAccountControl**](https://docs.microsoft.com/windows/desktop/ADSchema/a-useraccountcontrol) attribute bitmask (flags in a DWORD).                                                                                                                                                                                                                                 |
| Account Expires                         | [**accountExpires**](https://docs.microsoft.com/windows/desktop/ADSchema/a-accountexpires)                                                 | The **Account Expires** control displays the date that the account will expire at the end of. The [**accountExpires**](https://docs.microsoft.com/windows/desktop/ADSchema/a-accountexpires) attribute is stored as the date that the account expires on. Because of this, the date displayed in the **Account Expires** control will be displayed as one day earlier than the date contained in the **accountExpires** attribute. |



 

## Address Property Page

The following table lists the UI labels of the **Address** property page.



| UI label        | Attribute in Active Directory Domain Services                                                 | Comment                                                   |
|-----------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Street          | [**streetAddress**](https://docs.microsoft.com/windows/desktop/ADSchema/a-streetaddress)                                                 | No comment.                                               |
| P.O.Box         | [**postOfficeBox**](https://docs.microsoft.com/windows/desktop/ADSchema/a-postofficebox)                                                 | No comment.                                               |
| City            | [**l**](https://docs.microsoft.com/windows/desktop/ADSchema/a-l)                                                                         | The **l** attribute name is a lowercase "L" as in Locale. |
| State/Province  | [**st**](https://docs.microsoft.com/windows/desktop/ADSchema/a-st)                                                                       | No comment.                                               |
| Zip/Postal Code | [**postalCode**](https://docs.microsoft.com/windows/desktop/ADSchema/a-postalcode)                                                       | No comment.                                               |
| Country/Region  | [**c**](https://docs.microsoft.com/windows/desktop/ADSchema/a-c), [**co**](https://docs.microsoft.com/windows/desktop/ADSchema/a-co), and [**countryCode**](https://docs.microsoft.com/windows/desktop/ADSchema/a-countrycode) | No comment.                                               |



 

## Member Of Property Page

The following table lists UI labels of the **Member Of** property page.



| UI label          | Attribute in Active Directory Domain Services   | Comment                                                                                                                                                                    |
|-------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Member of         | [**memberOf**](https://docs.microsoft.com/windows/desktop/ADSchema/a-memberof)             | Includes all of the groups in the UI list, except the primary group, which is represented in the AD through the [**primaryGroupId**](https://docs.microsoft.com/windows/desktop/ADSchema/a-primarygroupid) attribute. |
| Set Primary Group | [**primaryGroupID**](https://docs.microsoft.com/windows/desktop/ADSchema/a-primarygroupid) | LDAP: Tied to [**primaryGroupToken**](https://docs.microsoft.com/windows/desktop/ADSchema/a-primarygrouptoken) of the primary group.                                                                                  |



 

## Organization Property Page

The following table shows the UI labels of the **Organization** property page.



| UI label       | Attribute in Active Directory Domain Services | Comment     |
|----------------|-----------------------------------------------|-------------|
| Title          | [**title**](https://docs.microsoft.com/windows/desktop/ADSchema/a-title)                 | No comment. |
| Department     | [**department**](https://docs.microsoft.com/windows/desktop/ADSchema/a-department)       | No comment. |
| Company        | [**company**](https://docs.microsoft.com/windows/desktop/ADSchema/a-company)             | No comment. |
| Manager:Name   | [**manager**](https://docs.microsoft.com/windows/desktop/ADSchema/a-manager)             | No comment. |
| Direct Reports | [**directReports**](https://docs.microsoft.com/windows/desktop/ADSchema/a-directreports) | No comment. |



 

## Profile Property Page

The following table lists the UI labels of the **Profile** property page.



| UI label                | Attribute in Active Directory Domain Services | Comment                                                                                                                 |
|-------------------------|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Profile Path            | [**profilePath**](https://docs.microsoft.com/windows/desktop/ADSchema/a-profilepath)     | No comment.                                                                                                             |
| Logon Script            | [**scriptPath**](https://docs.microsoft.com/windows/desktop/ADSchema/a-scriptpath)       | No comment.                                                                                                             |
| Home Folder: Local Path | [**homeDirectory**](https://docs.microsoft.com/windows/desktop/ADSchema/a-homedirectory) | If **Local path** is selected, the local path is stored in the [**homeDirectory**](https://docs.microsoft.com/windows/desktop/ADSchema/a-homedirectory) attribute. |
| Home Folder: Connect    | [**homeDrive**](https://docs.microsoft.com/windows/desktop/ADSchema/a-homedrive)         | If **Connect** is selected, the mapped drive is stored in the [**homeDrive**](https://docs.microsoft.com/windows/desktop/ADSchema/a-homedrive) attribute.          |
| Home Folder: To         | [**homeDirectory**](https://docs.microsoft.com/windows/desktop/ADSchema/a-homedirectory) | If **Connect** is selected, the path is stored in the [**homeDirectory**](https://docs.microsoft.com/windows/desktop/ADSchema/a-homedirectory) attribute.          |



 

## Telephones Property Page

The following table lists the UI elements of the **Telephones** property page and their corresponding Active Directory attributes.



| UI label        | Attribute in Active Directory Domain Services                                 |
|-----------------|-------------------------------------------------------------------------------|
| Home            | [**homePhone**](https://docs.microsoft.com/windows/desktop/ADSchema/a-homephone)                                         |
| Home: Other     | [**otherHomePhone**](https://docs.microsoft.com/windows/desktop/ADSchema/a-otherhomephone)                               |
| Pager           | [**pager**](https://docs.microsoft.com/windows/desktop/ADSchema/a-pager)                                                 |
| Pager: Other    | [**otherPager**](https://docs.microsoft.com/windows/desktop/ADSchema/a-otherpager)                                       |
| Mobile          | [**mobile**](https://docs.microsoft.com/windows/desktop/ADSchema/a-mobile)                                               |
| Mobile: Other   | [**otherMobile**](https://docs.microsoft.com/windows/desktop/ADSchema/a-othermobile)                                     |
| Fax             | [**facsimileTelephoneNumber**](https://docs.microsoft.com/windows/desktop/ADSchema/a-facsimiletelephonenumber)           |
| Fax: Other      | [**otherFacsimileTelephoneNumber**](https://docs.microsoft.com/windows/desktop/ADSchema/a-otherfacsimiletelephonenumber) |
| IP phone        | [**ipPhone**](https://docs.microsoft.com/windows/desktop/ADSchema/a-ipphone)                                             |
| IP phone: Other | [**otherIpPhone**](https://docs.microsoft.com/windows/desktop/ADSchema/a-otheripphone)                                   |
| Notes           | [**info**](https://docs.microsoft.com/windows/desktop/ADSchema/a-info)                                                   |



 

## Environment, Sessions, Remote Control, and Terminal Services Profile Property Pages

The **Environment**, **Sessions**, **Remote Control**, and **Terminal Services Profile** pages are supplied for a user object to support terminal services. The UI elements for these pages do not correspond to individual attributes. Instead, the settings are stored in private data within Active Directory Domain Services. The terminal services settings can be accessed with the [**IADsTsUserEx**](https://docs.microsoft.com/windows/desktop/api/tsuserex/nn-tsuserex-iadstsuserex) interface.

 

 




