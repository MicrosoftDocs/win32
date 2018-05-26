---
title: Remove method of the PS\_DhcpServerv4OptionValue class
description: Deletes one more IPv4 option values at the server, scope or reservation level, either for the standard IPv4 options or for the specified vendor or user Class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 27d762fa-9be9-4739-803c-9ba01cdfcdc8
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DhcpServerv4OptionValue class
- PS_DhcpServerv4OptionValue class, Remove method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4OptionValue.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_DhcpServerv4OptionValue class

Deletes one more IPv4 option values at the server, scope or reservation level, either for the standard IPv4 options or for the specified vendor or user Class.

## Syntax


```mof
uint32 Remove(
  [in]  string                  VendorClass,
  [in]  string                  ComputerName,
  [in]  uint32                  OptionId[],
  [in]  string                  UserClass,
  [in]  string                  ScopeId,
  [in]  string                  ReservedIP,
  [in]  boolean                 PassThru,
  [in]  string                  PolicyName,
  [out] DhcpServerv4OptionValue cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*VendorClass* \[in\]
</dt> <dd>

If specified, the option values for the specified vendor class are deleted

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*OptionId* \[in\]
</dt> <dd>

Numeric identifier(s) of the option(s) which are to be deleted

</dd> <dt>

*UserClass* \[in\]
</dt> <dd>

If specified, the option values for the specified user class are deleted

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier (in IPv4 address format) from which the option values are to be deleted

</dd> <dt>

*ReservedIP* \[in\]
</dt> <dd>

IPv4 address of the reservation from which the option values are to be deleted

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Passes the object created by this cmdlet through the pipeline. By default, this cmdlet does not pass any objects through the pipeline.

</dd> <dt>

*PolicyName* \[in\]
</dt> <dd>

Name of the policy from which the option values are to be deleted

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

 

 





