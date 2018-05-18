---
Description: 'This method returns an interface that provides access to the video data.'
ms.assetid: '084F020F-A6F5-4982-BA4B-A8F8D6182868'
title: 'IVideoFrameNative::GetData method'
---

# IVideoFrameNative::GetData method

This method returns an interface that provides access to the video data.

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

The IID of the interface to retrieve.

</dd> <dt>

*ppv* \[out\]
</dt> <dd>

When this method returns successfully, contains the interface pointer requested in *riid* parameter.

</dd> </dl>

## Return value

Returns S\_OK on successful completion. Returns E\_NOINTERFACE if the requested interface can't be found.

## See also

<dl> <dt>

[**IVideoFrameNative**](ivideoframenative.md)
</dt> </dl>

 

 



