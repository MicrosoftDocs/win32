---
title: GetInterfaces method of the PS\_RemoteAccessLocal class
description: This method gives the Internet and intranet interfaces.
audience: developer
ms.assetid: '574b3346-d31a-49ae-bb3d-a11a32934709'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetInterfaces method", "GetInterfaces method, PS_RemoteAccessLocal class", "PS_RemoteAccessLocal class, GetInterfaces method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal.GetInterfaces
api_location:
- RAServerPSProvider.dll
api_type:
- COM
---

# GetInterfaces method of the PS\_RemoteAccessLocal class

This method gives the Internet and intranet interfaces.

## Syntax


```mof
uint32 GetInterfaces(
  [in, out] uint32  DeploymentMode,
  [in]      string  ConnectTo,
  [in]      boolean isNlbDeployed,
  [out]     string  IntranetInterfaces[],
  [out]     string  InternetInterfaces[]
);
```



## Parameters

<dl> <dt>

*DeploymentMode* \[in, out\]
</dt> <dd>

Indicates the mode in which the server is deployed:1 - indicates On Internet2 - indicates Behind NAT with Double NIC3 - indicates Behind NAT with Single NIC0 - indicates unknown

<dt>

<span id="0"></span>

**0** (0)


</dt> <dd></dd> <dt>

<span id="1"></span>

**1** (1)


</dt> <dd></dd> <dt>

<span id="2"></span>

**2** (2)


</dt> <dd></dd> <dt>

<span id="3"></span>

**3** (3)


</dt> <dd></dd> </dl> </dd> <dt>

*ConnectTo* \[in\]
</dt> <dd>

Address to which all clients will be connecting to

</dd> <dt>

*isNlbDeployed* \[in\]
</dt> <dd>

Indicates that NLB is deployed

</dd> <dt>

*IntranetInterfaces* \[out\]
</dt> <dd>

Array of intranet interfaces

</dd> <dt>

*InternetInterfaces* \[out\]
</dt> <dd>

Array of Internet interfaces

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| Header<br/>                   | <dl> <dt>Mbnapi.h</dt> </dl>               |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessLocal**](ps-remoteaccesslocal.md)
</dt> </dl>

 

 





