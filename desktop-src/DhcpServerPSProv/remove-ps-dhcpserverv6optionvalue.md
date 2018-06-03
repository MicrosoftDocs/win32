---
title: Remove method of the PS\_DhcpServerv6OptionValue class
description: Deletes one or more DHCPv6 option values set at the reservation level, scope level or server level, either for the standard IPv6 options or for a specified vendor class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4bb514ae-1478-4d54-9dcf-5428f39013ca
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DhcpServerv6OptionValue class
- PS_DhcpServerv6OptionValue class, Remove method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6OptionValue.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_DhcpServerv6OptionValue class

Deletes one or more DHCPv6 option values set at the reservation level, scope level or server level, either for the standard IPv6 options or for a specified vendor class.

## Syntax


```mof
uint32 Remove(
  [in]  string                  ComputerName,
  [in]  string                  Prefix,
  [in]  string                  ReservedIP,
  [in]  uint32                  OptionId[],
  [in]  boolean                 PassThru,
  [in]  string                  VendorClass,
  [in]  string                  UserClass,
  [out] DhcpServerv6OptionValue cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the name of the target server to which you want to migrate data. The target server must be in the same subnet as the source server.

</dd> <dt>

*Prefix* \[in\]
</dt> <dd>

The IPv6 subnet prefix of the scope from which the option value(s) are to be deleted.

</dd> <dt>

*ReservedIP* \[in\]
</dt> <dd>

IPv6 address of the reservation from which the option value(s) are to be deleted.

</dd> <dt>

*OptionId* \[in\]
</dt> <dd>

Numeric identifier(s) of the option(s) which are to be deleted.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Passes the object created by this cmdlet through the pipeline. By default, this cmdlet does not pass any objects through the pipeline.

</dd> <dt>

*VendorClass* \[in\]
</dt> <dd>

If specified, option values only for the specified vendor class are deleted.

</dd> <dt>

*UserClass* \[in\]
</dt> <dd>

If specified, option values only for the specified user class are deleted.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6OptionValue**](dhcpserverv6optionvalue.md) class.

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

[**PS\_DhcpServerv6OptionValue**](ps-dhcpserverv6optionvalue.md)
</dt> </dl>

 

 





