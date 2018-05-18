---
title: SetByCommonOptions method of the PS\_DhcpServerv4OptionValue class
description: Sets an IPv4 Option Value at the Server, Scope or Reservation level. Any previously set option values for the specified option id are discarded.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e7035443-dc22-42c0-9371-1bae60ca2989'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByCommonOptions method", "SetByCommonOptions method, PS_DhcpServerv4OptionValue class", "PS_DhcpServerv4OptionValue class, SetByCommonOptions method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4OptionValue.SetByCommonOptions
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# SetByCommonOptions method of the PS\_DhcpServerv4OptionValue class

Sets an IPv4 Option Value at the Server, Scope or Reservation level. Any previously set option values for the specified option id are discarded.

## Syntax


```mof
uint32 SetByCommonOptions(
  [in]  string                  PolicyName,
  [in]  boolean                 PassThru,
  [in]  boolean                 Force,
  [in]  string                  DnsDomain,
  [in]  string                  DnsServer[],
  [in]  string                  ReservedIP,
  [in]  string                  Router[],
  [in]  string                  ScopeId,
  [in]  string                  UserClass,
  [in]  string                  WinsServer[],
  [in]  string                  Wpad,
  [in]  string                  ComputerName,
  [out] DhcpServerv4OptionValue cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*PolicyName* \[in\]
</dt> <dd>

Name of the policy for which the option values are to be set.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified the DNS server validation will be skipped. This is applicable only if the DNS Server option value is being set.

</dd> <dt>

*DnsDomain* \[in\]
</dt> <dd>

Value for the DNS domain option

</dd> <dt>

*DnsServer* \[in\]
</dt> <dd>

Value(s) for the DNS Server option in IPv4 address format

</dd> <dt>

*ReservedIP* \[in\]
</dt> <dd>

IPv4 address of the reservation for which the option values are to be set.

</dd> <dt>

*Router* \[in\]
</dt> <dd>

Values for the router/default gateway option in IPv4 address format.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier (in IPv4 address format) for which the option values need to be set.

</dd> <dt>

*UserClass* \[in\]
</dt> <dd>

If specified, sets the option Value for the specified user class.

</dd> <dt>

*WinsServer* \[in\]
</dt> <dd>

Values for the WINS server option in IPv4 address format.

</dd> <dt>

*Wpad* \[in\]
</dt> <dd>

Value for the Web Proxy Auto detection option. The value for this option is specified as a URL.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4OptionValue**](dhcpserverv4optionvalue.md) class.

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

[**PS\_DhcpServerv4OptionValue**](ps-dhcpserverv4optionvalue.md)
</dt> </dl>

 

 





