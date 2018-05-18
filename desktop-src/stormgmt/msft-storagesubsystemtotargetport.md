---
title: MSFT\_StorageSubSystemToTargetPort class
description: Association between StorageSubSystem and TargetPort.
ms.assetid: '70E186A0-7FBB-4EFB-ADAA-7EE7068DCF6F'
keywords: ["MSFT_StorageSubSystemToTargetPort class Windows Storage Management API", "MSFT_StorageSubSystemToTargetPort class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToTargetPort
- MSFT_StorageSubSystemToTargetPort.StorageSubSystem
- MSFT_StorageSubSystemToTargetPort.TargetPort
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageSubSystemToTargetPort class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**TargetPort**](msft-targetport.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToTargetPort
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_TargetPort       REF TargetPort;
};
```

## Members

The **MSFT\_StorageSubSystemToTargetPort** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToTargetPort** class has these properties.

<dl> <dt>

**StorageSubSystem**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_StorageSubSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**TargetPort**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_TargetPort**
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

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> <dt>

[**MSFT\_TargetPort**](msft-targetport.md)
</dt> </dl>

 

 





