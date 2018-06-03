---
title: MSFT\_OffloadDataTransferSetting class
description: Represents the offload data transfer (ODX) settings for a subsystem.
ms.assetid: DCE938F6-8901-409F-9CBB-CAAB1F38F9AA
keywords:
- MSFT_OffloadDataTransferSetting class Windows Storage Management API
- MSFT_OffloadDataTransferSetting class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_OffloadDataTransferSetting
- MSFT_OffloadDataTransferSetting.SupportInterSubsystem
- MSFT_OffloadDataTransferSetting.NumberOfTokensMax
- MSFT_OffloadDataTransferSetting.NumberOfTokensInUse
- MSFT_OffloadDataTransferSetting.OptimalDataTokenSize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_OffloadDataTransferSetting class

Represents the offload data transfer (ODX) settings for a subsystem.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_OffloadDataTransferSetting : MSFT_StorageObject
{
  Boolean SupportInterSubsystem;
  UInt32  NumberOfTokensMax;
  UInt32  NumberOfTokensInUse;
  UInt32  OptimalDataTokenSize;
};
```

## Members

The **MSFT\_OffloadDataTransferSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_OffloadDataTransferSetting** class has these properties.

<dl> <dt>

**NumberOfTokensInUse**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of tokens in use for the subsystem.

</dd> <dt>

**NumberOfTokensMax**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of tokens available for the subsystem.

</dd> <dt>

**OptimalDataTokenSize**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The optimal data token size, in bytes.

</dd> <dt>

**SupportInterSubsystem**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the subsystem supports transfer of data using tokens across different subsystems.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 





