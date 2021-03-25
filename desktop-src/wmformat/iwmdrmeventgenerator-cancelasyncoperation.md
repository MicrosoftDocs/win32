---
title: IWMDRMEventGenerator CancelAsyncOperation method (Wmdrmsdk.h)
description: The CancelAsyncOperation method cancels an asynchronous operation.
ms.assetid: 95c59e03-b6c8-40c2-b1dc-381cb6d8d558
keywords:
- CancelAsyncOperation method windows Media Format
- CancelAsyncOperation method windows Media Format , IWMDRMEventGenerator interface
- IWMDRMEventGenerator interface windows Media Format , CancelAsyncOperation method
topic_type:
- apiref
api_name:
- IWMDRMEventGenerator.CancelAsyncOperation
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMEventGenerator::CancelAsyncOperation method

The **CancelAsyncOperation** method cancels an asynchronous operation.

## Syntax


```C++
HRESULT CancelAsyncOperation(
  [in] IUnknown *punkCancelationCookie
);
```



## Parameters

<dl> <dt>

*punkCancelationCookie* \[in\]
</dt> <dd>

Pointer to the cancellation cookie that identifies the asynchronous operation to be canceled. This cookie is provided by the method used to start the operation.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

None.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMEventGenerator Interface**](iwmdrmeventgenerator.md)
</dt> </dl>

 

 





