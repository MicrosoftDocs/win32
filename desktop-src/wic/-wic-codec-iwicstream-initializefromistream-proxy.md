---
Description: 'Proxy function for the InitializeFromIStream method.'
ms.assetid: '3ab780bb-7fe7-4abe-9ea7-86f54ea15d91'
title: 'IWICStream\_InitializeFromIStream\_Proxy function'
---

# IWICStream\_InitializeFromIStream\_Proxy function

Proxy function for the [**InitializeFromIStream**](-wic-codec-iwicstream-initializefromistream.md) method.

## Syntax


```C++
HRESULT IWICStream_InitializeFromIStream_Proxy(
  _In_ IWICStream *THIS_PTR,
  _In_ IStream    *pIStream
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICStream**](-wic-codec-iwicstream.md)\***

Pointer to this [**IWICStream**](-wic-codec-iwicstream.md) object.

</dd> <dt>

*pIStream* \[in\]
</dt> <dd>

Type: **[IStream](https://msdn.microsoft.com/library/windows/desktop/aa380034)\***

The initialize stream.

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



 

 




