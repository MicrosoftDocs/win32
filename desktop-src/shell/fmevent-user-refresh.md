---
Description: 'Sent to an extension DLL when the user chooses the Refresh command from the View menu in File Manager. The extension can use this notification to update its menu.'
title: 'FMEVENT\_USER\_REFRESH message'
---

# FMEVENT\_USER\_REFRESH message

Sent to an extension DLL when the user chooses the **Refresh** command from the **View** menu in File Manager. The extension can use this notification to update its menu.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

An extension DLL should return zero if it processes this message.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



## See also

<dl> <dt>

[**FMExtensionProc**](fmextensionproc.md)
</dt> </dl>

 

 




