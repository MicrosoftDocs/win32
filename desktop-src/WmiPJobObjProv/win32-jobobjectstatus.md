---
Description: 'The Win32\_JobObjectStatus abstract WMI class reports error information obtained while attempting any failed operation in the Job Object provider.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '8306f140-fde4-4ac8-9014-be3305baba03'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_JobObjectStatus class'
---

# Win32\_JobObjectStatus class

The **Win32\_JobObjectStatus** abstract [WMI class](https://msdn.microsoft.com/library/aa393244) reports error information obtained while attempting any failed operation in the [Job Object provider](job-object-provider.md).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("{7E6475FE-CF3C-4e22-892E-0E58482158E3}"), AMENDMENT]
class Win32_JobObjectStatus : __ExtendedStatus
{
  string Description;
  string Operation;
  string ParameterInfo;
  string ProviderName;
  uint32 StatusCode;
  string AdditionalDescription;
  uint32 Win32ErrorCode;
};
```

## Members

The **Win32\_JobObjectStatus** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_JobObjectStatus** class has these properties.

<dl> <dt>

**AdditionalDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Additional information relating to the error.

</dd> <dt>

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

Operation that takes place at the time of a failure or anomaly. Typically, Windows Management Instrumentation (WMI) sets this property to the name of a COM API for WMI method such as the following: [**IWbemServices::CreateInstanceEnum**](https://msdn.microsoft.com/library/aa392097).

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

**Win32ErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Windows error code most recently encountered that caused the operation to fail.

</dd> </dl>

## Remarks

The **Win32\_JobObjectStatus** class is derived from [**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipjobj.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipjobj.dll</dt> </dl> |



## See also

<dl> <dt>

[**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 




