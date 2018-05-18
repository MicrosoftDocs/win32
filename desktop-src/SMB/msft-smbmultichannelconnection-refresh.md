---
title: Refresh method of the MSFT\_SmbMultichannelConnection class
description: Refreshes an SMB connection network interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2C4F5A25-01B0-47FC-B3C4-8738490C1962'
ms.prod: 'windows-server-dev'
ms.technology:
- 'server-message-block-(smb)'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Refresh method SMB", "Refresh method SMB , MSFT_SmbMultichannelConnection interface", "MSFT_SmbMultichannelConnection interface SMB , Refresh method"]
topic_type:
- apiref
api_name:
- MSFT_SmbMultichannelConnection.Refresh
api_location:
- SmbWmiV2.dll
api_type:
- COM
---

# Refresh method of the MSFT\_SmbMultichannelConnection class

Refreshes an SMB connection network interface.

## Syntax


```mof
uint32 Refresh(
  [in] string ServerName
);
```



## Parameters

<dl> <dt>

*ServerName* \[in\]
</dt> <dd>

The server name. If this parameter is specified, only multichannel connections made to the specified server will be refreshed. Otherwise, multichannel connections to all servers will be refreshed.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SmbMultichannelConnection**](msft-smbmultichannelconnection.md)
</dt> </dl>

 

 





