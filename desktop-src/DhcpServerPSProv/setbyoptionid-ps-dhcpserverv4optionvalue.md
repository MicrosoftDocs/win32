---
title: SetByOptionId method of the PS\_DhcpServerv4OptionValue class
description: Sets an IPv4 Option Value at the Server, Scope or Reservation level. Any previously set option value(s) for the specified option id are discarded.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 23142cc3-7d6f-479c-acc6-66d494ee9424
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByOptionId method
- SetByOptionId method, PS_DhcpServerv4OptionValue class
- PS_DhcpServerv4OptionValue class, SetByOptionId method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4OptionValue.SetByOptionId
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByOptionId method of the PS\_DhcpServerv4OptionValue class

Sets an IPv4 Option Value at the Server, Scope or Reservation level. Any previously set option value(s) for the specified option id are discarded.

## Syntax


```mof
uint32 SetByOptionId(
  [in]  string                  PolicyName,
  [in]  boolean                 PassThru,
  [in]  boolean                 Force,
  [in]  string                  VendorClass,
  [in]  string                  Value[],
  [in]  uint32                  OptionId,
  [in]  string                  ReservedIP,
  [in]  string                  ScopeId,
  [in]  string                  UserClass,
  [in]  string                  ComputerName,
  [out] DhcpServerv4OptionValue cmdletOutput
);
```



## Parameters

<dl> <dt>

*PolicyName* \[in\]
</dt> <dd>

Name of the policy for which the option value(s) are to be set.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Passes the object created by this cmdlet through the pipeline. By default, this cmdlet does not pass any objects through the pipeline.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified the DNS server validation will be skipped. This is applicable only if the DNS Server option value is being set.

</dd> <dt>

*VendorClass* \[in\]
</dt> <dd>

If specified, sets the option Value for the specified vendor class.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

Value(s) to be set for the option. The format that the values will be returned in are as follows: 1) Byte, Word, DWord, DWordDword (these need to be specified as decimal or hexadecimal strings); 2) IPAddress, IPv6Address (these will need to be specified as strings); 3) String (these will need to be specified as strings); 4) BinaryData, EncapsulatedData (these will need to be specified as hexadecimal strings).

</dd> <dt>

*OptionId* \[in\]
</dt> <dd>

Numeric identifier of the option for which the value(s) are to be set

</dd> <dt>

*ReservedIP* \[in\]
</dt> <dd>

IPv4 address of the reservation for which the option value(s) are to be set

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier (in IPv4 address format) for which the option value(s) need to be set

</dd> <dt>

*UserClass* \[in\]
</dt> <dd>

If specified, sets the option Value for the specified user class

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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4OptionValue**](ps-dhcpserverv4optionvalue.md)
</dt> </dl>

 

 





