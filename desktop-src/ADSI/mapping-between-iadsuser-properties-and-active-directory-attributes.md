---
title: Mapping Between IADsUser Properties and Active Directory Attributes
description: When applicable, a property of ADSI user object is mapped to an appropriate Active Directory attribute. The ADSI user object properties are associated with the IADsUser property methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 9b568084-5a6b-4a73-be88-9d9cd8007824
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Mapping between IADsUser Properties and Active Directory Attributes ADSI
- LDAP provider ADSI , user object, Mapping between IADsUser properties and Active Directory attributes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Mapping Between IADsUser Properties and Active Directory Attributes

When applicable, a property of ADSI user object is mapped to an appropriate Active Directory attribute. The ADSI user object properties are associated with the [**IADsUser**](/windows/win32/Iads/nn-iads-iadsuser?branch=master) property methods.

The following table lists the mapping between the [**IADsUser**](/windows/win32/Iads/nn-iads-iadsuser?branch=master) properties for the LDAP provider and the corresponding Active Directory attribute.



| IADsUser property                                           | Active Directory attribute                                                                                  |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**AccountDisabled**](iadsuser-property-methods.md)        | **ADS\_UF\_ACCOUNTDISABLE** flag in the [**userAccountControl**](https://msdn.microsoft.com/library/ms680832) attribute.  |
| [**AccountExpirationDate**](iadsuser-property-methods.md)  | [**accountExpires**](https://msdn.microsoft.com/library/ms675098)                                                             |
| [**BadLoginAddress**](iadsuser-property-methods.md)        | Not Supported.                                                                                              |
| [**BadLoginCount**](iadsuser-property-methods.md)          | [**badPwdCount**](https://msdn.microsoft.com/library/ms675244)                                                                   |
| [**Department**](iadsuser-property-methods.md)             | [**department**](https://msdn.microsoft.com/library/ms675490)                                                                     |
| [**Description**](iadsuser-property-methods.md)            | [**description**](https://msdn.microsoft.com/library/ms675492)                                                                   |
| [**Division**](iadsuser-property-methods.md)               | [**division**](https://msdn.microsoft.com/library/ms675518)                                                                         |
| [**EmailAddress**](iadsuser-property-methods.md)           | [**mail**](https://msdn.microsoft.com/library/ms676855)                                                                                 |
| [**EmployeeID**](iadsuser-property-methods.md)             | [**employeeID**](https://msdn.microsoft.com/library/ms675662)                                                                     |
| [**FaxNumber**](iadsuser-property-methods.md)              | [**facsimileTelephoneNumber**](https://msdn.microsoft.com/library/ms675675)                                         |
| [**FirstName**](iadsuser-property-methods.md)              | [**givenName**](https://msdn.microsoft.com/library/ms675719)                                                                       |
| [**FullName**](iadsuser-property-methods.md)               | [**displayName**](https://msdn.microsoft.com/library/ms675514)                                                                   |
| [**GraceLoginsAllowed**](iadsuser-property-methods.md)     | Not Supported.                                                                                              |
| [**GraceLoginsRemaining**](iadsuser-property-methods.md)   | Not Supported.                                                                                              |
| [**HomeDirectory**](iadsuser-property-methods.md)          | [**homeDirectory**](https://msdn.microsoft.com/library/ms676190)                                                               |
| [**HomePage**](iadsuser-property-methods.md)               | [**wWWHomePage**](https://msdn.microsoft.com/library/ms680927)                                                                   |
| [**IsAccountLocked**](iadsuser-property-methods.md)        | [**lockoutTime**](https://msdn.microsoft.com/library/ms676843)                                                                   |
| [**Languages**](iadsuser-property-methods.md)              | Not Supported.                                                                                              |
| [**LastFailedLogin**](iadsuser-property-methods.md)        | [**badPasswordTime**](https://msdn.microsoft.com/library/ms675243)                                                           |
| [**LastLogin**](iadsuser-property-methods.md)              | [**lastLogon**](https://msdn.microsoft.com/library/ms676823)                                                                       |
| [**LastLogoff**](iadsuser-property-methods.md)             | [**lastLogoff**](https://msdn.microsoft.com/library/ms676822)                                                                     |
| [**LastName**](iadsuser-property-methods.md)               | [**sn**](https://msdn.microsoft.com/library/ms679872)                                                                                     |
| [**LoginHours**](iadsuser-property-methods.md)             | [**logonHours**](https://msdn.microsoft.com/library/ms676846)                                                                     |
| [**LoginScript**](iadsuser-property-methods.md)            | [**scriptPath**](https://msdn.microsoft.com/library/ms679656)                                                                     |
| [**LoginWorkstations**](iadsuser-property-methods.md)      | [**userWorkstations**](https://msdn.microsoft.com/library/ms680868)                                                         |
| [**Manager**](iadsuser-property-methods.md)                | [**manager**](https://msdn.microsoft.com/library/ms676859)                                                                           |
| [**MaxLogins**](iadsuser-property-methods.md)              | Not Supported.                                                                                              |
| [**MaxStorage**](iadsuser-property-methods.md)             | [**maxStorage**](https://msdn.microsoft.com/library/ms676865)                                                                     |
| [**NamePrefix**](iadsuser-property-methods.md)             | [**personalTitle**](https://msdn.microsoft.com/library/ms679115)                                                               |
| [**NameSuffix**](iadsuser-property-methods.md)             | [**generationQualifier**](https://msdn.microsoft.com/library/ms675717)                                                   |
| [**OfficeLocations**](iadsuser-property-methods.md)        | [**physicalDeliveryOfficeName**](https://msdn.microsoft.com/library/ms679117)                                     |
| [**OtherName**](iadsuser-property-methods.md)              | [**middleName**](https://msdn.microsoft.com/library/ms677108)                                                                     |
| [**PasswordExpirationDate**](iadsuser-property-methods.md) | Set using Group Policy Editor                                                                               |
| [**PasswordLastChanged**](iadsuser-property-methods.md)    | [**pwdLastSet**](https://msdn.microsoft.com/library/ms679430)                                                                     |
| [**PasswordMinimumLength**](iadsuser-property-methods.md)  | Set using Group Policy Editor                                                                               |
| [**PasswordRequired**](iadsuser-property-methods.md)       | **ADS\_UF\_PASSWD\_NOTREQD** flag in the [**userAccountControl**](https://msdn.microsoft.com/library/ms680832) attribute. |
| [**Picture**](iadsuser-property-methods.md)                | [**thumbnailPhoto**](https://msdn.microsoft.com/library/ms680034)                                                             |
| [**PostalAddresses**](iadsuser-property-methods.md)        | [**postalAddress**](https://msdn.microsoft.com/library/ms679365)                                                               |
| [**PostalCodes**](iadsuser-property-methods.md)            | [**postalCode**](https://msdn.microsoft.com/library/ms679366)                                                                     |
| [**Profile**](iadsuser-property-methods.md)                | [**profilePath**](https://msdn.microsoft.com/library/ms679422)                                                                   |
| [**RequireUniquePassword**](iadsuser-property-methods.md)  | Set using Group Policy Editor                                                                               |
| [**SeeAlso**](iadsuser-property-methods.md)                | [**seeAlso**](https://msdn.microsoft.com/library/ms679769)                                                                           |
| [**TelephoneHome**](iadsuser-property-methods.md)          | [**homePhone**](https://msdn.microsoft.com/library/ms676192)                                                                       |
| [**TelephoneMobile**](iadsuser-property-methods.md)        | [**mobile**](https://msdn.microsoft.com/library/ms677119)                                                                             |
| [**TelephoneNumber**](iadsuser-property-methods.md)        | [**telephoneNumber**](https://msdn.microsoft.com/library/ms680027)                                                           |
| [**TelephonePager**](iadsuser-property-methods.md)         | [**pager**](https://msdn.microsoft.com/library/ms679102)                                                                               |
| [**Title**](iadsuser-property-methods.md)                  | [**title**](https://msdn.microsoft.com/library/ms680037)                                                                               |



 

 

 




