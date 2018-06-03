---
title: Create method of the MSFT\_NetRoute class
description: Create the Route.
audience: developer
ms.assetid: 3fa129b4-c369-4b8d-b58a-a7e268475fb6
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Create method
- Create method, MSFT_NetRoute class
- MSFT_NetRoute class, Create method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Create method of the MSFT\_NetRoute class

Create the Route.

## Syntax


```mof
uint32 Create(
  [in]  uint32        InterfaceIndex,
  [in]  string        InterfaceAlias,
  [in]  string        DestinationPrefix,
  [in]  string        NextHop,
  [in]  uint8         Publish,
  [in]  uint16        RouteMetric,
  [in]  uint16        Protocol,
  [in]  datetime      ValidLifetime,
  [in]  datetime      PreferredLifetime,
  [in]  string        PolicyStore,
  [in]  uint16        AddressFamily,
  [in]  boolean       PassThru,
  [out] MSFT_NetRoute CmdletOutput[]
);
```



## Parameters

<dl> <dt>

*InterfaceIndex* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*InterfaceAlias* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*DestinationPrefix* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*NextHop* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Publish* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*RouteMetric* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Protocol* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*ValidLifetime* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*PreferredLifetime* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*PolicyStore* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*AddressFamily* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*CmdletOutput* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetRoute**](msft-netroute.md)
</dt> </dl>

 

 





