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
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IAMWMBufferPass::SetNotify method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 