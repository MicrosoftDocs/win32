---
title: Set method of the PS\_RemoteAccessConfiguration class
description: Updates a remote access configuration.
audience: developer
ms.assetid: '8610d02b-1bab-4faf-82b5-b89db296d85a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_RemoteAccessConfiguration class", "PS_RemoteAccessConfiguration class, Set method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessConfiguration.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Set method of the PS\_RemoteAccessConfiguration class

Updates a remote access configuration.

## Syntax


```mof
static uint32 Set(
  [in]  RemoteAccessConfiguration Configuration,
  [in]  boolean                   RestartServiceIfRequired,
  [in]  boolean                   PassThru,
  [out] RemoteAccessConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*Configuration* \[in\]
</dt> <dd>

The remote access configuration to update.

</dd> <dt>

*RestartServiceIfRequired* \[in\]
</dt> <dd>

Indicates whether to restart the service after a service update.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether the *cmdletOutput* parameter returns and object. **True** to return and object; otherwise **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**RemoteAccessConfiguration**](remoteaccessconfiguration.md) object that receives the updated remote access configuration information.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessConfiguration**](ps-remoteaccessconfiguration.md)
</dt> </dl>

 

 





