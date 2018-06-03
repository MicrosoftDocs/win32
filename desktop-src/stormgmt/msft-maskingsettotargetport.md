---
title: MSFT\_MaskingSetToTargetPort class
description: Association between MaskingSet and TargetPort.
ms.assetid: CBB7BA43-8506-474C-BE1B-58326AAECD8F
keywords:
- MSFT_MaskingSetToTargetPort class Windows Storage Management API
- MSFT_MaskingSetToTargetPort class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_MaskingSetToTargetPort
- MSFT_MaskingSetToTargetPort.MaskingSet
- MSFT_MaskingSetToTargetPort.TargetPort
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

# MSFT\_MaskingSetToTargetPort class

Association between [**MaskingSet**](msft-maskingset.md) and [**TargetPort**](msft-targetport.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_MaskingSetToTargetPort
{
  MSFT_MaskingSet REF MaskingSet;
  MSFT_TargetPort REF TargetPort;
};
```

## Members

The **MSFT\_MaskingSetToTargetPort** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_MaskingSetToTargetPort** class has these properties.

<dl> <dt>

**MaskingSet**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_MaskingSet**
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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_MaskingSet**](msft-maskingset.md)
</dt> <dt>

[**MSFT\_TargetPort**](msft-targetport.md)
</dt> </dl>

 

 





