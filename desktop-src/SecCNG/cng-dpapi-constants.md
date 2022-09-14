---
description: The following constants are used by the CNG Data Protection API.
ms.assetid: 4E43FAA9-7D6F-43DB-A998-189411E0AB4C
title: CNG DPAPI Constants (NCryptprotect.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CNG DPAPI Constants

The following constants are used by the CNG Data Protection API.

<dl> <dt>

<span id="NCRYPT_DESCR_DELIMITER_AND"></span><span id="ncrypt_descr_delimiter_and"></span>**NCRYPT\_DESCR\_DELIMITER\_AND**
</dt> <dd> <dl> <dt>

L" AND "
</dt> <dt>



Can be used to test a protection descriptor string for an AND delimiter.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_DESCR_EQUAL"></span><span id="ncrypt_descr_equal"></span>**NCRYPT\_DESCR\_EQUAL**
</dt> <dd> <dl> <dt>

L"="
</dt> <dt>



Can be used to test a protection descriptor string for an equals sign.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_DESCR_DELIMITER_OR"></span><span id="ncrypt_descr_delimiter_or"></span>**NCRYPT\_DESCR\_DELIMITER\_OR**
</dt> <dd> <dl> <dt>

L" OR "
</dt> <dt>



Can be used to test a protection descriptor string for an OR delimiter.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_KEY_PROTECTION_ALGORITHM_LOCAL"></span><span id="ncrypt_key_protection_algorithm_local"></span>**NCRYPT\_KEY\_PROTECTION\_ALGORITHM\_LOCAL**
</dt> <dd> <dl> <dt>

"LOCAL"
</dt> <dt>



The LOCAL protection descriptor protects content to the logon session, the current user, or the local machine as identified by the following constants:

-   **NCRYPT\_KEY\_PROTECTION\_LOCAL\_LOGON**
-   **NCRYPT\_KEY\_PROTECTION\_LOCAL\_USER**
-   **NCRYPT\_KEY\_PROTECTION\_LOCAL\_MACHINE**


</dt> </dl> </dd> <dt>

<span id="NCRYPT_KEY_PROTECTION_ALGORITHM_SDDL"></span><span id="ncrypt_key_protection_algorithm_sddl"></span>**NCRYPT\_KEY\_PROTECTION\_ALGORITHM\_SDDL**
</dt> <dd> <dl> <dt>

"SDDL"
</dt> <dt>



Protects content to an SDDL (Security Descriptor Definition Language) string that contains security descriptor information.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_KEY_PROTECTION_ALGORITHM_SID"></span><span id="ncrypt_key_protection_algorithm_sid"></span>**NCRYPT\_KEY\_PROTECTION\_ALGORITHM\_SID**
</dt> <dd> <dl> <dt>

"SID"
</dt> <dt>



The SID protection descriptor contains a group or principal identity.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_KEY_PROTECTION_ALGORITHM_WEBCREDENTIALS"></span><span id="ncrypt_key_protection_algorithm_webcredentials"></span>**NCRYPT\_KEY\_PROTECTION\_ALGORITHM\_WEBCREDENTIALS**
</dt> <dd> <dl> <dt>

"WEBCREDENTIALS"
</dt> <dt>



Protects to a user's web account credentials.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_KEY_PROTECTION_LOCAL_LOGON"></span><span id="ncrypt_key_protection_local_logon"></span>**NCRYPT\_KEY\_PROTECTION\_LOCAL\_LOGON**
</dt> <dd> <dl> <dt>

"logon"
</dt> <dt>



Protects content to the current logon session. Users will not be able to decrypt the protected content after logoff or reboot.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_KEY_PROTECTION_LOCAL_MACHINE"></span><span id="ncrypt_key_protection_local_machine"></span>**NCRYPT\_KEY\_PROTECTION\_LOCAL\_MACHINE**
</dt> <dd> <dl> <dt>

"machine"
</dt> <dt>



Protects content to the local computer. All users on the local computer can decrypt the protected content.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_KEY_PROTECTION_LOCAL_USER"></span><span id="ncrypt_key_protection_local_user"></span>**NCRYPT\_KEY\_PROTECTION\_LOCAL\_USER**
</dt> <dd> <dl> <dt>

"user"
</dt> <dt>



Protects content to the current user session. Only this user on the local computer will be able to decrypt the protected content.


</dt> </dl> </dd> <dt>

<span id="MS_KEY_PROTECTION_PROVIDER"></span><span id="ms_key_protection_provider"></span>**MS\_KEY\_PROTECTION\_PROVIDER**
</dt> <dd> <dl> <dt>

"Microsoft Key Protection Provider"
</dt> <dt>



Represents the Microsoft key protection provider which supports formats represented by the following constants:

-   **NCRYPT\_KEY\_PROTECTION\_ALGORITHM\_SID**
-   **NCRYPT\_KEY\_PROTECTION\_ALGORITHM\_LOCAL**
-   **NCRYPT\_KEY\_PROTECTION\_ALGORITHM\_SDDL**


</dt> </dl> </dd> <dt>

<span id="WINDOWS_CLIENT_KEY_PROTECTION_PROVIDER"></span><span id="windows_client_key_protection_provider"></span>**WINDOWS\_CLIENT\_KEY\_PROTECTION\_PROVIDER**
</dt> <dd> <dl> <dt>

"Windows Client Key Protection Provider"
</dt> <dt>



Represents the Microsoft key protection provider that is available only on the client and which supports formats represented by the following constants:

-   **NCRYPT\_KEY\_PROTECTION\_ALGORITHM\_WEBCREDENTIALS**


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>NCryptprotect.h</dt> </dl> |



 

 




