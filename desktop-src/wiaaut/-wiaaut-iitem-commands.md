---
title: Item.Commands property
description: Retrieves a collection of all commands for this Item object.
ms.assetid: d2e00d58-057f-4e33-ab1c-23dd18fcdfa8
keywords:
- Commands property WIA Automation
- Commands property WIA Automation , Item object
- Item object WIA Automation , Commands property
topic_type:
- apiref
api_name:
- Item.Commands
api_location:
- Wiaaut.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Item.Commands property

Retrieves a collection of all commands for this [**Item**](-wiaaut-item.md) object.

This property is read-only.

## Syntax


```VB
Property Commands( _
)
```



## Property value

[**DeviceCommands**](-wiaaut-devicecommands.md) collection.

## Remarks

For example code, see [Enumerate the Supported Commands](-wiaaut-shared-samples.md#enumerate-the-supported-commands) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Item**](-wiaaut-item.md)
</dt> <dt>

[**Commands (Device)**](-wiaaut-idevice-commands.md)
</dt> </dl>

 

 





