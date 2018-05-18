---
Description: 'Creates an color transform object that implements IWICColorTransform. This COM object supports the free-threaded object model.'
ms.assetid: '43DCC3FB-B687-45F0-AAC6-DED76214716C'
title: 'WICCreateColorTransform\_Proxy function'
---

# WICCreateColorTransform\_Proxy function

Creates an color transform object that implements [**IWICColorTransform**](_wic_codec_iwiccolortransform). This COM object supports the free-threaded object model.

## Syntax


```C++
HRESULT WINAPI WICCreateColorTransform_Proxy(
  _Out_  **ppIColorTransform
);
```



## Parameters

<dl> <dt>

*ppIColorTransform* \[out\]
</dt> <dd>

The color transform created.

</dd> </dl>

## Return value

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                |                                                                                                 |
|----------------|-------------------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>WindowsCodecsExt.dll</dt> </dl> |



 

 




