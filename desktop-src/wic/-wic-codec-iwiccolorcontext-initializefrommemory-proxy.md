---
Description: 'Proxy function for the InitializeFromMemory method.'
ms.assetid: 'd98fe40c-c3f1-4c46-a558-1910e3dee51b'
title: 'IWICColorContext\_InitializeFromMemory\_Proxy function'
---

# IWICColorContext\_InitializeFromMemory\_Proxy function

Proxy function for the [**InitializeFromMemory**](-wic-codec-iwiccolorcontext-initializefrommemory.md) method.

## Syntax


```C++
HRESULT IWICColorContext_InitializeFromMemory_Proxy(
  _In_       IWICColorContext *THIS_PTR,
  _In_ const BYTE             *pbBuffer,
  _In_       UINT             cbBufferSize
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICColorContext**](-wic-codec-iwiccolorcontext.md)\***

</dd> <dt>

*pbBuffer* \[in\]
</dt> <dd>

Type: **const BYTE\***

The buffer used to initialize the [**IWICColorContext**](-wic-codec-iwiccolorcontext.md).

</dd> <dt>

*cbBufferSize* \[in\]
</dt> <dd>

Type: **UINT**

The size of the *pbBuffer* buffer.

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



|                                     |                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




