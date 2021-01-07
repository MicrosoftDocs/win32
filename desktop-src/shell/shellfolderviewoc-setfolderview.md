---
description: Forwards the events of the specified ShellFolderView object to the corresponding ShellFolderViewOC event handler.
ms.assetid: 44a2a0a5-aa87-43ae-b4ea-0d301fcb8464
title: ShellFolderViewOC.SetFolderView method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellFolderViewOC.SetFolderView
api_type: 
- COM
api_location: 
- Shell32.dll
---

# ShellFolderViewOC.SetFolderView method

Forwards the events of the specified [**ShellFolderView**](shellfolderview.md) object to the corresponding [**ShellFolderViewOC**](shellfolderviewoc-object.md) event handler.

## Syntax


```JScript
iRetVal = ShellFolderViewOC.SetFolderView(
  oShellFolderView
)
```



## Parameters

<dl> <dt>

*oShellFolderView* \[in\]
</dt> <dd>

Type: **[**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch)\***

A [**ShellFolderView**](shellfolderview.md) object. Its [**EnumDone**](shellfolderviewoc-enumdone.md) and [**SelectionChanged**](shellfolderview-selectionchanged.md) events will be forwarded to the corresponding [**ShellFolderViewOC**](shellfolderviewoc-object.md) event handler.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



 

 
