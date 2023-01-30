---
description: In the presence of WIP policy, writes an event to the WIP audit log.
title: EdpAuditAction function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EdpAuditAction
api_type: 
- DllExport
api_location: 
- edputil.dll
---

# EdpAuditAction function

> [!NOTE]
> Starting in July 2022, Microsoft is deprecating Windows Information Protection (WIP) and the APIs that support WIP. Microsoft will continue to support WIP on supported versions of Windows. New versions of Windows won't include new capabilities for WIP, and it won't be supported in future versions of Windows. For more information, see [Announcing sunset of Windows Information Protection](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/announcing-the-sunset-of-windows-information-protection-wip/ba-p/3579282).
>
> For your data protection needs, Microsoft recommends that you use [Microsoft Purview Information Protection](/microsoft-365/compliance/information-protection) and [Microsoft Purview Data Loss Prevention](/microsoft-365/compliance/dlp-learn-about-dlp). Purview simplifies the configuration set-up and provides an advanced set of capabilities.


In the presence of WIP policy, writes an event to the WIP audit log.

## Syntax


```C++
HRESULT
EdpAuditAction(
    _In_ PCWSTR ObjectDescription,
    _In_ EDP_AUDIT_ACTION Action,
    _In_opt_ PCWSTR SourceName,
    _In_opt_ PCWSTR SourceEID,
    _In_opt_ PCWSTR DestinationName,
    _In_opt_ PCWSTR DestinationEID,
    _In_opt_ PCWSTR Application
    );

```



## Parameters

### ObjectDescription

Description of data that is being transferred.

### Action

A member of the [EDP_AUDIT_ACTION](edp_audit_action-enum.md) enumeration.

### SourceName

Source of the data (such as application name or email address).

### SourceEID

Enterprise identity of the source data.

### DestinationName

Name of destination (such as application name or email address).

### DestinationEID

Enterprise identity of the destination.

### Application

Unique ID of the application where the transfer took place.


## Return value

An HRESULT value.

## Remarks

This must be called when an application detects data shared from work to personal, for example through copying and pasting.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |
| DLL                      | edputil.dll |



 

 




