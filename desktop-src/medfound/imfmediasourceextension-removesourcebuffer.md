---
Description: Removes the specified source buffer from the collection of source buffers managed by the IMFMediaSourceExtension object.
ms.assetid: 2f29cbac-4261-41ee-84c8-cb73686aeee5
title: IMFMediaSourceExtensionRemoveSourceBuffer method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMFMediaSourceExtension::RemoveSourceBuffer method

Removes the specified source buffer from the collection of source buffers managed by the [**IMFMediaSourceExtension**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfmediasourceextension?branch=master) object.

## Syntax


```C++
HRESULT RemoveSourceBuffer(
  [in] IMFSourceBuffer *pSourceBuffer
);
```



## Parameters

<dl> <dt>

*pSourceBuffer* \[in\]
</dt> <dd>

The buffer to remove.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

 

 




