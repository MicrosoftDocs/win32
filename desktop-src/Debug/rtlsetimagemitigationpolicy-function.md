---
title: RtlSetImageMitigationPolicy
description: Sets the specified mitigation policy for specified image.
ms.keywords: RtlSetImageMitigationPolicy
topic_type:
- apiref
api_name:
- RtlSetImageMitigationPolicy
api_location:
- ntdll.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 01/20/2023
---

# RtlSetImageMitigationPolicy

Sets the specified mitigation policy for specified image.


```C++
NTSYSAPI NTSTATUS NTAPI RtlSetImageMitigationPolicy(
    _In_opt_ PCWSTR ImagePathName,
    _In_ IMAGE_MITIGATION_POLICY MitigationPolicy,
    _In_ ULONG Flags,
    _In_reads_bytes_opt_(BufferSize) PVOID Buffer,
    _In_ ULONG BufferSize
    )
```

## Parameters

### ImagePathName

The name of the image whose mitigation policy is set. If *ImagePathName* is NULL, the system mitigation policy is being set.

### MitigationPolicy

The mitigation policy that is to be set. This parameter supports the following enumeration values:

| Field name | Value | Description |
|------------|-------|-------------|
| ImageUserShadowStackPolicy | 15 |  |

### Flags

Flags that control the behavior of the set operation. Supported flags for this parameter include:

| Flag | Value | Description |
|------|-------|-------------|
| MITIGATION_POLICY_FLAG_RESET_VALUE | 0x0 |  |
| MITIGATION_POLICY_FLAG_USE_AUDIT_POLICY | 0x8 |  |

### Buffer

A pointer to the buffer that holds the policy data.

### BufferSize

The length in bytes of the buffer provided in *Buffer*.


## Return value

Returns an  NTSTATUS success or error code. 

## Remarks

This API is not defined in a Windows SDK header file and must be manually declared. The API is exported from ntdll.dll.

## Requirements

## See also
