---
title: IGPMGPO Property Methods
description: The property methods of the IGPMGPO interface get and set the properties that are described in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1087a0b7-3b23-4bc1-aa4b-9cbd15a7b3f2'
ms.prod: 'windows-server-dev'
ms.technology: 'group-policy'
ms.tgt_platform: multiple
keywords: ["IGPMGPO Property Methods GPMC"]
topic_type:
- apiref
api_name:
- IGPMGPO Property Methods
- IGPMGPO.ComputerDSVersionNumber
- IGPMGPO.get_ComputerDSVersionNumber
- IGPMGPO.ComputerSysvolVersionNumber
- IGPMGPO.get_ComputerSysvolVersionNumber
- IGPMGPO.CreationTime
- IGPMGPO.get_CreationTime
- IGPMGPO.DisplayName
- IGPMGPO.put_DisplayName
- IGPMGPO.get_DisplayName
- IGPMGPO.DomainName
- IGPMGPO.get_DomainName
- IGPMGPO.ID
- IGPMGPO.get_ID
- IGPMGPO.ModificationTime
- IGPMGPO.get_ModificationTime
- IGPMGPO.Path
- IGPMGPO.get_Path
- IGPMGPO.UserDSVersionNumber
- IGPMGPO.get_UserDSVersionNumber
- IGPMGPO.UserSysvolVersionNumber
- IGPMGPO.get_UserSysvolVersionNumber
api_location:
- Gpmgmt.dll
api_type:
- COM
---

# IGPMGPO Property Methods

The property methods of the **IGPMGPO** interface get and set the properties that are described in the following table. For a general discussion of property methods, see [Interface Property Methods](https://msdn.microsoft.com/library/aa746378) in the Active Directory Service Interfaces (ADSI) documentation.

## Properties

<dl> <dt>

**ComputerDSVersionNumber**
</dt> <dd> <dl>

Version number of the directory service component of the computer configuration portion of the Group Policy object (GPO).

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ComputerDSVersionNumber(
  [out] long* pVal
);
```


</dt> </dl> </dd> <dt>

**ComputerSysvolVersionNumber**
</dt> <dd> <dl>

Version number of the system volume folder (SYSVOL) component of the computer configuration portion of the GPO.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ComputerSysvolVersionNumber(
  [out] long* pVal
);
```


</dt> </dl> </dd> <dt>

**CreationTime**
</dt> <dd> <dl>

Time at which the GPO was created. This property is given in the local time zone of the computer.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **Date**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_CreationTime(
  [out] DATE* pDate
);
```


</dt> </dl> </dd> <dt>

**DisplayName**
</dt> <dd> <dl>

Display name of the GPO. More than one GPO may have the same display name. GPOs are identified in the directory service by the GPO ID, which is a GUID. GPOs are not identified in the directory service by display name.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_DisplayName(
  [in] BSTR newVal
);
HRESULT get_DisplayName(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**DomainName**
</dt> <dd> <dl>

Domain name for the GPO. This name is the full Domain Name System (DNS) name, for example, example.microsoft.com.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_DomainName(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**ID**
</dt> <dd> <dl>

ID of the GPO.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ID(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**ModificationTime**
</dt> <dd> <dl>

Time at which the GPO was last modified. This property is given in the local time zone of the computer.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **Date**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ModificationTime(
  [out] DATE* pDate
);
```


</dt> </dl> </dd> <dt>

**Path**
</dt> <dd> <dl>

Distinguished name of the GPO; for example, cn={myguid},cn=policies,cn=system,dc=coname,dc=com.

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

**UserDSVersionNumber**
</dt> <dd> <dl>

Version number of the directory service component of the user configuration portion of the GPO.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_UserDSVersionNumber(
  [out] long* pVal
);
```


</dt> </dl> </dd> <dt>

**UserSysvolVersionNumber**
</dt> <dd> <dl>

Version number of the system volume folder (SYSVOL) component of the user configuration portion of the GPO.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_UserSysvolVersionNumber(
  [out] long* pVal
);
```


</dt> </dl> </dd> </dl>

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Gpmgmt.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Gpmgmt.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Gpmgmt.dll</dt> </dl> |
| IID<br/>                      | IID\_IGPMGPO is defined as 58CC4352-1CA3-48E5-9864-1DA4D6E0D60F<br/>            |



## See also

<dl> <dt>

[**IGPMGPO**](igpmgpo.md)
</dt> <dt>

[**IGPMGPOCollection**](igpmgpocollection.md)
</dt> </dl>

 

 





