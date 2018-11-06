---
title: ITransportParameters ActionInformation method
description: Obtains an IMediaRendererActionInformation interface that provides information about which methods can currently be invoked on the DMR.
ms.assetid: 3EEB94E1-B6BC-4111-AEF1-D5724BD0A2E7
keywords:
- ActionInformation method Media Streaming API
- ActionInformation method Media Streaming API , ITransportParameters interface
- ITransportParameters interface Media Streaming API , ActionInformation method
topic_type:
- apiref
api_name:
- ITransportParameters.ActionInformation
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# ITransportParameters::ActionInformation method

Obtains an [**IMediaRendererActionInformation**](https://msdn.microsoft.com/en-us/library/Hh828915(v=VS.85).aspx) interface that provides information about which methods can currently be invoked on the DMR.

## Syntax


```C++
HRESULT ActionInformation(
  [out, retval] IMediaRendererActionInformation **value
);
```



## Parameters

<dl> <dt>

*value* \[out, retval\]
</dt> <dd>

Receives a reference to an [**IMediaRendererActionInformation**](https://msdn.microsoft.com/en-us/library/Hh828915(v=VS.85).aspx) interface.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**ITransportParameters**](https://msdn.microsoft.com/en-us/library/Hh828956(v=VS.85).aspx)
</dt> </dl>

 

 





