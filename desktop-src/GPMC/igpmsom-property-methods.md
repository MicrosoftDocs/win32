---
title: IGPMSOM Property Methods
description: The property methods of the IGPMSOM interface get and set the properties described in the following table. For a general discussion of property methods, see Interface Property Methods in the ADSI documentation .
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 733be6ee-47bd-4599-93f3-989aeac67ed5
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
keywords:
- IGPMSOM Property Methods GPMC
topic_type:
- apiref
api_name:
- IGPMSOM Property Methods
- IGPMSOM.GPOInheritanceBlocked
- IGPMSOM.put_GPOInheritanceBlocked
- IGPMSOM.get_GPOInheritanceBlocked
- IGPMSOM.Name
- IGPMSOM.get_Name
- IGPMSOM.Path
- IGPMSOM.get_Path
- IGPMSOM.Type
- IGPMSOM.get_Type
api_location:
- Gpmgmt.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IGPMSOM Property Methods

The property methods of the **IGPMSOM** interface get and set the properties described in the following table. For a general discussion of property methods, see [Interface Property Methods](https://msdn.microsoft.com/library/aa746378) in the ADSI documentation .

## Properties

<dl> <dt>

**GPOInheritanceBlocked**
</dt> <dd> <dl>

Value that indicates whether GPO inheritance is blocked for the scope of management (SOM).

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **Boolean**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_GPOInheritanceBlocked(
  [in] VARIANT_BOOL newVal
);
HRESULT get_GPOInheritanceBlocked(
  [out] VARIANT_BOOL* pVal
);
```


</dt> </dl> </dd> <dt>

**Name**
</dt> <dd> <dl>

Name of the SOM.

If IGPMSOM points to an OU, as in "Ou=testou,dc=example,dc=Microsoft,dc=com", this property is the last part of the name, that is, "testou". If IGPMSOM points to a domain, as in "dc=example,dc=Microsoft,dc=com", this property is "example.microsoft.com". If it points to a site, this property is the website name; for example, "Default-first-site-name".

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Name(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**Path**
</dt> <dd> <dl>

Distinguished name of the SOM; for example, "ou=MyOU,dc=coname,dc=com".

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Path(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**Type**
</dt> <dd> <dl>

Type of the SOM. The following types are defined:

-   **somSite**
-   **somDomain**
-   **somOU**

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Type(
  [out] GPMSOMType* pVal
);
```


</dt> </dl> </dd> </dl>

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Gpmgmt.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Gpmgmt.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Gpmgmt.dll</dt> </dl> |
| IID<br/>                      | IID\_IGPMSOM is defined as C0A7F09E-05A1-4F0C-8158-9E5C33684F6B<br/>            |



## See also

<dl> <dt>

[**IGPMSOM**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmsom?branch=master)
</dt> </dl>

 

 





