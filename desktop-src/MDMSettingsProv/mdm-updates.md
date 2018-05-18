---
title: MDM\_Updates class
description: Provides access to Windows Update policies.
ms.assetid: '61005d79-4a35-4021-9fac-b8485ef526c5'
keywords: ["MDM_Updates class MDM Settings", "MDM_Updates class MDM Settings , described"]
topic_type:
- apiref
api_name:
- MDM_Updates
- MDM_Updates.key
- MDM_Updates.AutoUpdatePolicy
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
---

# MDM\_Updates class

Provides access to Windows Update policies.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_Updates
{
  uint32 key;
  uint32 AutoUpdatePolicy;
};
```

## Members

The **MDM\_Updates** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Updates** class has these properties.

<dl> <dt>

**AutoUpdatePolicy**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets the policy for the regular application of Windows updates.

The following list shows the possible values.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd>

Do not regularly apply Windows updates.

</dd> <dt>

<span id="Important"></span><span id="important"></span><span id="IMPORTANT"></span>

<span id="Important"></span><span id="important"></span><span id="IMPORTANT"></span>**Important** (1)


</dt> <dd>

Regularly apply important Windows updates.

</dd> <dt>

<span id="Recommended"></span><span id="recommended"></span><span id="RECOMMENDED"></span>

<span id="Recommended"></span><span id="recommended"></span><span id="RECOMMENDED"></span>**Recommended** (2)


</dt> <dd>

Regularly apply recommended Windows updates.

</dd> </dl>

</dd> <dt>

**key**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the instance of the **MDM\_Updates** class.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                         |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



 

 





