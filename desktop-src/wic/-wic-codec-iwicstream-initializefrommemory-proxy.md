---
description: IWICStream_InitializeFromMemory_Proxy function - Proxy function for the InitializeFromMemory method.
ms.assetid: 737526ac-fe79-4d53-83c5-33102f5ac67b
title: IWICStream_InitializeFromMemory_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICStream_InitializeFromMemory_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICStream\_InitializeFromMemory\_Proxy function

Proxy function for the [**InitializeFromMemory**](/windows/desktop/api/Wincodec/nf-wincodec-iwicstream-initializefrommemory) method.

## Syntax


```C++
HRESULT IWICStream_InitializeFromMemory_Proxy(
  _In_ IWICStream *THIS_PTR,
  _In_ BYTE       *pbBuffer,
  _In_ DWORD      cbBufferSize
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICStream**](/windows/desktop/api/Wincodec/nn-wincodec-iwicstream)\***

Pointer to this [**IWICStream**](/windows/desktop/api/Wincodec/nn-wincodec-iwicstream) object.

</dd> <dt>

*pbBuffer* \[in\]
</dt> <dd>

Type: **BYTE\***

Pointer to the buffer used to initialize the stream.

</dd> <dt>

*cbBufferSize* \[in\]
</dt> <dd>

Type: **DWORD**

The size of buffer.

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




