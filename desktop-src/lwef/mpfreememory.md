---
title: MpFreeMemory function (MpClient.h)
description: Frees memory for the malware protection manager.
ms.assetid: D0B43AE5-756F-4E86-B8A5-8268A41901BC
keywords:
- MpFreeMemory function Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MpFreeMemory
api_location:
- MpClient.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MpFreeMemory function

Frees memory for the malware protection manager. All buffers allocated and returned by malware protection functions must be freed by the caller using this function.

## Syntax


```C++
void WINAPI MpFreeMemory(
  _In_ PVOID pMemory
);
```



## Parameters

<dl> <dt>

*pMemory* \[in\]
</dt> <dd>

Type: **PVOID**

A pointer to memory allocated by a malware protection function.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

To facilitate memory management for clients, the malware protection manager also defines macros to free memory associated with various structures returned by malware protection functions. The following macros are defined in the header file mpmemfree.h:



| Name                            | Description                                                                      |
|---------------------------------|----------------------------------------------------------------------------------|
| MPRESOURCE\_INFO\_FREE          | Frees an allocated [**MPRESOURCE\_INFO**](mpresource-info.md).                  |
| MPTHREAT\_INFO\_FREE            | Frees an allocated [**MPTHREAT\_INFO**](mpthreat-info.md).                      |
| MPTHREAT\_LOCALIZED\_INFO\_FREE | Frees an allocated [**MPTHREAT\_LOCALIZED\_INFO**](mpthreat-localized-info.md). |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MpClient.dll</dt> </dl> |



## See also

<dl> <dt>

[**MpErrorMessageFormat**](mperrormessageformat.md)
</dt> <dt>

[**MPRESOURCE\_INFO**](mpresource-info.md)
</dt> <dt>

[**MPTHREAT\_INFO**](mpthreat-info.md)
</dt> <dt>

[**MPTHREAT\_LOCALIZED\_INFO**](mpthreat-localized-info.md)
</dt> </dl>

 

 





