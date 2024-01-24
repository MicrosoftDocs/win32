---
title: CFSTR_DSOP_DS_SELECTION_LIST (Objsel.h)
description: The CFSTR\_DSOP\_DS\_SELECTION\_LIST clipboard format provides an HGLOBAL that contains a DS\_SELECTION\_LIST structure. The DS\_SELECTION\_LIST structure contains data about the items selected in a Directory Object Picker dialog box.
ms.assetid: cd634e3b-0eb7-4144-b9e1-1d27a322f72c
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- CFSTR_DSOP_DS_SELECTION_LIST
api_location:
- Objsel.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CFSTR\_DSOP\_DS\_SELECTION\_LIST

<dl> <dt>

<span id="CFSTR_DSOP_DS_SELECTION_LIST"></span><span id="cfstr_dsop_ds_selection_list"></span>**CFSTR\_DSOP\_DS\_SELECTION\_LIST**
</dt> <dd> <dl> <dt>

"CFSTR\_DSOP\_DS\_SELECTION\_LIST"
</dt> <dt>



The **CFSTR\_DSOP\_DS\_SELECTION\_LIST** clipboard format is provided by the [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) obtained by calling [**IDsObjectPicker::InvokeDialog**](/windows/desktop/api/Objsel/nf-objsel-idsobjectpicker-invokedialog). The **CFSTR\_DSOP\_DS\_SELECTION\_LIST** clipboard format provides an **HGLOBAL** that contains a [**DS\_SELECTION\_LIST**](/windows/desktop/api/Objsel/ns-objsel-ds_selection_list) structure. The **DS\_SELECTION\_LIST** structure contains data about the items selected in a [Directory Object Picker](directory-object-picker.md) dialog box.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>Objsel.h</dt> </dl> |



## See also

<dl> <dt>

[**DS\_SELECTION\_LIST**](/windows/desktop/api/Objsel/ns-objsel-ds_selection_list)
</dt> <dt>

[**IDsObjectPicker::InvokeDialog**](/windows/desktop/api/Objsel/nf-objsel-idsobjectpicker-invokedialog)
</dt> <dt>

[Directory Object Picker](directory-object-picker.md)
</dt> </dl>

 

