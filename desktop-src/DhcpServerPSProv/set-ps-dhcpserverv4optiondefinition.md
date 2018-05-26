---
title: Set method of the PS\_DhcpServerv4OptionDefinition class
description: Modifies the properties of an existing IPv4 Option definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5f09f0fe-bd38-42fa-b6cb-486b4c62a3f9
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DhcpServerv4OptionDefinition class
- PS_DhcpServerv4OptionDefinition class, Set method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4OptionDefinition.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_DhcpServerv4OptionDefinition class

Modifies the properties of an existing IPv4 Option definition

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
  [out] DhcpServerv4OptionDefinition cmdletOutput
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

Numeric identifier of the option definition to be modified

</dd> <dt>

*Name* \[in\]
</dt> <dd>

New name to be set for the option definition

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description string to be set for the option definition

</dd> <dt>

*VendorClass* \[in\]
</dt> <dd>

If specified, properties of the option definition for the specified vendor class are modified

</dd> <dt>

*DefaultValue* \[in\]
</dt> <dd>

Default value to be set for the option definition

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4OptionDefinition**](dhcpserverv4optiondefinition.md) class.

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

[**PS\_DhcpServerv4OptionDefinition**](ps-dhcpserverv4optiondefinition.md)
</dt> </dl>

 

 





