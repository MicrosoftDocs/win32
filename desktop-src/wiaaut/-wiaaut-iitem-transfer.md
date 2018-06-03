---
title: Item.Transfer method
description: Retrieves an ImageFile object from an imaging device.
ms.assetid: fb315c60-4a57-4b08-9ad2-dcbe3e58ee01
keywords:
- Transfer method WIA Automation
- Transfer method WIA Automation , Item object
- Item object WIA Automation , Transfer method
topic_type:
- apiref
api_name:
- Item.Transfer
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

# Item.Transfer method

Retrieves an [**ImageFile**](-wiaaut-imagefile.md) object from an imaging device.

## Syntax


```VB
pvResult = .Transfer( _
  [ ByVal FormatID As BSTR ] _
) As HRESULT
```



## Parameters

<dl> <dt>

*FormatID* \[in, optional\]
</dt> <dd>

Type: **BSTR**

**String** value that specifies one of the [**FormatID Constants**](-wiaaut-consts-formatid.md) that indicates the requested image format.



| Value                                                                                                                                                                   | Meaning                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt></dt> <dt>{00000000-0000-0000-0000-000000000000}</dt> </dl> | Default. Unspecified format.<br/> |



 

</dd> </dl>

## Return value

Type: **VARIANT\***

Returns an [**ImageFile**](-wiaaut-imagefile.md) object in the format specified in *FormatID*, if the device supports that format; otherwise this method uses the preferred format for this imaging device.

## Remarks

**Transfer** is essentially a version of [**ShowTransfer**](-wiaaut-icommondialog-showtransfer.md) that does not display a UI or allow the user to cancel the transfer.

For example code, see [Implement a Windows Script Host Script that Runs Automatically](https://www.bing.com/search?q=Implement a Windows Script Host Script that Runs Automatically) in Shared Samples.

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

[**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md)
</dt> <dt>

[**ShowTransfer**](-wiaaut-icommondialog-showtransfer.md)
</dt> <dt>

[**FormatID**](-wiaaut-iimagefile-formatid.md)
</dt> <dt>

[**Item**](-wiaaut-item.md)
</dt> </dl>

 

 





