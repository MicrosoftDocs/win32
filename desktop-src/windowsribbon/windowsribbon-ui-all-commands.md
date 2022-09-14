---
title: UI_ALL_COMMANDS (Uiribbon.h)
description: Specifies a constant that identifies the collection of Commands declared in the Markup resource file.
ms.assetid: b0046d8c-bb54-4231-90f0-c0b2c8790b1a
topic_type:
- apiref
api_name:
- UI_ALL_COMMANDS
api_location:
- Uiribbon.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# UI\_ALL\_COMMANDS

Specifies a constant that identifies the collection of Commands declared in the Markup resource file.

## Remarks

**UI\_ALL\_COMMANDS** is useful when it is necessary to access similar properties across all Commands. For example, **UI\_ALL\_COMMANDS** can be passed to [**IUIFramework::InvalidateUICommand**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand) to invalidate and refresh all Ribbon Commands by querying the host application for new property values.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7, Windows Vista with SP2 and Platform Update for Windows Vista \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows Server 2008 R2, Windows Server 2008 with SP2 and Platform Update for Windows Server 2008 \[desktop apps only\]<br/> |
| Header<br/>                   | <dl> <dt>Uiribbon.h</dt> </dl>                                             |
| IDL<br/>                      | <dl> <dt>Uiribbon.idl</dt> </dl>                                           |



## See also

<dl> <dt>

[Constants and Enumerations](windowsribbon-reference-enumerations.md)
</dt> </dl>

 

