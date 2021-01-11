---
description: Sent to an application when the IME changes composition status as a result of a keystroke. A window receives this message through its WindowProc function.
ms.assetid: 6de1c4c2-d910-487c-8b82-408cb6e02c44
title: WM_IME_COMPOSITION message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_IME\_COMPOSITION message

Sent to an application when the IME changes composition status as a result of a keystroke. A window receives this message through its [*WindowProc*](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
LRESULT CALLBACK WindowProc(
  HWND  hwnd,     
  WM_IME_COMPOSITION,   
  WPARAM wParam,
  LPARAM lParam          
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

A handle to window.

</dd> <dt>

*wParam* 
</dt> <dd>

DBCS character representing the latest change to the composition string.

</dd> <dt>

*lParam* 
</dt> <dd>

Value specifying how the composition string or character changed. This parameter can be one or more of the following values. For more information about these values, see [IME Composition String Values](ime-composition-string-values.md).

<dl><span id="GCS_COMPATTR"></span><span id="gcs_compattr"></span><dt>

**GCS\_COMPATTR**
</dt><span id="GCS_COMPCLAUSE"></span><span id="gcs_compclause"></span><dt>

**GCS\_COMPCLAUSE**
</dt><span id="GCS_COMPREADSTR"></span><span id="gcs_compreadstr"></span><dt>

**GCS\_COMPREADSTR**
</dt><span id="GCS_COMPREADATTR"></span><span id="gcs_compreadattr"></span><dt>

**GCS\_COMPREADATTR**
</dt><span id="GCS_COMPREADCLAUSE"></span><span id="gcs_compreadclause"></span><dt>

**GCS\_COMPREADCLAUSE**
</dt><span id="GCS_COMPSTR"></span><span id="gcs_compstr"></span><dt>

**GCS\_COMPSTR**
</dt><span id="GCS_CURSORPOS"></span><span id="gcs_cursorpos"></span><dt>

**GCS\_CURSORPOS**
</dt><span id="GCS_DELTASTART"></span><span id="gcs_deltastart"></span><dt>

**GCS\_DELTASTART**
</dt><span id="GCS_RESULTCLAUSE"></span><span id="gcs_resultclause"></span><dt>

**GCS\_RESULTCLAUSE**
</dt><span id="GCS_RESULTREADCLAUSE"></span><span id="gcs_resultreadclause"></span><dt>

**GCS\_RESULTREADCLAUSE**
</dt><span id="GCS_RESULTREADSTR"></span><span id="gcs_resultreadstr"></span><dt>

**GCS\_RESULTREADSTR**
</dt><span id="GCS_RESULTSTR"></span><span id="gcs_resultstr"></span><dt>

**GCS\_RESULTSTR**
</dt> </dl>

The *lParam* parameter can also have one or more of the following values.



| Value                                                                                                                                                            | Meaning                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CS_INSERTCHAR"></span><span id="cs_insertchar"></span><dl> <dt>**CS\_INSERTCHAR**</dt> </dl>    | Insert the *wParam* composition character at the current insertion point. An application should display the composition character if it processes this message.<br/>                                                                                                                                                                                                                                |
| <span id="CS_NOMOVECARET"></span><span id="cs_nomovecaret"></span><dl> <dt>**CS\_NOMOVECARET**</dt> </dl> | Do not move the caret position as a result of processing the message. For example, if an IME specifies a combination of CS\_INSERTCHAR and CS\_NOMOVECARET, the application should insert the specified character at the current caret position but should not move the caret to the next position. A subsequent WM\_IME\_COMPOSITION message with GCS\_RESULTSTR will replace this character.<br/> |



 

</dd> </dl>

## Return value

This message has no return value.

## Remarks

An application should process this message if it displays composition characters itself. Otherwise, it should send the message to the IME window.

If the application has created an IME window, it should pass this message to that window. The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)  function processes this message by passing it to the default IME window. The IME window processes this message by updating its appearance based on the change flag specified. An application can call [**ImmGetCompositionString**](/windows/desktop/api/Imm/nf-imm-immgetcompositionstringa) to retrieve the new composition status.

If none of the GCS\_ values are set, the message indicates that the current composition has been canceled and applications that draw the composition string should delete the string.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                                                      |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h); </dt> <dt>Imm.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Input Method Manager](input-method-manager.md)
</dt> <dt>

[Input Method Manager Messages](input-method-manager-messages.md)
</dt> <dt>

[**ImmGetCompositionString**](/windows/desktop/api/Imm/nf-imm-immgetcompositionstringa)
</dt> </dl>

 

 
