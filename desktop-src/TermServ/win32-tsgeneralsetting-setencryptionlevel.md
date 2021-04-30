---
title: SetEncryptionLevel method of the Win32_TSGeneralSetting class
description: The SetEncryptionLevel method sets the encryption level.
ms.assetid: 1822c4dc-bce6-489f-b21e-f96faffd2fa5
ms.tgt_platform: multiple
keywords:
- SetEncryptionLevel method Remote Desktop Services
- SetEncryptionLevel method Remote Desktop Services , Win32_TSGeneralSetting class
- Win32_TSGeneralSetting class Remote Desktop Services , SetEncryptionLevel method
topic_type:
- apiref
api_name:
- Win32_TSGeneralSetting.SetEncryptionLevel
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetEncryptionLevel method of the Win32\_TSGeneralSetting class

The **SetEncryptionLevel** method sets the encryption level.

## Syntax


```mof
uint32 SetEncryptionLevel(
  [in] uint32 MinEncryptionLevel
);
```



## Parameters

<dl> <dt>

*MinEncryptionLevel* \[in\]
</dt> <dd>

The minimum encryption level to set.

<dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Low level of encryption. Only data sent from the client to the server is encrypted using 56-bit encryption. Note that data sent from the server to the client is not encrypted.

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

Client-compatible level of encryption. All data sent from client to server and from server to client is encrypted at the maximum key strength supported by the client.

</dd> <dt>

<span id="3"></span>

<span id="3"></span>**3**


</dt> <dd>

High level of encryption. All data sent from client to server and from server to client is encrypted using strong 128-bit encryption. Clients that do not support this level of encryption cannot connect.

</dd> <dt>

<span id="4"></span>

<span id="4"></span>**4**


</dt> <dd>

FIPS-compliant encryption. All data sent from client to server and from server to client is encrypted and decrypted with the Federal Information Processing Standard (FIPS) encryption algorithms using the Microsoft cryptographic modules. FIPS is a standard entitled "Security Requirements for Cryptographic Modules". FIPS 140-1 (1994) and FIPS 140-2 (2001) describe government requirements for hardware and software cryptographic modules used within the U.S. government.

</dd> </dl> </dd> </dl>

## Return value

Returns Success on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSGeneralSetting**](win32-tsgeneralsetting.md)
</dt> </dl>

 

