---
description: Sets or retrieves an enumeration value that specifies the CAPICOM name of the EKU. This is the default property.
ms.assetid: afce5553-ef18-4a7f-b1c8-fbe00d3277e0
title: IEKU::Name property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- IEKU.Name
- IEKU.get_Name
- IEKU.put_Name
- EKU.Name
api_type:
- COM
api_location:
- Capicom.dll
---

# IEKU::Name property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509EnhancedKeyUsageExtension Class**](/dotnet/api/system.security.cryptography.x509certificates.x509enhancedkeyusageextension?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace.\]

The **Name** property sets or retrieves an enumeration value that specifies the CAPICOM name of the EKU. This is the default property.

This property is read/write.

## Syntax


```VB
EKU.Name As CAPICOM_EKU
```



## Property value

A value of the [**CAPICOM\_EKU**](capicom-eku.md) enumeration that specifies the CAPICOM name of the EKU. The following table shows the possible values.



| Value                                                                                                                                                                                                                           | Meaning                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CAPICOM_EKU_OTHER"></span><span id="capicom_eku_other"></span><dl> <dt>**CAPICOM\_EKU\_OTHER**</dt> </dl>                                                      | Certificate has uses defined in local policy. This is used if the EKU needed is not predefined and the OID value must be set by the application.<br/> |
| <span id="CAPICOM_EKU_SERVER_AUTH"></span><span id="capicom_eku_server_auth"></span><dl> <dt>**CAPICOM\_EKU\_SERVER\_AUTH**</dt> </dl>                                   | Certificate can be used to authenticate a server.<br/>                                                                                                |
| <span id="CAPICOM_EKU_CLIENT_AUTH"></span><span id="capicom_eku_client_auth"></span><dl> <dt>**CAPICOM\_EKU\_CLIENT\_AUTH**</dt> </dl>                                   | Certificate can be used to authenticate a client.<br/>                                                                                                |
| <span id="CAPICOM_EKU_CODE_SIGNING"></span><span id="capicom_eku_code_signing"></span><dl> <dt>**CAPICOM\_EKU\_CODE\_SIGNING**</dt> </dl>                                | Certificate can be used to create a digital signature.<br/>                                                                                           |
| <span id="CAPICOM_EKU_EMAIL_PROTECTION"></span><span id="capicom_eku_email_protection"></span><dl> <dt>**CAPICOM\_EKU\_EMAIL\_PROTECTION**</dt> </dl>                    | Certificate can be used for email protection.<br/>                                                                                                    |
| <span id="CAPICOM_EKU_SMARTCARD_LOGON"></span><span id="capicom_eku_smartcard_logon"></span><dl> <dt>**CAPICOM\_EKU\_SMARTCARD\_LOGON**</dt> </dl>                       | Certificate can be used for smart card logon. Introduced in CAPICOM 2.0.<br/>                                                                         |
| <span id="CAPICOM_EKU_ENCRYPTING_FILE_SYSTEM"></span><span id="capicom_eku_encrypting_file_system"></span><dl> <dt>**CAPICOM\_EKU\_ENCRYPTING\_FILE\_SYSTEM**</dt> </dl> | Certificate can be used for EFS. Introduced in CAPICOM 2.0.<br/>                                                                                      |



 

## Remarks

When the value of this property is reset, directly or indirectly, the whole [*state*](../secgloss/s-gly.md) of the object is reset.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
