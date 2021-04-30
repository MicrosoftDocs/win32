---
description: Removes the media segments defined by the specified time range from the IMFSourceBuffer.
ms.assetid: 86536d73-18c0-4acc-81ec-72f1dfe400c5
title: IMFSourceBuffer::Remove method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMFSourceBuffer.Remove
api_type: 
- COM
api_location: 
- mfmediaengine.h
---

# IMFSourceBuffer::Remove method

Removes the media segments defined by the specified time range from the [**IMFSourceBuffer**](/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfsourcebuffer).

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



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                      |
| IDL<br/>                      | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMFSourceBuffer**](/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfsourcebuffer)
</dt> </dl>

 

 




