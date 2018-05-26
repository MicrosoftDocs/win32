---
Description: Appends the specified media segment to the IMFSourceBuffer.
ms.assetid: 824fa23d-57d9-411a-af8a-fb65dca124b2
title: IMFSourceBufferAppend method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMFSourceBuffer::Append method

Appends the specified media segment to the [**IMFSourceBuffer**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfsourcebuffer?branch=master).

## Syntax


```C++
HRESULT Append(
  [in] const BYTE  *pData,
  [in]       DWORD len
);
```



## Parameters

<dl> <dt>

*pData* \[in\]
</dt> <dd>

The media data to append.

</dd> <dt>

*len* \[in\]
</dt> <dd>

The length of the media data stored in *pData*.

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

[**IMFSourceBuffer**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfsourcebuffer?branch=master)
</dt> </dl>

 

 




