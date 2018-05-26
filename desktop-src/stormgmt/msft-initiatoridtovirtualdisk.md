---
title: MSFT\_InitiatorIdToVirtualDisk class
description: Association between InitiatorId and VirtualDisk.
ms.assetid: A0E84922-4D13-4934-8F00-2C2809062713
keywords:
- MSFT_InitiatorIdToVirtualDisk class Windows Storage Management API
- MSFT_InitiatorIdToVirtualDisk class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_InitiatorIdToVirtualDisk
- MSFT_InitiatorIdToVirtualDisk.InitiatorId
- MSFT_InitiatorIdToVirtualDisk.VirtualDisk
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

# MSFT\_InitiatorIdToVirtualDisk class

Association between [**InitiatorId**](msft-initiatorid.md) and [**VirtualDisk**](msft-virtualdisk.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_InitiatorIdToVirtualDisk
{
  MSFT_InitiatorId REF InitiatorId;
  MSFT_VirtualDisk REF VirtualDisk;
};
```

## Members

The **MSFT\_InitiatorIdToVirtualDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_InitiatorIdToVirtualDisk** class has these properties.

<dl> <dt>

**InitiatorId**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_InitiatorId**](msft-initiatorid.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**VirtualDisk**
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

[**MSFT\_InitiatorId**](msft-initiatorid.md)
</dt> <dt>

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
</dt> </dl>

 

 





