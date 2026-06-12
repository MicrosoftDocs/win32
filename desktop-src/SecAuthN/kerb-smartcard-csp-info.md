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
    PVOID   ContextInformation;
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

| Component (order from start of bBuffer) | Description | Requirement |
|---|---|---|
| DWORD prefix | Reserved placeholder (`sizeof(DWORD)` = 4 bytes) | Always present |
| CardName | Empty string or null-terminated card name | Optional |
| ReaderName | Empty string or null-terminated reader name | Optional |
| ContainerName | Null-terminated key container name | Required; must be non-empty |
| CSPName | Empty string or null-terminated CSP name | Optional |
| Additional data | CSP-specific appended data after names | Optional; CSP-defined format |

- **Offsets:** `nCardNameOffset`, `nReaderNameOffset`, `nContainerNameOffset`, and `nCSPNameOffset` are the number of characters from the start of `bBuffer` to the beginning of each respective string. These counts include the initial reserved `sizeof(DWORD)` region and are measured in `TCHAR` units (ANSI `char` or Unicode `wchar_t`, depending on build).
- **Empty names:** When a name is not provided, the buffer must contain an empty string (zero-length followed by the terminator) at that position.
- **Serialization alignment:** When serialized, structure members must be aligned to 2-byte boundaries.


## Examples

Because **KERB\_SMARTCARD\_CSP\_INFO** is not declared in a public header, you must declare it yourself. The `#pragma pack(push, 2)` directive is required to ensure 2-byte member alignment when the structure is serialized.

The examples below assume a Unicode build (`WCHAR` / `PCWSTR`), so offsets are measured in `WCHAR` units.

```C++
#pragma pack(push, 2)
typedef struct _KERB_SMARTCARD_CSP_INFO {
    DWORD   dwCspInfoLen;
    DWORD   MessageType;
    union {
        PVOID   ContextInformation;
        ULONG64 SpaceHolderForWow64;
    };
    DWORD   flags;
    DWORD   KeySpec;
    ULONG   nCardNameOffset;
    ULONG   nReaderNameOffset;
    ULONG   nContainerNameOffset;
    ULONG   nCSPNameOffset;
    WCHAR   bBuffer;
} KERB_SMARTCARD_CSP_INFO, *PKERB_SMARTCARD_CSP_INFO;
#pragma pack(pop)
```

The following helper function allocates and populates a **KERB\_SMARTCARD\_CSP\_INFO** structure. It demonstrates how to compute the total size, set the **bBuffer** offsets, and copy the name strings into the buffer.

```C++
// Returns a LocalAlloc'd KERB_SMARTCARD_CSP_INFO, or NULL on failure.
// The caller must free the returned pointer with LocalFree.
//
// szContainerName must be non-empty. All other name parameters may be L"".
PKERB_SMARTCARD_CSP_INFO CreateSmartCardCspInfo(
    _In_ PCWSTR szCardName,       // Smart card name, or L"" if not available
    _In_ PCWSTR szReaderName,     // Card reader name, or L"" if not available
    _In_ PCWSTR szContainerName,  // Key container name (required)
    _In_ PCWSTR szCspName,        // CSP/KSP name, or L"" to let Windows choose
    _In_ DWORD  dwKeySpec)        // AT_KEYEXCHANGE or AT_SIGNATURE
{
    if (!szCardName || !szReaderName || !szContainerName || !szCspName ||
        szContainerName[0] == L'\0')
    {
        return NULL;
    }

    // Compute the length of each name, including its null terminator.
    ULONG cchCard      = (ULONG)wcslen(szCardName)      + 1;
    ULONG cchReader    = (ULONG)wcslen(szReaderName)    + 1;
    ULONG cchContainer = (ULONG)wcslen(szContainerName) + 1;
    ULONG cchCsp       = (ULONG)wcslen(szCspName)       + 1;

    // bBuffer begins with a sizeof(DWORD)-byte reserved prefix (= 2 WCHARs in
    // Unicode builds), followed by the four null-terminated name strings.
    const ULONG cchPrefix = sizeof(DWORD) / sizeof(WCHAR); // = 2
    ULONGLONG cchBuf = (ULONGLONG)cchPrefix + cchCard + cchReader + cchContainer + cchCsp;

    // Total byte size = fixed header fields up to bBuffer, plus string data.
    ULONGLONG cbTotal = FIELD_OFFSET(KERB_SMARTCARD_CSP_INFO, bBuffer)
                      + cchBuf * sizeof(WCHAR);
    if (cbTotal > MAXDWORD)
        return NULL;

    PKERB_SMARTCARD_CSP_INFO p =
        (PKERB_SMARTCARD_CSP_INFO)LocalAlloc(LPTR, (SIZE_T)cbTotal);
    if (!p)
        return NULL;

    p->dwCspInfoLen = (DWORD)cbTotal;
    p->MessageType  = 1;         // Must always be 1.
    p->KeySpec      = dwKeySpec;

    // Each offset is the number of WCHARs from the start of bBuffer to the
    // beginning of the corresponding name string.
    p->nCardNameOffset      = cchPrefix;
    p->nReaderNameOffset    = p->nCardNameOffset      + cchCard;
    p->nContainerNameOffset = p->nReaderNameOffset    + cchReader;
    p->nCSPNameOffset       = p->nContainerNameOffset + cchContainer;

    // Copy names into bBuffer at the computed offsets.
    // The 2-WCHAR prefix region is already zeroed by LPTR.
    PWCH buf = &p->bBuffer;
    wcscpy_s(buf + p->nCardNameOffset,      cchCard,      szCardName);
    wcscpy_s(buf + p->nReaderNameOffset,    cchReader,    szReaderName);
    wcscpy_s(buf + p->nContainerNameOffset, cchContainer, szContainerName);
    wcscpy_s(buf + p->nCSPNameOffset,       cchCsp,       szCspName);

    return p;
}
```

