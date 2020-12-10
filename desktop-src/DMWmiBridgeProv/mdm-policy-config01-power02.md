---
title: MDM_Policy_Config01_Power02 class
description: The MDM\_Policy\_Config01\_Power02 class configures the power policies.
ms.assetid: 8913c38c-0d8d-456f-a412-d47c2ccd5d13
keywords:
- MDM_Policy_Config01_Power02 class
- MDM_Policy_Config01_Power02 class, described
topic_type:
- apiref
api_name:
- MDM_Policy_Config01_Power02
- MDM_Policy_Config01_Power02.InstanceID
- MDM_Policy_Config01_Power02.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_Policy\_Config01\_Power02 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The MDM\_Policy\_Config01\_Power02 class configures the power policies.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv")]
class MDM_Policy_Config01_Power02
{
  string InstanceID;
  string ParentID;
  string AllowStandbyWhenSleepingPluggedIn;
  string HibernateTimeoutPluggedIn;
  string HibernateTimeoutOnBattery;
  string DisplayOffTimeoutPluggedIn;
  string DisplayOffTimeoutOnBattery;
  string RequirePasswordWhenComputerWakesOnBattery;
  string RequirePasswordWhenComputerWakesPluggedIn;
  string StandbyTimeoutPluggedIn;
  string StandbyTimeoutOnBattery;
};
```

## Members

The **MDM\_Policy\_Config01\_Power02** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Policy\_Config01\_Power02** class has these properties.

<dl> <dt>

[AllowStandbyWhenSleepingPluggedIn](/windows/client-management/mdm/policy-csp-power#power-allowstandbywhensleepingpluggedin)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[DisplayOffTimeoutOnBattery](/windows/client-management/mdm/policy-csp-power#power-displayofftimeoutonbattery)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[DisplayOffTimeoutPluggedIn](/windows/client-management/mdm/policy-csp-power#power-displayofftimeoutpluggedin)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HibernateTimeoutOnBattery](/windows/client-management/mdm/policy-csp-power#power-hibernatetimeoutonbattery)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HibernateTimeoutPluggedIn](/windows/client-management/mdm/policy-csp-power#power-hibernatetimeoutpluggedin)
</dt> <dd> <dl> <dt>

Data type: **string**
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

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

</dd> <dt>

[RequirePasswordWhenComputerWakesOnBattery](/windows/client-management/mdm/policy-csp-power#power-requirepasswordwhencomputerwakesonbattery)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[RequirePasswordWhenComputerWakesPluggedIn](/windows/client-management/mdm/policy-csp-power#power-requirepasswordwhencomputerwakespluggedin)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[StandbyTimeoutOnBattery](/windows/client-management/mdm/policy-csp-power#power-standbytimeoutonbattery)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[StandbyTimeoutPluggedIn](/windows/client-management/mdm/policy-csp-power#power-standbytimeoutpluggedin)
</dt> <dd> <dl> <dt>

Data type: **string**
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



 

