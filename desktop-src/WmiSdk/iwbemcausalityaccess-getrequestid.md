---
description: The GetRequestId method returns a Globally Unique Identifier (GUID) value for a request. A GUID is a unique 128-bit number.
ms.assetid: c8df15cf-ab48-491f-ac18-1dad567bbc0b
ms.tgt_platform: multiple
title: IWbemCausalityAccess::GetRequestId method (Wbemint.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWbemCausalityAccess.GetRequestId
api_type: 
- COM
api_location: 
- Fastprox.dll
---

# IWbemCausalityAccess::GetRequestId method

The **GetRequestId** method returns a Globally Unique Identifier (GUID) value for a request. A GUID is a unique 128-bit number.

## Syntax


```C++
HRESULT GetRequestId(
  [out] REQUESTID *pId
);
```



## Parameters

<dl> <dt>

*pId* \[out\]
</dt> <dd>

The GUID value that uniquely identifies a request. For example, 5b2fc63a-8af4-44cb-960c-aefdced908d6.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemint.h</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Fastprox.dll</dt> </dl> |



## See also

<dl> <dt>

[**IWbemCausalityAccess**](iwbemcausalityaccess.md)
</dt> </dl>

 

 




