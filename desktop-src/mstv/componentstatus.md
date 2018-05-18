---
title: ComponentStatus enumeration
description: Specifies the status of a sub-stream (component).
ms.assetid: '687ae778-0c25-47ca-bec9-9e6c28f22249'
keywords: ["ComponentStatus enumeration Microsoft TV Technologies"]
topic_type:
- apiref
api_name:
- ComponentStatus
api_location:
- bdatypes.h
api_type:
- HeaderDef
---

# ComponentStatus enumeration

Specifies the status of a sub-stream (component).

## Syntax


```C++
enum ComponentStatus {
  StatusActive       = 0, 
  StatusInactive     = 1, 
  StatusUnavailable  = 2 

};
```



## Constants

<dl> <dt>

<span id="StatusActive"></span><span id="statusactive"></span><span id="STATUSACTIVE"></span>**StatusActive**
</dt> <dd>

The component is active.

</dd> <dt>

<span id="StatusInactive"></span><span id="statusinactive"></span><span id="STATUSINACTIVE"></span>**StatusInactive**
</dt> <dd>

The component is inactive

</dd> <dt>

<span id="StatusUnavailable"></span><span id="statusunavailable"></span><span id="STATUSUNAVAILABLE"></span>**StatusUnavailable**
</dt> <dd>

The component is not available.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h (include Bdaiface.h)</dt> </dl> |



## See also

<dl> <dt>

[**IComponent::get\_Status**](icomponent-get-status.md)
</dt> <dt>

[Tuning Model Enumerations](tuning-model-enumerations.md)
</dt> </dl>

 

 





