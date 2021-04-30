---
title: IADsUser Property Methods (Iads.h)
description: The property methods of the IADsUser interface get or set the properties described in the following table. For more information, see Interface Property Methods.
ms.assetid: 02d0e5f1-8bc9-4ef6-962d-432654ca8433
ms.tgt_platform: multiple
keywords:
- IADsUser Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsUser Property Methods
- IADsUser.AccountDisabled
- IADsUser.get_AccountDisabled
- IADsUser.put_AccountDisabled
- IADsUser.AccountExpirationDate
- IADsUser.get_AccountExpirationDate
- IADsUser.put_AccountExpirationDate
- IADsUser.BadLoginAddress
- IADsUser.get_BadLoginAddress
- IADsUser.BadLoginCount
- IADsUser.get_BadLoginCount
- IADsUser.Department
- IADsUser.get_Department
- IADsUser.put_Department
- IADsUser.Description
- IADsUser.get_Description
- IADsUser.put_Description
- IADsUser.Division
- IADsUser.get_Division
- IADsUser.put_Division
- IADsUser.EmailAddress
- IADsUser.get_EmailAddress
- IADsUser.put_EmailAddress
- IADsUser.EmployeeID
- IADsUser.get_EmployeeID
- IADsUser.put_EmployeeID
- IADsUser.FaxNumber
- IADsUser.get_FaxNumber
- IADsUser.put_FaxNumber
- IADsUser.FirstName
- IADsUser.get_FirstName
- IADsUser.put_FirstName
- IADsUser.FullName
- IADsUser.get_FullName
- IADsUser.put_FullName
- IADsUser.GraceLoginsAllowed
- IADsUser.get_GraceLoginsAllowed
- IADsUser.put_GraceLoginsAllowed
- IADsUser.GraceLoginsRemaining
- IADsUser.get_GraceLoginsRemaining
- IADsUser.put_GraceLoginsRemaining
- IADsUser.HomeDirectory
- IADsUser.get_HomeDirectory
- IADsUser.put_HomeDirectory
- IADsUser.HomePage
- IADsUser.get_HomePage
- IADsUser.put_HomePage
- IADsUser.IsAccountLocked
- IADsUser.get_IsAccountLocked
- IADsUser.put_IsAccountLocked
- IADsUser.Languages
- IADsUser.get_Languages
- IADsUser.put_Languages
- IADsUser.LastFailedLogin
- IADsUser.get_LastFailedLogin
- IADsUser.LastLogin
- IADsUser.get_LastLogin
- IADsUser.LastLogoff
- IADsUser.get_LastLogoff
- IADsUser.LastName
- IADsUser.get_LastName
- IADsUser.put_LastName
- IADsUser.LoginHours
- IADsUser.get_LoginHours
- IADsUser.put_LoginHours
- IADsUser.LoginScript
- IADsUser.get_LoginScript
- IADsUser.put_LoginScript
- IADsUser.LoginWorkstations
- IADsUser.get_LoginWorkstations
- IADsUser.put_LoginWorkstations
- IADsUser.Manager
- IADsUser.get_Manager
- IADsUser.put_Manager
- IADsUser.MaxLogins
- IADsUser.get_MaxLogins
- IADsUser.put_MaxLogins
- IADsUser.MaxStorage
- IADsUser.get_MaxStorage
- IADsUser.put_MaxStorage
- IADsUser.NamePrefix
- IADsUser.get_NamePrefix
- IADsUser.put_NamePrefix
- IADsUser.NameSuffix
- IADsUser.get_NameSuffix
- IADsUser.put_NameSuffix
- IADsUser.OfficeLocations
- IADsUser.get_OfficeLocations
- IADsUser.put_OfficeLocations
- IADsUser.OtherName
- IADsUser.get_OtherName
- IADsUser.put_OtherName
- IADsUser.PasswordExpirationDate
- IADsUser.get_PasswordExpirationDate
- IADsUser.put_PasswordExpirationDate
- IADsUser.PasswordLastChanged
- IADsUser.get_PasswordLastChanged
- IADsUser.PasswordMinimumLength
- IADsUser.get_PasswordMinimumLength
- IADsUser.put_PasswordMinimumLength
- IADsUser.PasswordRequired
- IADsUser.get_PasswordRequired
- IADsUser.put_PasswordRequired
- IADsUser.Picture
- IADsUser.get_Picture
- IADsUser.put_Picture
- IADsUser.PostalAddresses
- IADsUser.get_PostalAddresses
- IADsUser.put_PostalAddresses
- IADsUser.PostalCodes
- IADsUser.get_PostalCodes
- IADsUser.put_PostalCodes
- IADsUser.Profile
- IADsUser.get_Profile
- IADsUser.put_Profile
- IADsUser.RequireUniquePassword
- IADsUser.get_RequireUniquePassword
- IADsUser.put_RequireUniquePassword
- IADsUser.SeeAlso
- IADsUser.get_SeeAlso
- IADsUser.put_SeeAlso
- IADsUser.TelephoneHome
- IADsUser.get_TelephoneHome
- IADsUser.put_TelephoneHome
- IADsUser.TelephoneMobile
- IADsUser.get_TelephoneMobile
- IADsUser.put_TelephoneMobile
- IADsUser.TelephoneNumber
- IADsUser.get_TelephoneNumber
- IADsUser.put_TelephoneNumber
- IADsUser.TelephonePager
- IADsUser.get_TelephonePager
- IADsUser.put_TelephonePager
- IADsUser.Title
- IADsUser.get_Title
- IADsUser.put_Title
api_location:
- Activeds.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IADsUser Property Methods

