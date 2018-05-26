---
title: CommonDialog.ShowTransfer method
description: Displays a Progress dialog box while transferring the specified Item to the local computer.
ms.assetid: cbc4d669-bb36-439b-9071-85cf112bb11d
keywords:
- ShowTransfer method WIA Automation
- ShowTransfer method WIA Automation , CommonDialog object
- CommonDialog object WIA Automation , ShowTransfer method
topic_type:
- apiref
api_name:
- CommonDialog.ShowTransfer
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

# CommonDialog.ShowTransfer method

Displays a **Progress** dialog box while transferring the specified [**Item**](-wiaaut-item.md) to the local computer.

## Syntax


```VB
pvResult = .ShowTransfer( _
  ByVal Item As Item, _
  [ ByVal FormatID As BSTR ], _
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

*FormatID* \[in, optional\]
</dt> <dd>

Type: **BSTR**

**String** value that specifies one of the [**FormatID Constants**](-wiaaut-consts-formatid.md) that indicates the requested image format.



| Value                                                                                                                                                                   | Meaning                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt></dt> <dt>{00000000-0000-0000-0000-000000000000}</dt> </dl> | Default. Unspecified format.<br/> |



 

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

Type: **VARIANT\***

Returns an [**ImageFile**](-wiaaut-imagefile.md) object in the format specified in *FormatID*, if the device supports that format; otherwise this method uses the preferred format for this imaging device.

## Remarks

[**Transfer**](-wiaaut-iitem-transfer.md) is essentially a version of **ShowTransfer** that does not display a UI or allow the user to cancel the transfer.

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

[**CommonDialog**](-wiaaut-commondialog.md)
</dt> <dt>

[**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md)
</dt> <dt>

[**ShowItemProperties**](-wiaaut-icommondialog-showitemproperties.md)
</dt> <dt>

[**ExecuteCommand (Device)**](-wiaaut-idevice-executecommand.md)
</dt> <dt>

[**GetItem**](-wiaaut-idevice-getitem.md)
</dt> <dt>

[**FormatID Constants**](-wiaaut-consts-formatid.md)
</dt> <dt>

[**FormatID**](-wiaaut-iimagefile-formatid.md)
</dt> <dt>

[**Item**](-wiaaut-item.md)
</dt> <dt>

[**ExecuteCommand (Item)**](-wiaaut-iitem-executecommand.md)
</dt> <dt>

[**Transfer**](-wiaaut-iitem-transfer.md)
</dt> <dt>

[**Item (Items)**](-wiaaut-iitems-item.md)
</dt> </dl>

 

 





