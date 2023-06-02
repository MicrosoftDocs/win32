---
description: The Active Directory database contains a set of objects known as DPAPI backup keys.
ms.assetid: 08bc55c8-e2cd-4af0-bf26-f4071fe2335c
title: DPAPI backup keys on Active Directory domain controllers
ms.topic: article
ms.date: 06/02/2023
---

# DPAPI backup keys on Active Directory domain controllers

The Active Directory database contains a set of objects known as DPAPI backup keys. These objects include:

- BCKUPKEY_P Secret
- BCKUPKEY_PREFERRED Secret
- BCKUPKEY_guid1
- BCKUPKEY_guid2

These objects are part of the schema class "secret", and they exist in the "CN=System,DC=contoso,DC=com" container within the Domain partition.

Normally, domain users encrypt DPAPI-protected data using keys that are derived from their own passwords. However, if the user forgets their password, or if their password is administratively reset or reset from another device, the previously encrypted data can no longer be decrypted using the new keys derived from the user's new password.

When this occurs, the data can still be decrypted using the Backup keys stored on the Active Directory domain controllers. They can then be re-encrypted with the user's new password-derived key. This means that anyone who has the DPAPI Backup keys for a domain will be able to decrypt DPAPI-encrypted data for any domain user, even after the user's password is changed.

The DPAPI Backup keys on Active Directory domain controllers are randomly generated only once, during the initial creation of the domain.

Due to the sensitive nature of these keys, it is imperative that access to these keys be protected and regarded as one of the most highly confidential pieces of information in the entire Active Directory domain. By default, access to these keys is restricted to domain administrators.

There currently is no officially supported way of changing or rotating these DPAPI backup keys on the domain controllers. In accordance with the document [MS-BKRP](/openspecs/windows_protocols/ms-bkrp/90b08be4-5175-4177-b4ce-d920d797e3a8), 3rd parties have the ability to develop an application or script that creates a new DPAPI Backup key and sets the new key to be the preferred key for the domain. However, these 3rd party solutions would be unsupported by Microsoft.

Should the DPAPI Backup keys for the domain be compromised, the recommendation is to create a new domain and migrate users to that new domain. If a malicious actor is able to gain access to the DPAPI backup keys, it's likely that they have acquired domain administrator-level access to the domain and have full access to its resources. An attacker may also install other backdoor systems in the domain with the level of access that they now have, hence the recommendation to migrate to a new domain.

Active Directory administration best practices are the defense against this scenario. When granting domain access to users, provide the minimum level of access users need. It's also critical to protect Active Directory backups with as much vigilance as you protect the domain controllers themselves.

## See also

[CNG DPAPI](cng-dpapi.md)

[MS-BKRP: BackupKey Remote Protocol document](/openspecs/windows_protocols/ms-bkrp/90b08be4-5175-4177-b4ce-d920d797e3a8)
