---
title: EapHostPeerNapInfo structure (Eaphostpeerapis.h)
description: Contains the Network Access Protection (NAP) information on an EAP supplicant.
ms.assetid: 703eda56-5932-44d5-ae7f-0a6328d82237
keywords:
- EapHostPeerNapInfo structure EAPHost
topic_type:
- apiref
api_name:
- EapHostPeerNapInfo
api_location:
- eaphostpeerapis.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# EapHostPeerNapInfo structure

The **EapHostPeerNapInfo** structure contains the Network Access Protection (NAP) information on an EAP supplicant.

## Syntax


```C++
typedef struct _tagEapHostPeerNapInfo {
  ISOLATION_STATE isolationState;
  ProbationTime   probationTime;
  UINT32          stringCorrelationIdLength;
} EapHostPeerNapInfo;
```



## Members

<dl> <dt>

**isolationState**
</dt> <dd>

An [**ISOLATION\_STATE**](/windows/desktop/api/eaphostpeertypes/ne-eaphostpeertypes-isolation_state) structure that specifies the NAP isolation state of a computer. The isolation state determines the level of network access granted.

</dd> <dt>

**probationTime**
</dt> <dd>

A **ProbationTime** structure that specifies the time required for the connection to come out of quarantine after which the connection will be dropped. A **ProbationTime** structure is identical to a [FILETIME](/windows/win32/api/minwinbase/ns-minwinbase-filetime) structure.

</dd> <dt>

**stringCorrelationIdLength**
</dt> <dd>

The length, in bytes, of the NAP [stringCorrelationId](/windows/desktop/NAP/nap-datatypes) that follows this structure.

</dd> </dl>

## Remarks

The **EapHostPeerNapInfo** structure precedes the NAP [stringCorrelationId](/windows/desktop/NAP/nap-datatypes) of data type **WCHAR** in the RPC byte stream.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                      |
| Header<br/>                   | <dl> <dt>Eaphostpeerapis.h</dt> </dl> |



## See also

<dl> <dt>

[EAPHost Supplicant Structures](eap-host-supplicant-structures.md)
</dt> <dt>

[**EapHostPeerGetAuthStatus**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeergetauthstatus)
</dt> <dt>

[**EapHostPeerMethodAuthParams**](/windows/win32/api/eaphostpeertypes/ne-eaphostpeertypes-eaphostpeerauthparams)
</dt> </dl>

 

