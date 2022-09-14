---
title: IAMWMBufferPass SetNotify method
description: The SetNotify method is used by applications to provide the WM ASF Writer or WM ASF Reader filter with a pointer to the application's IAMWMBufferPassCallback interface.
ms.assetid: b0fff344-a20c-4cfc-828b-c6fc49d990ea
keywords:
- SetNotify method windows Media Format
- SetNotify method windows Media Format , IAMWMBufferPass interface
- IAMWMBufferPass interface windows Media Format , SetNotify method
topic_type:
- apiref
api_name:
- IAMWMBufferPass.SetNotify
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IAMWMBufferPass::SetNotify method

The **SetNotify** method is used by applications to provide the WM ASF Writer or [WM ASF Reader](wm-asf-reader-filter.md) filter with a pointer to the application's [**IAMWMBufferPassCallback**](/previous-versions/windows/desktop/api/dshowasf/nn-dshowasf-iamwmbufferpasscallback) interface.

## Syntax


```C++
HRESULT SetNotify(
  [in] IAMWMBufferPassCallback *pCallback
);
```



## Parameters

<dl> <dt>

*pCallback* \[in\]
</dt> <dd>

Pointer to the application's **IAMWMBufferPassCallback** interface.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.

## Remarks

Call this method before putting the filter graph into the run state.

## See also

<dl> <dt>

[**IAMWMBufferPass Interface**](/previous-versions/windows/desktop/api/dshowasf/nn-dshowasf-iamwmbufferpass)
</dt> </dl>

 

 