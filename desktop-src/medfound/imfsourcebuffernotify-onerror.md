---
description: Used to indicate that an error has occurred with the source buffer.
ms.assetid: a7187b7a-0090-4380-82bb-a7f72d54232e
title: IMFSourceBufferNotify::OnError method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMFSourceBufferNotify.OnError
api_type: 
- COM
api_location: 
- mfmediaengine.h
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



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                      |
| IDL<br/>                      | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMFSourceBufferNotify**](/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfsourcebuffernotify)
</dt> </dl>

 

 




