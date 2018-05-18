---
title: SetByCommonOptions method of the PS\_DhcpServerv6OptionValue class
description: Sets an IPv6 option value at the Server, Scope or Reservation Level. Any previously set option value(s) for the specified option id are discarded.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cd3c6759-6904-4eed-8d95-5cf08664cee6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByCommonOptions method", "SetByCommonOptions method, PS_DhcpServerv6OptionValue class", "PS_DhcpServerv6OptionValue class, SetByCommonOptions method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv6OptionValue.SetByCommonOptions
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# SetByCommonOptions method of the PS\_DhcpServerv6OptionValue class

Sets an IPv6 option value at the Server, Scope or Reservation Level. Any previously set option value(s) for the specified option id are discarded.

## Syntax


```mof
uint32 SetByCommonOptions(
  [in]  boolean                 PassThru,
  [in]  boolean                 Force,
  [in]  string                  Prefix,
  [in]  string                  UserClass,
  [in]  string                  DnsServer[],
  [in]  string                  DomainSearchList[],
  [in]  uint32                  InfoRefreshTime,
  [in]  string                  ComputerName,
  [in]  string                  ReservedIP,
  [out] DhcpServerv6OptionValue cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet return the PowerShell objects which are deleted.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified the DNS server validation will be skipped. This is applicable only if the DNS Server option value is being set.

</dd> <dt>

*Prefix* \[in\]
</dt> <dd>

IPv6 subnet prefix of the scope on which the option value is to be set.

</dd> <dt>

*UserClass* \[in\]
</dt> <dd>

If specified, sets the option value for the specified user class

</dd> <dt>

*DnsServer* \[in\]
</dt> <dd>

Value(s) for the DNS server option.

</dd> <dt>

*DomainSearchList* \[in\]
</dt> <dd>

Value(s) for the Domain Search List option.

</dd> <dt>

*InfoRefreshTime* \[in\]
</dt> <dd>

Value for the information refresh option.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*ReservedIP* \[in\]
</dt> <dd>

IPv6 address of the reservation for which the option value is to be set.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6OptionValue**](dhcpserverv6optionvalue.md) class.

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

[**PS\_DhcpServerv6OptionValue**](ps-dhcpserverv6optionvalue.md)
</dt> </dl>

 

 





