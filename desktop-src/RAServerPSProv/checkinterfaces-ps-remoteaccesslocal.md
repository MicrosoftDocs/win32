---
title: CheckInterfaces method of the PS\_RemoteAccessLocal class
description: This method validates the interfaces that are passed here are of profile what they say they are.
audience: developer
ms.assetid: 'a728539b-85f6-4f37-a8b4-032025b9d951'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CheckInterfaces method", "CheckInterfaces method, PS_RemoteAccessLocal class", "PS_RemoteAccessLocal class, CheckInterfaces method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal.CheckInterfaces
api_location:
- RAServerPSProvider.dll
api_type:
- COM
---

# CheckInterfaces method of the PS\_RemoteAccessLocal class

This method validates the interfaces that are passed here are of profile what they say they are.

## Syntax


```mof
uint32 CheckInterfaces(
  [in]  string  IntranetInterface,
  [in]  string  InternetInterface,
  [in]  boolean BehindNat,
  [in]  string  ConnectTo,
  [in]  boolean isNlbDeployed,
  [out] boolean Status
);
```



## Parameters

<dl> <dt>

*IntranetInterface* \[in\]
</dt> <dd>

Intranet Interface to check

</dd> <dt>

*InternetInterface* \[in\]
</dt> <dd>

Internet Interface to check

</dd> <dt>

*BehindNat* \[in\]
</dt> <dd>

Indicates whether the server is behind a NAT box

</dd> <dt>

*ConnectTo* \[in\]
</dt> <dd>

Address to which all clients will be connecting to

</dd> <dt>

*isNlbDeployed* \[in\]
</dt> <dd>

Indicates that NLB is deployed

</dd> <dt>

*Status* \[out\]
</dt> <dd>

Indication whether the method has succeeded or failed.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessLocal**](ps-remoteaccesslocal.md)
</dt> </dl>

 

 





