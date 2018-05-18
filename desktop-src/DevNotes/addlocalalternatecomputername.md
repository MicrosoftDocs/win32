---
Description: 'Adds an alternate local network name for the computer from which it is called.'
ms.assetid: 'e4d8355b-0492-4b6f-988f-3887e63a2bba'
title: AddLocalAlternateComputerName function
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

The alternate name to be added. The name must be in the **ComputerNameDnsFullyQualified** format as defined in the [**COMPUTER\_NAME\_FORMAT**](base.computer_name_format_str) enumeration, and the [**DnsValidateName\_W**](dns.dnsvalidatename) function must be able to validate it with its format set to **DnsNameHostnameFull**.

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



|                                   |                                                                                                       |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| Library<br/>                | <dl> <dt>Kernel32.lib</dt> </dl>               |
| DLL<br/>                    | <dl> <dt>Kernel32.dll</dt> </dl>               |
| Unicode and ANSI names<br/> | **AddLocalAlternateComputerNameW** (Unicode) and **AddLocalAlternateComputerNameA** (ANSI)<br/> |



## See also

<dl> <dt>

[**COMPUTER\_NAME\_FORMAT**](base.computer_name_format_str)
</dt> <dt>

[**DnsValidateName\_W**](dns.dnsvalidatename)
</dt> </dl>

 

 




