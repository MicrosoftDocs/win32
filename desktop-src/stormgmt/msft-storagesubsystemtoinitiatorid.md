---
title: MSFT\_StorageSubSystemToInitiatorId class
description: Association between StorageSubSystem and InitiatorId.
ms.assetid: 'C7F30596-DEA8-4179-8C2B-0F8F65248CF9'
keywords: ["MSFT_StorageSubSystemToInitiatorId class Windows Storage Management API", "MSFT_StorageSubSystemToInitiatorId class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToInitiatorId
- MSFT_StorageSubSystemToInitiatorId.StorageSubSystem
- MSFT_StorageSubSystemToInitiatorId.InitiatorId
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageSubSystemToInitiatorId class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**InitiatorId**](msft-initiatorid.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToInitiatorId
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_InitiatorId      REF InitiatorId;
};
```

## Members

The **MSFT\_StorageSubSystemToInitiatorId** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToInitiatorId** class has these properties.

<dl> <dt>

**InitiatorId**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_InitiatorId**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**StorageSubSystem**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_StorageSubSystem**
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

[**MSFT\_InitiatorId**](msft-initiatorid.md)
</dt> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





