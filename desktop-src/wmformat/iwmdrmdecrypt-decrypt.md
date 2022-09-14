---
title: IWMDRMDecrypt Decrypt method (Wmdrmsdk.h)
description: The Decrypt method decrypts a data buffer in place.
ms.assetid: ca0a5b2f-d25f-423e-8956-fca264399083
keywords:
- Decrypt method windows Media Format
- Decrypt method windows Media Format , IWMDRMDecrypt interface
- IWMDRMDecrypt interface windows Media Format , Decrypt method
topic_type:
- apiref
api_name:
- IWMDRMDecrypt.Decrypt
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMDecrypt::Decrypt method

The **Decrypt** method decrypts a data buffer in place.

## Syntax


```C++
HRESULT Decrypt(
  [in, out] BYTE            *pbData,
  [in]      DWORD           cbData,
  [in]      WMDRMCryptoData *pWMCryptoData
);
```



## Parameters

<dl> <dt>

*pbData* \[in, out\]
</dt> <dd>

Data to be decrypted. If the method succeeds, this data is decrypted on return.

</dd> <dt>

*cbData* \[in\]
</dt> <dd>

Size of the data in bytes.

</dd> <dt>

*pWMCryptoData* \[in\]
</dt> <dd>

Pointer to a [**WMDRMCryptoData**](wmdrmcryptodata.md) structure containing extra parameters. Can be **NULL** if the content was encrypted using the default parameters.

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
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMDecrypt Interface**](iwmdrmdecrypt.md)
</dt> <dt>

[**WMDRMCryptoData**](wmdrmcryptodata.md)
</dt> </dl>

 

 





