---
title: MDM_WindowsAdvancedThreatProtection_DeviceTagging01 class
description: The MDM\_WindowsAdvancedThreatProtection\_DeviceTagging01 class is used to onboard, determine configuration and health status, and offboard endpoints for Windows Defender Advanced Threat Protection.
ms.assetid: b56d5d46-e994-404a-865a-c59bb948f2b3
keywords:
- MDM_WindowsAdvancedThreatProtection_DeviceTagging01 class
- MDM_WindowsAdvancedThreatProtection_DeviceTagging01 class, described
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MDM_WindowsAdvancedThreatProtection_DeviceTagging01
- MDM_WindowsAdvancedThreatProtection_DeviceTagging01.InstanceID
- MDM_WindowsAdvancedThreatProtection_DeviceTagging01.ParentID
- MDM_WindowsAdvancedThreatProtection_DeviceTagging01.IdMethod
api_type: 
- DllExport
api_location: 
- DMWmiBridgeProv.dll
---

# MDM\_WindowsAdvancedThreatProtection\_DeviceTagging01 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The MDM\_WindowsAdvancedThreatProtection\_DeviceTagging01 class is used to onboard, determine configuration and health status, and offboard endpoints for Windows Defender Advanced Threat Protection.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv1")]
class MDM_WindowsAdvancedThreatProtection_DeviceTagging01
{
  string InstanceID;
  string ParentID;
  string Group;
  sint32 Criticality;
  sint32 IdMethod;
};
```

## Members

The **MDM\_WindowsAdvancedThreatProtection\_DeviceTagging01** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_WindowsAdvancedThreatProtection\_DeviceTagging01** class has these properties.

<dl> <dt>

[Criticality](/windows/client-management/mdm/windowsadvancedthreatprotection-csp#criticality)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[Group](/windows/client-management/mdm/windowsadvancedthreatprotection-csp#group)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**IdMethod**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

TBD

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

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | None supported<br/>                                                                       |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                              |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv1.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl>  |



 

