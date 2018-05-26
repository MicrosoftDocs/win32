---
title: Get method of the PS\_DhcpServerv6OptionValue class
description: Returns the IPv6 option values for one or more IPv6 options either for a specific Reserved IP, scope or server level.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 87e4d082-4174-49ef-aca7-053f76ef01be
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv6OptionValue class
- PS_DhcpServerv6OptionValue class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6OptionValue.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DhcpServerv6OptionValue class

Returns the IPv6 option values for one or more IPv6 options either for a specific Reserved IP, scope or server level.

## Syntax


```mof
uint32 Get(
  [in]  string                  ComputerName,
  [in]  string                  VendorClass,
  [in]  string                  Prefix,
  [in]  string                  ReservedIP,
  [in]  string                  UserClass,
  [in]  uint32                  OptionId[],
  [in]  boolean                 All,
  [in]  boolean                 Brief,
  [out] DhcpServerv6OptionValue cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*VendorClass* \[in\]
</dt> <dd>

If specified, the Option Values for the specified vendor class are returned.

</dd> <dt>

*Prefix* \[in\]
</dt> <dd>

The IPv6 subnet prefix of the scope for which the option values are being requested.

</dd> <dt>

*ReservedIP* \[in\]
</dt> <dd>

A reserved IPv6 address for which the option values are being requested.

</dd> <dt>

*UserClass* \[in\]
</dt> <dd>

If specified, the Option Values for the specified user class are returned.

</dd> <dt>

*OptionId* \[in\]
</dt> <dd>

The numerical identifier of the options whose value(s) is being requested. If not specified, all option values configured are returned.

</dd> <dt>

*All* \[in\]
</dt> <dd>

When only All is specified, all the option values (including vendor class and user class specific) for a scope/server/reservation are returned. When All is specified with a specific option id, option values for the specified option id for all vendor and user classes are returned. When Vendorclass and All is specified, all option values for the specified vendor class including those for any user class are returned. When Userclass and All is specified, all option values for the specified user class including any vendor specific options are returned.

</dd> <dt>

*Brief* \[in\]
</dt> <dd>

If specified, the name of the option is not returned. This provides a way to run this cmdlet faster if the same is being run repetitively by the caller.

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

 

 





