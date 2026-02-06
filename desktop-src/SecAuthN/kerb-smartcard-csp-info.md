---
description: Contains information about a smart card cryptographic service provider (CSP).
ms.assetid: b3e6722a-25dd-4137-b224-4082e846ddec
title: KERB_SMARTCARD_CSP_INFO structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- KERB_SMARTCARD_CSP_INFO
api_type: 
- NA
api_location: 
---

# KERB\_SMARTCARD\_CSP\_INFO structure

The **KERB\_SMARTCARD\_CSP\_INFO** structure contains information about a smart card [*cryptographic service provider*](../secgloss/c-gly.md) (CSP).

This structure is not declared in a public header.

## Syntax


```C++
typedef struct _KERB_SMARTCARD_CSP_INFO {
  DWORD dwCspInfoLen;
  DWORD MessageType;
  union {
    PVOID   ContextInformation;
    ULONG64 SpaceHolderForWow64;
  };
  DWORD flags;
  DWORD KeySpec;
  ULONG nCardNameOffset;
  ULONG nReaderNameOffset;
  ULONG nContainerNameOffset;
  ULONG nCSPNameOffset;
  TCHAR bBuffer;
} KERB_SMARTCARD_CSP_INFO, *PKERB_SMARTCARD_CSP_INFO;
```



## Members

<dl> <dt>

**dwCspInfoLen**
</dt> <dd>

The size, in bytes, of this structure, including any appended data.

</dd> <dt>

**MessageType**
</dt> <dd>

The type of message being passed. This member must be set to 1.

</dd> <dt>

**ContextInformation**
</dt> <dd>

Reserved.

</dd> <dt>

**SpaceHolderForWow64**
</dt> <dd>

Reserved.

</dd> <dt>

**flags**
</dt> <dd>

Reserved.

</dd> <dt>

**KeySpec**
</dt> <dd>

The private key to use from the key container specified within the buffer **bBuffer**. The key can be one of the following values, defined in WinCrypt.h.



| Value                                                                                                                                                                                                                   | Meaning                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| <span id="AT_KEYEXCHANGE"></span><span id="at_keyexchange"></span><dl> <dt>**AT\_KEYEXCHANGE**</dt> <dt>1</dt> </dl> | The key is a key-exchange key.<br/> |
| <span id="AT_SIGNATURE"></span><span id="at_signature"></span><dl> <dt>**AT\_SIGNATURE**</dt> <dt>2</dt> </dl>       | The key is a signature key.<br/>    |



 

</dd> <dt>

**nCardNameOffset**
</dt> <dd>

The number of characters in the **bBuffer** buffer that precede the name of the smart card in that buffer.

> [!IMPORTANT]
> If the name of the smart card is not provided, the buffer must contain an empty string.

 

</dd> <dt>

**nReaderNameOffset**
</dt> <dd>

The number of characters in the **bBuffer** buffer that precede the name of the smart card reader in that buffer.

> [!IMPORTANT]
> If the name of the smart card reader is not provided, the buffer must contain an empty string.

 

</dd> <dt>

**nContainerNameOffset**
</dt> <dd>

The number of characters in the **bBuffer** buffer that precede the name of the key container in that buffer. This string cannot be empty.

</dd> <dt>

**nCSPNameOffset**
</dt> <dd>

The number of characters in the **bBuffer** buffer that precede the name of the CSP in that buffer.

</dd> <dt>

**bBuffer**
</dt> <dd>

An array of characters initialized to a length of `sizeof(DWORD)`. This buffer contains the names referred to by the **nCardNameOffset**, **nReaderNameOffset**, **nContainerNameOffset**, and **nCSPNameOffset** members, as well as any additional data provided by the CSP.

Any names that are not provided must be represented in this buffer by empty strings.


</dd> </dl>



## Remarks

**bBuffer layout**

The **bBuffer** begins with a DWORD-sized placeholder/prefix of `sizeof(DWORD)` bytes and then stores null-terminated strings for the card, reader, container, and CSP names (each may be an empty string except the container name which must be non-empty), followed by any CSP-specific extra data.


| Start of bBuffer |
|------------------|
| DWORD reserve (4 bytes) |
| CardName string ("" or null-terminated) |
| ReaderName string ("" or null-terminated) |
| ContainerName string (null-terminated, required) |
| CSPName string ("" or null-terminated) |
| Additional CSP-specific data ... |


- **Offsets:** `nCardNameOffset`, `nReaderNameOffset`, `nContainerNameOffset`, and `nCSPNameOffset` are the number of characters from the start of `bBuffer` to the beginning of each respective string. These counts include the initial reserved `sizeof(DWORD)` region and are measured in `TCHAR` units (ANSI `char` or Unicode `wchar_t`, depending on build).
- **Empty names:** When a name is not provided, the buffer must contain an empty string (zero-length followed by the terminator) at that position.
- **Serialization alignment:** When serialized, structure members must be aligned to 2-byte boundaries.


## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**KERB\_CERTIFICATE\_LOGON**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-kerb_certificate_logon)
</dt> </dl>

 

 
