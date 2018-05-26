---
Description: This method returns a device associated with the video data.
ms.assetid: 9A61159B-C383-4770-AD8F-9F69F720E3E2
title: IVideoFrameNativeGetDevice method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVideoFrameNative::GetDevice method

This method returns a device associated with the video data.

## Syntax


```C++
HRESULT GetDevice(
  [in]  REFIID riid,
  [out] LPVOID *ppv
);
```



## Parameters

<dl> <dt>

*riid* \[in\]
</dt> <dd>

The IID of the device to retrieve.

</dd> <dt>

*ppv* \[out\]
</dt> <dd>

When this method returns successfully, contains the device pointer requested in *riid* parameter.

</dd> </dl>

## Return value

Returns S\_OK on successful completion.

## See also

<dl> <dt>

[**IVideoFrameNative**](/windows/win32/windows.media.core.interop/nn-windows-media-core-interop-ivideoframenative?branch=master)
</dt> </dl>

 

 



