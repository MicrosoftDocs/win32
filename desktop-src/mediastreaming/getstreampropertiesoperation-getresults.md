---
title: GetStreamPropertiesOperation.GetResults method
description: Returns the results of the asynchronous operation started by GetStreamPropertiesAsync.
ms.assetid: D09DCDF5-2B9E-4E03-908B-AEEC7DC228C1
keywords:
- GetResults method Media Streaming API
- GetResults method Media Streaming API , GetStreamPropertiesOperation interface
- GetStreamPropertiesOperation interface Media Streaming API , GetResults method
topic_type:
- apiref
api_name:
- GetStreamPropertiesOperation.GetResults
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetStreamPropertiesOperation.GetResults method

Returns the results of the asynchronous operation started by [**GetStreamPropertiesAsync**](streamselector-getstreampropertiesasync.md).

## Syntax


```C++
HRESULT GetResults(
  [out, retval] UINT32 *value
);
```



## Parameters

<dl> <dt>

*value* \[out, retval\]
</dt> <dd></dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**GetStreamPropertiesOperation**](getstreampropertiesoperation.md)
</dt> </dl>

 

 





