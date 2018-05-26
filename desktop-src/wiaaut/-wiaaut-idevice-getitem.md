---
title: Device.GetItem method
description: Retrieves the specified item.
ms.assetid: 6f2a66dd-2bde-4434-9910-71de694240f1
keywords:
- GetItem method WIA Automation
- GetItem method WIA Automation , Device object
- Device object WIA Automation , GetItem method
topic_type:
- apiref
api_name:
- Device.GetItem
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

# Device.GetItem method

Retrieves the specified item.

## Syntax


```VB
ppResult = .GetItem( _
  ByVal ItemID As BSTR _
) As HRESULT
```



## Parameters

<dl> <dt>

*ItemID* \[in\]
</dt> <dd>

Type: **BSTR**

Required. **String** value.

</dd> </dl>

## Return value

Type: **[**Item**](-wiaaut-item.md)\*\***

Returns the [**Item**](-wiaaut-item.md) object specified by *ItemID* if it exists, otherwise returns **Nothing**.

## Remarks

For example code, see [Download New Items as They are Created](-wiaaut-shared-samples.md#download-new-items-as-they-are-created) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**ShowItemProperties**](-wiaaut-icommondialog-showitemproperties.md)
</dt> <dt>

[**ShowTransfer**](-wiaaut-icommondialog-showtransfer.md)
</dt> <dt>

[**Device**](-wiaaut-device.md)
</dt> <dt>

[**ExecuteCommand (Device)**](-wiaaut-idevice-executecommand.md)
</dt> <dt>

[**OnEvent**](-wiaaut--idevicemanagerevents-onevent.md)
</dt> <dt>

[**Item**](-wiaaut-item.md)
</dt> <dt>

[**ExecuteCommand (Item)**](-wiaaut-iitem-executecommand.md)
</dt> <dt>

[**ItemID**](-wiaaut-iitem-itemid.md)
</dt> <dt>

[**Item (Items)**](-wiaaut-iitems-item.md)
</dt> </dl>

 

 





