---
title: IGPMConstants2 Property Methods
description: The property methods of the IGPMConstants2 interface get the properties described in the following table. For a general discussion of property methods, see Interface Property Methods in the ADSI documentation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7afe2354-7d0a-45c5-bbd8-1aae8519ba5f
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
keywords:
- IGPMConstants2 Property Methods GPMC
topic_type:
- apiref
api_name:
- IGPMConstants2 Property Methods
api_location:
- Gpmgmt.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IGPMConstants2 Property Methods

The property methods of the [**IGPMConstants2**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmconstants2?branch=master) interface get the properties described in the following table. For a general discussion of property methods, see [Interface Property Methods](https://msdn.microsoft.com/library/aa746378) in the ADSI documentation.

The [**IGPMConstants2**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmconstants?branch=master) interface defines the following properties.

## Properties

<dl> <dt>

[**BackupTypeGPO**](igpmconstants-property-methods.md)
</dt> <dd> <dl>

Value corresponding to the **GPMBackupType** of typeGPO.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_BackupTypeGPO(
  [out] GPMBackupType* pVal
);
```


</dt> </dl> </dd> <dt>

[**BackupTypeStarterGPO**](igpmconstants-property-methods.md)
</dt> <dd> <dl>

Value corresponding to the **GPMBackupType** of typeStarterGPO.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT BackupTypeStarterGPO(
  [out] GPMBackupType* pVal
);
```


</dt> </dl> </dd> <dt>

[**PermStarterGPOCustom**](igpmconstants-property-methods.md)
</dt> <dd> <dl>

Constant value corresponding to the **permStarterGPOCustom** permission type.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermStarterGPOCustom(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

[**PermStarterGPOEdit**](igpmconstants-property-methods.md)
</dt> <dd> <dl>

Value corresponding to the **permStarterGPOEdit** permission type.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermStarterGPOEdit(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

[**PermStarterGPOFullControl**](igpmconstants-property-methods.md)
</dt> <dd> <dl>

Constant value corresponding to the **permStarterGPOFullControl** permission type.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermStarterGPOFullControl(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

[**PermStarterGPORead**](igpmconstants-property-methods.md)
</dt> <dd> <dl>

Value corresponding to the **permStarterGPORead** permission type .

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermStarterGPORead(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

[**ReportComments**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmconstants?branch=master)
</dt> <dd> <dl>

Value corresponding to the **ReportComments** property. Passed to **GenerateReport** methods to Specifies whether comments should be included in the report.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ReportComments(
  [out] GPMReportingOptions* pVal
);
```


</dt> </dl> </dd> <dt>

[**ReportLegacy**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmconstants?branch=master)
</dt> <dd> <dl>

Value corresponding to the **ReportLegacy** property. Passed to **GenerateReport** methods to generate a report.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ReportLegacy(
  [out] GPMReportingOptions* pVal
);
```


</dt> </dl> </dd> <dt>

[**SearchPropertyStarterGPODisplayName**](igpmconstants-property-methods.md)
</dt> <dd> <dl>

Value corresponding to the **starterGPODisplayName** search property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchPropertyStarterGPODisplayName(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

[**SearchPropertyStarterGPODomain**](igpmconstants-property-methods.md)
</dt> <dd> <dl>

Value corresponding to the **starterGPODomain** search property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchPropertyStarterGPODomain(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

[**SearchPropertyStarterGPOEffectivePermissions**](igpmconstants-property-methods.md)
</dt> <dd> <dl>

Value corresponding to the **starterGPOEffectivePermissions** search property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchPropertyStarterGPOEffectivePermissions(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

[**SearchPropertyStarterGPOID**](igpmconstants-property-methods.md)
</dt> <dd> <dl>

Value corresponding to the **starterGPOID** search property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchPropertyStarterGPOID(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

[**SearchPropertyStarterGPOPermissions**](igpmconstants-property-methods.md)
</dt> <dd> <dl>

Value corresponding to the **starterGPOPermissions** search property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchPropertyStarterGPOPermissions(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

[**StarterGPOTypeCustom**](igpmconstants-property-methods.md)
</dt> <dd> <dl>

Value corresponding to the **GPMStarterGPOType** of typeCustom.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_StarterGPOTypeCustom(
  [out] GPMStarterGPOType* pVal
);
```


</dt> </dl> </dd> <dt>

[**StarterGPOTypeSystem**](igpmconstants-property-methods.md)
</dt> <dd> <dl>

Value corresponding to the **GPMStarterGPOType** of typeSystem.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_StarterGPOTypeSystem(
  [out] GPMStarterGPOType* pVal
);
```


</dt> </dl> </dd> </dl>

 

## Remarks

Properties that begin with **PermGPO** apply only to GPOs; properties that begin with **PermWMIFilter** apply only to WMI filters.

For more information about policy-related permissions, see [**IGPM::CreatePermission**](/windows/previous-versions/Gpmgmt/nf-gpmgmt-igpm-createpermission?branch=master).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Gpmgmt.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Gpmgmt.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Gpmgmt.dll</dt> </dl> |
| IID<br/>                      | IID\_IGPMConstants2 is defined as 05AE21B0-AC09-4032-A26F-9E7DA786DC19<br/>     |



## See also

<dl> <dt>

[IGPMConstants2](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmconstants2?branch=master)
</dt> <dt>

[**IGPMConstants**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmconstants?branch=master)
</dt> <dt>

[**IGPM**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpm?branch=master)
</dt> </dl>

 

 





