---
title: ADSI Enumerations
description: Active Directory Service Interfaces (ADSI) define and use the enumerations listed in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f0ad5ce5-742d-40dc-ac5a-31d779e40bfd
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- ADSI ADSI , Reference, Enumerations
- Enumerations ADSI
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ADSI Enumerations

Active Directory Service Interfaces (ADSI) define and use the enumerations listed in the following table.



| Enumeration                                                           | Description                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ADS\_ACEFLAG\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0048_0003?branch=master)                        | Specifies how security propagates for inherited access-control entries (ACEs) and types of auditing for a system ACE.                                                                                                                                             |
| [**ADS\_ACETYPE\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0048_0002?branch=master)                        | Specifies the ACE type.                                                                                                                                                                                                                                           |
| [**ADS\_AUTHENTICATION\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0000_0000_0018?branch=master)          | Specifies the security level used in authenticating a client.                                                                                                                                                                                                     |
| [**ADS\_CHASE\_REFERRALS\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0000_0000_0024?branch=master)       | Specifies the behavior of referral chasing.                                                                                                                                                                                                                       |
| [**ADS\_DEREFENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0000_0000_0020?branch=master)                               | Specifies the behavior of alias dereferencing.                                                                                                                                                                                                                    |
| [**ADS\_DISPLAY\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0078_0003?branch=master)                        | Specifies how a path is displayed.                                                                                                                                                                                                                                |
| [**ADS\_ESCAPE\_MODE\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0078_0004?branch=master)               | Specifies whether special characters are escaped, unescaped, or untouched.                                                                                                                                                                                        |
| [**ADS\_FLAGTYPE\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0048_0004?branch=master)                      | Specifies the presence of the **ObjectType** or **InheritedObjectType** fields in an ACE.                                                                                                                                                                         |
| [**ADS\_FORMAT\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0078_0002?branch=master)                          | Specifies the type of values in a pathname object.                                                                                                                                                                                                                |
| [**ADS\_GROUP\_TYPE\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0023_0001?branch=master)                 | Specifies the group type of the member.                                                                                                                                                                                                                           |
| [**ADS\_NAME\_INITTYPE\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0050_0002?branch=master)           | Specifies the type of initialization to be performed on a name translate object.                                                                                                                                                                                  |
| [**ADS\_NAME\_TYPE\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0050_0001?branch=master)                   | Specifies the format used to represent distinguished names.                                                                                                                                                                                                       |
| [**ADS\_OPTION\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0077_0001?branch=master)                          | Specifies the available options that the [**IADsObjectOptions**](/windows/win32/Iads/nn-iads-iadsobjectoptions?branch=master) interface uses for manipulating directory objects.                                                                                                                        |
| [**ADS\_PASSWORD\_ENCODING\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0000_0000_0026?branch=master)   | Used to identify the type of password encoding used with the **ADS\_OPTION\_PASSWORD\_METHOD** option in the [**IADsObjectOptions::GetOption**](/windows/win32/Iads/nf-iads-iadsobjectoptions-getoption?branch=master) and [**IADsObjectOptions::SetOption**](/windows/win32/Iads/nf-iads-iadsobjectoptions-setoption?branch=master) methods. |
| [**ADS\_PATHTYPE\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0088_0001?branch=master)                      | Specifies the type of object on which the security descriptor is modified.                                                                                                                                                                                        |
| [**ADS\_PREFERENCES\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0000_0000_0022?branch=master)                | Specifies the query preferences of the OLE DB for ADSI.                                                                                                                                                                                                           |
| [**ADS\_PROPERTY\_OPERATION\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0000_0000_0027?branch=master) | Specifies the ways to update property values in the property cache.                                                                                                                                                                                               |
| [**ADS\_RIGHTS\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0048_0001?branch=master)                          | Specifies the access rights to a directory service object.                                                                                                                                                                                                        |
| [**ADS\_SCOPEENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0000_0000_0021?branch=master)                               | Specifies the scope of a directory search.                                                                                                                                                                                                                        |
| [**ADS\_SD\_CONTROL\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0048_0005?branch=master)                 | Specifies that an access-control list (ACL) is to be protected when new permissions are recursively applied to a directory tree.                                                                                                                                  |
| [**ADS\_SD\_FORMAT\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0088_0002?branch=master)                   | Specifies the format for converting the security descriptor.                                                                                                                                                                                                      |
| [**ADS\_SD\_REVISION\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0048_0006?branch=master)               | Specifies the revision number of an ACE or ACL.                                                                                                                                                                                                                   |
| [**ADS\_SEARCHPREF\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0000_0000_0025?branch=master)                  | Specifies preferences of the search.                                                                                                                                                                                                                              |
| [**ADS\_SECURITY\_INFO\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0077_0002?branch=master)           | Specifies the options for examining security data.                                                                                                                                                                                                                |
| [**ADS\_SETTYPE\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0078_0001?branch=master)                        | Specifies the path format in [**IADsPathname::Set**](/windows/win32/Iads/nf-iads-iadspathname-set?branch=master).                                                                                                                                                                                       |
| [**ADS\_STATUSENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0000_0000_0019?branch=master)                             | Specifies the status of search preferences.                                                                                                                                                                                                                       |
| [**ADS\_SYSTEMFLAG\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0017_0001?branch=master)                  | Specifies the types of attributes represented by an **attributeSchema** object.                                                                                                                                                                                   |
| [**ADS\_USER\_FLAG\_ENUM**](/windows/win32/Iads/ne-iads-ads_user_flag?branch=master)                   | Specifies flags used for manipulating user properties.                                                                                                                                                                                                            |
| [**ADSI\_DIALECT\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0000_0000_0023?branch=master)                      | Specifies available ADSI query dialects.                                                                                                                                                                                                                          |
| [**ADSTYPEENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0000_0000_0001?branch=master)                                    | Specifies data types used to interpret an ADSI extended syntax string.                                                                                                                                                                                            |



 

## Remarks

Because Visual Basic Scripting Edition applications cannot read data from a type library, VBScript applications cannot recognize symbolic constants as defined in these enumerations. Use the numeric constants instead to set the appropriate flags in a VBScript applications. To use the symbolic constants as a good programming practice, write explicit declarations of such constants, as done here, in VBScript applications.

## Related topics

<dl> <dt>

[**IADsObjectOptions**](/windows/win32/Iads/nn-iads-iadsobjectoptions?branch=master)
</dt> <dt>

[**IADsPathname::Set**](/windows/win32/Iads/nf-iads-iadspathname-set?branch=master)
</dt> </dl>

 

 




