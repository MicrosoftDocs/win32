---
description: Allows limits to be set on host process usage of system resources.
ms.assetid: 5f5ed1c6-bd1a-406d-a682-7a52059d9450
ms.tgt_platform: multiple
title: '__ProviderHostQuotaConfiguration class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __ProviderHostQuotaConfiguration
- All
- All
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_ProviderHostQuotaConfiguration class

The **\_\_ProviderHostQuotaConfiguration** system class is a configuration class for host provider processes. This class resides in the root namespace and allows limits to be set on host process usage of system resources.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __ProviderHostQuotaConfiguration : __SystemClass
{
  uint32 ThreadsPerHost;
  uint32 HandlesPerHost;
  uint32 ProcessLimitAllHosts;
  uint64 MemoryPerHost;
  uint64 MemoryAllHosts;
};
```

## Members

The **\_\_ProviderHostQuotaConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_ProviderHostQuotaConfiguration** class has these properties.

<dl> <dt>

**HandlesPerHost**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of kernel object handles each host can have.

</dd> <dt>

**MemoryAllHosts**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Combined amount of private memory in bytes that can be held by all hosts.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> <dt>

**MemoryPerHost**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Amount of private memory that can be held by each host.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> <dt>

**ProcessLimitAllHosts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Total number of host processes that can be executing concurrently.

</dd> <dt>

**ThreadsPerHost**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of threads owned by any one host.

</dd> </dl>

## Remarks

The properties that represent limits can be changed but because the class is a singleton, all the provider hosts share the same limits.

The following parameters are used when configuring the job object limits for the host job object:

-   **MemoryAllHosts**
-   **MemoryPerHost**
-   **ProcessLimitAllHosts**
-   **ThreadsPerHost**

The host process polls handle usage and exits the process if the **HandlesPerHost** quota is violated. Changes to these values take effect after the computer is restarted.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_SystemClass**](/windows/desktop/WmiSdk/--systemclass)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> </dl>

 

