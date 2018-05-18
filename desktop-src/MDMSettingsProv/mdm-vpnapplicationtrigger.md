---
title: MDM\_VpnApplicationTrigger class
description: Enables adding an application trigger to MDM-installed Virtual Private Network (VPN) profiles.
ms.assetid: 'b953a277-5b5b-45f9-9181-1bf653b4c0f1'
keywords: ["MDM_VpnApplicationTrigger class MDM Settings", "MDM_VpnApplicationTrigger class MDM Settings , described"]
topic_type:
- apiref
api_name:
- MDM_VpnApplicationTrigger
- MDM_VpnApplicationTrigger.ApplicationID
- MDM_VpnApplicationTrigger.TriggerEnabledInAllMDMProfiles
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
---

# MDM\_VpnApplicationTrigger class

Enables adding an application trigger to MDM-installed Virtual Private Network (VPN) profiles.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_VpnApplicationTrigger
{
  string  ApplicationID;
  boolean TriggerEnabledInAllMDMProfiles;
};
```

## Members

The **MDM\_VpnApplicationTrigger** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_VpnApplicationTrigger** class has these properties.

<dl> <dt>

**ApplicationID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The package family name of the application.

</dd> <dt>

**TriggerEnabledInAllMDMProfiles**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if an application trigger is added to all MDM-installed VPN profiles.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                         |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





