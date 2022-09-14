---
title: MDM_Policy_Result01_EventLogService02 class
description: The MDM\_Policy\_Result01\_EventLogService02 class represents the event log behavior.
ms.assetid: 6d4908e9-d283-486a-8309-57d5c5ec83d0
keywords:
- MDM_Policy_Result01_EventLogService02 class
- MDM_Policy_Result01_EventLogService02 class, described
topic_type:
- apiref
api_name:
- MDM_Policy_Result01_EventLogService02
- MDM_Policy_Result01_EventLogService02.InstanceID
- MDM_Policy_Result01_EventLogService02.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_Policy\_Result01\_EventLogService02 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The MDM\_Policy\_Result01\_EventLogService02 class represents the event log behavior.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv")]
class MDM_Policy_Result01_EventLogService02
{
  string InstanceID;
  string ParentID;
  string ControlEventLogBehavior;
  string SpecifyMaximumFileSizeApplicationLog;
  string SpecifyMaximumFileSizeSecurityLog;
  string SpecifyMaximumFileSizeSystemLog;
};
```

## Members

The **MDM\_Policy\_Result01\_EventLogService02** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Policy\_Result01\_EventLogService02** class has these properties.

<dl> <dt>

[ControlEventLogBehavior](/windows/client-management/mdm/policy-csp-eventlogservice#eventlogservice-controleventlogbehavior)
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

[SpecifyMaximumFileSizeApplicationLog](/windows/client-management/mdm/policy-csp-eventlogservice#eventlogservice-specifymaximumfilesizeapplicationlog)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[SpecifyMaximumFileSizeSecurityLog](/windows/client-management/mdm/policy-csp-eventlogservice#eventlogservice-specifymaximumfilesizesecuritylog)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[SpecifyMaximumFileSizeSystemLog](/windows/client-management/mdm/policy-csp-eventlogservice#eventlogservice-specifymaximumfilesizesystemlog)
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



 

