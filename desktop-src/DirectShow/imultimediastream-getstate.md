---
Description: 'Note  This interface is deprecated. New applications should not use it. The GetState method retrieves the current state of the multimedia stream object.'
ms.assetid: '8d01c4cf-2de9-4e9c-8b6e-921284f4f1b6'
title: 'IMultiMediaStream::GetState method'
---

# IMultiMediaStream::GetState method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

The `GetState` method retrieves the current state of the multimedia stream object.

## Syntax


```C++
HRESULT GetState(
  [out] STREAM_STATE *pCurrentState
);
```



## Parameters

<dl> <dt>

*pCurrentState* \[out\]
</dt> <dd>

Pointer to a variable that receives a member of the [**STREAM\_STATE**](stream-state.md) enumeration.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                               | Description                           |
|-------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>      | Success.<br/>                   |



 

## See also

<dl> <dt>

[**IMultiMediaStream Interface**](imultimediastream.md)
</dt> </dl>

 

 




