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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMSecureBuffer::Decrypt method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