The property methods of the [**IADsUser**](/windows/desktop/api/Iads/nn-iads-iadsuser) interface get or set the properties described in the following table. For more information, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**AccountDisabled**
</dt> <dd> <dl>

A flag to indicate if the account is, or should be, disabled.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **Boolean**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_AccountDisabled(
  [out] VARIANT_BOOL* pfAccountDisabled
);
HRESULT put_AccountDisabled(
  [in] VARIANT_BOOL fAccountDisabled
);
```


</dt> </dl> </dd> <dt>

**AccountExpirationDate**
</dt> <dd> <dl>

The date and time after which the user cannot log on.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **DATE**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_AccountExpirationDate(
  [out] DATE* pdateAccountExpirationDate
);
HRESULT put_AccountExpirationDate(
  [in] DATE dateAccountExpirationDate
);
```


</dt> </dl> </dd> <dt>

**BadLoginAddress**
</dt> <dd> <dl>

The last node that is considered a possible intruder; this is available if Intruder detection is active.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_BadLoginAddress(
  [out] BSTR* pbstrBadLoginAddress
);
```


</dt> </dl> </dd> <dt>

**BadLoginCount**
</dt> <dd> <dl>

The number of bad logon attempts since the last reset.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_BadLoginCount(
  [out] LONG* plBadLoginCount
);
```


</dt> </dl> </dd> <dt>

**Department**
</dt> <dd> <dl>

The department, an organizational unit (OU), within the company to which the user belongs.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Department(
  [out] BSTR* pbstrDepartment
);
HRESULT put_Department(
  [in] BSTR bstrDepartment
);
```


</dt> </dl> </dd> <dt>

**Description**
</dt> <dd> <dl>

The text description of the user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Description(
  [out] BSTR* pbstrDescription
);
HRESULT put_Description(
  [in] BSTR bstrDescription
);
```


</dt> </dl> </dd> <dt>

**Division**
</dt> <dd> <dl>

The division within a company or organization.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Division(
  [out] BSTR* pbstrDivision
);
HRESULT put_Division(
  [in] BSTR bstrDivision
);
```


</dt> </dl> </dd> <dt>

**EmailAddress**
</dt> <dd> <dl>

The email address of the user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_EmailAddress(
  [out] BSTR* pbstrEmailAddress
);
HRESULT put_EmailAddress(
  [in] BSTR bstrEmailAddress
);
```


