---
title: EapHostPeerNapInfo structure
description: Contains the Network Access Protection (NAP) information on an EAP supplicant.
ms.assetid: '703eda56-5932-44d5-ae7f-0a6328d82237'
keywords: ["EapHostPeerNapInfo structure EAPHost"]
topic_type:
- apiref
api_name:
- EapHostPeerNapInfo
api_location:
- eaphostpeerapis.h
api_type:
- HeaderDef
---

# EapHostPeerNapInfo structure

The **EapHostPeerNapInfo** structure contains the Network Access Protection (NAP) information on an EAP supplicant.

## Syntax


```C++
typedef struct _tagEapHostPeerNapInfo {
  ISOLATION_STATE isolationState;
  ProbationTime   probationTime;
  UINT32          stringCorrelationIdLength;
} EapHostPeerNapInfo;
```



## Members

<dl> <dt>

**isolationState**
</dt> <dd>

An [**ISOLATION\_STATE**](isolation-state.md) structure that specifies the NAP isolation state of a computer. The isolation state determines the level of network access granted.

</dd> <dt>

**probationTime**
</dt> <dd>

A **ProbationTime** structure that specifies the time required for the connection to come out of quarantine after which the connection will be dropped. A **ProbationTime** structure is identical to a [FILETIME](http://go.microsoft.com/fwlink/p/?linkid=90006) structure.

</dd> <dt>

**stringCorrelationIdLength**
</dt> <dd>

The length, in bytes, of the NAP [stringCorrelationId](https://msdn.microsoft.com/library/windows/desktop/cc441807) that follows this structure.

</dd> </dl>

## Remarks

The **EapHostPeerNapInfo** structure precedes the NAP [stringCorrelationId](https://msdn.microsoft.com/library/windows/desktop/cc441807) of data type **WCHAR** in the RPC byte stream.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                      |
| Header<br/>                   | <dl> <dt>Eaphostpeerapis.h</dt> </dl> |



## See also

<dl> <dt>

[EAPHost Supplicant Structures](eap-host-supplicant-structures.md)
</dt> <dt>

[**EapHostPeerGetAuthStatus**](eaphostpeergetauthstatus.md)
</dt> <dt>

[**EapHostPeerMethodAuthParams**](eaphostpeerauthparams.md)
</dt> </dl>

 

 





