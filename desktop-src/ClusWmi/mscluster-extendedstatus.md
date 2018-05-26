---
title: MSCluster\_ExtendedStatus class
description: Contains the error type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4E45081F-CAA6-43B5-88DC-F47C945781D7
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_ExtendedStatus class
- MSCluster_ExtendedStatus class, described
topic_type:
- apiref
api_name:
- MSCluster_ExtendedStatus
- MSCluster_ExtendedStatus.Description
- MSCluster_ExtendedStatus.Operation
- MSCluster_ExtendedStatus.ParameterInfo
- MSCluster_ExtendedStatus.ProviderName
- MSCluster_ExtendedStatus.StatusCode
- MSCluster_ExtendedStatus.ErrorType
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSCluster\_ExtendedStatus class

Contains the error type.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{A09B95AB-B364-410C-8431-4C5A6EB791A9}"), AMENDMENT]
class MSCluster_ExtendedStatus : __ExtendedStatus
{
  string Description;
  string Operation;
  string ParameterInfo;
  string ProviderName;
  uint32 StatusCode;
  uint32 ErrorType;
};
```

## Members

The **MSCluster\_ExtendedStatus** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ExtendedStatus** class has these properties.

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

**ErrorType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of error which is returned.

The possible values are.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (0)


</dt> <dd></dd> <dt>

<span id="Win32"></span><span id="win32"></span><span id="WIN32"></span>

**Win32** (1)


</dt> <dd></dd> <dt>

<span id="Com"></span><span id="com"></span><span id="COM"></span>

**Com** (2)


</dt> <dd></dd> <dt>

<span id="Virtual_Machine"></span><span id="virtual_machine"></span><span id="VIRTUAL_MACHINE"></span>

**Virtual Machine** (3)


</dt> <dd></dd> </dl>

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

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> </dl>

 

 





