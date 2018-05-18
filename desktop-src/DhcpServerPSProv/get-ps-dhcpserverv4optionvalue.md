---
title: Get method of the PS\_DhcpServerv4OptionValue class
description: Returns the IPv4 option Values for one or more IPv4 options at the server, scope or reservation level.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '735a3ae1-5771-405c-9be5-88298a22616e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DhcpServerv4OptionValue class", "PS_DhcpServerv4OptionValue class, Get method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4OptionValue.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Get method of the PS\_DhcpServerv4OptionValue class

Returns the IPv4 option Values for one or more IPv4 options at the server, scope or reservation level.

## Syntax


```mof
uint32 Get(
  [in]  string                  VendorClass,
  [in]  string                  ComputerName,
  [in]  string                  ScopeId,
  [in]  string                  ReservedIP,
  [in]  uint32                  OptionId[],
  [in]  string                  UserClass,
  [in]  boolean                 All,
  [in]  boolean                 Brief,
  [in]  string                  PolicyName,
  [out] DhcpServerv4OptionValue cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*VendorClass* \[in\]
</dt> <dd>

If specified, gets the option values for that vendor class

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

The identifier of the scope (in IP address format) for which the option value(s) are requested.

</dd> <dt>

*ReservedIP* \[in\]
</dt> <dd>

IPv4 address of the reservation for which the option values are requested.

</dd> <dt>

*OptionId* \[in\]
</dt> <dd>

The numerical identifiers of the options being requested.

</dd> <dt>

*UserClass* \[in\]
</dt> <dd>

If specified, gets the option values for that user class

</dd> <dt>

*All* \[in\]
</dt> <dd>

When only All is specified, the above cmdlet will get all the option values (including vendor class, user class and policy specific) for a scope/server/reservation. When All is specified with a specific option id, option values for the specified option id for all vendor, user classes and policies will be returned. When Vendorclass and All is specified, all option values for the specified vendor class including those for any user class or policy would be returned. When Userclass and All is specified, all option values for the specified user class including any vendor specific options would be returned. When PolicyName and All is specified, all option values for the specified policy including any vendor specific options would be returned.

</dd> <dt>

*Brief* \[in\]
</dt> <dd>

If specified, the Name of the option is not returned in the option value object. This improves the execution speed of the cmdlet since the name of the option is not requested from the DHCP server. In case where the cmdlet is called repeatedly to fetch a large number of option values, using -Brief is recommended.

</dd> <dt>

*PolicyName* \[in\]
</dt> <dd>

The name of the policy for which the option value(s) are requested.

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

 

 





