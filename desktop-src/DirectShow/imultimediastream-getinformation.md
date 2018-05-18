---
Description: 'Note  This interface is deprecated. New applications should not use it. The GetInformation method retrieves the capabilities of the multimedia stream object.'
ms.assetid: '27be6104-9ca4-48d7-aeda-5b633460e252'
title: 'IMultiMediaStream::GetInformation method'
---

# IMultiMediaStream::GetInformation method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

The `GetInformation` method retrieves the capabilities of the multimedia stream object.

## Syntax


```C++
HRESULT GetInformation(
  [out] DWORD       *pdwFlags,
  [out] STREAM_TYPE *pStreamType
);
```



## Parameters

<dl> <dt>

*pdwFlags* \[out\]
</dt> <dd>

Pointer to a variable that receives a bitwise combination of the following flags.



| Value               | Description                                                                    |
|---------------------|--------------------------------------------------------------------------------|
| MMSSF\_ASYNCHRONOUS | The object supports asynchronous sample updates. This flag is always returned. |
| MMSSF\_HASCLOCK     | The object has a clock.                                                        |
| MMSSF\_SUPPORTSEEK  | The object supports seeking.                                                   |



 

This parameter can be **NULL**.

</dd> <dt>

*pStreamType* \[out\]
</dt> <dd>

Pointer to a variable that receives a member of the [**STREAM\_TYPE**](stream-type.md) enumeration. This value indicates whether the multimedia stream is read-only, write-only, or read/write. This parameter can be **NULL**.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                  | Description                  |
|----------------------------------------------------------------------------------------------|------------------------------|
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | Unexpected error.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>          |



 

## See also

<dl> <dt>

[**IMultiMediaStream Interface**](imultimediastream.md)
</dt> </dl>

 

 




