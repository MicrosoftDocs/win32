---
title: MSFT\_StorageJobToAffectedStorageObject class
description: Association between a MSFT\_StorageJob and MSFT\_StorageObject objects that are affected by the job operation.
ms.assetid: 86056850-8918-4AD4-BAFC-EE73DEFF8958
keywords:
- MSFT_StorageJobToAffectedStorageObject class Windows Storage Management API
- MSFT_StorageJobToAffectedStorageObject class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageJobToAffectedStorageObject
- MSFT_StorageJobToAffectedStorageObject.StorageJob
- MSFT_StorageJobToAffectedStorageObject.AffectedStorageObject
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

# MSFT\_StorageJobToAffectedStorageObject class

Association between a [**MSFT\_StorageJob**](msft-storagejob.md) and [**MSFT\_StorageObject**](msft-storageobject.md) objects that are affected by the job operation.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageJobToAffectedStorageObject
{
  MSFT_StorageJob    REF StorageJob;
  MSFT_StorageObject REF AffectedStorageObject;
};
```

## Members

The **MSFT\_StorageJobToAffectedStorageObject** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageJobToAffectedStorageObject** class has these properties.

<dl> <dt>

**AffectedStorageObject**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageObject**](msft-storageobject.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The storage object that is affected by the job operation.

</dd> <dt>

**StorageJob**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageJob**](msft-storagejob.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The job object for the storage job.

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

[**MSFT\_StorageJob**](msft-storagejob.md)
</dt> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 





