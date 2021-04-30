---
description: Adds an alternate local network name for the computer from which it is called.
ms.assetid: e4d8355b-0492-4b6f-988f-3887e63a2bba
title: AddLocalAlternateComputerName function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AddLocalAlternateComputerName
- AddLocalAlternateComputerNameA
- AddLocalAlternateComputerNameW
api_type: 
- DllExport
api_location: 
- Kernel32.dll
- API-MS-Win-Core-Kernel32-Legacy-l1-1-0.dll
- kernel32legacy.dll
- API-MS-Win-Core-Kernel32-Legacy-l1-1-1.dll
- API-MS-Win-Core-Kernel32-Legacy-l1-1-2.dll
- API-MS-Win-Core-Kernel32-Legacy-L1-1-3.dll
- API-Ms-Win-Core-Kernel32-Legacy-Ansi-L1-1-0.dll
- API-MS-Win-Core-Kernel32-Legacy-L1-1-4.dll
- API-MS-Win-Core-Kernel32-Legacy-L1-1-5.dll
---

# AddLocalAlternateComputerName function

Adds an alternate local network name for the computer from which it is called.

## Syntax


```C++
DWORD AddLocalAlternateComputerName(
  _In_ LPCTSTR lpDnsFQHostname,
  _In_ ULONG   ulFlags
);
```



## Parameters

<dl> <dt>

*lpDnsFQHostname* \[in\]
</dt> <dd>

The alternate name to be added. The name must be in the **ComputerNameDnsFullyQualified** format as defined in the [**COMPUTER\_NAME\_FORMAT**](/windows/win32/api/sysinfoapi/ne-sysinfoapi-computer_name_format) enumeration, and the [**DnsValidateName\_W**](/windows/win32/api/windns/nf-windns-dnsvalidatename) function must be able to validate it with its format set to **DnsNameHostnameFull**.

</dd> <dt>

*ulFlags* \[in\]
</dt> <dd>

This parameter is reserved and must be set to zero.

</dd> </dl>

## Return value

If the function succeeds, the function returns **ERROR\_SUCCESS**. If the function fails, it returns a nonzero error code. Among the error codes that it returns are the following:



| Return code                                                                                               | Description                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl>  | Indicates that the *lpDnsFQHostname* parameter does not point to a valid DNS name, or that the *ulFlags* parameter is not equal to zero.<br/> |
| <dl> <dt>**ERROR\_NOT\_ENOUGH\_MEMORY**</dt> </dl> | There is not enough memory to complete the operation.<br/>                                                                                    |



 

## Requirements



| Requirement | Value |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| Library<br/>                | <dl> <dt>Kernel32.lib</dt> </dl>               |
| DLL<br/>                    | <dl> <dt>Kernel32.dll</dt> </dl>               |
| Unicode and ANSI names<br/> | **AddLocalAlternateComputerNameW** (Unicode) and **AddLocalAlternateComputerNameA** (ANSI)<br/> |



## See also

<dl> <dt>

[**COMPUTER\_NAME\_FORMAT**](/windows/win32/api/sysinfoapi/ne-sysinfoapi-computer_name_format)
</dt> <dt>

[**DnsValidateName\_W**](/windows/win32/api/windns/nf-windns-dnsvalidatename)
</dt> </dl>

 

 
