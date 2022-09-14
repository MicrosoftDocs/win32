---
description: Retrieves the current size, in bytes, of the free virtual address space available to the process.
ms.assetid: 13b3b347-5db1-484f-bd1d-3a604eb6bc5b
ms.tgt_platform: multiple
title: GetAvailableVirtualSize method of the Win32_Process class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Process.GetAvailableVirtualSize
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# GetAvailableVirtualSize method of the Win32\_Process class

Retrieves the current size, in bytes, of the free virtual address space available to the process.

## Syntax


```mof
uint32 GetAvailableVirtualSize(
  [out] uint64 AvailableVirtualSize
);
```



## Parameters

<dl> <dt>

*AvailableVirtualSize* \[out\]
</dt> <dd>

The *AvailableVirtualSize* parameter returns the free virtual address space available to this process.

</dd> </dl>

## Return value

Returns zero (0) to indicate success. Any other number indicates an error. For additional error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**Successful completion**
</dt> <dd>

0

The operation completed successfully.

</dd> <dt>

**Access denied**
</dt> <dd>

2

The user does not have access to the requested information

</dd> <dt>

**Insufficient privilege**
</dt> <dd>

3

The user does not have sufficient privilege.

</dd> <dt>

**Unknown failure**
</dt> <dd>

8

Unknown failure.

</dd> <dt>

**Path not found**
</dt> <dd>

9

The path specified does not exist.

</dd> <dt>

**Invalid parameter**
</dt> <dd>

21

The specified parameter is invalid.

</dd> <dt>

**Other**
</dt> <dd>

22 4294967295

For values other than those listed, refer to the [System Error Codes](/windows/desktop/Debug/system-error-codes) documentation.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Process**](win32-process.md)
</dt> </dl>

 

