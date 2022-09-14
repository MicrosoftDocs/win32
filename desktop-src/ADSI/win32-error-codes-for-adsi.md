---
title: Win32 Error Codes for ADSI
description: Standard Win32 error codes are also used to return ADSI error messages.
ms.assetid: 5b7b85c9-ccca-4ea3-8b37-54f6b30a509f
ms.tgt_platform: multiple
keywords:
- Win32 Error Codes for ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Win32 Error Codes for ADSI

Standard Win32 error codes are also used to return ADSI error messages. Specifically, the ADSI LDAP provider maps all the LDAP error codes to Win32 error codes. The **HRESULT** values of these error codes are of the 0x8007XXXX format, where the last four hexadecimal digits, XXXX, corresponds to the **DWORD** values of the appropriate Win32 error code. For example, the ADSI error value 0x80072020 gives the Win32 error value of 0x2020 in hexadecimal or 8224 in decimal.

To convert the **HRESULT** value of an ADSI error code, returned by your application, to the corresponding the Win32 error **DWORD** value, as defined in the header files above, use the following procedure.

Most of the Win32 error codes for ADSI are defined in Winerror.h or Lmerr.h. The error values are listed as decimal values in these files.

**To convert the **HRESULT** value of an ADSI error code to the corresponding the Win32 error **DWORD** value**

1.  Convert the **HRESULT** value to a hexadecimal number if starting with a decimal value as you may get from a Visual Basic application.
2.  Drop the 0x8007 part produce the remainder.
3.  Convert the remainder to a decimal number.
4.  Look up the decimal remainder in Winerror.h.
5.  If not found in Winerror.h, subtract 2100 from the decimal remainder and look up the result in Lmerr.h.

ADSI 2.0 maps the LDAP error codes to a set of Win32 error codes that is different from that used in ADSI for Windows 2000 and DS Client. The differences are listed in:

-   [Win32 Error Codes](win32-error-codes.md)
-   [Win32 Error Codes for ADSI 2.0](win32-error-codes-for-adsi-2-0.md)

 

 




