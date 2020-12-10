---
title: MDM_PassportForWork_ExcludeSecurityDevices03 class
description: The MDM\_PassportForWork\_ExcludeSecurityDevices03 class defines the Trusted Platform Modules allowed to use with Windows Hello for Business.
ms.assetid: ca8fba3a-736b-4bd3-ac93-e0d44d54798d
keywords:
- MDM_PassportForWork_ExcludeSecurityDevices03 class
- MDM_PassportForWork_ExcludeSecurityDevices03 class, described
topic_type:
- apiref
api_name:
- MDM_PassportForWork_ExcludeSecurityDevices03
- MDM_PassportForWork_ExcludeSecurityDevices03.InstanceID
- MDM_PassportForWork_ExcludeSecurityDevices03.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_PassportForWork\_ExcludeSecurityDevices03 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The MDM\_PassportForWork\_ExcludeSecurityDevices03 class defines the Trusted Platform Modules allowed to use with Windows Hello for Business.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv")]
class MDM_PassportForWork_ExcludeSecurityDevices03
{
  string  InstanceID;
  string  ParentID;
  boolean TPM12;
};
```

## Members

The **MDM\_PassportForWork\_ExcludeSecurityDevices03** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_PassportForWork\_ExcludeSecurityDevices03** class has these properties.

<dl> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Root node.

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Describes the full path to the parent node. For more information, see [PassportForWork CSP](/windows/client-management/mdm/passportforwork-csp).

</dd> <dt>

[TPM12](/windows/client-management/mdm/passportforwork-csp)
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



 

