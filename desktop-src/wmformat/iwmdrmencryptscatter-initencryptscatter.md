---
title: IWMDRMEncryptScatter InitEncryptScatter method (Wmdrmsdk.h)
description: The InitEncryptScatter method initializes the IWMDRMEncryptScatter interface for use.
ms.assetid: c5f2fa14-9465-4c53-bc42-ffcec34af083
keywords:
- InitEncryptScatter method windows Media Format
- InitEncryptScatter method windows Media Format , IWMDRMEncryptScatter interface
- IWMDRMEncryptScatter interface windows Media Format , InitEncryptScatter method
topic_type:
- apiref
api_name:
- IWMDRMEncryptScatter.InitEncryptScatter
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMEncryptScatter::InitEncryptScatter method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **InitEncryptScatter** method initializes the **IWMDRMEncryptScatter** interface for use.

## Syntax


```C++
HRESULT InitEncryptScatter(
  [in] DWORD                      cStreams,
  [in] WMDRM_ENCRYPT_SCATTER_INFO *rgInfos
);
```



## Parameters

<dl> <dt>

*cStreams* \[in\]
</dt> <dd>

Number of elements in the *rgInfos* array. This is also the number of streams that are included in the data to be encrypted.

</dd> <dt>

*rgInfos* \[in\]
</dt> <dd>

Array of one or more [**WMDRM\_ENCRYPT\_SCATTER\_INFO**](wmdrm-encrypt-scatter-info.md) structures. Each element contains encryption information for a stream. The number of elements in this array must be equal to the value of *cStreams*.

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

[**EncryptScatter**](iwmdrmencryptscatter-encryptscatter.md)
</dt> <dt>

[**IWMDRMEncryptScatter Interface**](iwmdrmencryptscatter.md)
</dt> </dl>

 

 





