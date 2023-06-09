---
description: Specifies metadata about the process.
title: PROCESS_TELEMETRY_ID_INFORMATION_TYPE structure
ms.topic: reference
ms.date: 06/08/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PROCESS_TELEMETRY_ID_INFORMATION_TYPE
api_type: 
- HeaderDef
api_location: 
- None
---

# PROCESS_TELEMETRY_ID_INFORMATION_TYPE structure

Specifies metadata about the process.

## Syntax

```C++
typedef struct _PROCESS_TELEMETRY_ID_INFORMATION {
    ULONG HeaderSize;
    ULONG ProcessId;
    ULONG64 ProcessStartKey;
    ULONG64 CreateTime;
    ULONG64 CreateInterruptTime;
    ULONG64 CreateUnbiasedInterruptTime;
    ULONG64 ProcessSequenceNumber;
    ULONG64 SessionCreateTime;
    ULONG SessionId;
    ULONG BootId;
    ULONG ImageChecksum;
    ULONG ImageTimeDateStamp;
    ULONG UserSidOffset;
    ULONG ImagePathOffset;
    ULONG PackageNameOffset;
    ULONG RelativeAppNameOffset;
    ULONG CommandLineOffset;
} PROCESS_TELEMETRY_ID_INFORMATION, *PPROCESS_TELEMETRY_ID_INFORMATION;
```

## Members

<dt>

**HeaderSize**

</dt> 

<dd>

The size, in bytes, of the resource header data that follows.

</dd> 

<dt>

**ProcessId**

</dt> 

<dd>

The ID of the process.

</dd> 

<dt>

**ProcessStartKey**

</dt> 

<dd>

The time the process was created.

</dd> 

<dt>

**CreateInterruptTime**

</dt> 

<dd>

Current interrupt-time count.

</dd> 

<dt>

**CreateUnbiasedInterruptTime**

</dt> 

<dd>

current unbiased interrupt-time count.

</dd> 

<dt>

**ProcessSequenceNumber**

</dt> 

<dd>

The process sequence number.

</dd> 

<dt>

**SessionCreateTime**

</dt> 

<dd>

Date and time the session was created.

</dd> 

<dt>

**SessionId**

</dt> 

<dd>

The session associated with client connection.

</dd> 

<dt>

**BootId**

</dt> 

<dd>

The boot ID.

</dd> 

<dt>

**ImageChecksum**

</dt> 

<dd>

The image file checksum.

</dd> 

<dt>

**ImageTimeDateStamp**

</dt> 

<dd>

The image file time stamp.

</dd> 

<dt>

**UserSidOffset**

</dt> 

<dd>

The User Sid offset.

</dd> 

<dt>

**ImagePathOffset**

</dt> 

<dd>

The name and path of the image offset.

</dd> 

<dt>

**PackageNameOffset**

</dt> 

<dd>

The package name offset.

</dd> 

<dt>

**RelativeAppNameOffset**

</dt> 

<dd>

The relative app name offset.

</dd> 

<dt>

**CommandLineOffset**

</dt> 

<dd>

The process command line offset.

</dd> 

</dl>

## Remarks

This struct has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from the DiagnosticDatasettings.dll.

## Requirements

| Requirement | Value |
|-----------------------------------|---------------------------------|
| Minimum supported client          | Windows 10                      |
| DLL                               | DiagnosticDatasettings.dll      |
