---
title: CommonDialog.ShowItemProperties method
description: Displays the Properties dialog box for the specified Item.
ms.assetid: 669f0261-9af5-42be-a818-2e5b24d9d616
keywords:
- ShowItemProperties method WIA Automation
- ShowItemProperties method WIA Automation , CommonDialog object
- CommonDialog object WIA Automation , ShowItemProperties method
topic_type:
- apiref
api_name:
- CommonDialog.ShowItemProperties
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

# CommonDialog.ShowItemProperties method

Displays the **Properties** dialog box for the specified [**Item**](-wiaaut-item.md).

## Syntax


```VB
CommonDialog.ShowItemProperties( _
  ByVal Item As Item, _
  [ ByVal CancelError As VARIANT_BOOL ] _
) As HRESULT
```



## Parameters

<dl> <dt>

*Item* \[in\]
</dt> <dd>

Type: **[**Item**](-wiaaut-item.md)\***

Required. [**Item**](-wiaaut-item.md) value.

</dd> <dt>

*CancelError* \[in, optional\]
</dt> <dd>

Type: **VARIANT\_BOOL**

**Boolean** value that indicates whether to generate an error if the user cancels the dialog box.



| Value                                                                                                                                  | Meaning                                       |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt></dt> <dt>False</dt> </dl> | Default. Do not generate an error.<br/> |
| <dl> <dt></dt> <dt>True</dt> </dl>  | Generate an error.<br/>                 |



 

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Examples

The following example shows how to display the [**Item**](-wiaaut-item.md)  **Properties** dialog box for the selected item.


```
Dim dev 'As Device
Dim itms 'As Items
Dim itm 'As Item

Set dev = CommonDialog1.ShowSelectDevice
Set itms = CommonDialog1.ShowSelectItems(dev, UnspecifiedIntent, _
                                         MaximizeQuality, True)
Set itm = itms(1)
CommonDialog1.ShowItemProperties itm
```



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

[**CommonDialog**](-wiaaut-commondialog.md)
</dt> <dt>

[**ShowTransfer**](-wiaaut-icommondialog-showtransfer.md)
</dt> <dt>

[**ExecuteCommand (Device)**](-wiaaut-idevice-executecommand.md)
</dt> <dt>

[**GetItem**](-wiaaut-idevice-getitem.md)
</dt> <dt>

[**Item**](-wiaaut-item.md)
</dt> <dt>

[**ExecuteCommand (Item)**](-wiaaut-iitem-executecommand.md)
</dt> <dt>

[**Item (Items)**](-wiaaut-iitems-item.md)
</dt> </dl>

 

 





