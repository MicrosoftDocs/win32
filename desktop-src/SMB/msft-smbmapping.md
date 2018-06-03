---
title: MSFT\_SmbMapping class
description: Represents an SMB mapping.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: F8D70743-6EE5-4DE1-AA4E-BCDBEB7D38A9
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SmbMapping class SMB
- MSFT_SmbMapping class SMB , described
topic_type:
- apiref
api_name:
- MSFT_SmbMapping
- MSFT_SmbMapping.LocalPath
- MSFT_SmbMapping.RemotePath
- MSFT_SmbMapping.Status
api_location:
- SmbWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SmbMapping class

Represents an SMB mapping.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[dynamic, provider("smbwmiv2"), ClassVersion("7")]
class MSFT_SmbMapping
{
  string LocalPath;
  string RemotePath;
  uint32 Status;
};
```

## Members

The **MSFT\_SmbMapping** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SmbMapping** class has these methods.



| Method                                   | Description                        |
|:-----------------------------------------|:-----------------------------------|
| [**Create**](msft-smbmapping-create.md) | Creates an SMB mapping.<br/> |
| [**Remove**](msft-smbmapping-remove.md) | Removes an SMB mapping.<br/> |



 

### Properties

The **MSFT\_SmbMapping** class has these properties.

<dl> <dt>

**LocalPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The local path for the shared resource.

</dd> <dt>

**RemotePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The remote path for the shared resource.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Status of the SMB mapping.

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** (0)


</dt> <dd></dd> <dt>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>

**Paused** (1)


</dt> <dd></dd> <dt>

<span id="Disconnected"></span><span id="disconnected"></span><span id="DISCONNECTED"></span>

**Disconnected** (2)


</dt> <dd></dd> <dt>

<span id="NetworkError"></span><span id="networkerror"></span><span id="NETWORKERROR"></span>

**NetworkError** (3)


</dt> <dd></dd> <dt>

<span id="Connecting"></span><span id="connecting"></span><span id="CONNECTING"></span>

**Connecting** (4)


</dt> <dd></dd> <dt>

<span id="Reconnecting"></span><span id="reconnecting"></span><span id="RECONNECTING"></span>

**Reconnecting** (5)


</dt> <dd></dd> <dt>

<span id="Unavailable"></span><span id="unavailable"></span><span id="UNAVAILABLE"></span>

**Unavailable** (6)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



 

 





