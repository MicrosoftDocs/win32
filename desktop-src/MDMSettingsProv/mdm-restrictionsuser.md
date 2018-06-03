---
title: MDM\_RestrictionsUser class
description: Represents the configuration of restriction settings on the device for standard users.
ms.assetid: aba81eb0-b2bb-4e35-bedd-be5e34b3a3ed
keywords:
- MDM_RestrictionsUser class MDM Settings
- MDM_RestrictionsUser class MDM Settings , described
topic_type:
- apiref
api_name:
- MDM_RestrictionsUser
- MDM_RestrictionsUser.Key
- MDM_RestrictionsUser.PCSettingsSyncEnabled
- MDM_RestrictionsUser.PCSettingsMeteredNetworkSyncEnabled
- MDM_RestrictionsUser.PCSettingsPasswordSyncEnabled
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MDM\_RestrictionsUser class

Represents the configuration of restriction settings on the device for standard users.

**Windows 8.1:** This class is supported beginning with Windows 8.1 Update.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_RestrictionsUser
{
  Uint32  Key;
  boolean PCSettingsSyncEnabled;
  boolean PCSettingsMeteredNetworkSyncEnabled;
  boolean PCSettingsPasswordSyncEnabled;
};
```

## Members

The **MDM\_RestrictionsUser** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_RestrictionsUser** class has these properties.

<dl> <dt>

**Key**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the **MDM\_RestrictionsUser** class instance.

</dd> <dt>

**PCSettingsMeteredNetworkSyncEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the **Sync settings over metered connection** option under **Change Settings** is on.

</dd> <dt>

**PCSettingsPasswordSyncEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the **Passwords** option under **Change Settings** is on.

</dd> <dt>

**PCSettingsSyncEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the **Sync your settings** option under **Change Settings** is on.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                         |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





