---
title: SetSecurityLayer method of the Win32_TSGeneralSetting class
description: The SetSecurityLayer method sets the security layer.
ms.assetid: 3b894494-2180-4f1d-8e67-a66c679d286c
ms.tgt_platform: multiple
keywords:
- SetSecurityLayer method Remote Desktop Services
- SetSecurityLayer method Remote Desktop Services , Win32_TSGeneralSetting class
- Win32_TSGeneralSetting class Remote Desktop Services , SetSecurityLayer method
topic_type:
- apiref
api_name:
- Win32_TSGeneralSetting.SetSecurityLayer
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetSecurityLayer method of the Win32\_TSGeneralSetting class

The **SetSecurityLayer** method sets the security layer.

## Syntax


```mof
uint32 SetSecurityLayer(
  [in] uint32 SecurityLayer
);
```



## Parameters

<dl> <dt>

*SecurityLayer* \[in\]
</dt> <dd>

The security layer to set. If the current Encryption Level is 1, then a value of 2 for *SecurityLayer* is not valid.

<dt>

<span id="RDP_Security_Layer"></span><span id="rdp_security_layer"></span><span id="RDP_SECURITY_LAYER"></span>

<span id="RDP_Security_Layer"></span><span id="rdp_security_layer"></span><span id="RDP_SECURITY_LAYER"></span>**RDP Security Layer** (0)


</dt> <dd>

Communication between the server and the client will use native RDP encryption.

</dd> <dt>

<span id="Negotiate"></span><span id="negotiate"></span><span id="NEGOTIATE"></span>

<span id="Negotiate"></span><span id="negotiate"></span><span id="NEGOTIATE"></span>**Negotiate** (1)


</dt> <dd>

The most secure layer that is supported by the client will be used. If supported, SSL (TLS 1.0) will be used.

</dd> <dt>

<span id="SSL"></span><span id="ssl"></span>

<span id="SSL"></span><span id="ssl"></span>**SSL** (2)


</dt> <dd>

SSL (TLS 1.0) will be used for server authentication as well as for encrypting all data transferred between the server and the client. This setting requires the server to have an SSL compatible certificate. This setting is not compatible with a **MinEncryptionLevel** value of 1.

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
</dt> <dt>

[**SetEncryptionLevel**](win32-tsgeneralsetting-setencryptionlevel.md)
</dt> </dl>

 

