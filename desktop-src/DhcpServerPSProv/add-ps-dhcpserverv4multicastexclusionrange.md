---
title: Add method of the PS\_DhcpServerv4MulticastExclusionRange class
description: Sets the range of addresses to exclude from a multicast scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1c4cdde0-0f8e-4440-9c1f-310bc94a6017
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DhcpServerv4MulticastExclusionRange class
- PS_DhcpServerv4MulticastExclusionRange class, Add method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4MulticastExclusionRange.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_DhcpServerv4MulticastExclusionRange class

Sets the range of addresses to exclude from a multicast scope

## Syntax


```mof
uint32 Add(
  [in]  string                              ComputerName,
  [in]  string                              Name,
  [in]  string                              StartRange,
  [in]  string                              EndRange,
  [in]  boolean                             PassThru,
  [out] DhcpServerv4MulticastExclusionRange cmdletOutput
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

Name of the multicast scope for which to set the IP address exclusion range

</dd> <dt>

*StartRange* \[in\]
</dt> <dd>

Start of the range of IP addresses to exclude from the Scope

</dd> <dt>

*EndRange* \[in\]
</dt> <dd>

End of the range of IP addresses to exclude from the Scope

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is added.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4MulticastExclusionRange**](dhcpserverv4multicastexclusionrange.md) class.

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

[**PS\_DhcpServerv4MulticastExclusionRange**](ps-dhcpserverv4multicastexclusionrange.md)
</dt> </dl>

 

 





