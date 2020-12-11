---
title: IMsTscAxEvents OnMouseInputModeChanged method
description: Called when the mouse input mode has changed.
ms.assetid: d0554c59-967d-4181-98cd-9e88dde32752
ms.tgt_platform: multiple
keywords:
- OnMouseInputModeChanged method Remote Desktop Services
- OnMouseInputModeChanged method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnMouseInputModeChanged method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnMouseInputModeChanged
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnMouseInputModeChanged method

Called when the mouse input mode has changed.

## Syntax


```C++
void OnMouseInputModeChanged(
  [in] VARIANT_BOOL fMouseModeRelative
);
```



## Parameters

<dl> <dt>

*fMouseModeRelative* \[in\]
</dt> <dd>

Indicates whether the mouse is in relative mode.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Implement this method in your event sink to receive notification that the mouse input mode has changed.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IMsTscAxEvents is defined as 336d5562-efa8-482e-8cb3-c5c0fc7a7db6<br/>           |



## See also

<dl> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

 





