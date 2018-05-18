---
title: ISCPSecureAuthenticate2 GetSCPSession method
description: The GetSCPSession method is used to obtain a pointer to the ISCPSecureQuery interface that represents a session object.
ms.assetid: '7e09d8ea-65aa-427b-a876-00b089659b1b'
keywords: ["GetSCPSession method windows Media Device Manager", "GetSCPSession method windows Media Device Manager , ISCPSecureAuthenticate2 interface", "ISCPSecureAuthenticate2 interface windows Media Device Manager , GetSCPSession method"]
topic_type:
- apiref
api_name:
- ISCPSecureAuthenticate2.GetSCPSession
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSecureAuthenticate2::GetSCPSession method

The **GetSCPSession** method is used to obtain a pointer to the [**ISCPSecureQuery**](iscpsecurequery.md) interface that represents a session object.

## Syntax


```C++
HRESULT GetSCPSession(
  [out] ISCPSession **ppSCPSession
);
```



## Parameters

<dl> <dt>

*ppSCPSession* \[out\]
</dt> <dd>

Pointer to an [**ISCPSession**](iscpsession.md) object.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.

## Remarks

This method is used to obtain a secure content provider (SCP) session. An SCP session is useful during transfer of multiple files, where the session can help SCP do some of the operations only once instead of once for every file transfer. This results in better transfer performance.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSecureAuthenticate2 Interface**](iscpsecureauthenticate2.md)
</dt> </dl>

 

 





