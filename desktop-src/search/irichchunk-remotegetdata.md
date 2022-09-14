---
description: Retrieves the PROPVARIANT and input string that represents a chunk of data. Calling this method is the same as calling GetData.
ms.assetid: 78846D1D-923F-4FEA-8BF2-B16BB1B21BB3
title: IRichChunk::RemoteGetData method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRichChunk.RemoteGetData
api_type: 
- COM
api_location: 
---

# IRichChunk::RemoteGetData method

Retrieves the [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) and input string that represents a chunk of data. Calling this method is the same as calling [**GetData**](/windows/desktop/api/StructuredQueryCondition/nf-structuredquerycondition-irichchunk-getdata).

## Syntax


```C++
HRESULT RemoteGetData(
  [out] ULONG       *pFirstPos,
  [out] ULONG       *pLength,
  [out] LPWSTR      *ppsz,
  [out] PROPVARIANT *pValue
);
```



## Parameters

<dl> <dt>

*pFirstPos* \[out\]
</dt> <dd>

Receives the zero-based starting position of the range. This parameter can be **NULL**.

</dd> <dt>

*pLength* \[out\]
</dt> <dd>

Receives the length of the range. This parameter can be **NULL**.

</dd> <dt>

*ppsz* \[out\]
</dt> <dd>

Receives the associated Unicode string value, or **NULL** if not available.

</dd> <dt>

*pValue* \[out\]
</dt> <dd>

Receives the associated [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) value, or **VT\_EMPTY** if not available. This parameter can be **NULL**.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## See also

<dl> <dt>

[**IRichChunk**](/windows/desktop/api/Structuredquerycondition/nn-structuredquerycondition-irichchunk)
</dt> </dl>

 

 