</dt> </dl> </dd> <dt>

**EmployeeID**
</dt> <dd> <dl>

The employee identifier of the user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_EmployeeID(
  [out] BSTR* pbstrEmployeeID
);
HRESULT put_EmployeeID(
  [in] BSTR bstrEmployeeID
);
```


</dt> </dl> </dd> <dt>

**FaxNumber**
</dt> <dd> <dl>

The fax number, or numbers, of the user. In Active Directory, this property is single-valued and the **VARIANT** array has one element.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_FaxNumber(
  [out] VARIANT* pvarFaxNumber
);
HRESULT put_FaxNumber(
  [in] VARIANT varFaxNumber
);
```


</dt> </dl> </dd> <dt>

**FirstName**
</dt> <dd> <dl>

The first name of the user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_FirstName(
  [out] BSTR* pbstrFirstName
);
HRESULT put_FirstName(
  [in] BSTR bstrFirstName
);
```


</dt> </dl> </dd> <dt>

**FullName**
</dt> <dd> <dl>

The full name of the user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_FullName(
  [out] BSTR* pbstrFullName
);
HRESULT put_FullName(
  [in] BSTR bstrFullName
);
```


</dt> </dl> </dd> <dt>

**GraceLoginsAllowed**
</dt> <dd> <dl>

The number of times the user can log on after the password has expired.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_GraceLoginsAllowed(
  [out] LONG* plGraceLoginsAllowed
);
HRESULT put_GraceLoginsAllowed(
  [in] LONG lGraceLoginsAllowed
);
```


</dt> </dl> </dd> <dt>

**GraceLoginsRemaining**
</dt> <dd> <dl>

The number of logons allowed before the account is locked.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_GraceLoginsRemaining(
  [out] LONG* plGraceLoginsRemaining
);
HRESULT put_GraceLoginsRemaining(
  [in] LONG lGraceLoginsRemaining
);
```


</dt> </dl> </dd> <dt>

**HomeDirectory**
</dt> <dd> <dl>

The home directory of the user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_HomeDirectory(
  [out] BSTR* pbstrHomeDirectory
);
HRESULT put_HomeDirectory(
  [in] BSTR bstrHomeDirectory
);
```


</dt> </dl> </dd> <dt>

**HomePage**
</dt> <dd> <dl>

The URL for the home page of the user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_HomePage(
  [out] BSTR* pbstrHomePage
);
HRESULT put_HomePage(
  [in] BSTR bstrHomePage
);
```


</dt> </dl> </dd> <dt>

**IsAccountLocked**
</dt> <dd> <dl>

A flag that indicates if the account is locked because of intruder detection. This property has limited usage when used with the LDAP ADSI provider. For more information about these limitations, see [Account Lockout (LDAP Provider)](ldap-account-lockout.md).

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **Boolean**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_IsAccountLocked(
  [out] VARIANT_BOOL* pfIsAccountLocked
);
HRESULT put_IsAccountLocked(
  [in] VARIANT_BOOL fIsAccountLocked
);
```


</dt> </dl> </dd> <dt>

**Languages**
</dt> <dd> <dl>

An array of **BSTR** language names for the user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Languages(
  [out] VARIANT* pvLanguages
);
HRESULT put_Languages(
  [in] VARIANT vLanguages
);
```


</dt> </dl> </dd> <dt>

**LastFailedLogin**
</dt> <dd> <dl>

The date and time of the last failed network login.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **DATE**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_LastFailedLogin(
  [out] DATE* pdateLastFailedLogin
);
```


</dt> </dl> </dd> <dt>

**LastLogin**
</dt> <dd> <dl>

The date and time of the last network login.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **DATE**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_LastLogin(
  [out] DATE* pdateLastLogin
);
```


</dt> </dl> </dd> <dt>

