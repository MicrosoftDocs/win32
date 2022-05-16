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
ms.date: 05/31/2018
api_location: 
- msitss55.dll
- apss.dll
---

# WMCreateStreamForURL function

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

 

 




