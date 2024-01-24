---
description: Contains EAPOL configuration parameters.
ms.assetid: 4157a643-86f2-4f6f-8517-6207b11ea9a1
title: EAPOL_INTF_PARAMS structure (Wzcsapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EAPOL_INTF_PARAMS
api_type: 
- HeaderDef
api_location: 
- wzcsapi.h
---

# EAPOL\_INTF\_PARAMS structure

\[**EAPOL\_INTF\_PARAMS** is no longer supported as of Windows Vista and Windows Server 2008. Instead, use the [Native Wifi API](native-wifi-reference.md), which provides similar functionality. For more information, see [About the Native Wifi API](about-the-native-wifi-api.md).\]

Contains EAPOL configuration parameters.

## Syntax


```C++
typedef struct _EAPOL_INTF_PARAMS {
  DWORD dwVersion;
  DWORD dwReserved2;
  DWORD dwEapFlags;
  DWORD dwEapType;
  DWORD dwSizeOfSSID;
  BYTE  bSSID[MAX_NETWORK_NAME_LENGTH];
} EAPOL_INTF_PARAMS, *PEAPOL_INTF_PARAMS;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

Version of the caller. Default is 0.

</dd> <dt>

**dwReserved2**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**dwEapFlags**
</dt> <dd>

Not used.

</dd> <dt>

**dwEapType**
</dt> <dd>

The EAP extension type to be used. Set to 0x00000013 for EAP-TLS and 0x00000026 for PEAP.

</dd> <dt>

**dwSizeOfSSID**
</dt> <dd>

Size of network identifier.

</dd> <dt>

**bSSID**
</dt> <dd>

Network identifier.

</dd> </dl>

## Remarks

The header file wzcsapi.h is not available in the Windows SDK.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                 |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows XP with SP3<br/>                                                       |
| End of server support<br/>    | Windows Server 2003<br/>                                                       |
| Header<br/>                   | <dl> <dt>Wzcsapi.h</dt> </dl> |



 

 




