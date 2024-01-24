---
title: WMCreateStreamForURL function
description: The WMCreateStreamForURL function is implemented by the application to create a COM IStream object for a given URL.
ms.assetid: df8d0e57-9f71-4be3-a0b0-cf61b68611bc
keywords:
- WMCreateStreamForURL function windows Media Format
topic_type:
- apiref
api_name:
- WMCreateStreamForURL
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
api_location: 
- msitss55.dll
- apss.dll
ms.custom: UpdateFrequency5
---

# WMCreateStreamForURL function

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WMCreateStreamForURL** function is implemented by the application to create a COM **IStream** object for a given URL.

## Syntax


```C++
HRESULT WMCreateStreamForURL(
  _In_  LPCWSTR pwszURL,
  _Out_ BOOL    *pfCorrectSource,
  _Out_ IStream **ppStream
);
```



## Parameters

<dl> <dt>

*pwszURL* \[in\]
</dt> <dd>

Pointer to a wide-character string containing the URL.

</dd> <dt>

*pfCorrectSource* \[out\]
</dt> <dd>

Pointer to a flag, true will prevent the SDK from trying other source plug-ins for this URL.

</dd> <dt>

*ppStream* \[out\]
</dt> <dd>

Pointer to a pointer to the **IStream** object created by the method.

</dd> </dl>

## Return value

If the function succeeds, it must return S\_OK. If it fails, it must return an appropriate **HRESULT** error code, and \**ppStream* should be set to **NULL**.

## See also

<dl> <dt>

[**Source Plug-ins**](source-plug-ins.md)
</dt> </dl>

 

 




