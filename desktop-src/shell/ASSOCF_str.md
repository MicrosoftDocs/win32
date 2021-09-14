---
description: 'Provides information to the IQueryAssociations interface methods.'
ms.assetid: 'e67d0282-9090-43e6-aedf-bb1fc0443221'
title: ASSOCF enumeration
ms.topic: reference
ms.date: 05/31/2018
---

# ASSOCF enumeration

Provides information to the [**IQueryAssociations**](/windows/win32/api/shlwapi/nn-shlwapi-iqueryassociations) interface methods.

## Syntax

```cpp
typedef enum  {
    ASSOCF_NONE                  = 0x00000000,  
    ASSOCF_INIT_NOREMAPCLSID     = 0x00000001,  
    ASSOCF_INIT_BYEXENAME        = 0x00000002,  
    ASSOCF_OPEN_BYEXENAME        = 0x00000002,  
    ASSOCF_INIT_DEFAULTTOSTAR    = 0x00000004,  
    ASSOCF_INIT_DEFAULTTOFOLDER  = 0x00000008,  
    ASSOCF_NOUSERSETTINGS        = 0x00000010,  
    ASSOCF_NOTRUNCATE            = 0x00000020,  
    ASSOCF_VERIFY                = 0x00000040,  
    ASSOCF_REMAPRUNDLL           = 0x00000080,  
    ASSOCF_NOFIXUPS              = 0x00000100,  
    ASSOCF_IGNOREBASECLASS       = 0x00000200,  
    ASSOCF_INIT_IGNOREUNKNOWN    = 0x00000400,  
    ASSOCF_INIT_FIXED_PROGID     = 0x00000800,  
    ASSOCF_IS_PROTOCOL           = 0x00001000,  
    ASSOCF_INIT_FOR_FILE         = 0x00002000
} ASSOCF;
```

## Constants

 <span id="ASSOCF_NONE"></span><span id="assocf_none"></span>**ASSOCF\_NONE** 

None of the following options are set.

 <span id="ASSOCF_INIT_NOREMAPCLSID"></span><span id="assocf_init_noremapclsid"></span>**ASSOCF\_INIT\_NOREMAPCLSID** 

Instructs [**IQueryAssociations**](/windows/win32/api/shlwapi/nn-shlwapi-iqueryassociations) interface methods not to map CLSID values to ProgID values.

 <span id="ASSOCF_INIT_BYEXENAME"></span><span id="assocf_init_byexename"></span>**ASSOCF\_INIT\_BYEXENAME** 

Identifies the value of the *pwszAssoc* parameter of [**IQueryAssociations::Init**](/windows/win32/api/shlwapi/nf-shlwapi-iqueryassociations-init) as an executable file name. If this flag is not set, the root key will be set to the ProgID associated with the **.exe** key instead of the executable file's ProgID.

 <span id="ASSOCF_OPEN_BYEXENAME"></span><span id="assocf_open_byexename"></span>**ASSOCF\_OPEN\_BYEXENAME** 

Identical to **ASSOCF\_INIT\_BYEXENAME**.

 <span id="ASSOCF_INIT_DEFAULTTOSTAR"></span><span id="assocf_init_defaulttostar"></span>**ASSOCF\_INIT\_DEFAULTTOSTAR** 

Specifies that when an [**IQueryAssociations**](/windows/win32/api/shlwapi/nn-shlwapi-iqueryassociations) method does not find the requested value under the root key, it should attempt to retrieve the comparable value from the **\*** subkey.

 <span id="ASSOCF_INIT_DEFAULTTOFOLDER"></span><span id="assocf_init_defaulttofolder"></span>**ASSOCF\_INIT\_DEFAULTTOFOLDER** 

Specifies that when a [**IQueryAssociations**](/windows/win32/api/shlwapi/nn-shlwapi-iqueryassociations) method does not find the requested value under the root key, it should attempt to retrieve the comparable value from the **Folder** subkey.

 <span id="ASSOCF_NOUSERSETTINGS"></span><span id="assocf_nousersettings"></span>**ASSOCF\_NOUSERSETTINGS** 

