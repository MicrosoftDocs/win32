---
title: DtcLogFileSettings class
description: Represents DTC log file settings for a DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4ad61318-f007-4819-bd1a-38767b8dcbaf'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DtcLogFileSettings class", "DtcLogFileSettings class, described"]
topic_type:
- apiref
api_name:
- DtcLogFileSettings
- DtcLogFileSettings.Path
- DtcLogFileSettings.SizeInMB
- DtcLogFileSettings.MaxSizeInMB
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
---

# DtcLogFileSettings class

Represents DTC log file settings for a DTC instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1.0"), AMENDMENT]
class DtcLogFileSettings
{
  string Path;
  uint32 SizeInMB;
  uint32 MaxSizeInMB;
};
```

## Members

The **DtcLogFileSettings** class has these types of members:

-   [Properties](#properties)

### Properties

The **DtcLogFileSettings** class has these properties.

<dl> <dt>

**MaxSizeInMB**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum size of the log file, in megabytes.

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path to the DTC instance.

</dd> <dt>

**SizeInMB**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The size of the log file, in megabytes.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[Distributed Transaction Coordinator WMI Provider](distributed-transaction-coordinator-wmi-provider-portal.md)
</dt> </dl>

 

 





