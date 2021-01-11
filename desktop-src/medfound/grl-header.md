---
description: Contains the global revocation list (GRL) header.
ms.assetid: 806ae550-5106-47ec-8466-f967598d3e61
title: GRL_HEADER structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GRL_HEADER
api_type: 
- NA
api_location: 
---

# GRL\_HEADER structure

Contains the global revocation list (GRL) header.

## Syntax


```C++
typedef struct _GRL_HEADER {
  WCHAR    wszIdentifier[6];
  WORD     wFormatMajor;
  WORD     wFormatMinor;
  FILETIME CreationTime;
  DWORD    dwSequenceNumber;
  DWORD    dwForceRebootVersion;
  DWORD    dwForceProcessRestartVersion;
  DWORD    cbRevocationSectionOffset;
  DWORD    cRevokedKernelBinaries;
  DWORD    cRevokedUserBinaries;
  DWORD    cRevokedCertificates;
  DWORD    cTrustedRoots;
  DWORD    cbExtensibleSectionOffset;
  DWORD    cExtensibleEntries;
  DWORD    cbRenewalSectionOffset;
  DWORD    cRevokedKernelBinaryRenewals;
  DWORD    cRevokedUserBinaryRenewals;
  DWORD    cRevokedCertificateRenewals;
  DWORD    cbSignatureCoreOffset;
  DWORD    cbSignatureExtOffset;
} GRL_HEADER;
```



## Members

<dl> <dt>

**wszIdentifier**
</dt> <dd>

The GRL identifier. The value is always L"MSGRL".

</dd> <dt>

**wFormatMajor**
</dt> <dd>

The major version number. Currently the value must be 1.

</dd> <dt>

**wFormatMinor**
</dt> <dd>

The minor version number. Currently the value must be zero.

</dd> <dt>

**CreationTime**
</dt> <dd>

A **FILETIME** value that specifies when the file was created.

</dd> <dt>

**dwSequenceNumber**
</dt> <dd>

The GRL version number. Currently the value must be at least 3

</dd> <dt>

**dwForceRebootVersion**
</dt> <dd>

Reserved.

</dd> <dt>

**dwForceProcessRestartVersion**
</dt> <dd>

Reserved.

</dd> <dt>

**cbRevocationSectionOffset**
</dt> <dd>

The offset, in bytes, from the start of the GRL to the Core section.

</dd> <dt>

**cRevokedKernelBinaries**
</dt> <dd>

The number of revoked kernel binaries listed in the GRL.

</dd> <dt>

**cRevokedUserBinaries**
</dt> <dd>

The number of revoked user-mode binaries listed in the GRL.

</dd> <dt>

**cRevokedCertificates**
</dt> <dd>

The number of revoked certificates listed in the GRL.

</dd> <dt>

**cTrustedRoots**
</dt> <dd>

The number of trusted roots listed in the GRL.

</dd> <dt>

**cbExtensibleSectionOffset**
</dt> <dd>

The offset, in bytes, from the start of the GRL to the Extensible section.

</dd> <dt>

**cExtensibleEntries**
</dt> <dd>

The number of entries in the Extensible section.

</dd> <dt>

**cbRenewalSectionOffset**
</dt> <dd>

The offset, in bytes, from the start of the GRL to the Renewals section.

</dd> <dt>

**cRevokedKernelBinaryRenewals**
</dt> <dd>

The number of kernel binary renewals listed in the GRL.

</dd> <dt>

**cRevokedUserBinaryRenewals**
</dt> <dd>

The number of user-mode binary renewals listed in the GRL.

</dd> <dt>

**cRevokedCertificateRenewals**
</dt> <dd>

The number of certificate renewals listed in the GRL.

</dd> <dt>

**cbSignatureCoreOffset**
</dt> <dd>

The offset, in bytes, from the start of the GRL to the Core section signature.

</dd> <dt>

**cbSignatureExtOffset**
</dt> <dd>

The offset, in bytes, from the start of the GRL to the Extensible section signature.

</dd> </dl>

## Remarks

All integers in the GRL have little-endian byte ordering. All structures are aligned to 1-byte boundaries.

This structure is not declared in an SDK header. To use this structure, add the declaration shown here to your source code.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[OPM Certificate Revocation](opm-certificate-revocation.md)
</dt> <dt>

[OPM Structures](opm-structures.md)
</dt> </dl>

 

 




