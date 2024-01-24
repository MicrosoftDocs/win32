---
description: "Learn more about: IMFMediaKeys::Shutdown method"
ms.assetid: 464b598c-5fa7-40af-83ba-8619fbd84b04
title: IMFMediaKeys::Shutdown method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMFMediaKeys.Shutdown
api_type: 
- COM
api_location: 
- mfmediaengine.h
---

# IMFMediaKeys::Shutdown method

## Syntax


```C++
HRESULT Shutdown();
```



## Parameters

This method has no parameters.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

**Shutdown** should be called by the application before final release. The Content Decryption Module (CDM) reference and any other resources is released at this point. However, related sessions are not freed or closed.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                      |
| IDL<br/>                      | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMFMediaKeys**](/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediakeys)
</dt> </dl>

 

 




