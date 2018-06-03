---
title: ImageFile.SaveFile method
description: Saves the ImageFile object to the specified file.
ms.assetid: 7bf00f6f-7359-4731-82cb-e48b70121e87
keywords:
- SaveFile method WIA Automation
- SaveFile method WIA Automation , ImageFile object
- ImageFile object WIA Automation , SaveFile method
topic_type:
- apiref
api_name:
- ImageFile.SaveFile
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

# ImageFile.SaveFile method

Saves the [**ImageFile**](-wiaaut-imagefile.md) object to the specified file.

## Syntax


```VB
ImageFile.SaveFile( _
  ByVal Filename As BSTR _
) As HRESULT
```



## Parameters

<dl> <dt>

*Filename* \[in\]
</dt> <dd>

Type: **BSTR**

Required. **String** value.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

For example code, see [Create an ImageFile Object that Contains a Blank Page](https://www.bing.com/search?q=Create an ImageFile Object that Contains a Blank Page) in Shared Samples.

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

[**ImageFile**](-wiaaut-imagefile.md)
</dt> <dt>

[**LoadFile**](-wiaaut-iimagefile-loadfile.md)
</dt> </dl>

 

 





