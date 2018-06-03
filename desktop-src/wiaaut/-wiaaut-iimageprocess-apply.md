---
title: ImageProcess.Apply method
description: Applies filters to an ImageFile object.
ms.assetid: 8acc07b3-0e8a-44fa-a94d-5f55f2d9829a
keywords:
- Apply method WIA Automation
- Apply method WIA Automation , ImageProcess object
- ImageProcess object WIA Automation , Apply method
topic_type:
- apiref
api_name:
- ImageProcess.Apply
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

# ImageProcess.Apply method

Applies filters to an [**ImageFile**](-wiaaut-imagefile.md) object.

## Syntax


```VB
ppResult = .Apply( _
  ByVal Source As ImageFile _
) As HRESULT
```



## Parameters

<dl> <dt>

*Source* \[in\]
</dt> <dd>

Type: **[**ImageFile**](-wiaaut-imagefile.md)\***

Required. [**ImageFile**](-wiaaut-imagefile.md) value.

</dd> </dl>

## Return value

Type: **[**ImageFile**](-wiaaut-imagefile.md)\*\***

Returns a new [**ImageFile**](-wiaaut-imagefile.md) object with all the filters applied on success, otherwise returns **Nothing**.

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

[**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md)
</dt> <dt>

[**ImageFile**](-wiaaut-imagefile.md)
</dt> <dt>

[**ImageProcess**](-wiaaut-imageprocess.md)
</dt> <dt>

[**ImageFile (Vector)**](-wiaaut-ivector-imagefile.md)
</dt> </dl>

 

 





