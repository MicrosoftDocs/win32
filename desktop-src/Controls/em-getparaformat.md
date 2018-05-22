---
title: EM\_GETPARAFORMAT message
description: Retrieves the paragraph formatting of the current selection in a rich edit control.
ms.assetid: '79a7d34f-5da1-452d-b31f-b2eec913f5cb'
keywords: ["EM_GETPARAFORMAT message Windows Controls"]
topic_type:
- apiref
api_name:
- EM_GETPARAFORMAT
api_location:
- Richedit.h
api_type:
- HeaderDef
---

# EM\_GETPARAFORMAT message

Retrieves the paragraph formatting of the current selection in a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**PARAFORMAT**](paraformat.md) structure that receives the paragraph formatting attributes of the current selection.

If more than one paragraph is selected, the structure receives the attributes of the first paragraph, and the **dwMask** member specifies which attributes are consistent throughout the entire selection.

Microsoft Rich Edit 2.0 and later: This parameter can be a pointer to a [**PARAFORMAT2**](paraformat2.md) structure, which is an extension of the [**PARAFORMAT**](paraformat.md) structure. Before sending the **EM\_GETPARAFORMAT** message, set the structure's **cbSize** member to indicate the version of the structure.

</dd> </dl>

## Return value

This message returns the value of the **dwMask** member of the [**PARAFORMAT**](paraformat.md) structure.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**PARAFORMAT**](paraformat.md)
</dt> <dt>

[**PARAFORMAT2**](paraformat2.md)
</dt> </dl>

 

 





