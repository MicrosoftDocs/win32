---
title: IMediaRendererActionInformation PlaySpeeds method
description: Retrieves the complete list of PlaySpeed values that are accepted by the DMR.
ms.assetid: 0AB63E39-6A26-4199-9978-A10866A7C805
keywords:
- PlaySpeeds method Media Streaming API
- PlaySpeeds method Media Streaming API , IMediaRendererActionInformation interface
- IMediaRendererActionInformation interface Media Streaming API , PlaySpeeds method
topic_type:
- apiref
api_name:
- IMediaRendererActionInformation.PlaySpeeds
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMediaRendererActionInformation::PlaySpeeds method

Retrieves the complete list of [**PlaySpeed**](https://www.bing.com/search?q=**PlaySpeed**) values that are accepted by the DMR.

## Syntax


```C++
HRESULT PlaySpeeds(
  [out] IVector< PlaySpeed > **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a vector of [**PlaySpeed**](https://www.bing.com/search?q=**PlaySpeed**) structures specifying the complete list of **PlaySpeed** values that are accepted by the DMR.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**IMediaRendererActionInformation**](https://www.bing.com/search?q=**IMediaRendererActionInformation**)
</dt> </dl>

 

 





