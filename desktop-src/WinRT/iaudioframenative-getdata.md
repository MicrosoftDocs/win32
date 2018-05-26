---
Description: This method returns an interface that provides access to the audio data.
ms.assetid: 4FA7CC9D-D379-4C08-8D4F-5301ECCDF372
title: IAudioFrameNativeGetData method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IAudioFrameNative::GetData method

This method returns an interface that provides access to the audio data.

## Syntax


```C++
HRESULT GetData(
  [in]  REFIID riid,
  [out] LPVOID *ppv
);
```



## Parameters

<dl> <dt>

*riid* \[in\]
</dt> <dd>

Type: **REFIID**

The IID of the interface to retrieve.

</dd> <dt>

*ppv* \[out\]
</dt> <dd>

Type: **LPVOID\***

When this method returns successfully, contains the interface pointer requested in *riid* parameter.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

Returns S\_OK on successful completion. Returns E\_NOINTERFACE if the requested interface can't be found.

## See also

<dl> <dt>

[**IAudioFrameNative**](/windows/win32/windows.media.core.interop/nn-windows-media-core-interop-iaudioframenative?branch=master)
</dt> </dl>

 

 