**LastLogoff**
</dt> <dd> <dl>

The date and time of the last network logoff.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **DATE**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_LastLogoff(
  [out] DATE* pdateLastLogoff
);
```


</dt> </dl> </dd> <dt>

**LastName**
</dt> <dd> <dl>

The last name of the user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_LastName(
  [out] BSTR* pbstrLastName
);
HRESULT put_LastName(
  [in] BSTR bstrLastName
);
```


</dt> </dl> </dd> <dt>

**LoginHours**
</dt> <dd> <dl>

Time periods for each day of the week during which logons are permitted for the user. Represented as a table of Boolean values for the week, each indicating if that time slot is a valid logon time. Be aware that the representation is provider and directory-specific.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_LoginHours(
  [out] VARIANT* pvLoginHours
);
HRESULT put_LoginHours(
  [in] VARIANT vLoginHours
);
```


</dt> </dl> </dd> <dt>

**LoginScript**
</dt> <dd> <dl>

The logon script path.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_LoginScript(
  [out] BSTR* pbstrLoginScript
);
HRESULT put_LoginScript(
  [in] BSTR bstrLoginScript
);
```


</dt> </dl> </dd> <dt>

**LoginWorkstations**
</dt> <dd> <dl>

Addresses or names of workstations, of the **BSTR** data type, from which the user can log on.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_LoginWorkstations(
  [out] VARIANT* pvLoginWorkstations
);
HRESULT put_LoginWorkstations(
  [in] VARIANT vLoginWorkstations
);
```


</dt> </dl> </dd> <dt>

**Manager**
</dt> <dd> <dl>

The manager of the user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Manager(
  [out] BSTR* pbstrManager
);
HRESULT put_Manager(
  [in] BSTR bstrManager
);
```


</dt> </dl> </dd> <dt>

**MaxLogins**
</dt> <dd> <dl>

The number of simultaneous login sessions allowed.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_MaxLogins(
  [out] LONG* plMaxLogins
);
HRESULT put_MaxLogins(
  [in] LONG lMaxLogins
);
```


</dt> </dl> </dd> <dt>

**MaxStorage**
</dt> <dd> <dl>

The maximum amount of disk space, in kilobytes, that the user can use.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_MaxStorage(
  [out] LONG* plMaxStorage
);
HRESULT put_MaxStorage(
  [in] LONG lMaxStorage
);
```


</dt> </dl> </dd> <dt>

**NamePrefix**
</dt> <dd> <dl>

Name prefix of the user, for example "Ms.", or "Hon."

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_NamePrefix(
  [out] BSTR* pbstrNamePrefix
);
HRESULT put_NamePrefix(
  [in] BSTR bstrNamePrefix
);
```


</dt> </dl> </dd> <dt>

**NameSuffix**
</dt> <dd> <dl>

Name suffix of the user, for example "Jr.", or "III".

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_NameSuffix(
  [out] BSTR* pbstrNameSuffix
);
HRESULT put_NameSuffix(
  [in] BSTR bstrNameSuffix
);
```


</dt> </dl> </dd> <dt>

**OfficeLocations**
</dt> <dd> <dl>

Office location as a **BSTR** array for the user. For Active Directory, this property is single-valued and the array has one element.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_OfficeLocations(
  [out] VARIANT* pvOfficeLocations
);
HRESULT put_OfficeLocations(
  [in] VARIANT vOfficeLocations
);
```


</dt> </dl> </dd> <dt>

**OtherName**
</dt> <dd> <dl>

An additional name, for example, the middle name, for the user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_OtherName(
  [out] BSTR* pbstrOtherName
);
HRESULT put_OtherName(
  [in] BSTR bstrOtherName
);
```


</dt> </dl> </dd> <dt>

**PasswordExpirationDate**
</dt> <dd> <dl>

