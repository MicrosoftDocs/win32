---
description: Indicates that the suspend process is starting and resources should be brought into a consistent state.
ms.assetid: 5cf3d249-3d8b-4596-9d8b-e7b95a270eff
title: IMFCdmSuspendNotify::Begin method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMFCdmSuspendNotify.Begin
api_type: 
- COM
api_location: 
- mfmediaengine.h
---

# IMFCdmSuspendNotify::Begin method

Indicates that the suspend process is starting and resources should be brought into a consistent state.

## Syntax


```C++
HRESULT Begin();
```



## Parameters

This method has no parameters.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                      |
| IDL<br/>                      | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMFCdmSuspendNotify**](/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfcdmsuspendnotify)
</dt> </dl>

 

 




