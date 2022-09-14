---
title: TB_ADDSTRING message (Commctrl.h)
description: Adds a new string to the toolbar's string pool.
ms.assetid: e22ee2cc-6443-49d3-aea6-a4ab256d4538
keywords:
- TB_ADDSTRING message Windows Controls
topic_type:
- apiref
api_name:
- TB_ADDSTRING
- TB_ADDSTRINGA
- TB_ADDSTRINGW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_ADDSTRING message

Adds a new string to the toolbar's string pool.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Handle to the module instance with an executable file that contains the string resource. If *lParam* instead points to a character array with one or more strings, set this parameter to **NULL**.

</dd> <dt>

*lParam* 
</dt> <dd>

Resource identifier for the string resource, or a pointer to a TCHAR array. See Remarks.

</dd> </dl>

## Return value

Returns the index of the first new string if successful, or -1 otherwise.

## Remarks

If *wParam* is **NULL**, *lParam* points to a character array with one or more null-terminated strings. The last string in the array must be terminated with two null characters.

If *wParam* is the HINSTANCE of the application or of another module containing a string resource, *lParam* is the resource identifier of the string. Each item in the string must begin with an arbitrary separator character, and the string must end with two such characters. For example, the text for three buttons might appear in the string table as "/New/Open/Save//". The message returns the index of "New" in the toolbar's string pool, and the other items are in consecutive positions.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TB\_ADDSTRINGW** (Unicode) and **TB\_ADDSTRINGA** (ANSI)<br/>                 |



 

 





