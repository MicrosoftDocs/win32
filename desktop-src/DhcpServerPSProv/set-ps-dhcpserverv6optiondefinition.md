---
title: Set method of the PS\_DhcpServerv6OptionDefinition class
description: Modifies the properties of an existing DHCPv6 option definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b1375cf3-2a40-41cb-952d-d79250009623
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DhcpServerv6OptionDefinition class
- PS_DhcpServerv6OptionDefinition class, Set method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6OptionDefinition.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_DhcpServerv6OptionDefinition class

Modifies the properties of an existing DHCPv6 option definition.

## Syntax


```mof
uint32 Set(
  [in]  string                       ComputerName,
  [in]  uint32                       OptionId,
  [in]  string                       Name,
  [in]  string                       Description,
  [in]  string                       VendorClass,
  [in]  string                       DefaultValue[],
  [in]  boolean                      PassThru,
  [out] DhcpServerv6OptionDefinition cmdletOutput
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

Numeric identifier of the option whose definition is to be modified.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

New name for the option.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description string of the option definition.

</dd> <dt>

*VendorClass* \[in\]
</dt> <dd>

If specified, the option definition only for the specified vendor class is modified.

</dd> <dt>

*DefaultValue* \[in\]
</dt> <dd>

Default value of the option

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

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

 

 





