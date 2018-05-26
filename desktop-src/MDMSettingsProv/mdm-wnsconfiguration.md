---
title: MDM\_WNSConfiguration class
description: Enables configuration of the Windows Notification Service (WNS) notifications for the MDM agent.
ms.assetid: b4dd7b93-2460-4501-9117-3ad66c5af69e
keywords:
- MDM_WNSConfiguration class MDM Settings
- MDM_WNSConfiguration class MDM Settings , described
topic_type:
- apiref
api_name:
- MDM_WNSConfiguration
- MDM_WNSConfiguration.AppId
- MDM_WNSConfiguration.ConfigurationStatus
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MDM\_WNSConfiguration class

Enables configuration of the Windows Notification Service (WNS) notifications for the MDM agent.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_WNSConfiguration
{
  string AppId;
  uint32 ConfigurationStatus;
};
```

## Members

The **MDM\_WNSConfiguration** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MDM\_WNSConfiguration** class has these methods.



| Method                                                                              | Description                                                              |
|:------------------------------------------------------------------------------------|:-------------------------------------------------------------------------|
| [**UpdateConfiguration**](https://msdn.microsoft.com/library/dn610407) | Updates the Windows Notification Service (WNS) configuration.<br/> |



 

### Properties

The **MDM\_WNSConfiguration** class has these properties.

<dl> <dt>

**AppId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the MDM application.

</dd> <dt>

**ConfigurationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the application is configured.

Possible values are.

<dt>

0
</dt> <dd>

Not configured.

</dd> <dt>

1
</dt> <dd>

Configured.

</dd> </dl>

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

 

 





