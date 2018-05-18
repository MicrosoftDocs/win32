---
title: ADSI Enumerations
description: Active Directory Service Interfaces (ADSI) define and use the enumerations listed in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'f0ad5ce5-742d-40dc-ac5a-31d779e40bfd'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["ADSI ADSI , Reference, Enumerations", "Enumerations ADSI"]
---

# ADSI Enumerations

Active Directory Service Interfaces (ADSI) define and use the enumerations listed in the following table.



| Enumeration                                                           | Description                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ADS\_ACEFLAG\_ENUM**](ads-aceflag-enum.md)                        | Specifies how security propagates for inherited access-control entries (ACEs) and types of auditing for a system ACE.                                                                                                                                             |
| [**ADS\_ACETYPE\_ENUM**](ads-acetype-enum.md)                        | Specifies the ACE type.                                                                                                                                                                                                                                           |
| [**ADS\_AUTHENTICATION\_ENUM**](ads-authentication-enum.md)          | Specifies the security level used in authenticating a client.                                                                                                                                                                                                     |
| [**ADS\_CHASE\_REFERRALS\_ENUM**](ads-chase-referrals-enum.md)       | Specifies the behavior of referral chasing.                                                                                                                                                                                                                       |
| [**ADS\_DEREFENUM**](ads-derefenum.md)                               | Specifies the behavior of alias dereferencing.                                                                                                                                                                                                                    |
| [**ADS\_DISPLAY\_ENUM**](ads-display-enum.md)                        | Specifies how a path is displayed.                                                                                                                                                                                                                                |
| [**ADS\_ESCAPE\_MODE\_ENUM**](ads-escape-mode-enum.md)               | Specifies whether special characters are escaped, unescaped, or untouched.                                                                                                                                                                                        |
| [**ADS\_FLAGTYPE\_ENUM**](ads-flagtype-enum.md)                      | Specifies the presence of the **ObjectType** or **InheritedObjectType** fields in an ACE.                                                                                                                                                                         |
| [**ADS\_FORMAT\_ENUM**](ads-format-enum.md)                          | Specifies the type of values in a pathname object.                                                                                                                                                                                                                |
| [**ADS\_GROUP\_TYPE\_ENUM**](ads-group-type-enum.md)                 | Specifies the group type of the member.                                                                                                                                                                                                                           |
| [**ADS\_NAME\_INITTYPE\_ENUM**](ads-name-inittype-enum.md)           | Specifies the type of initialization to be performed on a name translate object.                                                                                                                                                                                  |
| [**ADS\_NAME\_TYPE\_ENUM**](ads-name-type-enum.md)                   | Specifies the format used to represent distinguished names.                                                                                                                                                                                                       |
| [**ADS\_OPTION\_ENUM**](ads-option-enum.md)                          | Specifies the available options that the [**IADsObjectOptions**](iadsobjectoptions.md) interface uses for manipulating directory objects.                                                                                                                        |
| [**ADS\_PASSWORD\_ENCODING\_ENUM**](ads-password-encoding-enum.md)   | Used to identify the type of password encoding used with the **ADS\_OPTION\_PASSWORD\_METHOD** option in the [**IADsObjectOptions::GetOption**](iadsobjectoptions-getoption.md) and [**IADsObjectOptions::SetOption**](iadsobjectoptions-setoption.md) methods. |
| [**ADS\_PATHTYPE\_ENUM**](ads-pathtype-enum.md)                      | Specifies the type of object on which the security descriptor is modified.                                                                                                                                                                                        |
| [**ADS\_PREFERENCES\_ENUM**](ads-preferences-enum.md)                | Specifies the query preferences of the OLE DB for ADSI.                                                                                                                                                                                                           |
| [**ADS\_PROPERTY\_OPERATION\_ENUM**](ads-property-operation-enum.md) | Specifies the ways to update property values in the property cache.                                                                                                                                                                                               |
| [**ADS\_RIGHTS\_ENUM**](ads-rights-enum.md)                          | Specifies the access rights to a directory service object.                                                                                                                                                                                                        |
| [**ADS\_SCOPEENUM**](ads-scopeenum.md)                               | Specifies the scope of a directory search.                                                                                                                                                                                                                        |
| [**ADS\_SD\_CONTROL\_ENUM**](ads-sd-control-enum.md)                 | Specifies that an access-control list (ACL) is to be protected when new permissions are recursively applied to a directory tree.                                                                                                                                  |
| [**ADS\_SD\_FORMAT\_ENUM**](ads-sd-format-enum.md)                   | Specifies the format for converting the security descriptor.                                                                                                                                                                                                      |
| [**ADS\_SD\_REVISION\_ENUM**](ads-sd-revision-enum.md)               | Specifies the revision number of an ACE or ACL.                                                                                                                                                                                                                   |
| [**ADS\_SEARCHPREF\_ENUM**](ads-searchpref-enum.md)                  | Specifies preferences of the search.                                                                                                                                                                                                                              |
| [**ADS\_SECURITY\_INFO\_ENUM**](ads-security-info-enum.md)           | Specifies the options for examining security data.                                                                                                                                                                                                                |
| [**ADS\_SETTYPE\_ENUM**](ads-settype-enum.md)                        | Specifies the path format in [**IADsPathname::Set**](iadspathname-set.md).                                                                                                                                                                                       |
| [**ADS\_STATUSENUM**](ads-statusenum.md)                             | Specifies the status of search preferences.                                                                                                                                                                                                                       |
| [**ADS\_SYSTEMFLAG\_ENUM**](ads-systemflag-enum.md)                  | Specifies the types of attributes represented by an **attributeSchema** object.                                                                                                                                                                                   |
| [**ADS\_USER\_FLAG\_ENUM**](ads-user-flag-enum.md)                   | Specifies flags used for manipulating user properties.                                                                                                                                                                                                            |
| [**ADSI\_DIALECT\_ENUM**](adsi-dialect-enum.md)                      | Specifies available ADSI query dialects.                                                                                                                                                                                                                          |
| [**ADSTYPEENUM**](adstypeenum.md)                                    | Specifies data types used to interpret an ADSI extended syntax string.                                                                                                                                                                                            |



 

## Remarks

Because Visual Basic Scripting Edition applications cannot read data from a type library, VBScript applications cannot recognize symbolic constants as defined in these enumerations. Use the numeric constants instead to set the appropriate flags in a VBScript applications. To use the symbolic constants as a good programming practice, write explicit declarations of such constants, as done here, in VBScript applications.

## Related topics

<dl> <dt>

[**IADsObjectOptions**](iadsobjectoptions.md)
</dt> <dt>

[**IADsPathname::Set**](iadspathname-set.md)
</dt> </dl>

 

 




