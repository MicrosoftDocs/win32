---
title: MSFT\_StorageSubSystemToTargetPortal class
description: Association between StorageSubSystem and TargetPortal.
ms.assetid: 40AEE0E9-85C7-4DCA-AE74-17E26399CE08
keywords:
- MSFT_StorageSubSystemToTargetPortal class Windows Storage Management API
- MSFT_StorageSubSystemToTargetPortal class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToTargetPortal
- MSFT_StorageSubSystemToTargetPortal.StorageSubSystem
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

# MSFT\_StorageSubSystemToTargetPortal class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**TargetPortal**](msft-targetportal.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToTargetPortal
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_TargetPortal     REF TargetPortal;
};
```

## Members

The **MSFT\_StorageSubSystemToTargetPortal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToTargetPortal** class has these properties.

<dl> <dt>

**StorageSubSystem**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

[**TargetPortal**](msft-targetportal.md)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_TargetPortal**](msft-targetportal.md)**
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

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> <dt>

[**MSFT\_TargetPortal**](msft-targetportal.md)
</dt> </dl>

 

 





