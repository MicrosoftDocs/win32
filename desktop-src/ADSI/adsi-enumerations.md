---
title: ADSI Enumerations
description: Active Directory Service Interfaces (ADSI) define and use the enumerations listed in the following table.
ms.assetid: f0ad5ce5-742d-40dc-ac5a-31d779e40bfd
ms.tgt_platform: multiple
keywords:
- ADSI ADSI , Reference, Enumerations
- Enumerations ADSI
ms.topic: article
ms.date: 05/31/2018
---

# ADSI Enumerations

Active Directory Service Interfaces (ADSI) define and use the enumerations listed in the following table.



| Enumeration                                                           | Description                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ADS\_ACEFLAG\_ENUM**](/windows/win32/api/iads/ne-iads-ads_aceflag_enum)                        | Specifies how security propagates for inherited access-control entries (ACEs) and types of auditing for a system ACE.                                                                                                                                             |
| [**ADS\_ACETYPE\_ENUM**](/windows/win32/api/iads/ne-iads-ads_acetype_enum)                        | Specifies the ACE type.                                                                                                                                                                                                                                           |
| [**ADS\_AUTHENTICATION\_ENUM**](/windows/win32/api/iads/ne-iads-ads_authentication_enum)          | Specifies the security level used in authenticating a client.                                                                                                                                                                                                     |
| [**ADS\_CHASE\_REFERRALS\_ENUM**](/windows/win32/api/iads/ne-iads-ads_chase_referrals_enum)       | Specifies the behavior of referral chasing.                                                                                                                                                                                                                       |
| [**ADS\_DEREFENUM**](/windows/win32/api/iads/ne-iads-ads_derefenum)                               | Specifies the behavior of alias dereferencing.                                                                                                                                                                                                                    |
| [**ADS\_DISPLAY\_ENUM**](/windows/win32/api/iads/ne-iads-ads_display_enum)                        | Specifies how a path is displayed.                                                                                                                                                                                                                                |
| [**ADS\_ESCAPE\_MODE\_ENUM**](/windows/win32/api/iads/ne-iads-ads_escape_mode_enum)               | Specifies whether special characters are escaped, unescaped, or untouched.                                                                                                                                                                                        |
| [**ADS\_FLAGTYPE\_ENUM**](/windows/win32/api/iads/ne-iads-ads_flagtype_enum)                      | Specifies the presence of the **ObjectType** or **InheritedObjectType** fields in an ACE.                                                                                                                                                                         |
| [**ADS\_FORMAT\_ENUM**](/windows/win32/api/iads/ne-iads-ads_format_enum)                          | Specifies the type of values in a pathname object.                                                                                                                                                                                                                |
| [**ADS\_GROUP\_TYPE\_ENUM**](/windows/win32/api/iads/ne-iads-ads_group_type_enum)                 | Specifies the group type of the member.                                                                                                                                                                                                                           |
| [**ADS\_NAME\_INITTYPE\_ENUM**](/windows/win32/api/iads/ne-iads-ads_name_inittype_enum)           | Specifies the type of initialization to be performed on a name translate object.                                                                                                                                                                                  |
| [**ADS\_NAME\_TYPE\_ENUM**](/windows/win32/api/iads/ne-iads-ads_name_type_enum)                   | Specifies the format used to represent distinguished names.                                                                                                                                                                                                       |
| [**ADS\_OPTION\_ENUM**](/windows/win32/api/iads/ne-iads-ads_option_enum)                          | Specifies the available options that the [**IADsObjectOptions**](/windows/desktop/api/Iads/nn-iads-iadsobjectoptions) interface uses for manipulating directory objects.                                                                                                                        |
| [**ADS\_PASSWORD\_ENCODING\_ENUM**](/windows/win32/api/iads/ne-iads-ads_password_encoding_enum)   | Used to identify the type of password encoding used with the **ADS\_OPTION\_PASSWORD\_METHOD** option in the [**IADsObjectOptions::GetOption**](/windows/desktop/api/Iads/nf-iads-iadsobjectoptions-getoption) and [**IADsObjectOptions::SetOption**](/windows/desktop/api/Iads/nf-iads-iadsobjectoptions-setoption) methods. |
| [**ADS\_PATHTYPE\_ENUM**](/windows/win32/api/iads/ne-iads-ads_pathtype_enum)                      | Specifies the type of object on which the security descriptor is modified.                                                                                                                                                                                        |
| [**ADS\_PREFERENCES\_ENUM**](/windows/win32/api/iads/ne-iads-ads_preferences_enum)                | Specifies the query preferences of the OLE DB for ADSI.                                                                                                                                                                                                           |
| [**ADS\_PROPERTY\_OPERATION\_ENUM**](/windows/win32/api/iads/ne-iads-ads_property_operation_enum) | Specifies the ways to update property values in the property cache.                                                                                                                                                                                               |
| [**ADS\_RIGHTS\_ENUM**](/windows/win32/api/iads/ne-iads-ads_rights_enum)                          | Specifies the access rights to a directory service object.                                                                                                                                                                                                        |
| [**ADS\_SCOPEENUM**](/windows/win32/api/iads/ne-iads-ads_scopeenum)                               | Specifies the scope of a directory search.                                                                                                                                                                                                                        |
| [**ADS\_SD\_CONTROL\_ENUM**](/windows/win32/api/iads/ne-iads-ads_sd_control_enum)                 | Specifies that an access-control list (ACL) is to be protected when new permissions are recursively applied to a directory tree.                                                                                                                                  |
| [**ADS\_SD\_FORMAT\_ENUM**](/windows/win32/api/iads/ne-iads-ads_sd_format_enum)                   | Specifies the format for converting the security descriptor.                                                                                                                                                                                                      |
| [**ADS\_SD\_REVISION\_ENUM**](/windows/win32/api/iads/ne-iads-ads_sd_revision_enum)               | Specifies the revision number of an ACE or ACL.                                                                                                                                                                                                                   |
| [**ADS\_SEARCHPREF\_ENUM**](/windows/win32/api/iads/ne-iads-ads_searchpref_enum)                  | Specifies preferences of the search.                                                                                                                                                                                                                              |
| [**ADS\_SECURITY\_INFO\_ENUM**](/windows/win32/api/iads/ne-iads-ads_security_info_enum)           | Specifies the options for examining security data.                                                                                                                                                                                                                |
| [**ADS\_SETTYPE\_ENUM**](/windows/win32/api/iads/ne-iads-ads_settype_enum)                        | Specifies the path format in [**IADsPathname::Set**](/windows/desktop/api/Iads/nf-iads-iadspathname-set).                                                                                                                                                                                       |
| [**ADS\_STATUSENUM**](/windows/win32/api/iads/ne-iads-ads_statusenum)                             | Specifies the status of search preferences.                                                                                                                                                                                                                       |
| [**ADS\_SYSTEMFLAG\_ENUM**](/windows/win32/api/iads/ne-iads-ads_systemflag_enum)                  | Specifies the types of attributes represented by an **attributeSchema** object.                                                                                                                                                                                   |
| [**ADS\_USER\_FLAG\_ENUM**](/windows/win32/api/iads/ne-iads-ads_user_flag_enum)                   | Specifies flags used for manipulating user properties.                                                                                                                                                                                                            |
| [**ADSI\_DIALECT\_ENUM**](/windows/win32/api/iads/ne-iads-adsi_dialect_enum)                      | Specifies available ADSI query dialects.                                                                                                                                                                                                                          |
| [**ADSTYPEENUM**](/windows/win32/api/iads/ne-iads-adstypeenum)                                    | Specifies data types used to interpret an ADSI extended syntax string.                                                                                                                                                                                            |



 

## Remarks

Because Visual Basic Scripting Edition applications cannot read data from a type library, VBScript applications cannot recognize symbolic constants as defined in these enumerations. Use the numeric constants instead to set the appropriate flags in a VBScript applications. To use the symbolic constants as a good programming practice, write explicit declarations of such constants, as done here, in VBScript applications.

## Related topics

<dl> <dt>

[**IADsObjectOptions**](/windows/desktop/api/Iads/nn-iads-iadsobjectoptions)
</dt> <dt>

[**IADsPathname::Set**](/windows/desktop/api/Iads/nf-iads-iadspathname-set)
</dt> </dl>

 

 




