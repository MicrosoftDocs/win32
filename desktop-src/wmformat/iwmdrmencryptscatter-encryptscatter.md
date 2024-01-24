---
title: IWMDRMEncryptScatter EncryptScatter method (Wmdrmsdk.h)
description: The EncryptScatter method unscrambles and encrypts data.
ms.assetid: e7f87aac-387b-4483-956e-bfbca0cec0f2
keywords:
- EncryptScatter method windows Media Format
- EncryptScatter method windows Media Format , IWMDRMEncryptScatter interface
- IWMDRMEncryptScatter interface windows Media Format , EncryptScatter method
topic_type:
- apiref
api_name:
- IWMDRMEncryptScatter.EncryptScatter
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMEncryptScatter::EncryptScatter method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **EncryptScatter** method unscrambles and encrypts data.

## Syntax


```C++
HRESULT EncryptScatter(
  [in]  DWORD                       cBlocks,
  [in]  WMDRM_ENCRYPT_SCATTER_BLOCK *rgBlocks,
  [in]  WMDRMCryptoData             *pWMCryptoData,
  [in]  DWORD                       cbOutput,
  [out] BYTE                        *pbOutput
);
```



## Parameters

<dl> <dt>

*cBlocks* \[in\]
</dt> <dd>

Number of elements in the *rgBlocks* array.

</dd> <dt>

*rgBlocks* \[in\]
</dt> <dd>

Array of one or more [**WMDRM\_ENCRYPT\_SCATTER\_BLOCK**](wmdrm-encrypt-scatter-block.md) structures. Each element describes a block of data to be unscrambled and encrypted.

</dd> <dt>

*pWMCryptoData* \[in\]
</dt> <dd>

Pointer to a [**WMDRMCryptoData**](wmdrmcryptodata.md) structure that contains encryption parameters. Set to **NULL** to use the default parameters.

</dd> <dt>

*cbOutput* \[in\]
</dt> <dd>

Size of the output data buffer passed as *pbOutput*.

</dd> <dt>

*pbOutput* \[out\]
</dt> <dd>

Output buffer.

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

[**InitEncryptScatter**](iwmdrmencryptscatter-initencryptscatter.md)
</dt> <dt>

[**IWMDRMEncryptScatter Interface**](iwmdrmencryptscatter.md)
</dt> </dl>

 

 





