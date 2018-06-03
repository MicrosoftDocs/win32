---
title: MSFT\_MaskingSetToVirtualDisk class
description: Association between MaskingSet and VirtualDisk.
ms.assetid: 4E5328D1-655B-45A5-9D76-A2042377F7F1
keywords:
- MSFT_MaskingSetToVirtualDisk class Windows Storage Management API
- MSFT_MaskingSetToVirtualDisk class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_MaskingSetToVirtualDisk
- MSFT_MaskingSetToVirtualDisk.MaskingSet
- MSFT_MaskingSetToVirtualDisk.VirtualDisk
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

# MSFT\_MaskingSetToVirtualDisk class

Association between [**MaskingSet**](msft-maskingset.md) and [**VirtualDisk**](msft-virtualdisk.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_MaskingSetToVirtualDisk
{
  MSFT_MaskingSet  REF MaskingSet;
  MSFT_VirtualDisk REF VirtualDisk;
};
```

## Members

The **MSFT\_MaskingSetToVirtualDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_MaskingSetToVirtualDisk** class has these properties.

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

**VirtualDisk**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_VirtualDisk**
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

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
</dt> </dl>

 

 





