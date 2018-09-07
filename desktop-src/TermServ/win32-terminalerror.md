---
title: Win32_TerminalError class
description: Represents a terminal error.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d3f622cd-e4ce-4c7e-999e-940b67fd116c
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- Win32_TerminalError class Remote Desktop Services
- Win32_TerminalError class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TerminalError
- Win32_TerminalError.Description
- Win32_TerminalError.Operation
- Win32_TerminalError.ParameterInfo
- Win32_TerminalError.ProviderName
- Win32_TerminalError.StatusCode
- Win32_TerminalError.TerminalName
api_location:
- TSCfgWmi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_TerminalError class

Represents a terminal error.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class Win32_TerminalError : __ExtendedStatus
{
  string Description;
  string Operation;
  string ParameterInfo;
  string ProviderName;
  uint32 StatusCode;
  string TerminalName;
};
```

## Members

The **Win32\_TerminalError** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_TerminalError** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Any user-defined string that describes an error or operational status.

This property is inherited from [**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645).

</dd> <dt>

**Operation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Operation that takes place at the time of a failure or anomaly. Typically, WMI sets this property to the name of a COM API for WMI method such as the following: [**IWbemServices::CreateInstanceEnum**](https://msdn.microsoft.com/library/aa392097).

This property is inherited from [**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645).

</dd> <dt>

**ParameterInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Parameters involved in an error or status change. For example, if an application attempts to retrieve a class that does not exist, this property is set to the offending class name.

This property is inherited from [**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645).

</dd> <dt>

**ProviderName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies the provider that causes or reports an error or status change. If a provider is not involved, this string is set to "Windows Management".

This property is inherited from [**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645).

</dd> <dt>

**StatusCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains an error or information code for an operation. This can be any value defined by the provider, but the value 0 (zero) is usually reserved to indicate success. This property is inherited from [**\_\_NotifyStatus**](https://msdn.microsoft.com/library/aa394662).

</dd> <dt>

**TerminalName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the terminal sin which the error occurred.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\cimv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645)
</dt> </dl>

 

 





