---
description: The IsChildOf method determines if a request is a child of a specified request (pId).
ms.assetid: 7be52496-7dcf-41c0-853a-859810a57d21
ms.tgt_platform: multiple
title: IWbemCausalityAccess::IsChildOf method (Wbemint.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWbemCausalityAccess.IsChildOf
api_type: 
- COM
api_location: 
- Fastprox.dll
---

# IWbemCausalityAccess::IsChildOf method

The **IsChildOf** method determines if a request is a child of a specified request (pId). A parent request can have multiple child requests. Each request is identified by a Globally Unique Identifier (GUID) and can have a parent request or can be a top request. A GUID is a unique 128-bit number.

## Syntax


```C++
HRESULT IsChildOf(
  [in] REQUESTID pId
);
```



## Parameters

<dl> <dt>

*pId* \[in\]
</dt> <dd>

The GUID value that uniquely identifies a request. For example, 5b2fc63a-8af4-44cb-960c-aefdced908d6.

</dd> </dl>

## Return value

Returns successful if the specified request is a child of the request calling the **IsChildOf** method.

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

 

 