Specifies that only **HKEY\_CLASSES\_ROOT** should be searched, and that **HKEY\_CURRENT\_USER** should be ignored.

 <span id="ASSOCF_NOTRUNCATE"></span><span id="assocf_notruncate"></span>**ASSOCF\_NOTRUNCATE** 

Specifies that the return string should not be truncated. Instead, return an error value and the required size for the complete string.

 <span id="ASSOCF_VERIFY"></span><span id="assocf_verify"></span>**ASSOCF\_VERIFY** 

Instructs [**IQueryAssociations**](/windows/win32/api/shlwapi/nn-shlwapi-iqueryassociations) methods to verify that data is accurate. This setting allows **IQueryAssociations** methods to read data from the user's hard disk for verification. For example, they can check the friendly name in the registry against the one stored in the .exe file. Setting this flag typically reduces the efficiency of the method.

 <span id="ASSOCF_REMAPRUNDLL"></span><span id="assocf_remaprundll"></span>**ASSOCF\_REMAPRUNDLL** 

Instructs [**IQueryAssociations**](/windows/win32/api/shlwapi/nn-shlwapi-iqueryassociations) methods to ignore Rundll.exe and return information about its target. Typically **IQueryAssociations** methods return information about the first .exe or .dll in a command string. If a command uses Rundll.exe, setting this flag tells the method to ignore Rundll.exe and return information about its target.

 <span id="ASSOCF_NOFIXUPS"></span><span id="assocf_nofixups"></span>**ASSOCF\_NOFIXUPS** 

Instructs [**IQueryAssociations**](/windows/win32/api/shlwapi/nn-shlwapi-iqueryassociations) methods not to fix errors in the registry, such as the friendly name of a function not matching the one found in the .exe file.

 <span id="ASSOCF_IGNOREBASECLASS"></span><span id="assocf_ignorebaseclass"></span>**ASSOCF\_IGNOREBASECLASS** 

Specifies that the BaseClass value should be ignored.

 <span id="ASSOCF_INIT_IGNOREUNKNOWN"></span><span id="assocf_init_ignoreunknown"></span>**ASSOCF\_INIT\_IGNOREUNKNOWN** 

**Introduced in Windows 7**. Specifies that the "Unknown" ProgID should be ignored; instead, fail.

 <span id="ASSOCF_INIT_FIXED_PROGID"></span><span id="assocf_init_fixed_progid"></span>**ASSOCF\_INIT\_FIXED\_PROGID** 

**Introduced in Windows 8**. Specifies that the supplied ProgID should be mapped using the system defaults, rather than the current user defaults.

 <span id="ASSOCF_IS_PROTOCOL"></span><span id="assocf_is_protocol"></span>**ASSOCF\_IS\_PROTOCOL** 

**Introduced in Windows 8**. Specifies that the value is a protocol, and should be mapped using the current user defaults.

 <span id="ASSOCF_INIT_FOR_FILE"></span><span id="assocf_init_for_file"></span>**ASSOCF\_INIT\_FOR\_FILE** 

**Introduced in Windows 8.1**. Specifies that the ProgID corresponds with a file extension based association. Use together with **ASSOCF\_INIT\_FIXED\_PROGID**.

 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client | Windows 2000 Professional, Windows XP \[desktop apps only\]               |
| Minimum supported server | Windows 2000 Server \[desktop apps only\]                                 |
| Header                   |  Shlwapi.h  |



## See also

 [**AssocQueryKey**](/windows/win32/api/shlwapi/nf-shlwapi-assocquerykeya) [**AssocQueryString**](/windows/win32/api/shlwapi/nf-shlwapi-assocquerystringa) [**AssocQueryStringByKey**](/windows/win32/api/shlwapi/nf-shlwapi-assocquerystringa) 

 

 

© 2017 Microsoft. All rights reserved.
