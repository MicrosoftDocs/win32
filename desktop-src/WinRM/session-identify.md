---
title: Session.Identify method (WSManDisp.h)
description: Queries a remote computer to determine if it supports the WS-Management protocol.
ms.assetid: b86ec9b8-8fc4-4c3e-aca7-2f7d039749df
ms.tgt_platform: multiple
keywords:
- Identify method Windows Remote Management
- Identify method Windows Remote Management , Session object
- Session object Windows Remote Management , Identify method
topic_type:
- apiref
api_name:
- Session.Identify
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Session.Identify method

The **Session.Identify** method queries a remote computer to determine if it supports the WS-Management protocol. For more information, see [Detecting Whether a Remote Computer Supports WS-Management Protocol](detecting-whether-a-remote-computer-supports-ws-management-protocol.md).

## Syntax


```VB
Session.Identify( _
  [ ByVal flags ] _
)
```



## Parameters

<dl> <dt>

*flags* \[in, optional\]
</dt> <dd>

To send the request in authenticated mode use authentication constant from the **WSManSessionFlags** enumeration. To send in unauthenticated mode, use **WSManFlagUseNoAuthentication**. For more information, see [**Authentication Constants**](authentication-constants.md).

</dd> </dl>

## Return value

An XML string that specifies the WS-Management protocol version, the operating system vendor and, if the request was sent authenticated, the operating system version.

## Remarks

**Session.Identify** is based on the [WS-Management Protocol](ws-management-protocol.md) operation defined as wsmanIdentity. This is specified in the SOAP packet as follows:


```XML
xmlns:wsmid="https://schemas.dmtf.org/wbem/wsman/identity/1/wsmanidentity"
```



## Examples

The following VBScript example sends an unauthenticated Identify request to the remote computer named Remote in the same domain.


```VB
set WSMan = CreateObject("Wsman.Automation")
set Session = WSMan.CreateSession("Remote", _
  WSMan.SessionFlagUseNoAuthentication)
WScript.Echo Session.Identify
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>WSManDisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WSManDisp.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>WSManDisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WSMAuto.dll</dt> </dl>   |



## See also

<dl> <dt>

[**Session**](session.md)
</dt> <dt>

[**IWSManSession::Identify**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmansession-identify)
</dt> <dt>

[WS-Management Protocol](ws-management-protocol.md)
</dt> </dl>

 

 





