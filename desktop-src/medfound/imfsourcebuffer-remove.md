---
Description: Removes the media segments defined by the specified time range from the IMFSourceBuffer.
ms.assetid: 86536d73-18c0-4acc-81ec-72f1dfe400c5
title: IMFSourceBufferRemove method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMFSourceBuffer::Remove method

Removes the media segments defined by the specified time range from the [**IMFSourceBuffer**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfsourcebuffer?branch=master).

## Syntax


```C++
HRESULT Remove(
  [in] double start,
  [in] double end
);
```



## Parameters

<dl> <dt>

*start* \[in\]
</dt> <dd>

The start of the time range.

</dd> <dt>

*end* \[in\]
</dt> <dd>

The end of the time range.

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

 

 




