---
description: Gets an IMemoryBuffer as an array of bytes.
ms.assetid: E9C2AF2D-ADBE-4D76-A549-2DBCB9818B09
title: IMemoryBufferByteAccess::GetBuffer method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMemoryBufferByteAccess.GetBuffer
api_type: 
- COM
api_location: 
---

# IMemoryBufferByteAccess::GetBuffer method

Gets an [**IMemoryBuffer**](/uwp/api/Windows.Foundation.IMemoryBuffer) as an array of bytes.

## Syntax


```C++
HRESULT GetBuffer(
  [out] BYTE   **value,
  [out] UINT32 *capacity
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

A pointer to a byte array containing the buffer data.

</dd> <dt>

*capacity* \[out\]
</dt> <dd>

The number of bytes in the returned array

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

When [**MemoryBuffer::Close**](/uwp/api/Windows.Foundation.MemoryBuffer) is called, the code using this buffer should set the *value* pointer to null.

## See also

<dl> <dt>

[**IMemoryBufferByteAccess**](/previous-versions//mt297505(v=vs.85))
</dt> </dl>

 

 
