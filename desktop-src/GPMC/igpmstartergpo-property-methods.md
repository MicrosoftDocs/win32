---
title: IGPMStarterGPO Property Methods
description: The property methods of the IGPMStarterGPO interface get and set the properties described in the following table. For a general discussion of property methods, see Interface Property Methods in the ADSI documentation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2cc1d707-d269-40ff-9356-c3ac2fa36de1'
ms.prod: 'windows-server-dev'
ms.technology: 'group-policy'
ms.tgt_platform: multiple
keywords: ["IGPMStarterGPO Property Methods GPMC"]
topic_type:
- apiref
api_name:
- IGPMStarterGPO Property Methods
- IGPMStarterGPO.DisplayName
- IGPMStarterGPO.put_DisplayName
- IGPMStarterGPO.get_DisplayName
- IGPMStarterGPO.Description
- IGPMStarterGPO.put_Description
- IGPMStarterGPO.get_Description
- IGPMStarterGPO.Author
- IGPMStarterGPO.get_Author
- IGPMStarterGPO.Product
- IGPMStarterGPO.get_Product
- IGPMStarterGPO.CreationTime
- IGPMStarterGPO.get_CreationTime
- IGPMStarterGPO.ID
- IGPMStarterGPO.get_ID
- IGPMStarterGPO.ModifiedTime
- IGPMStarterGPO.get_ModificationTime
- IGPMStarterGPO.Type
- IGPMStarterGPO.get_Type
- IGPMStarterGPO.ComputerVersion
- IGPMStarterGPO.get_ComputerVersion
- IGPMStarterGPO.UserVersion
- IGPMStarterGPO.get_UserVersion
- IGPMStarterGPO.StarterGPOVersion
- IGPMStarterGPO.get_StarterGPOVersion
api_location:
- Gpmgmt.dll
api_type:
- COM
---

# IGPMStarterGPO Property Methods

The property methods of the [**IGPMStarterGPO**](igpmstartergpo.md) interface get and set the properties described in the following table. For a general discussion of property methods, see [Interface Property Methods](https://msdn.microsoft.com/library/aa746378) in the ADSI documentation.

## Properties

<dl> <dt>

**Author**
</dt> <dd> <dl>

Name of the person who created the Starter GPO.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Author(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**ComputerVersion**
</dt> <dd> <dl>

Version number of the computer configuration portion of the Starter GPO.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ComputerVersion(
  [out] USHORT* pVal
);
```


</dt> </dl> </dd> <dt>

**CreationTime**
</dt> <dd> <dl>

Time when the Starter GPO was created. This property is given in the system's local time zone.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **Date**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_CreationTime(
  [out] DATE* pVal
);
```


</dt> </dl> </dd> <dt>

**Description**
</dt> <dd> <dl>

GPO comment or description.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_Description(
  [in] BSTR newVal
);
HRESULT get_Description(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**DisplayName**
</dt> <dd> <dl>

Friendly display name of the Starter GPO. Starter GPOs are identified in the Directory Service by ID (GUID), not by friendly name.

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

**ID**
</dt> <dd> <dl>

ID of the Starter GPO.

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

**ModifiedTime**
</dt> <dd> <dl>

Time when the Starter GPO was last modified. This property is given in the system's local time zone.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **Date**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ModificationTime(
  [out] DATE* pVal
);
```


</dt> </dl> </dd> <dt>

**Product**
</dt> <dd> <dl>

Name of the product this Starter GPO is designed to manage. For example, a Starter GPO might be created to configure MS Office. This property is applicable to system Starter GPOs. For custom Starter GPOs this property will be blank. This property is read-only.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Product(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**StarterGPOVersion**
</dt> <dd> <dl>

Version number of the Starter GPO.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_StarterGPOVersion(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**Type**
</dt> <dd> <dl>

Specifies the type of Starter GPO.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Type(
  [out] GPMStarterGPOType* pVal
);
```


</dt> </dl> </dd> <dt>

**UserVersion**
</dt> <dd> <dl>

Version number of the user configuration portion of the Starter GPO.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_UserVersion(
  [out] USHORT* pVal
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
| IID<br/>                      | IID\_IGPMStarterGPO is defined as DFC3F61B-8880-4490-9337-D29C7BA8C2F0<br/>     |



## See also

<dl> <dt>

[**IGPMStarterGPO**](igpmstartergpo.md)
</dt> <dt>

[**IGPMStarterGPOCollection**](igpmstartergpocollection.md)
</dt> </dl>

 

 





