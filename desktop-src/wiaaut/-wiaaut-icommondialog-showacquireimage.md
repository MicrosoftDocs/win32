---
title: CommonDialog.ShowAcquireImage method
description: Displays one or more dialog boxes that enable the user to acquire an image from a hardware device.
ms.assetid: fa1acf61-6820-4386-b272-d55d0131f8ad
keywords:
- ShowAcquireImage method WIA Automation
- ShowAcquireImage method WIA Automation , CommonDialog object
- CommonDialog object WIA Automation , ShowAcquireImage method
topic_type:
- apiref
api_name:
- CommonDialog.ShowAcquireImage
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

# CommonDialog.ShowAcquireImage method

Displays one or more dialog boxes that enable the user to acquire an image from a hardware device.

## Syntax


```VB
ppResult = .ShowAcquireImage( _
  [ ByVal DeviceType As WiaDeviceType ], _
  [ ByVal Intent As WiaImageIntent ], _
  [ ByVal Bias As WiaImageBias ], _
  [ ByVal FormatID As BSTR ], _
  [ ByVal AlwaysSelectDevice As VARIANT_BOOL ], _
  [ ByVal UseCommonUI As VARIANT_BOOL ], _
  [ ByVal CancelError As VARIANT_BOOL ] _
) As HRESULT
```



## Parameters

<dl> <dt>

*DeviceType* \[in, optional\]
</dt> <dd>

Type: **[**WiaDeviceType**](-wiaaut-wiadevicetype.md)**

[**WiaDeviceType**](-wiaaut-wiadevicetype.md) value.



| Value                                                                                                                                                  | Meaning                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt></dt> <dt>UnspecifiedDeviceType</dt> </dl> | Default. The device type is unknown.<br/> |



 

</dd> <dt>

*Intent* \[in, optional\]
</dt> <dd>

Type: **[**WiaImageIntent**](-wiaaut-wiaimageintent.md)**

[**WiaImageIntent**](-wiaaut-wiaimageintent.md) value.



| Value                                                                                                                                              | Meaning                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt></dt> <dt>UnspecifiedIntent</dt> </dl> | Default. No intent specified.<br/> |



 

</dd> <dt>

*Bias* \[in, optional\]
</dt> <dd>

Type: **[**WiaImageBias**](-wiaaut-wiaimagebias.md)**

[**WiaImageBias**](-wiaaut-wiaimagebias.md) value.



| Value                                                                                                                                            | Meaning                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt></dt> <dt>MaximizeQuality</dt> </dl> | Default. Use a higher quality scan to maximize the quality of the image.<br/> |



 

</dd> <dt>

*FormatID* \[in, optional\]
</dt> <dd>

Type: **BSTR**

**String** value that specifies one of the [**FormatID Constants**](-wiaaut-consts-formatid.md) that indicates the requested image format.



| Value                                                                                                                                                                   | Meaning                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt></dt> <dt>{00000000-0000-0000-0000-000000000000}</dt> </dl> | Default. Unspecified format.<br/> |



 

</dd> <dt>

*AlwaysSelectDevice* \[in, optional\]
</dt> <dd>

Type: **VARIANT\_BOOL**

**Boolean** value that indicates whether to always show the select device dialog box.



| Value                                                                                                                                  | Meaning                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt></dt> <dt>False</dt> </dl> | Default. Do not show the select device dialog box.<br/> |
| <dl> <dt></dt> <dt>True</dt> </dl>  | Show the select device dialog box.<br/>                 |



 

</dd> <dt>

*UseCommonUI* \[in, optional\]
</dt> <dd>

Type: **VARIANT\_BOOL**

**Boolean** value that indicates whether to use the common UI.



| Value                                                                                                                                  | Meaning                                |
|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt></dt> <dt>False</dt> </dl> | Do not use the common UI.<br/>   |
| <dl> <dt></dt> <dt>True</dt> </dl>  | Default. Use the common UI.<br/> |



 

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

Type: **[**ImageFile**](-wiaaut-imagefile.md)\*\***

Returns an [**ImageFile**](-wiaaut-imagefile.md) object on success, otherwise returns **Nothing**.

## Remarks

For example code, see [Convert a File](https://www.bing.com/search?q=Convert a File) in Shared Samples.

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

[**ShowSelectDevice**](-wiaaut-icommondialog-showselectdevice.md)
</dt> <dt>

[**ShowSelectItems**](-wiaaut-icommondialog-showselectitems.md)
</dt> <dt>

[**ShowTransfer**](-wiaaut-icommondialog-showtransfer.md)
</dt> <dt>

[**Type (Device)**](-wiaaut-idevice-type.md)
</dt> <dt>

[**Type (DeviceInfo)**](-wiaaut-ideviceinfo-type.md)
</dt> <dt>

[**FormatID Constants**](-wiaaut-consts-formatid.md)
</dt> <dt>

[**ImageFile**](-wiaaut-imagefile.md)
</dt> <dt>

[**FormatID**](-wiaaut-iimagefile-formatid.md)
</dt> <dt>

[**Apply**](-wiaaut-iimageprocess-apply.md)
</dt> <dt>

[**Transfer**](-wiaaut-iitem-transfer.md)
</dt> <dt>

[**ImageFile (Vector)**](-wiaaut-ivector-imagefile.md)
</dt> <dt>

[**WiaDeviceType**](-wiaaut-wiadevicetype.md)
</dt> <dt>

[**WiaImageBias**](-wiaaut-wiaimagebias.md)
</dt> <dt>

[**WiaImageIntent**](-wiaaut-wiaimageintent.md)
</dt> </dl>

 

 





