---
title: ImageFile.LoadFile method
description: Loads the ImageFile object with the specified file.
ms.assetid: 2426556c-0397-44b0-8323-ff98507f417f
keywords:
- LoadFile method WIA Automation
- LoadFile method WIA Automation , ImageFile object
- ImageFile object WIA Automation , LoadFile method
topic_type:
- apiref
api_name:
- ImageFile.LoadFile
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

# ImageFile.LoadFile method

Loads the [**ImageFile**](-wiaaut-imagefile.md) object with the specified file.

## Syntax


```VB
ImageFile.LoadFile( _
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

For example code, see [Display Detailed Image Information](https://www.bing.com/search?q=Display Detailed Image Information) in Shared Samples.

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

[**SaveFile**](-wiaaut-iimagefile-savefile.md)
</dt> </dl>

 

 





