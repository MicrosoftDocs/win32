---
title: MDM_Policy_Config01_DataProtection02 class
description: The MDM\_Policy\_Config01\_DataProtection02 class represents the data protection policies available.
ms.assetid: 54750bae-ee5d-4db9-896f-28d9550c4d5d
keywords:
- MDM_Policy_Config01_DataProtection02 class
- MDM_Policy_Config01_DataProtection02 class, described
topic_type:
- apiref
api_name:
- MDM_Policy_Config01_DataProtection02
- MDM_Policy_Config01_DataProtection02.InstanceID
- MDM_Policy_Config01_DataProtection02.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_Policy\_Config01\_DataProtection02 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_Policy\_Config01\_DataProtection02** class represents the data protection policies available.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv")]
class MDM_Policy_Config01_DataProtection02
{
  string InstanceID;
  string ParentID;
  sint32 AllowDirectMemoryAccess;
  string LegacySelectiveWipeID;
};
```

## Members

The **MDM\_Policy\_Config01\_DataProtection02** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Policy\_Config01\_DataProtection02** class has these properties.

<dl> <dt>

[AllowDirectMemoryAccess](/windows/client-management/mdm/policy-csp-dataprotection#dataprotection-allowdirectmemoryaccess)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Identifies the name of the parent node. For this class, the string is "DataProtection".

</dd> <dt>

[LegacySelectiveWipeID](/windows/client-management/mdm/policy-csp-dataprotection#dataprotection-legacyselectivewipeid)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/Policy/Config"

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM\\DMMap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](/windows/client-management/mdm/using-powershell-scripting-with-the-wmi-bridge-provider)
</dt> </dl>

 

