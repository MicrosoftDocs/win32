---
title: MSFT\_SmbBandwidthLimit class
description: Represents an SMB bandwidth limit, which is used to throttle SMB traffic.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: DEF282BB-F642-4F34-B51D-B5237E86BE3A
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SmbBandwidthLimit class SMB
- MSFT_SmbBandwidthLimit class SMB , described
topic_type:
- apiref
api_name:
- MSFT_SmbBandwidthLimit
- MSFT_SmbBandwidthLimit.Category
- MSFT_SmbBandwidthLimit.BytesPerSecond
api_location:
- SmbWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SmbBandwidthLimit class

Represents an SMB bandwidth limit, which is used to throttle SMB traffic.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[dynamic, provider("smbwmiv2"), ClassVersion("7")]
class MSFT_SmbBandwidthLimit
{
  uint32 Category;
  uint64 BytesPerSecond;
};
```

## Members

The **MSFT\_SmbBandwidthLimit** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SmbBandwidthLimit** class has these methods.



| Method                                    | Description                                                                         |
|:------------------------------------------|:------------------------------------------------------------------------------------|
| [**Set**](msft-smbbandwidthlimit-set.md) | Specifies the bandwidth limit for SMB traffic of the specified category.<br/> |



 

### Properties

The **MSFT\_SmbBandwidthLimit** class has these properties.

<dl> <dt>

**BytesPerSecond**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the bandwidth limit in bytes per second.

</dd> <dt>

**Category**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the type of SMB traffic.

<dt>

<span id="9"></span>

<span id="9"></span>**9** (0)


</dt> <dd>

Regular Hyper-V over SMB traffic. Default.

</dd> <dt>

<span id="53"></span>

<span id="53"></span>**53** (1)


</dt> <dd>

VirtualMachine.

</dd> <dt>

<span id="54"></span>

<span id="54"></span>**54** (2)


</dt> <dd>

LiveMigration.

</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                       |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[SMB Management API](smb-management-api-portal.md)
</dt> </dl>

 

 





