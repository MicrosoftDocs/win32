---
description: The NETWORKINFO structure describes a NIC.
ms.assetid: 40169409-7de5-44d1-8dff-dfa9f647edc9
title: NETWORKINFO structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NETWORKINFO
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# NETWORKINFO structure

The NETWORKINFO structure describes a NIC.

## Syntax


```C++
typedef struct _NETWORKINFO {
  BYTE    PermanentAddr[6];
  BYTE    CurrentAddr[6];
  ADDRESS OtherAddress;
  DWORD   LinkSpeed;
  DWORD   MacType;
  DWORD   MaxFrameSize;
  DWORD   Flags;
  DWORD   TimestampScaleFactor;
  BYTE    NodeName[32];
  BOOL    PModeSupported;
  BYTE    Comment[ADAPTER_COMMENT_LENGTH];
} NETWORKINFO, *LPNETWORKINFO;
```



## Members

<dl> <dt>

**PermanentAddr**
</dt> <dd>

Permanent MAC address.

</dd> <dt>

**CurrentAddr**
</dt> <dd>

Current MAC address.

</dd> <dt>

**OtherAddress**
</dt> <dd>

Other address that support this (for example IP, IPX).

</dd> <dt>

**LinkSpeed**
</dt> <dd>

Link speed, in Mbps.

</dd> <dt>

**MacType**
</dt> <dd>

Media type.

</dd> <dt>

**MaxFrameSize**
</dt> <dd>

Maximum frame size allowed.

</dd> <dt>

**Flags**
</dt> <dd>

This parameter can be one of the following informational flags:



| Value                                                                                                                                                                                                                                       | Meaning                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="NETWORKINFO_FLAGS_PMODE_NOT_SUPPORTED"></span><span id="networkinfo_flags_pmode_not_supported"></span><dl> <dt>**NETWORKINFO\_FLAGS\_PMODE\_NOT\_SUPPORTED**</dt> </dl>    | The network card does not support promiscuous mode, meaning that it will only capture traffic which is broadcast in nature or only involves the local machine.<br/> |
| <span id="NETWORKINFO_FLAGS_RAS"></span><span id="networkinfo_flags_ras"></span><dl> <dt>**NETWORKINFO\_FLAGS\_RAS**</dt> </dl>                                                      | This is a virtual network card that is a RAS (Remote Access Server) connection through a modem or another network card.<br/>                                        |
| <span id="NETWORKINFO_FLAGS_REMOTE_CARD"></span><span id="networkinfo_flags_remote_card"></span><dl> <dt>**NETWORKINFO\_FLAGS\_REMOTE\_CARD**</dt> </dl>                             | The network card is not on the local computer, but is capturing on a remote machine at the bequest of the local computer.<br/>                                      |
| <span id="NETWORKINFO_FLAGS_REMOTE_NAL"></span><span id="networkinfo_flags_remote_nal"></span><dl> <dt>**NETWORKINFO\_FLAGS\_REMOTE\_NAL**</dt> </dl>                                | Obsolete; do not use.<br/>                                                                                                                                          |
| <span id="NETWORKINFO_FLAGS_REMOTE_NAL_CONNECTED"></span><span id="networkinfo_flags_remote_nal_connected"></span><dl> <dt>**NETWORKINFO\_FLAGS\_REMOTE\_NAL\_CONNECTED**</dt> </dl> | Obsolete; do not use.<br/>                                                                                                                                          |



 

</dd> <dt>

**TimestampScaleFactor**
</dt> <dd>

For example, a value of 1 indicates 1/1 ms, 10 indicates 1/10 ms, 100 indicates 1/100 ms, and so on.

</dd> <dt>

**NodeName**
</dt> <dd>

Name of remote workstation.

</dd> <dt>

**PModeSupported**
</dt> <dd>

NIC P-mode support indicator.

</dd> <dt>

**Comment**
</dt> <dd>

Adapter comment field.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




