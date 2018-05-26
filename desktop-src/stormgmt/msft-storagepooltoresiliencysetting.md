---
title: MSFT\_StoragePoolToResiliencySetting class
description: Association between StoragePool and ResiliencySetting.
ms.assetid: 8EA9D275-ED5D-4901-B0CD-546247512800
keywords:
- MSFT_StoragePoolToResiliencySetting class Windows Storage Management API
- MSFT_StoragePoolToResiliencySetting class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StoragePoolToResiliencySetting
- MSFT_StoragePoolToResiliencySetting.StoragePool
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_StoragePoolToResiliencySetting class

Association between [**StoragePool**](msft-storagepool.md) and [**ResiliencySetting**](msft-resiliencysetting.md)

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StoragePoolToResiliencySetting
{
  MSFT_StoragePool       REF StoragePool;
  MSFT_ResiliencySetting REF ResiliencySetting;
};
```

## Members

The **MSFT\_StoragePoolToResiliencySetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StoragePoolToResiliencySetting** class has these properties.

<dl> <dt>

[**ResiliencySetting**](msft-resiliencysetting.md)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_ResiliencySetting**](msft-resiliencysetting.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**StoragePool**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StoragePool**](msft-storagepool.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

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

[**MSFT\_ResiliencySetting**](msft-resiliencysetting.md)
</dt> <dt>

[**MSFT\_StoragePool**](msft-storagepool.md)
</dt> </dl>

 

 





