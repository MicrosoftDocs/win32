---
Description: Gets an IMemoryBuffer as an array of bytes.
ms.assetid: E9C2AF2D-ADBE-4D76-A549-2DBCB9818B09
title: IMemoryBufferByteAccess::GetBuffer method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMemoryBufferByteAccess::GetBuffer method

Gets an [**IMemoryBuffer**](https://www.bing.com/search?q=**IMemoryBuffer**) as an array of bytes.

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

When [**MemoryBuffer::Close**](https://www.bing.com/search?q=**MemoryBuffer::Close**) is called, the code using this buffer should set the *value* pointer to null.

## See also

<dl> <dt>

[**IMemoryBufferByteAccess**](/windows/desktop/api/memorybuffer/ns-memorybuffer-imemorybufferbyteaccess)
</dt> </dl>

 

 



