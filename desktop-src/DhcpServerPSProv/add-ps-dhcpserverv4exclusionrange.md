---
title: Add method of the PS\_DhcpServerv4ExclusionRange class
description: Adds a range of excluded IP addresses for an IPv4 scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bc11d683-b1d0-4e2d-897c-2d4faa7c93cf
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DhcpServerv4ExclusionRange class
- PS_DhcpServerv4ExclusionRange class, Add method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4ExclusionRange.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_DhcpServerv4ExclusionRange class

Adds a range of excluded IP addresses for an IPv4 scope.

## Syntax


```mof
uint32 Add(
  [in]  string                     ComputerName,
  [in]  string                     ScopeId,
  [in]  string                     StartRange,
  [in]  string                     EndRange,
  [in]  boolean                    PassThru,
  [out] DhcpServerv4ExclusionRange cmdletOutput
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

The id of the IPv4 scope from which the IP addresses are being excluded.

</dd> <dt>

*StartRange* \[in\]
</dt> <dd>

The start IP address of the range being excluded

</dd> <dt>

*EndRange* \[in\]
</dt> <dd>

The end IP address of the range being excluded

</dd> <dt>

*PassThru* \[in\]
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

 

 





