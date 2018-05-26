---
title: MSFT\_SmbConnection class
description: Represents a connection established from an SMB client to an SMB server from the clients perspective.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 228d560d-5acd-4e0c-8ef4-aecd4d712b8f
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SmbConnection class SMB
- MSFT_SmbConnection class SMB , described
topic_type:
- apiref
api_name:
- MSFT_SmbConnection
- MSFT_SmbConnection.ServerName
- MSFT_SmbConnection.ShareName
- MSFT_SmbConnection.UserName
- MSFT_SmbConnection.SmbInstance
- MSFT_SmbConnection.Credential
- MSFT_SmbConnection.NumOpens
- MSFT_SmbConnection.Dialect
- MSFT_SmbConnection.ContinuouslyAvailable
- MSFT_SmbConnection.Encrypted
- MSFT_SmbConnection.Redirected
- MSFT_SmbConnection.Signed
api_location:
- SmbWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SmbConnection class

Represents a connection established from an SMB client to an SMB server from the client's perspective.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("smbwmiv2"), ClassVersion("7")]
class MSFT_SmbConnection
{
  string  ServerName;
  string  ShareName;
  string  UserName;
  uint32  SmbInstance;
  string  Credential;
  uint64  NumOpens;
  string  Dialect;
  boolean ContinuouslyAvailable;
  boolean Encrypted;
  boolean Redirected;
  boolean Signed;
};
```

## Members

The **MSFT\_SmbConnection** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SmbConnection** class has these methods.



| Method                                      | Description                                           |
|:--------------------------------------------|:------------------------------------------------------|
| [**Create**](create-msft-smbconnection.md) | Establishes a connection to an SMB server.<br/> |



 

### Properties

The **MSFT\_SmbConnection** class has these properties.

<dl> <dt>

**ContinuouslyAvailable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the connection is continuously available.

</dd> <dt>

**Credential**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The credential (domain + user name) that was used to establish the connection.

</dd> <dt>

**Dialect**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The SMB version.

</dd> <dt>

**Encrypted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the SMB connection is encrypted. For more information, see [SMB Encryption](https://technet.microsoft.com/library/dn551363.aspx#bkmk-smbencryption).

</dd> <dt>

**NumOpens**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of handles opened on the server and share.

</dd> <dt>

**Redirected**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the SMB connection was redirected.

</dd> <dt>

**ServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The server name.

</dd> <dt>

**ShareName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The name of the shared resource to which the connection is established.

</dd> <dt>

**Signed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the SMB connection is encrypted. If the SMB connection is encrypted (the **Encrypted** property is **True**) then the **Signed** property will be set to **False**, even though an encrypted connection is also signed. For more information, see [Require SMB Security Signatures](https://technet.microsoft.com/library/cc731957.aspx).

**Windows Server 2012 R2, Windows 8.1, Windows Server 2012 and Windows 8:** This property is not supported before Windows Server 2016 and Windows 10.

</dd> <dt>

**SmbInstance**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The identifier of the SMB server instance that hosts the shares.

**Windows Server 2012 and Windows 8:** This property is not supported before Windows Server 2012 R2 and Windows 8.1.

<dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>**Default** (0)


</dt> <dd></dd> <dt>

<span id="CSV"></span><span id="csv"></span>

<span id="CSV"></span><span id="csv"></span>**CSV** (1)


</dt> <dd>

Represents a Cluster Shared Volume (CSV).

**Windows 10 and Windows 8.1:** Cluster Shared Volumes are only supported on Windows Server systems.

</dd> <dt>

<span id="SBL"></span><span id="sbl"></span>

<span id="SBL"></span><span id="sbl"></span>**SBL** (2)


</dt> <dd>

Represents a Software Storage Bus used in Storage Spaces Direct.

**Windows Server 2012 R2:** This value is not supported before Windows Server 2016.

**Windows 10 and Windows 8.1:** Storage Spaces Direct is only supported on Windows Server systems.

</dd> <dt>

<span id="SR"></span><span id="sr"></span>

<span id="SR"></span><span id="sr"></span>**SR** (2)


</dt> <dd>

Represents a Storage Replica (SR).

**Windows Server 2012 R2:** This value is not supported before Windows Server 2016.

**Windows 10 and Windows 8.1:** Storage Replica is only supported on Windows Server systems.

</dd> </dl>

</dd> <dt>

**UserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The user name that was used to establish the connection.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



 

 





