---
title: CFSTR\_DSOP\_DS\_SELECTION\_LIST
description: The CFSTR\_DSOP\_DS\_SELECTION\_LIST clipboard format provides an HGLOBAL that contains a DS\_SELECTION\_LIST structure. The DS\_SELECTION\_LIST structure contains data about the items selected in a Directory Object Picker dialog box.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: cd634e3b-0eb7-4144-b9e1-1d27a322f72c
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- CFSTR_DSOP_DS_SELECTION_LIST
api_location:
- Objsel.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CFSTR\_DSOP\_DS\_SELECTION\_LIST

<dl> <dt>

<span id="CFSTR_DSOP_DS_SELECTION_LIST"></span><span id="cfstr_dsop_ds_selection_list"></span>**CFSTR\_DSOP\_DS\_SELECTION\_LIST**
</dt> <dd> <dl> <dt>

"CFSTR\_DSOP\_DS\_SELECTION\_LIST"
</dt> <dt>



The **CFSTR\_DSOP\_DS\_SELECTION\_LIST** clipboard format is provided by the [**IDataObject**](_ole_idataobject) obtained by calling [**IDsObjectPicker::InvokeDialog**](/windows/win32/Objsel/nf-objsel-idsobjectpicker-invokedialog?branch=master). The **CFSTR\_DSOP\_DS\_SELECTION\_LIST** clipboard format provides an **HGLOBAL** that contains a [**DS\_SELECTION\_LIST**](/windows/win32/Objsel/ns-objsel-_ds_selection_list?branch=master) structure. The **DS\_SELECTION\_LIST** structure contains data about the items selected in a [Directory Object Picker](directory-object-picker.md) dialog box.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>Objsel.h</dt> </dl> |



## See also

<dl> <dt>

[**DS\_SELECTION\_LIST**](/windows/win32/Objsel/ns-objsel-_ds_selection_list?branch=master)
</dt> <dt>

[**IDsObjectPicker::InvokeDialog**](/windows/win32/Objsel/nf-objsel-idsobjectpicker-invokedialog?branch=master)
</dt> <dt>

[Directory Object Picker](directory-object-picker.md)
</dt> </dl>

 

 





