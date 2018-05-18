---
Description: 'Sent by a File Manager extension to retrieve the type of File Manager window that has the input focus.'
title: 'FM\_GETFOCUS message'
---

# FM\_GETFOCUS message

Sent by a File Manager extension to retrieve the type of File Manager window that has the input focus.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the type of File Manager window that has the input focus. It can be one of the following values.



| Return code                                                                                    | Description                                         |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**FMFOCUS\_DIR**</dt> </dl>    | Directory portion of a directory window.<br/> |
| <dl> <dt>**FMFOCUS\_TREE**</dt> </dl>   | Tree portion of a directory window.<br/>      |
| <dl> <dt>**FMFOCUS\_DRIVES**</dt> </dl> | Drive bar of a directory window.<br/>         |
| <dl> <dt>**FMFOCUS\_SEARCH**</dt> </dl> | Search Results window.<br/>                   |



 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



 

 




