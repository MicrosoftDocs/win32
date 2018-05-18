---
title: Remove method of the PS\_DhcpServerv4OptionDefinition class
description: Delete one or more IPv4 option definitions from a DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6b686704-6ce6-4f58-986d-15e871297ac2'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Remove method", "Remove method, PS_DhcpServerv4OptionDefinition class", "PS_DhcpServerv4OptionDefinition class, Remove method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4OptionDefinition.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Remove method of the PS\_DhcpServerv4OptionDefinition class

Delete one or more IPv4 option definitions from a DHCP Server.

## Syntax


```mof
uint32 Remove(
  [in]  string                       ComputerName,
  [in]  uint32                       OptionId[],
  [in]  string                       VendorClass,
  [in]  boolean                      Passthru,
  [out] DhcpServerv4OptionDefinition cmdletOutput[]
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

Numeric identifiers of the option definitions to be deleted.

</dd> <dt>

*VendorClass* \[in\]
</dt> <dd>

If specified, deletes option definitions only for the specified vendor class

</dd> <dt>

*Passthru* \[in\]
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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4OptionDefinition**](ps-dhcpserverv4optiondefinition.md)
</dt> </dl>

 

 