The date and time when the password expires.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **DATE**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PasswordExpirationDate(
  [out] DATE* pdatePasswordExpirationDate
);
HRESULT put_PasswordExpirationDate(
  [in] DATE datePasswordExpirationDate
);
```


</dt> </dl> </dd> <dt>

**PasswordLastChanged**
</dt> <dd> <dl>

The last time the password was changed.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **DATE**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PasswordLastChanged(
  [out] DATE* pdatePasswordLastChanged
);
```


</dt> </dl> </dd> <dt>

**PasswordMinimumLength**
</dt> <dd> <dl>

The minimum length of the password.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PasswordMinimumLength(
  [out] LONG* plPasswordMinimumLength
);
HRESULT put_PasswordMinimumLength(
  [in] LONG lPasswordMinimumLength
);
```


</dt> </dl> </dd> <dt>

**PasswordRequired**
</dt> <dd> <dl>

A flag that indicates if the password is required.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **Boolean**
</dt> <dt>



``` syntax
// C++ method syntax
VARIANT_BOOL get_PasswordRequired(
  [out] VARIANT_BOOL* pfPasswordRequired
);
HRESULT put_PasswordRequired(
  [in] VARIANT_BOOL fPasswordRequired
);
```


</dt> </dl> </dd> <dt>

**Picture**
</dt> <dd> <dl>

An OctetString array of bytes that store an image.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Picture(
  [out] VARIANT* pvarPicture
);
HRESULT put_Picture(
  [in] VARIANT varPicture
);
```


</dt> </dl> </dd> <dt>

**PostalAddresses**
</dt> <dd> <dl>

Postal address as a **BSTR** array. This property is multi-valued to hold more than addresses of the user. The internal format of a PostalAddress should comply with CCITT F.401 as referenced in X.521-1993, which defines a PostalAddress as six elements of 30 bytes each, holding a street address, (optionally) Post Office Box, city or locality, state or province, Postal Code, and Country/Region.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PostalAddresses(
  [out] VARIANT* pvPostalAddresses
);
HRESULT put_PostalAddresses(
  [in] VARIANT vPostalAddresses
);
```


</dt> </dl> </dd> <dt>

**PostalCodes**
</dt> <dd> <dl>

Postal codes as a **BSTR** array. Postal codes are positionally linked to the **PostalAddresses** array. In Active Directory, however, this property is single-valued and the array has a single element.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PostalCodes(
  [out] VARIANT* pvPostalCodes
);
HRESULT put_PostalCodes(
  [in] VARIANT vPostalCodes
);
```


</dt> </dl> </dd> <dt>

**Profile**
</dt> <dd> <dl>

The path to the user profile.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Profile(
  [out] BSTR* pbstrProfile
);
HRESULT put_Profile(
  [in] BSTR bstrProfile
);
```


</dt> </dl> </dd> <dt>

**RequireUniquePassword**
</dt> <dd> <dl>

A flag that indicates if a new password should be different from those known through a password history.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **Boolean**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_RequireUniquePassword(
  [out] VARIANT_BOOL* pfRequireUniquePassword
);
HRESULT put_RequireUniquePassword(
  [in] VARIANT_BOOL fRequireUniquePassword
);
```


</dt> </dl> </dd> <dt>

**SeeAlso**
</dt> <dd> <dl>

An array of ADsPaths of other objects related to the user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SeeAlso(
  [out] VARIANT* pvSeeAlso
);
HRESULT put_SeeAlso(
  [in] VARIANT vSeeAlso
);
```


</dt> </dl> </dd> <dt>

**TelephoneHome**
</dt> <dd> <dl>

An array of home phone numbers of the user. In Active Directory, this property is single-valued and the array has one element.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_TelephoneHome(
  [out] VARIANT* pvarTelephoneHome
);
HRESULT put_TelephoneHome(
  [in] VARIANT varTelephoneHome
);
```


</dt> </dl> </dd> <dt>

**TelephoneMobile**
</dt> <dd> <dl>

