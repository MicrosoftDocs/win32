---
Description: Creates an color transform object that implements IWICColorTransform. This COM object supports the free-threaded object model.
ms.assetid: 43DCC3FB-B687-45F0-AAC6-DED76214716C
title: WICCreateColorTransform\_Proxy function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WICCreateColorTransform\_Proxy function

Creates an color transform object that implements [**IWICColorTransform**](https://msdn.microsoft.com/windows/desktop/6c8ae787-3175-4128-ae9f-e11cb0e4c317). This COM object supports the free-threaded object model.

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



 

 




