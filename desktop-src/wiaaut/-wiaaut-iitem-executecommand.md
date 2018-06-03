---
title: Item.ExecuteCommand method
description: Issues the command specified by CommandID.
ms.assetid: 75466b70-1fd6-45bb-bab7-ab7c78f38dc6
keywords:
- ExecuteCommand method WIA Automation
- ExecuteCommand method WIA Automation , Item object
- Item object WIA Automation , ExecuteCommand method
topic_type:
- apiref
api_name:
- Item.ExecuteCommand
api_location:
- Wiaaut.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Item.ExecuteCommand method

Issues the command specified by *CommandID*.

## Syntax


```VB
ppResult = .ExecuteCommand( _
  ByVal CommandID As BSTR _
) As HRESULT
```



## Parameters

<dl> <dt>

*CommandID* \[in\]
</dt> <dd>

Type: **BSTR**

Required. **String** value.

</dd> </dl>

## Return value

Type: **[**Item**](-wiaaut-item.md)\*\***

Required. [**Item**](-wiaaut-item.md) value.

## Remarks

All the imaging devices expose most of their commands on devices rather than items. *CommandID*s are device dependent. Valid *CommandID*s for this [**Item**](-wiaaut-item.md) are contained in the [**Commands (Item)**](-wiaaut-iitem-commands.md) collection.

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

**Reference**
</dt> <dt>

[**CommandID Constants**](-wiaaut-consts-commandid.md)
</dt> <dt>

[**ShowItemProperties**](-wiaaut-icommondialog-showitemproperties.md)
</dt> <dt>

[**ShowTransfer**](-wiaaut-icommondialog-showtransfer.md)
</dt> <dt>

[**ExecuteCommand (Device)**](-wiaaut-idevice-executecommand.md)
</dt> <dt>

[**GetItem**](-wiaaut-idevice-getitem.md)
</dt> <dt>

[**CommandID**](-wiaaut-idevicecommand-commandid.md)
</dt> <dt>

[**Item (Items)**](-wiaaut-iitems-item.md)
</dt> </dl>

 

 





