---
title: MSFT\_StorageSubSystemToOffloadDataTransferSetting class
description: Association between StorageSubSystem and OffloadDataTransferSetting.
ms.assetid: '63E7794B-BD92-47AD-A1C3-0FF57B80AC2B'
keywords: ["MSFT_StorageSubSystemToOffloadDataTransferSetting class Windows Storage Management API", "MSFT_StorageSubSystemToOffloadDataTransferSetting class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToOffloadDataTransferSetting
- MSFT_StorageSubSystemToOffloadDataTransferSetting.StorageSubSystem
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageSubSystemToOffloadDataTransferSetting class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**OffloadDataTransferSetting**](msft-offloaddatatransfersetting.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToOffloadDataTransferSetting
{
  MSFT_StorageSubSystem           REF StorageSubSystem;
  MSFT_OffloadDataTransferSetting REF OffloadDataTransferSetting;
};
```

## Members

The **MSFT\_StorageSubSystemToOffloadDataTransferSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToOffloadDataTransferSetting** class has these properties.

<dl> <dt>

[**OffloadDataTransferSetting**](msft-offloaddatatransfersetting.md)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_OffloadDataTransferSetting**](msft-offloaddatatransfersetting.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**StorageSubSystem**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_OffloadDataTransferSetting**](msft-offloaddatatransfersetting.md)
</dt> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





