---
title: IWMSecureBuffer Decrypt method (Wmdrmsdk.h)
description: The Decrypt method decrypts a data pointer that was encrypted by calling the Encrypt method.
ms.assetid: 15cedb56-686a-4a3c-81a5-b1797cfe0838
keywords:
- Decrypt method windows Media Format
- Decrypt method windows Media Format , IWMSecureBuffer interface
- IWMSecureBuffer interface windows Media Format , Decrypt method
topic_type:
- apiref
api_name:
- IWMSecureBuffer.Decrypt
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMSecureBuffer::Decrypt method

The **Decrypt** method decrypts a data pointer that was encrypted by calling the [**Encrypt**](iwmsecurebuffer-encrypt.md) method.

## Syntax


```C++
HRESULT Decrypt(
  [in] IWMSecureChannel *pSecureChannel
);
```



## Parameters

<dl> <dt>

*pSecureChannel* \[in\]
</dt> <dd>

Pointer to a secure channel interface containing the encrypted data pointer.

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

[**Encrypt**](iwmsecurebuffer-encrypt.md)
</dt> <dt>

[**IWMSecureBuffer Interface**](iwmsecurebuffer.md)
</dt> </dl>

 

 





