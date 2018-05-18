---
Description: 'Sent by the default context menu implementation to request LPFNDFMCALLBACK to invoke an extended menu command.'
title: 'DFM\_INVOKECOMMANDEX message'
---

# DFM\_INVOKECOMMANDEX message

Sent by the default context menu implementation to request [**LPFNDFMCALLBACK**](lpfndfmcallback.md) to invoke an extended menu command.


```C++
                DFM_INVOKECOMMANDEX
    wParam = (WPARAM)(int) idCmd;           
    lParam = (LPARAM)(DFMICS) PDFMICS;
            
```



## Parameters

<dl> <dt>

*idCmd* \[in\]
</dt> <dd>

The command ID of the selected menu command. The following flags are recognized.

<dt>

<span id="DFM_CMD_DELETE"></span><span id="dfm_cmd_delete"></span>

<span id="DFM_CMD_DELETE"></span><span id="dfm_cmd_delete"></span>**DFM\_CMD\_DELETE**


</dt> <dd></dd> <dt>

<span id="DFM_CMD_MOVE"></span><span id="dfm_cmd_move"></span>

<span id="DFM_CMD_MOVE"></span><span id="dfm_cmd_move"></span>**DFM\_CMD\_MOVE**


</dt> <dd></dd> <dt>

<span id="DFM_CMD_COPY"></span><span id="dfm_cmd_copy"></span>

<span id="DFM_CMD_COPY"></span><span id="dfm_cmd_copy"></span>**DFM\_CMD\_COPY**


</dt> <dd></dd> <dt>

<span id="DFM_CMD_LINK"></span><span id="dfm_cmd_link"></span>

<span id="DFM_CMD_LINK"></span><span id="dfm_cmd_link"></span>**DFM\_CMD\_LINK**


</dt> <dd></dd> <dt>

<span id="DFM_CMD_PROPERTIES"></span><span id="dfm_cmd_properties"></span>

<span id="DFM_CMD_PROPERTIES"></span><span id="dfm_cmd_properties"></span>**DFM\_CMD\_PROPERTIES**


</dt> <dd>

Show the **Properties** UI for the item the menu was invoked on.

</dd> <dt>

<span id="DFM_CMD_NEWFOLDER"></span><span id="dfm_cmd_newfolder"></span>

<span id="DFM_CMD_NEWFOLDER"></span><span id="dfm_cmd_newfolder"></span>**DFM\_CMD\_NEWFOLDER**


</dt> <dd></dd> <dt>

<span id="DFM_CMD_PASTE"></span><span id="dfm_cmd_paste"></span>

<span id="DFM_CMD_PASTE"></span><span id="dfm_cmd_paste"></span>**DFM\_CMD\_PASTE**


</dt> <dd></dd> <dt>

<span id="DFM_CMD_VIEWLIST"></span><span id="dfm_cmd_viewlist"></span>

<span id="DFM_CMD_VIEWLIST"></span><span id="dfm_cmd_viewlist"></span>**DFM\_CMD\_VIEWLIST**


</dt> <dd></dd> <dt>

<span id="DFM_CMD_VIEWDETAILS"></span><span id="dfm_cmd_viewdetails"></span>

<span id="DFM_CMD_VIEWDETAILS"></span><span id="dfm_cmd_viewdetails"></span>**DFM\_CMD\_VIEWDETAILS**


</dt> <dd></dd> <dt>

<span id="DFM_CMD_PASTELINK"></span><span id="dfm_cmd_pastelink"></span>

<span id="DFM_CMD_PASTELINK"></span><span id="dfm_cmd_pastelink"></span>**DFM\_CMD\_PASTELINK**


</dt> <dd></dd> <dt>

<span id="DFM_CMD_PASTESPECIAL"></span><span id="dfm_cmd_pastespecial"></span>

<span id="DFM_CMD_PASTESPECIAL"></span><span id="dfm_cmd_pastespecial"></span>**DFM\_CMD\_PASTESPECIAL**


</dt> <dd></dd> <dt>

<span id="DFM_CMD_MODALPROP"></span><span id="dfm_cmd_modalprop"></span>

<span id="DFM_CMD_MODALPROP"></span><span id="dfm_cmd_modalprop"></span>**DFM\_CMD\_MODALPROP**


</dt> <dd></dd> <dt>

<span id="DFM_CMD_RENAME"></span><span id="dfm_cmd_rename"></span>

<span id="DFM_CMD_RENAME"></span><span id="dfm_cmd_rename"></span>**DFM\_CMD\_RENAME**


</dt> <dd></dd> </dl> </dd> <dt>

*PDFMICS* \[in\]
</dt> <dd>

A pointer to a [**DFMICS**](dfmics.md) structure that contains additional arguments to the selected menu command. This parameter can be **NULL**.

</dd> </dl>

## Remarks

Upon receipt of this message, your function should return S\_FALSE if you want the default implementation to invoke the default handler for the command. Return S\_OK if the message was handled. Otherwise, return a standard HRESULT error code.

This message is sent to either the callback function or the callback object depending on how the callback is implemented. There are two APIs for callback construction, [**CDefFolderMenu\_Create2**](cdeffoldermenu-create2.md) that takes a pointer to a callback function, or [**SHCreateDefaultContextMenu**](shcreatedefaultcontextmenu.md) that uses a callback object that supports [**IContextMenuCB**](icontextmenucb.md).

The items on which the command is being invoked are provided in a data object passed to the callback function or to the [**IContextMenuCB::CallBack**](icontextmenucb-callback.md) method. This data object is provided by the data source that implements the callback. To extract the items from the data object, use [**SHCreateShellItemArrayFromDataObject**](shcreateshellitemarrayfromdataobject.md).

[**DFM\_INVOKECOMMAND**](dfm-invokecommand.md) is a simpler version of this message which does not provide as much information to the callback. Use **DFM\_INVOKECOMMAND** if the additional information provided by **DFM\_INVOKECOMMANDEX** is not needed in your implementation.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




