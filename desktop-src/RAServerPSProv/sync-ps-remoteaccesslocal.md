---
title: Sync method of the PS\_RemoteAccessLocal class
description: This method will trigger the process to synchronize the DA server with the Group Policy.
audience: developer
ms.assetid: '2812cece-ec5b-4137-bf1e-f27d620f326b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Sync method", "Sync method, PS_RemoteAccessLocal class", "PS_RemoteAccessLocal class, Sync method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal.Sync
api_location:
- RAServerPSProvider.dll
api_type:
- COM
---

# Sync method of the PS\_RemoteAccessLocal class

This method will trigger the process to synchronize the DA server with the Group Policy.

## Syntax


```mof
uint32 Sync(
  [in] uint32 Options
);
```



## Parameters

<dl> <dt>

*Options* \[in\]
</dt> <dd>

Bitmask parameter that indicates the type of Group Policy update to be applied on the server. 1st bit - Delayed Group Policy update will be triggered.

2nd bit - Immediate Group Policy update will to be triggered.

3rd bit - The call will wait for the raconfigtask to start.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| Header<br/>                   | <dl> <dt>Mlang.h</dt> </dl>                |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessLocal**](ps-remoteaccesslocal.md)
</dt> </dl>

 

 





