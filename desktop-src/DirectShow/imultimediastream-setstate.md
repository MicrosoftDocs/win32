---
Description: 'Note  This interface is deprecated. New applications should not use it. The SetState method runs or stops the multimedia stream object.'
ms.assetid: '69c3612f-e91a-4ab3-8f6d-2966e64a9220'
title: 'IMultiMediaStream::SetState method'
---

# IMultiMediaStream::SetState method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

The `SetState` method runs or stops the multimedia stream object.

## Syntax


```C++
HRESULT SetState(
  [in] STREAM_STATE NewState
);
```



## Parameters

<dl> <dt>

*NewState* \[in\]
</dt> <dd>

A member of the [**STREAM\_STATE**](stream-state.md) enumeration, specifying the new state (running or stopped).

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                  | Description                  |
|----------------------------------------------------------------------------------------------|------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Invalid argument.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>          |



 

## Remarks

Stopping the multimedia stream object deletes any data that is pending.

## See also

<dl> <dt>

[**IMultiMediaStream Interface**](imultimediastream.md)
</dt> </dl>

 

 




