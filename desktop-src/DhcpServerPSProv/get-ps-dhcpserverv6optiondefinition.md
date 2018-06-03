---
title: Get method of the PS\_DhcpServerv6OptionDefinition class
description: Get the option definition for the option identified by the option id. If no option id is specified, all option definitions will be returned.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8247bec3-6907-4b7e-8c58-2e3dc5b0923d
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv6OptionDefinition class
- PS_DhcpServerv6OptionDefinition class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6OptionDefinition.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DhcpServerv6OptionDefinition class

Get the option definition for the option identified by the option id. If no option id is specified, all option definitions will be returned.

## Syntax


```mof
uint32 Get(
  [in]  string                       ComputerName,
  [in]  uint32                       OptionId[],
  [in]  string                       VendorClass,
  [in]  boolean                      All,
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

The numeric identifier of the option.

</dd> <dt>

*VendorClass* \[in\]
</dt> <dd>

If specified, returns the option Definitions only for the specified vendor class.

</dd> <dt>

*All* \[in\]
</dt> <dd>

If specified, returns all the option definitions including the vendor class specific option definitions.

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

 

 





