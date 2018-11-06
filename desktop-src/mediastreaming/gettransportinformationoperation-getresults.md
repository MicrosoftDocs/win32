---
title: GetTransportInformationOperation GetResults method
description: Returns the results of the asynchronous operation started by GetTransportInformationAsync.
ms.assetid: 8CC6641E-C1E6-4C64-90EC-4120ECB54135
keywords:
- GetResults method Media Streaming API
- GetResults method Media Streaming API , GetTransportInformationOperation interface
- GetTransportInformationOperation interface Media Streaming API , GetResults method
topic_type:
- apiref
api_name:
- GetTransportInformationOperation.GetResults
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# GetTransportInformationOperation::GetResults method

Returns the results of the asynchronous operation started by [**GetTransportInformationAsync**](https://msdn.microsoft.com/en-us/library/Hh828932(v=VS.85).aspx).

## Syntax


```C++
HRESULT GetResults(
  [out, retval] TransportInformation *value
);
```



## Parameters

<dl> <dt>

*value* \[out, retval\]
</dt> <dd>

A reference to a [**TransportInformation**](https://msdn.microsoft.com/en-us/library/Hh829005(v=VS.85).aspx) structure that contains the results of the operation.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

The **GetResults** method is typically called from the event handler that was registered by setting the [**Completed**](gettransportinformationoperation-completed.md) property.

## See also

<dl> <dt>

[**GetTransportInformationOperation**](gettransportinformationoperation.md)
</dt> </dl>

 

 





