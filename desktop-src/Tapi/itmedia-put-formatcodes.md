---
description: The put\_FormatCodes method sets the list of media payload format codes. The variant contains a SAFEARRAY of BSTRs. Each BSTR within that array is a format code string.
ms.assetid: b76a7fee-0fae-41fb-a8cd-6803458d9182
title: ITMedia::put_FormatCodes method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITMedia::put\_FormatCodes method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **put\_FormatCodes** method sets the list of media payload format codes. The variant contains a SAFEARRAY of **BSTR**s. Each **BSTR** within that array is a format code string.

## Syntax


```C++
HRESULT put_FormatCodes(
  [in] VARIANT NewVal
);
```



## Parameters

<dl> <dt>

*NewVal* \[in\]
</dt> <dd>

List of media payload format codes.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *NewVal* parameter is not valid.<br/>                 |
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

[**ITMedia::get\_FormatCodes**](itmedia-get-formatcodes.md)
</dt> </dl>

 

 




