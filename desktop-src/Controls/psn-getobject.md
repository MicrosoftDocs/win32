---
title: PSN_GETOBJECT notification code (Prsht.h)
description: Sent by a property sheet to request a drop target object when the cursor passes over one of the tab control's buttons. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 179ac47c-9b32-4682-866d-1a1fad85080c
keywords:
- PSN_GETOBJECT notification code Windows Controls
topic_type:
- apiref
api_name:
- PSN_GETOBJECT
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PSN\_GETOBJECT notification code

Sent by a property sheet to request a drop target object when the cursor passes over one of the tab control's buttons. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
PSN_GETOBJECT

    lpnmon = (LPNMOBJECTNOTIFY) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMOBJECTNOTIFY**](/windows/win32/api/commctrl/ns-commctrl-nmobjectnotify) structure that, on entry, contains information about the notification code. If this notification code is processed, you must insert object information into this structure.

</dd> </dl>

## Return value

The application processing this notification code must return zero.

## Remarks

To provide an object, an application must set values in some members of the [**NMOBJECTNOTIFY**](/windows/win32/api/commctrl/ns-commctrl-nmobjectnotify) structure at *lParam*. The **pObject** member must be set to a valid object pointer, and the **hResult** member must be set to a success flag. To comply with Component Object Model (COM) standards, always increment the object's reference count when providing an object pointer.

If an application does not provide an object, it must set **pObject** to **NULL** and **hResult** to a failure flag.

> [!Note]  
> This notification code is not supported when using the Aero wizard style ([**PSH\_AEROWIZARD**](/windows/desktop/api/Prsht/ns-prsht-propsheetheadera_v2)).

 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





