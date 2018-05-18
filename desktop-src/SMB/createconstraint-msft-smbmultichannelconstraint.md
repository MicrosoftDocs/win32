---
title: CreateConstraint method of the MSFT\_SmbMultichannelConstraint class
description: Creates a new Server Message Block (SMB) multichannel constraint for the specified server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '34282405-f136-4129-9cdb-e3dd631e9d52'
ms.prod: 'windows-server-dev'
ms.technology:
- 'server-message-block-(smb)'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateConstraint method SMB", "CreateConstraint method SMB , MSFT_SmbMultichannelConstraint class", "MSFT_SmbMultichannelConstraint class SMB , CreateConstraint method"]
topic_type:
- apiref
api_name:
- MSFT_SmbMultichannelConstraint.CreateConstraint
api_location:
- SmbWmiV2.dll
api_type:
- COM
---

# CreateConstraint method of the MSFT\_SmbMultichannelConstraint class

Creates a new Server Message Block (SMB) multichannel constraint for the specified server.

## Syntax


```mof
uint32 CreateConstraint(
  [in]  string                         ServerName,
  [in]  uint32                         InterfaceIndex[],
  [in]  string                         InterfaceAlias[],
  [out] MSFT_SmbMultichannelConstraint Output[]
);
```



## Parameters

<dl> <dt>

*ServerName* \[in\]
</dt> <dd>

Name of the server where the created [**MSFT\_SmbMultichannelConstraint**](msft-smbmultichannelconstraint.md) instance is used.

</dd> <dt>

*InterfaceIndex* \[in\]
</dt> <dd>

The interface indexes of the network interfaces that are used to connect to the server.

</dd> <dt>

*InterfaceAlias* \[in\]
</dt> <dd>

The interface aliases of the network interfaces that are used to connect to the server.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Embedded instances of the [**MSFT\_SmbMultichannelConstraint**](msft-smbmultichannelconstraint.md) class for the specified network interfaces.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>Smbwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SmbMultichannelConstraint**](msft-smbmultichannelconstraint.md)
</dt> </dl>

 

 





