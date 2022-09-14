---
title: MDM_Reporting_EnterpriseDataProtection01_RetrieveByTimeRange02 class
description: The MDM\_Reporting\_EnterpriseDataProtection01\_RetrieveByTimeRange02 class is used to retrieve the logs that exist within the StartTime and StopTime.
ms.assetid: 6abec00e-901f-4f79-840d-a4ef3a4d392d
keywords:
- MDM_Reporting_EnterpriseDataProtection01_RetrieveByTimeRange02 class
- MDM_Reporting_EnterpriseDataProtection01_RetrieveByTimeRange02 class, described
topic_type:
- apiref
api_name:
- MDM_Reporting_EnterpriseDataProtection01_RetrieveByTimeRange02
- MDM_Reporting_EnterpriseDataProtection01_RetrieveByTimeRange02.InstanceID
- MDM_Reporting_EnterpriseDataProtection01_RetrieveByTimeRange02.ParentID
api_location:
- Mofs\DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_Reporting\_EnterpriseDataProtection01\_RetrieveByTimeRange02 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_Reporting\_EnterpriseDataProtection01\_RetrieveByTimeRange02** class is used to retrieve the logs that exist within the StartTime and StopTime. The StartTime and StopTime are expressed in ISO 8601 format. If the StartTime and StopTime are not specified, then the values are interpreted as either first existing or last existing time.

Here are the other possible scenarios:

-   If the StartTime and StopTime are not specified, then it returns all existing logs.
-   If the StopTime is specified, but the StartTime is not specified, then all logs that exist before the StopTime are returned.
-   If the StartTime is specified, but the StopTime is not specified, then all that logs that exist from the StartTime are returned.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv1")]
class MDM_Reporting_EnterpriseDataProtection01_RetrieveByTimeRange02
{
  string InstanceID;
  string ParentID;
  string Logs;
  string StartTime;
  string StopTime;
  sint32 Type;
};
```

## Members

The **MDM\_Reporting\_EnterpriseDataProtection01\_RetrieveByTimeRange02** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Reporting\_EnterpriseDataProtection01\_RetrieveByTimeRange02** class has these properties.

<dl> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Identifies the name of the parent node. For this class, the string is "RetrieveByTimeRange".

</dd> <dt>

[Logs](/windows/client-management/mdm/reporting-csp#logs)
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

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/EnterpriseDataProtection"

</dd> <dt>

[StartTime](/windows/client-management/mdm/reporting-csp#starttime)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[StopTime](/windows/client-management/mdm/reporting-csp#stoptime)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[Type](/windows/client-management/mdm/reporting-csp#type)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | None supported<br/>                                                                            |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv1.mof</dt> </dl>      |
| DLL<br/>                      | <dl> <dt>Mofs\\DMWmiBridgeProv.dll</dt> </dl> |



 

