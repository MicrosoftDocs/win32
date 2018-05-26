---
title: Remove method of the PS\_DhcpServerv4MulticastScope class
description: Remove the specified multicast scope(s) from the DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5db6ac84-d5dc-45c3-8ba1-7984117ab446
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DhcpServerv4MulticastScope class
- PS_DhcpServerv4MulticastScope class, Remove method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4MulticastScope.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_DhcpServerv4MulticastScope class

Remove the specified multicast scope(s) from the DHCP Server.

## Syntax


```mof
uint32 Remove(
  [in]  string                     ComputerName,
  [in]  string                     Name[],
  [in]  boolean                    Force,
  [in]  boolean                    PassThru,
  [out] DhcpServerv4MulticastScope cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Names of multicast scopes

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, deletes the scope even if there are active leases in the scope

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether this method returns the [**DhcpServerv4MulticastScope**](dhcpserverv4multicastscope.md) object. **True** returns the object, **False** does not.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4MulticastScope**](dhcpserverv4multicastscope.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4MulticastScope**](ps-dhcpserverv4multicastscope.md)
</dt> </dl>

 

 





