---
title: MSFT\_TargetPortToVirtualDisk class
description: Association between TargetPort and VirtualDisk.
ms.assetid: EF675F41-FD41-4C95-97AD-6189ACF4032A
keywords:
- MSFT_TargetPortToVirtualDisk class Windows Storage Management API
- MSFT_TargetPortToVirtualDisk class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_TargetPortToVirtualDisk
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

# MSFT\_TargetPortToVirtualDisk class

Association between [**TargetPort**](msft-targetport.md) and [**VirtualDisk**](msft-virtualdisk.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_TargetPortToVirtualDisk
{
  MSFT_TargetPort  REF TargetPort;
  MSFT_VirtualDisk REF VirtualDisk;
};
```

## Members

The **MSFT\_TargetPortToVirtualDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_TargetPortToVirtualDisk** class has these properties.

<dl> <dt>

[**TargetPort**](msft-targetport.md)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_TargetPort**](msft-targetport.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

[**VirtualDisk**](msft-virtualdisk.md)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_VirtualDisk**](msft-virtualdisk.md)**
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

[**MSFT\_TargetPort**](msft-targetport.md)
</dt> <dt>

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
</dt> </dl>

 

 





