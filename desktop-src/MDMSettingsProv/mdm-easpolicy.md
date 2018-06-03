---
title: MDM\_EASPolicy class
description: Represents Microsoft \ 160;Exchange \ 160;ActiveSync (EAS) PIN Password Policy configuration on the device.
ms.assetid: 80e5b7d2-a1fb-4095-8624-cc9802f1aa2f
keywords:
- MDM_EASPolicy class MDM Settings
- MDM_EASPolicy class MDM Settings , described
topic_type:
- apiref
api_name:
- MDM_EASPolicy
- MDM_EASPolicy.Key
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

# MDM\_EASPolicy class

Represents Microsoft Exchange ActiveSync (EAS) PIN Password Policy configuration on the device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_EASPolicy
{
  Uint32 Key;
};
```

## Members

The **MDM\_EASPolicy** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MDM\_EASPolicy** class has these methods.



| Method                                                   | Description                                      |
|:---------------------------------------------------------|:-------------------------------------------------|
| [**SetValues**](https://msdn.microsoft.com/library/dn610405) | Sets password-related setting values.<br/> |



 

### Properties

The **MDM\_EASPolicy** class has these properties.

<dl> <dt>

**Key**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the **MDM\_EASPolicy** class instance.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





