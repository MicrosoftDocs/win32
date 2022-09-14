---
title: EM_GETIMESTATUS message (Winuser.h)
description: Gets a set of status flags that indicate how the edit control interacts with the Input Method Editor (IME).
ms.assetid: 56705aed-afab-4f4d-9e0b-dc533b516a15
keywords:
- EM_GETIMESTATUS message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETIMESTATUS
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETIMESTATUS message

Gets a set of status flags that indicate how the edit control interacts with the Input Method Editor (IME).

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The type of status to retrieve. This parameter can be the following value.



| Value                                                                                                                                                                                       | Meaning                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <span id="EMSIS_COMPOSITIONSTRING"></span><span id="emsis_compositionstring"></span><dl> <dt>**EMSIS\_COMPOSITIONSTRING**</dt> </dl> | Sets behavior for handling the composition string.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Data specific to the type of status to retrieve. With the **EMSIS\_COMPOSITIONSTRING** value for *status*, this return value is one or more of the following values.



| Return code                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**EIMES\_GETCOMPSTRATONCE**</dt> </dl>         | If this flag is set, the edit control hooks the [**WM\_IME\_COMPOSITION**](/windows/desktop/Intl/wm-ime-composition) message with *fFlags* set to GCS\_RESULTSTR and returns the result string immediately. If this flag is not set, the edit control passes the **WM\_IME\_COMPOSITION** message to the default window procedure and processes the result string from the [**WM\_CHAR**](/windows/desktop/inputdev/wm-char) message; this is the default behavior of the edit control.<br/> |
| <dl> <dt>**EIMES\_CANCELCOMPSTRINFOCUS**</dt> </dl>     | If this flag is set, the edit control cancels the composition string when it receives the [**WM\_SETFOCUS**](/windows/desktop/inputdev/wm-setfocus) message. If this flag is not set, the edit control does not cancel the composition string; this is the default behavior of the edit control.<br/>                                                                                                                                                                       |
| <dl> <dt>**EIMES\_COMPLETECOMPSTRKILLFOCUS**</dt> </dl> | If this flag is set, the edit control completes the composition string upon receiving the [**WM\_KILLFOCUS**](/windows/desktop/inputdev/wm-killfocus) message. If this flag is not set, the edit control does not complete the composition string; this is the default behavior of the edit control.<br/>                                                                                                                                                                   |



 

## Remarks

**Rich Edit:** The **EM\_GETIMESTATUS** message is not supported.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**EM\_SETIMESTATUS**](em-setimestatus.md)
</dt> </dl>

 

