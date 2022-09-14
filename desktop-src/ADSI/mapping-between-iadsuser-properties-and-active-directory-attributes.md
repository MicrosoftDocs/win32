---
title: Mapping Between IADsUser Properties and Active Directory Attributes
description: When applicable, a property of ADSI user object is mapped to an appropriate Active Directory attribute. The ADSI user object properties are associated with the IADsUser property methods.
ms.assetid: 9b568084-5a6b-4a73-be88-9d9cd8007824
ms.tgt_platform: multiple
keywords:
- Mapping between IADsUser Properties and Active Directory Attributes ADSI
- LDAP provider ADSI , user object, Mapping between IADsUser properties and Active Directory attributes
ms.topic: article
ms.date: 05/31/2018
---

# Mapping Between IADsUser Properties and Active Directory Attributes

When applicable, a property of ADSI user object is mapped to an appropriate Active Directory attribute. The ADSI user object properties are associated with the [**IADsUser**](/windows/desktop/api/Iads/nn-iads-iadsuser) property methods.

The following table lists the mapping between the [**IADsUser**](/windows/desktop/api/Iads/nn-iads-iadsuser) properties for the LDAP provider and the corresponding Active Directory attribute.



| IADsUser property                                           | Active Directory attribute                                                                                  |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**AccountDisabled**](iadsuser-property-methods.md)        | **ADS\_UF\_ACCOUNTDISABLE** flag in the [**userAccountControl**](/windows/desktop/ADSchema/a-useraccountcontrol) attribute.  |
| [**AccountExpirationDate**](iadsuser-property-methods.md)  | [**accountExpires**](/windows/desktop/ADSchema/a-accountexpires)                                                             |
| [**BadLoginAddress**](iadsuser-property-methods.md)        | Not Supported.                                                                                              |
| [**BadLoginCount**](iadsuser-property-methods.md)          | [**badPwdCount**](/windows/desktop/ADSchema/a-badpwdcount)                                                                   |
| [**Department**](iadsuser-property-methods.md)             | [**department**](/windows/desktop/ADSchema/a-department)                                                                     |
| [**Description**](iadsuser-property-methods.md)            | [**description**](/windows/desktop/ADSchema/a-description)                                                                   |
| [**Division**](iadsuser-property-methods.md)               | [**division**](/windows/desktop/ADSchema/a-division)                                                                         |
| [**EmailAddress**](iadsuser-property-methods.md)           | [**mail**](/windows/desktop/ADSchema/a-mail)                                                                                 |
| [**EmployeeID**](iadsuser-property-methods.md)             | [**employeeID**](/windows/desktop/ADSchema/a-employeeid)                                                                     |
| [**FaxNumber**](iadsuser-property-methods.md)              | [**facsimileTelephoneNumber**](/windows/desktop/ADSchema/a-facsimiletelephonenumber)                                         |
| [**FirstName**](iadsuser-property-methods.md)              | [**givenName**](/windows/desktop/ADSchema/a-givenname)                                                                       |
| [**FullName**](iadsuser-property-methods.md)               | [**displayName**](/windows/desktop/ADSchema/a-displayname)                                                                   |
| [**GraceLoginsAllowed**](iadsuser-property-methods.md)     | Not Supported.                                                                                              |
| [**GraceLoginsRemaining**](iadsuser-property-methods.md)   | Not Supported.                                                                                              |
| [**HomeDirectory**](iadsuser-property-methods.md)          | [**homeDirectory**](/windows/desktop/ADSchema/a-homedirectory)                                                               |
| [**HomePage**](iadsuser-property-methods.md)               | [**wWWHomePage**](/windows/desktop/ADSchema/a-wwwhomepage)                                                                   |
| [**IsAccountLocked**](iadsuser-property-methods.md)        | [**lockoutTime**](/windows/desktop/ADSchema/a-lockouttime)                                                                   |
| [**Languages**](iadsuser-property-methods.md)              | Not Supported.                                                                                              |
| [**LastFailedLogin**](iadsuser-property-methods.md)        | [**badPasswordTime**](/windows/desktop/ADSchema/a-badpasswordtime)                                                           |
| [**LastLogin**](iadsuser-property-methods.md)              | [**lastLogon**](/windows/desktop/ADSchema/a-lastlogon)                                                                       |
| [**LastLogoff**](iadsuser-property-methods.md)             | [**lastLogoff**](/windows/desktop/ADSchema/a-lastlogoff)                                                                     |
| [**LastName**](iadsuser-property-methods.md)               | [**sn**](/windows/desktop/ADSchema/a-sn)                                                                                     |
| [**LoginHours**](iadsuser-property-methods.md)             | [**logonHours**](/windows/desktop/ADSchema/a-logonhours)                                                                     |
| [**LoginScript**](iadsuser-property-methods.md)            | [**scriptPath**](/windows/desktop/ADSchema/a-scriptpath)                                                                     |
| [**LoginWorkstations**](iadsuser-property-methods.md)      | [**userWorkstations**](/windows/desktop/ADSchema/a-userworkstations)                                                         |
| [**Manager**](iadsuser-property-methods.md)                | [**manager**](/windows/desktop/ADSchema/a-manager)                                                                           |
| [**MaxLogins**](iadsuser-property-methods.md)              | Not Supported.                                                                                              |
| [**MaxStorage**](iadsuser-property-methods.md)             | [**maxStorage**](/windows/desktop/ADSchema/a-maxstorage)                                                                     |
| [**NamePrefix**](iadsuser-property-methods.md)             | [**personalTitle**](/windows/desktop/ADSchema/a-personaltitle)                                                               |
| [**NameSuffix**](iadsuser-property-methods.md)             | [**generationQualifier**](/windows/desktop/ADSchema/a-generationqualifier)                                                   |
| [**OfficeLocations**](iadsuser-property-methods.md)        | [**physicalDeliveryOfficeName**](/windows/desktop/ADSchema/a-physicaldeliveryofficename)                                     |
| [**OtherName**](iadsuser-property-methods.md)              | [**middleName**](/windows/desktop/ADSchema/a-middlename)                                                                     |
| [**PasswordExpirationDate**](iadsuser-property-methods.md) | Set using Group Policy Editor                                                                               |
| [**PasswordLastChanged**](iadsuser-property-methods.md)    | [**pwdLastSet**](/windows/desktop/ADSchema/a-pwdlastset)                                                                     |
| [**PasswordMinimumLength**](iadsuser-property-methods.md)  | Set using Group Policy Editor                                                                               |
| [**PasswordRequired**](iadsuser-property-methods.md)       | **ADS\_UF\_PASSWD\_NOTREQD** flag in the [**userAccountControl**](/windows/desktop/ADSchema/a-useraccountcontrol) attribute. |
| [**Picture**](iadsuser-property-methods.md)                | [**thumbnailPhoto**](/windows/desktop/ADSchema/a-thumbnailphoto)                                                             |
| [**PostalAddresses**](iadsuser-property-methods.md)        | [**postalAddress**](/windows/desktop/ADSchema/a-postaladdress)                                                               |
| [**PostalCodes**](iadsuser-property-methods.md)            | [**postalCode**](/windows/desktop/ADSchema/a-postalcode)                                                                     |
| [**Profile**](iadsuser-property-methods.md)                | [**profilePath**](/windows/desktop/ADSchema/a-profilepath)                                                                   |
| [**RequireUniquePassword**](iadsuser-property-methods.md)  | Set using Group Policy Editor                                                                               |
| [**SeeAlso**](iadsuser-property-methods.md)                | [**seeAlso**](/windows/desktop/ADSchema/a-seealso)                                                                           |
| [**TelephoneHome**](iadsuser-property-methods.md)          | [**homePhone**](/windows/desktop/ADSchema/a-homephone)                                                                       |
| [**TelephoneMobile**](iadsuser-property-methods.md)        | [**mobile**](/windows/desktop/ADSchema/a-mobile)                                                                             |
| [**TelephoneNumber**](iadsuser-property-methods.md)        | [**telephoneNumber**](/windows/desktop/ADSchema/a-telephonenumber)                                                           |
| [**TelephonePager**](iadsuser-property-methods.md)         | [**pager**](/windows/desktop/ADSchema/a-pager)                                                                               |
| [**Title**](iadsuser-property-methods.md)                  | [**title**](/windows/desktop/ADSchema/a-title)                                                                               |



 

 

 