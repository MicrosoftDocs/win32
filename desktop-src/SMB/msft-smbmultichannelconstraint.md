---
title: MSFT\_SmbMultichannelConstraint class
description: Represents a network interface that SMB can use to connect to a server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ce838603-b037-44d9-8478-5397f6e75db9
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SmbMultichannelConstraint class SMB
- MSFT_SmbMultichannelConstraint class SMB , described
topic_type:
- apiref
api_name:
- MSFT_SmbMultichannelConstraint
- MSFT_SmbMultichannelConstraint.ServerName
- MSFT_SmbMultichannelConstraint.InterfaceGuid
- MSFT_SmbMultichannelConstraint.InterfaceIndex
- MSFT_SmbMultichannelConstraint.InterfaceAlias
api_location:
- SmbWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SmbMultichannelConstraint class

Represents a network interface that SMB can use to connect to a server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("smbwmiv2"), ClassVersion("7")]
class MSFT_SmbMultichannelConstraint
{
  string ServerName;
  string InterfaceGuid;
  uint32 InterfaceIndex;
  string InterfaceAlias;
};
```

## Members

The **MSFT\_SmbMultichannelConstraint** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SmbMultichannelConstraint** class has these methods.



| Method                                                                      | Description                                                                                           |
|:----------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|
| [**CreateConstraint**](createconstraint-msft-smbmultichannelconstraint.md) | Creates a new Server Message Block (SMB) multichannel constraint for the specified server.<br/> |



 

### Properties

The **MSFT\_SmbMultichannelConstraint** class has these properties.

<dl> <dt>

**InterfaceAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Alias of the network interface.

</dd> <dt>

**InterfaceGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

GUID of the network interface.

</dd> <dt>

**InterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Index of the network interface.

</dd> <dt>

**ServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Name of the server to which the network interface connects.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>Smbwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



 

 





