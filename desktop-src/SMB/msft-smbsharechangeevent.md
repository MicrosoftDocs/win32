---
title: MSFT\_SmbShareChangeEvent class
description: This is an indication class. Any subscriber to it will receive an indication whenever a share is created, deleted, or modified.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2934f452-9cc0-49f9-b505-93e58a0c1dac
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SmbShareChangeEvent class SMB
- MSFT_SmbShareChangeEvent class SMB , described
topic_type:
- apiref
api_name:
- MSFT_SmbShareChangeEvent
- MSFT_SmbShareChangeEvent.EventType
- MSFT_SmbShareChangeEvent.Share
api_location:
- SmbWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SmbShareChangeEvent class

This is an indication class. Any subscriber to it will receive an indication whenever a share is created, deleted, or modified.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Indication, dynamic, provider("smbwmiv2"), ClassVersion("7")]
class MSFT_SmbShareChangeEvent
{
  uint32        EventType;
  MSFT_SmbShare Share;
};
```

## Members

The **MSFT\_SmbShareChangeEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SmbShareChangeEvent** class has these properties.

<dl> <dt>

**EventType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The event type.

<dt>

<span id="Add"></span><span id="add"></span><span id="ADD"></span>

**Add** (0)


</dt> <dd></dd> <dt>

<span id="Modify"></span><span id="modify"></span><span id="MODIFY"></span>

**Modify** (1)


</dt> <dd></dd> <dt>

<span id="Remove"></span><span id="remove"></span><span id="REMOVE"></span>

**Remove** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**Share**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SmbShare**](msft-smbshare.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_SmbShare**](msft-smbshare.md)")
</dt> </dl>

An instance of the [**MSFT\_SmbShare**](msft-smbshare.md) class that represents the share.

</dd> </dl>

## Remarks

> [!Note]  
> Subscribers must be administrators.

 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



 

 





