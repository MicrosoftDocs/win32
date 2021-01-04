---
title: MDM_Reporting_SecurityAuditing01_RetrieveByCount02 class
description: The MDM\_Reporting\_SecurityAuditing01\_RetrieveByCount02 class is used to retrieve a specified number of logs from the StartTime.
ms.assetid: dfa50c04-99d6-4f6a-90ff-70a829bd317d
keywords:
- MDM_Reporting_SecurityAuditing01_RetrieveByCount02 class
- MDM_Reporting_SecurityAuditing01_RetrieveByCount02 class, described
topic_type:
- apiref
api_name:
- MDM_Reporting_SecurityAuditing01_RetrieveByCount02
- MDM_Reporting_SecurityAuditing01_RetrieveByCount02.InstanceID
- MDM_Reporting_SecurityAuditing01_RetrieveByCount02.ParentID
api_location:
- Mofs\DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_Reporting\_SecurityAuditing01\_RetrieveByCount02 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The [**MDM\_Reporting\_SecurityAuditing01\_RetrieveByCount02**](mdm-reporting-enterprisedataprotection01-retrievebycount02.md) class is used to retrieve a specified number of logs from the StartTime. The StartTime is expressed in ISO 8601 format. You can set the number of logs required by setting LogCount and StartTime. It returns the specified number of log or less, if the total number logs is less than LogCount.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv1")]
class MDM_Reporting_SecurityAuditing01_RetrieveByCount02
{
  string InstanceID;
  string ParentID;
  string Logs;
  sint32 LogCount;
  string StartTime;
};
```

## Members

The **MDM\_Reporting\_SecurityAuditing01\_RetrieveByCount02** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Reporting\_SecurityAuditing01\_RetrieveByCount02** class has these properties.

<dl> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Identifies the name of the parent node. For this class, the string is "RetrieveByCount".

</dd> <dt>

[LogCount](/windows/client-management/mdm/reporting-csp#logcount)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

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

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/SecurityAuditing"

</dd> <dt>

[StartTime](/windows/client-management/mdm/reporting-csp#starttime)
</dt> <dd> <dl> <dt>

Data type: **string**
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



 

