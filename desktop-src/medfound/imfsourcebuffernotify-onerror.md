---
Description: Used to indicate that an error has occurred with the source buffer.
ms.assetid: a7187b7a-0090-4380-82bb-a7f72d54232e
title: IMFSourceBufferNotifyOnError method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMFSourceBufferNotify::OnError method

Used to indicate that an error has occurred with the source buffer.

## Syntax


```C++
void OnError(
  [in] HRESULT hr
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd></dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                      |
| IDL<br/>                      | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMFSourceBufferNotify**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfsourcebuffernotify?branch=master)
</dt> </dl>

 

 




