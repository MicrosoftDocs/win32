---
title: Remove method of the PS\_DhcpServerv4ExclusionRange class
description: Deletes a range of IPv4 addresses previously excluded from an IPv4 Scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 37173d7b-20a2-48bb-af70-c09b133f5a5b
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DhcpServerv4ExclusionRange class
- PS_DhcpServerv4ExclusionRange class, Remove method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4ExclusionRange.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_DhcpServerv4ExclusionRange class

Deletes a range of IPv4 addresses previously excluded from an IPv4 Scope.

## Syntax


```mof
uint32 Remove(
  [in]  string                     ComputerName,
  [in]  string                     ScopeId,
  [in]  string                     StartRange,
  [in]  string                     EndRange,
  [in]  boolean                    Passthru,
  [out] DhcpServerv4ExclusionRange cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier (in IPv4 address format) from which the exclusion ranges are to be deleted

</dd> <dt>

*StartRange* \[in\]
</dt> <dd>

Start IP address of the excluded IP range which is to be deleted

</dd> <dt>

*EndRange* \[in\]
</dt> <dd>

End IP address of the excluded IP range which is to be deleted

</dd> <dt>

*Passthru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet return the PowerShell objects which are deleted.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4ExclusionRange**](dhcpserverv4exclusionrange.md) object.

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

[**PS\_DhcpServerv4ExclusionRange**](ps-dhcpserverv4exclusionrange.md)
</dt> </dl>

 

 





