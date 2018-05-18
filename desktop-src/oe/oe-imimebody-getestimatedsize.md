---
title: IMimeBody GetEstimatedSize method
description: Gets the estimated size of the data stored in the body.
ms.assetid: '4848833f-9525-4173-b245-3bacf647b7a9'
keywords: ["GetEstimatedSize method Windows Mail (formerly Outlook Express)", "GetEstimatedSize method Windows Mail (formerly Outlook Express) , IMimeBody interface", "IMimeBody interface Windows Mail (formerly Outlook Express) , GetEstimatedSize method"]
topic_type:
- apiref
api_name:
- IMimeBody.GetEstimatedSize
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeBody::GetEstimatedSize method

Gets the estimated size of the data stored in the body.

## Syntax


```C++
HRESULT GetEstimatedSize(
  [in]  ENCODINGTYPE ietEncoding,
  [out] ULONG        *pcbSize
);
```



## Parameters

<dl> <dt>

*ietEncoding* \[in\]
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

Specifies the [**ENCODINGTYPE**](oe-encodingtype.md) in which to compute the estimated size.

</dd> <dt>

*pcbSize* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the size, in bytes, of the body data.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                   | Description                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                          | Indicates success.<br/>                                                                                                               |
| <dl> <dt>**E\_FAIL**</dt> </dl>                        | Indicates that an unknown error has occurred.<br/>                                                                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                  | Indicates that *pcbSize* is **NULL** or that *ietEncoding* is greater than or equal to [**IET\_UNKNOWN**](oe-encodingtype.md). <br/> |
| <dl> <dt>**MIME\_E\_INVALID\_ENCODINGTYPE**</dt> </dl> | Indicates that *ietEncoding* is equal to [**IET\_UNKNOWN**](oe-encodingtype.md). <br/>                                               |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>              | Indicates that the body has no data. <br/>                                                                                            |



 

## Remarks

The size returned is estimated because the actual cannot always be determined. For example, if *ietEncoding* is set to [**IET\_DECODED**](oe-encodingtype.md) and the data stored in the body is encoded, this method does not actually decode the data, but instead computes the actual size of data based on how the data is encoded.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





