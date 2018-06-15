---
title: IMediaRendererActionInformation IsSeekAvailable method
description: Retrieves a value that indicates whether the DMR is currently accepting the SeekAsync method.
ms.assetid: F0817184-70F2-43AC-A2BE-A15F4B195085
keywords:
- IsSeekAvailable method Media Streaming API
- IsSeekAvailable method Media Streaming API , IMediaRendererActionInformation interface
- IMediaRendererActionInformation interface Media Streaming API , IsSeekAvailable method
topic_type:
- apiref
api_name:
- IMediaRendererActionInformation.IsSeekAvailable
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMediaRendererActionInformation::IsSeekAvailable method

Retrieves a value that indicates whether the DMR is currently accepting the [**SeekAsync**](https://msdn.microsoft.com/en-us/library/Hh828942(v=VS.85).aspx) method.

## Syntax


```C++
HRESULT IsSeekAvailable(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

A boolean value that is **True** if the DMR is currently accepting the [**SeekAsync**](https://msdn.microsoft.com/en-us/library/Hh828942(v=VS.85).aspx) method and **False** if it is not.

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

 

 





