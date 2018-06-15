---
title: IMediaRendererActionInformation IsSetNextSourceAvailable method
description: Retrieves a value that indicates whether the DMR is currently accepting the SetNextSourceFromUriAsync method, the SetNextSourceFromStreamAsync method or the SetNextSourceFromMediaSourceAsync method.
ms.assetid: 7588E992-4070-4E0F-8C4B-7DFC097A5076
keywords:
- IsSetNextSourceAvailable method Media Streaming API
- IsSetNextSourceAvailable method Media Streaming API , IMediaRendererActionInformation interface
- IMediaRendererActionInformation interface Media Streaming API , IsSetNextSourceAvailable method
topic_type:
- apiref
api_name:
- IMediaRendererActionInformation.IsSetNextSourceAvailable
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMediaRendererActionInformation::IsSetNextSourceAvailable method

Retrieves a value that indicates whether the DMR is currently accepting the [**SetNextSourceFromUriAsync**](https://msdn.microsoft.com/en-us/library/Hh828946(v=VS.85).aspx) method, the [**SetNextSourceFromStreamAsync**](https://msdn.microsoft.com/en-us/library/Hh828945(v=VS.85).aspx) method or the [**SetNextSourceFromMediaSourceAsync**](https://msdn.microsoft.com/en-us/library/Hh828944(v=VS.85).aspx) method.

## Syntax


```C++
HRESULT IsSetNextSourceAvailable(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

A boolean value that is **True** if the DMR is currently accepting the [**SetNextSourceFromUriAsync**](https://msdn.microsoft.com/en-us/library/Hh828946(v=VS.85).aspx) method, the [**SetNextSourceFromStreamAsync**](https://msdn.microsoft.com/en-us/library/Hh828945(v=VS.85).aspx) method or the [**SetNextSourceFromMediaSourceAsync**](https://msdn.microsoft.com/en-us/library/Hh828944(v=VS.85).aspx) method and **False** if it is not.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**IMediaRendererActionInformation**](https://msdn.microsoft.com/en-us/library/Hh828915(v=VS.85).aspx)
</dt> </dl>

 

 





