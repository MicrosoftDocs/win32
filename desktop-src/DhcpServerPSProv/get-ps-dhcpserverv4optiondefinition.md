---
title: Get method of the PS\_DhcpServerv4OptionDefinition class
description: Gets the DHCPv4 option definition for the specified option ids.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e5e80742-e375-417b-a4bd-bd4ba93bf7d7
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv4OptionDefinition class
- PS_DhcpServerv4OptionDefinition class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4OptionDefinition.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DhcpServerv4OptionDefinition class

Gets the DHCPv4 option definition for the specified option ids

## Syntax


```mof
uint32 Get(
  [in]  string                       ComputerName,
  [in]  uint32                       OptionId[],
  [in]  string                       VendorClass,
  [in]  boolean                      All,
  [out] DhcpServerv4OptionDefinition cmdletOutput[]
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

The numerical identifiers of the options for which the option definitions are requested. If none are specified, all the DHCPv4 option definitions are returned.

</dd> <dt>

*VendorClass* \[in\]
</dt> <dd>

If specified, returns the option definitions only for the specified vendor class

</dd> <dt>

*All* \[in\]
</dt> <dd>

If specified, returns all the option definitions including the vendor class specific option definitions.

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

 

 





