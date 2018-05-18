---
title: MSFT\_StorageModificationEvent class
description: Represents a storage modification event. Storage modification events are used when the underlying state of an object has changed.
ms.assetid: '7AD4584D-09DA-40BB-B686-AD704119A78B'
keywords: ["MSFT_StorageModificationEvent class Windows Storage Management API", "MSFT_StorageModificationEvent class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageModificationEvent
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageModificationEvent class

Represents a storage modification event. Storage modification events are used when the underlying state of an object has changed.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Indication]
class MSFT_StorageModificationEvent : MSFT_StorageEvent
{
};
```

## Members

The **MSFT\_StorageModificationEvent** class does not define any members.

## Remarks

Not all properties should be tracked (for example, **AllocatedSize** may change so frequently that sending events would be impractical). At a minimum, an event should be sent any time an object's **HealthStatus** or **OperationalStatus** properties change.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageEvent**](msft-storageevent.md)
</dt> </dl>

 

 





