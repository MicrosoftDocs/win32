---
title: MoveClient method of the MSFT\_SmbWitnessClient class
description: Moves an SMB witness client that is connected to a scale-out cluster node to a different scale-out cluster node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 770CA7F9-8B4E-4FBA-B9BA-F31D938AA39E
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MoveClient method SMB
- MoveClient method SMB , MSFT_SmbWitnessClient interface
- MSFT_SmbWitnessClient interface SMB , MoveClient method
topic_type:
- apiref
api_name:
- MSFT_SmbWitnessClient.MoveClient
api_location:
- WitnessWmiv2Provider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MoveClient method of the MSFT\_SmbWitnessClient class

Moves an SMB witness client that is connected to a scale-out cluster node to a different scale-out cluster node.

## Syntax


```mof
uint32 MoveClient(
  [in] string ClientName,
  [in] string DestinationNode,
  [in] string NetworkName
);
```



## Parameters

<dl> <dt>

*ClientName* \[in\]
</dt> <dd>

The name of the SMB witness client.

</dd> <dt>

*DestinationNode* \[in\]
</dt> <dd>

The name of the scale-out cluster node to which the client is to be moved.

</dd> <dt>

*NetworkName* \[in\]
</dt> <dd>

The name of the network to which the client is to be moved.

**Windows Server 2012 and Windows 8:** This parameter is not supported before Windows Server 2012 R2 and Windows 8.1.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\SmbWitness<br/>                                                        |
| MOF<br/>                      | <dl> <dt>SmbWitnessWmiv2Provider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WitnessWmiv2Provider.dll</dt> </dl>    |



## See also

<dl> <dt>

[**MSFT\_SmbWitnessClient**](msft-smbwitnessclient-.md)
</dt> </dl>

 

 