An array of mobile phone numbers of the user. In Active Directory this property is single-valued and the array has one element only.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_TelephoneMobile(
  [out] VARIANT* pvarTelephoneMobile
);
HRESULT put_TelephoneMobile(
  [in] VARIANT varTelephoneMobile
);
```


</dt> </dl> </dd> <dt>

**TelephoneNumber**
</dt> <dd> <dl>

An array of, usually work-related, phone numbers associated with the user. In Active Directory this property is single-valued and the array is of a single element.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_TelephoneNumber(
  [out] VARIANT* pvarTelephoneNumber
);
HRESULT put_TelephoneNumber(
  [in] VARIANT varTelephoneNumber
);
```


</dt> </dl> </dd> <dt>

**TelephonePager**
</dt> <dd> <dl>

An array of pager numbers of the user. In Active Directory this property is single-valued and the array is of a single element.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_TelephonePager(
  [out] VARIANT* pvarTelephonePager
);
HRESULT put_TelephonePager(
  [in] VARIANT varTelephonePager
);
```


</dt> </dl> </dd> <dt>

**Title**
</dt> <dd> <dl>

The title of the user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Title(
  [out] BSTR* pbstrTitle
);
HRESULT put_Title(
  [in] BSTR bstrTitle
);
```


</dt> </dl> </dd> </dl>

 

## Remarks

The WinNT provider supplied by Microsoft does not support all the [**IADsUser**](/windows/desktop/api/Iads/nn-iads-iadsuser) property methods as presented above. However, the provider supports other properties that can be accessed using the [**IADs::Get**](/windows/desktop/api/Iads/nf-iads-iads-get) or [**IADs::Put**](/windows/desktop/api/Iads/nf-iads-iads-put) method. For more information and a list of unsupported properties and code examples, see [WinNT User Object](winnt-user-object.md) in [ADSI WinNT Provider](adsi-winnt-provider.md).

For more information about ADSI LDAP provider specific features of the user class object, see [LDAP User Object](ldap-user-object.md) in [ADSI LDAP Provider](adsi-ldap-provider.md). The topic includes [**IADsUser**](/windows/desktop/api/Iads/nn-iads-iadsuser), as well as code examples for managing a user account.

## Examples

The following code example shows how to bind to a user account object and retrieve the full name of the user.


```VB
Dim usr As IADsUser
Dim sFullName as String

On Error GoTo Cleanup
Set usr = GetObject("WinNT://Fabrikam/JeffSmith,user")
sFullName = usr.FullName

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If

    Set usr = Nothing
```



The following code example shows how to bind to a user account object and retrieve the full name of the user.


```C++
IADsUser *GetUserObject(LPWSTR uPath)
{
    IADsUser *pUser;
    HRESULT hr = ADsGetObject(uPath,IID_IADsUser,(void**)&pUser);
    if (FAILED(hr)) {return NULL;}
    BSTR bstr;
    hr = pUser->get_FullName(&bstr);
    printf("User: %S\n", bstr);
    SysFreeString(bstr);
    return pUser;
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl> |
| IID<br/>                      | IID\_IADsUser is defined as 3E37E320-17E2-11CF-ABC4-02608C9E7553<br/>             |



## See also

<dl> <dt>

[**IADsUser**](/windows/desktop/api/Iads/nn-iads-iadsuser)
</dt> <dt>

[Interface Property Methods](interface-property-methods.md)
</dt> <dt>

[**IADs::Get**](/windows/desktop/api/Iads/nf-iads-iads-get)
</dt> <dt>

[**IADs::Put**](/windows/desktop/api/Iads/nf-iads-iads-put)
</dt> <dt>

[WinNT User Object](winnt-user-object.md)
</dt> <dt>

[ADSI WinNT Provider](adsi-winnt-provider.md)
</dt> <dt>

[LDAP User Object](ldap-user-object.md)
</dt> <dt>

[ADSI LDAP Provider](adsi-ldap-provider.md)
</dt> </dl>

 

 





