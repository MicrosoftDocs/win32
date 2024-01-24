---
description: This method returns an interface that provides access to the audio data.
ms.assetid: 4FA7CC9D-D379-4C08-8D4F-5301ECCDF372
title: IAudioFrameNative::GetData method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAudioFrameNative.GetData
api_type: 
- COM
api_location: 
- windows.media.core.interop.h
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

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

Returns S\_OK on successful completion. Returns E\_NOINTERFACE if the requested interface can't be found.

## See also

<dl> <dt>

[**IAudioFrameNative**](/windows/desktop/api/windows.media.core.interop/nn-windows-media-core-interop-iaudioframenative)
</dt> </dl>

 

 



