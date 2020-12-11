---
title: SetLoadBalancingState method of the Win32_TSSessionDirectory class
description: Sets the value to indicate whether the server will participate in Remote Desktop Connection Broker (RD Connection Broker) load balancing.
ms.assetid: 6368043c-1808-4757-9756-10b3800190b0
ms.tgt_platform: multiple
keywords:
- SetLoadBalancingState method Remote Desktop Services
- SetLoadBalancingState method Remote Desktop Services , Win32_TSSessionDirectory class
- Win32_TSSessionDirectory class Remote Desktop Services , SetLoadBalancingState method
topic_type:
- apiref
api_name:
- Win32_TSSessionDirectory.SetLoadBalancingState
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetLoadBalancingState method of the Win32\_TSSessionDirectory class

Sets the value to indicate whether the server will participate in Remote Desktop Connection Broker (RD Connection Broker) load balancing.

## Syntax


```mof
uint32 SetLoadBalancingState(
  [in] uint32 StateValue
);
```



## Parameters

<dl> <dt>

*StateValue* \[in\]
</dt> <dd>

Type: **uint32**

Indicates whether the server will participate in RD Connection Broker load balancing.

<dt>

0
</dt> <dd>

The server will not participate in RD Connection Broker load balancing.

</dd> <dt>

1
</dt> <dd>

The server will participate in RD Connection Broker load balancing.

</dd> </dl> </dd> </dl>

## Remarks

The server must be joined to a farm in RD Connection Broker.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSSessionDirectory**](win32-tssessiondirectory.md)
</dt> </dl>

 

