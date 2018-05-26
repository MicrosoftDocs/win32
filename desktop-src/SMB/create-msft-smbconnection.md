---
title: Create method of the MSFT\_SmbConnection class
description: Establishes a connection to an SMB server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a7cde6bf-262b-405e-ae95-c98e9a6250f3
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Create method SMB
- Create method SMB , MSFT_SmbConnection class
- MSFT_SmbConnection class SMB , Create method
topic_type:
- apiref
api_name:
- MSFT_SmbConnection.Create
api_location:
- SmbWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Create method of the MSFT\_SmbConnection class

Establishes a connection to an SMB server.

## Syntax


```mof
uint32 Create(
  [in]  string             LocalPath,
  [in]  string             RemotePath,
  [in]  string             UserName,
  [in]  string             Password,
  [in]  boolean            Persistent,
  [in]  boolean            SaveCredentials,
  [in]  boolean            HomeFolder,
  [out] MSFT_SmbConnection CreatedConnection
);
```



## Parameters

<dl> <dt>

*LocalPath* \[in\]
</dt> <dd>

The local path to which the remote share will be mapped.

</dd> <dt>

*RemotePath* \[in\]
</dt> <dd>

The path of the remote share to which a connection will be established.

</dd> <dt>

*UserName* \[in\]
</dt> <dd>

The user name that will be used to establish the connection.

</dd> <dt>

*Password* \[in\]
</dt> <dd>

The password that will be used to establish the connection.

</dd> <dt>

*Persistent* \[in\]
</dt> <dd>

Controls whether the connection will be persistent.

</dd> <dt>

*SaveCredentials* \[in\]
</dt> <dd>

Determines whether or not credentials are saved and used when a mapping is created against the same server.

</dd> <dt>

*HomeFolder* \[in\]
</dt> <dd>

Controls whether the connection will be made to the user s home folder.

</dd> <dt>

*CreatedConnection* \[out\]
</dt> <dd>

This parameter returns the [**MSFT\_SmbConnection**](msft-smbconnection.md) object created with this call.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SmbConnection**](msft-smbconnection.md)
</dt> </dl>

 

 





