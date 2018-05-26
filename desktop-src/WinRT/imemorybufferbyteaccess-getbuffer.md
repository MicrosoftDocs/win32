---
Description: Gets an IMemoryBuffer as an array of bytes.
ms.assetid: E9C2AF2D-ADBE-4D76-A549-2DBCB9818B09
title: IMemoryBufferByteAccessGetBuffer method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMemoryBufferByteAccess::GetBuffer method

Gets an [**IMemoryBuffer**](w_found.imemorybuffer) as an array of bytes.

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

When [**MemoryBuffer::Close**](w_found.memorybuffer_close) is called, the code using this buffer should set the *value* pointer to null.

## See also

<dl> <dt>

[**IMemoryBufferByteAccess**](/windows/win32/memorybuffer/ns-memorybuffer-imemorybufferbyteaccess?branch=master)
</dt> </dl>

 

 



