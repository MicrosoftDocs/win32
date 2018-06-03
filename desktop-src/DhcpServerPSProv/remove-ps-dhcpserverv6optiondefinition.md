---
title: Remove method of the PS\_DhcpServerv6OptionDefinition class
description: Deletes one or more IPv4 option definitions from the Server. If VendorClass is specified, only option definitions for the specified vendor class are deleted.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 81e641b0-9997-4b6d-bb57-f2a6e0ca887d
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DhcpServerv6OptionDefinition class
- PS_DhcpServerv6OptionDefinition class, Remove method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6OptionDefinition.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_DhcpServerv6OptionDefinition class

Deletes one or more IPv4 option definitions from the Server. If VendorClass is specified, only option definitions for the specified vendor class are deleted.

## Syntax


```mof
uint32 Remove(
  [in]  string                       ComputerName,
  [in]  uint32                       OptionId[],
  [in]  string                       VendorClass,
  [in]  boolean                      Passthru,
  [out] DhcpServerv6OptionDefinition cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*OptionId* \[in\]
</dt> <dd>

The numeric identifier(s) of the option(s) whose definition needs to be deleted.

</dd> <dt>

*VendorClass* \[in\]
</dt> <dd>

If specified, removes option definitions only for the specified vendor class.

</dd> <dt>

*Passthru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet return the PowerShell objects which are deleted.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6OptionDefinition**](dhcpserverv6optiondefinition.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv6OptionDefinition**](ps-dhcpserverv6optiondefinition.md)
</dt> </dl>

 

 





