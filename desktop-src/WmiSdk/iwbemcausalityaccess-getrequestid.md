---
Description: The GetRequestId method returns a Globally Unique Identifier (GUID) value for a request. A GUID is a unique 128-bit number.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c8df15cf-ab48-491f-ac18-1dad567bbc0b
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: IWbemCausalityAccessGetRequestId method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
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



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemint.h</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Fastprox.dll</dt> </dl> |



## See also

<dl> <dt>

[**IWbemCausalityAccess**](iwbemcausalityaccess.md)
</dt> </dl>

 

 




