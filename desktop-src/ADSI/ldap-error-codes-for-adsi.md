---
title: LDAP Error Codes for ADSI
description: When an LDAP server generates an error and passes the error to the client, the error is then translated into a string by the LDAP client.
ms.assetid: 7a0a5a1b-8473-405b-a590-3f917e50cbdc
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# LDAP Error Codes for ADSI

When an LDAP server generates an error and passes the error to the client, the error is then translated into a string by the LDAP client.

This method is similar to [Win32 error codes for ADSI](win32-error-codes-for-adsi.md). In this example, the client error code is the WIN32 error 0x80072020.

**To Determine the LDAP error codes for ADSI**

1.  Drop the 8007 from the WIN32 error code. In the example, the remaining hex value is 2020.
2.  Convert the remaining hex value to a decimal value. In the example, the remaining hex value 2020 converts to the decimal value 8224.
3.  Search in the WinError.h file for the definition of the decimal value. In the example, 8224L corresponds to the error **ERROR\_DS\_OPERATIONS\_ERROR**.
4.  Replace the prefix **ERROR\_DS** with **LDAP\_**. In the example, the new definition is **LDAP\_OPERATIONS\_ERROR**.
5.  Search in the Winldap.h file for the value of the LDAP error definition. In the example, the value of **LDAP\_OPERATIONS\_ERROR** in the Winldap.h file is 0x01.

 

 




