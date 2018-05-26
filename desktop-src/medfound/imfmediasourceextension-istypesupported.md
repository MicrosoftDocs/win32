---
Description: Gets a value that indicates if the specified MIME type is supported by the media source.
ms.assetid: 894ef7d2-d008-42e1-8a61-26f35a8877be
title: IMFMediaSourceExtensionIsTypeSupported method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMFMediaSourceExtension::IsTypeSupported method

Gets a value that indicates if the specified MIME type is supported by the media source.

## Syntax


```C++
BOOL IsTypeSupported(
  [in] BSTR type
);
```



## Parameters

<dl> <dt>

*type* \[in\]
</dt> <dd>

The media type to check support for.

</dd> </dl>

## Return value

**true** if the media type is supported; otherwise, **false**.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                      |
| IDL<br/>                      | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMFMediaSourceExtension**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfmediasourceextension?branch=master)
</dt> </dl>

 

 




