---
description: Sets the position of an item in the Shell view. Used by SHShellFolderView\_Message.
title: SFVM_SETITEMPOS message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: b89f2d62-095b-4cad-a47e-2d41e122cb3e
api_name: 
 - SFVM_SETITEMPOS
api_type: 
 - HeaderDef
api_location: 
 - Shlobj.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SFVM\_SETITEMPOS message

Sets the position of an item in the Shell view. Used by [**SHShellFolderView\_Message**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shshellfolderview_message).


```C++

                SFVM_SETITEMPOS 

    lParam = (LPSFV_SETITEMPOS)&sip;

            
```



## Parameters

<dl> <dt>

*sip* \[in\]
</dt> <dd>

A pointer to an [**SFV\_SETITEMPOS**](/windows/desktop/api/Shlobj/ns-shlobj-sfv_setitempos) structure.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




