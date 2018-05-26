---
Description: Adds a IMFSourceBuffer to the collection of buffers associated with the IMFMediaSourceExtension.
ms.assetid: 1ecb7047-4dc9-4657-8a19-12108de299c0
title: IMFMediaSourceExtensionAddSourceBuffer method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMFMediaSourceExtension::AddSourceBuffer method

Adds a [**IMFSourceBuffer**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfsourcebuffer?branch=master) to the collection of buffers associated with the [**IMFMediaSourceExtension**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfmediasourceextension?branch=master).

## Syntax


```C++
HRESULT AddSourceBuffer(
  [in]  BSTR                  type,
  [in]  IMFSourceBufferNotify *pNotify,
  [out] IMFSourceBuffer       **ppSourceBuffer
);
```



## Parameters

<dl> <dt>

*type* \[in\]
</dt> <dd></dd> <dt>

*pNotify* \[in\]
</dt> <dd></dd> <dt>

*ppSourceBuffer* \[out\]
</dt> <dd></dd> </dl>

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

 

 




