---
title: IWMSecureBuffer Encrypt method (Wmdrmsdk.h)
description: The Encrypt method encrypts a data pointer.
ms.assetid: da391dcb-3ef8-4c09-bca6-507f67a24ee6
keywords:
- Encrypt method windows Media Format
- Encrypt method windows Media Format , IWMSecureBuffer interface
- IWMSecureBuffer interface windows Media Format , Encrypt method
topic_type:
- apiref
api_name:
- IWMSecureBuffer.Encrypt
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMSecureBuffer::Encrypt method

The **Encrypt** method encrypts a data pointer.

## Syntax


```C++
HRESULT Encrypt(
  [in] IWMSecureChannel *pSecureChannel
);
```



## Parameters

<dl> <dt>

*pSecureChannel* \[in\]
</dt> <dd>

Pointer to a secure channel interface containing the data pointer to encrypt.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

Use this method to encrypt data pointers so they can be sent across DLL boundaries.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**Decrypt**](iwmsecurebuffer-decrypt.md)
</dt> <dt>

[**IWMSecureBuffer Interface**](iwmsecurebuffer.md)
</dt> </dl>

 

 





