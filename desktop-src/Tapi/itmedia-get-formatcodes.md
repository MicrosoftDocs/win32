---
description: The get\_FormatCodes method gets the list of media payload format codes. The variant returns a SAFEARRAY of BSTRs. Each BSTR within that array is a format code string.
ms.assetid: 8663d7e8-d46f-44d1-93db-9b5142bb28dd
title: ITMedia::get_FormatCodes method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITMedia::get\_FormatCodes method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_FormatCodes** method gets the list of media payload format codes. The variant returns a SAFEARRAY of **BSTR**s. Each **BSTR** within that array is a format code string.

## Syntax


```C++
HRESULT get_FormatCodes(
  [out] VARIANT *pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out\]
</dt> <dd>

Array of media payload format codes.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pVal* parameter is not a valid pointer.<br/>         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

When a list of payload formats is given, this implies that all of these formats may be used in the session, but the first of these formats is the default format for the session. When the transport protocol is RTP, the format codes are RTP payload types.

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITMedia**](itmedia.md)
</dt> <dt>

[**ITMedia::put\_FormatCodes**](itmedia-put-formatcodes.md)
</dt> </dl>

 

 