The following example uses `CreateSmartCardCspInfo` together with [**KERB\_CERTIFICATE\_LOGON**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-kerb_certificate_logon) to perform an interactive smart card logon via [**LsaLogonUser**](/windows/desktop/api/ntsecapi/nf-ntsecapi-lsalogonuser). All pointer-type fields in **KERB\_CERTIFICATE\_LOGON** are stored as byte offsets relative to the start of the structure, not as absolute pointers.

```C++
// Performs an interactive smart card logon.
// On success, *phToken receives a handle to the logon token.
NTSTATUS SmartCardCertLogon(
    _In_  PCWSTR  szPin,
    _In_  PCWSTR  szCardName,
    _In_  PCWSTR  szReaderName,
    _In_  PCWSTR  szContainerName,
    _In_  PCWSTR  szCspName,
    _Out_ PHANDLE phToken)
{
    PKERB_SMARTCARD_CSP_INFO pCspInfo = CreateSmartCardCspInfo(
        szCardName, szReaderName, szContainerName, szCspName, AT_KEYEXCHANGE);
    if (!pCspInfo)
        return STATUS_NO_MEMORY;

    // Build a single contiguous buffer:
    //   [KERB_CERTIFICATE_LOGON | PIN string | KERB_SMARTCARD_CSP_INFO]
    ULONG cbLogon = sizeof(KERB_CERTIFICATE_LOGON);
    ULONG cbPin   = ((ULONG)wcslen(szPin) + 1) * sizeof(WCHAR);
    ULONG cbCsp   = pCspInfo->dwCspInfoLen;
    ULONG cbTotal = cbLogon + cbPin + cbCsp;

    NTSTATUS status = STATUS_NO_MEMORY;
    PBYTE pBuf = (PBYTE)LocalAlloc(LPTR, cbTotal);
    if (pBuf)
    {
        PKERB_CERTIFICATE_LOGON pLogon = (PKERB_CERTIFICATE_LOGON)pBuf;
        PWCH  pPinDst = (PWCH)(pBuf + cbLogon);
        PBYTE pCspDst =        pBuf + cbLogon + cbPin;

        wcscpy_s(pPinDst, cbPin / sizeof(WCHAR), szPin);
        memcpy(pCspDst, pCspInfo, cbCsp);

        // Pointer fields are stored as byte offsets relative to pBuf.
        pLogon->MessageType       = KerbCertificateLogon;
        pLogon->Pin.Length        = (USHORT)(wcslen(szPin) * sizeof(WCHAR));
        pLogon->Pin.MaximumLength = (USHORT)cbPin;
        pLogon->Pin.Buffer        = (PWSTR)(ULONG_PTR)cbLogon;
        pLogon->CspDataLength     = cbCsp;
        pLogon->CspData           = (PUCHAR)(ULONG_PTR)(cbLogon + cbPin);

        HANDLE hLsa;
        status = LsaConnectUntrusted(&hLsa);
        if (status >= 0)
        {
            LSA_STRING packageName;
            ULONG authPackage;
            RtlInitString(&packageName, MICROSOFT_KERBEROS_NAME_A);
            status = LsaLookupAuthenticationPackage(
                hLsa, &packageName, &authPackage);
            if (status >= 0)
            {
                LSA_STRING   origin      = {};
                TOKEN_SOURCE tokenSource = {};
                PVOID        pProfile   = NULL;
                ULONG        cbProfile  = 0;
                LUID         logonId;
                QUOTA_LIMITS quotas;
                NTSTATUS     subStatus;

                RtlInitString(&origin, "LogonOrigin");
                memcpy(tokenSource.SourceName, "SmartCrd", TOKEN_SOURCE_LENGTH);
                AllocateLocallyUniqueId(&tokenSource.SourceIdentifier);

                status = LsaLogonUser(
                    hLsa, &origin, Interactive, authPackage,
                    pBuf, cbTotal, NULL, &tokenSource,
                    &pProfile, &cbProfile, &logonId, phToken,
                    &quotas, &subStatus);

                if (status >= 0 && pProfile != NULL)
                    LsaFreeReturnBuffer(pProfile);
                else if (subStatus < 0)
                    status = subStatus;
            }
            LsaDeregisterLogonProcess(hLsa);
        }
        LocalFree(pBuf);
    }

    LocalFree(pCspInfo);
    return status;
}
```


## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**KERB\_CERTIFICATE\_LOGON**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-kerb_certificate_logon)
</dt> </dl>
