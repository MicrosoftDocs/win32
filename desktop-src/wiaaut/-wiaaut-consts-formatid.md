---
title: FormatID Constants
description: Indicates the file format of an image as String versions of GUIDs.
ms.assetid: 'a548d805-c419-454e-bfe4-54082aa30144'
topic_type:
- apiref
api_name:
- wiaFormatBMP
- wiaFormatPNG
- wiaFormatGIF
- wiaFormatJPEG
- wiaFormatTIFF
api_location:
- Wiaaut.h
api_type:
- HeaderDef
---

# FormatID Constants

Indicates the file format of an image as **String** versions of GUIDs.



| Constant/value                                                                                                                                                                                                                                                                           | Description                                     |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------|
| <span id="wiaFormatBMP"></span><span id="wiaformatbmp"></span><span id="WIAFORMATBMP"></span><dl> <dt>**wiaFormatBMP**</dt> <dt>{B96B3CAB-0728-11D3-9D7B-0000F81EF32E}</dt> </dl>     | FormatID for the Windows BMP format.<br/> |
| <span id="wiaFormatPNG"></span><span id="wiaformatpng"></span><span id="WIAFORMATPNG"></span><dl> <dt>**wiaFormatPNG**</dt> <dt>{B96B3CAF-0728-11D3-9D7B-0000F81EF32E}</dt> </dl>     | FormatID for the PNG format.<br/>         |
| <span id="wiaFormatGIF"></span><span id="wiaformatgif"></span><span id="WIAFORMATGIF"></span><dl> <dt>**wiaFormatGIF**</dt> <dt>{B96B3CB0-0728-11D3-9D7B-0000F81EF32E}</dt> </dl>     | FormatID for the GIF format.<br/>         |
| <span id="wiaFormatJPEG"></span><span id="wiaformatjpeg"></span><span id="WIAFORMATJPEG"></span><dl> <dt>**wiaFormatJPEG**</dt> <dt>{B96B3CAE-0728-11D3-9D7B-0000F81EF32E}</dt> </dl> | FormatID for the JPEG format.<br/>        |
| <span id="wiaFormatTIFF"></span><span id="wiaformattiff"></span><span id="WIAFORMATTIFF"></span><dl> <dt>**wiaFormatTIFF**</dt> <dt>{B96B3CB1-0728-11D3-9D7B-0000F81EF32E}</dt> </dl> | FormatID for the TIFF format.<br/>        |



## Remarks

Use a **FormatID Constants** constant as the value for the FormatID parameter for the [**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md), [**ShowTransfer**](-wiaaut-icommondialog-showtransfer.md), and [**Transfer**](-wiaaut-iitem-transfer.md) methods. You can also use a **FormatID Constants** constant as the value of the FormatID property in a "Convert" filter to specify the format that results from the conversion.

The following example shows how to determine if the file returned from [**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md) is a JPEG file.


```
Dim Img 'As ImageFile

Set Img = CommonDialog1.ShowAcquireImage(UnspecifiedDeviceType, _
                                         UnspecifiedIntent, _
                                         MaximizeQuality, _
                                         wiaFormatJPEG)
If Img.FormatID <> wiaFormatJPEG Then
    MsgBox "Device does not support JPEG files"
End If
```



For additional example code, see [Convert a File](-wiaaut-shared-samples.md#convert-a-file) in Shared Samples .

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**FormatID**](-wiaaut-iimagefile-formatid.md)
</dt> </dl>

 

 





