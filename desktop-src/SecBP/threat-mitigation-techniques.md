---
description: There are a number of threat-mitigation techniques available that you can use to better secure passwords.
ms.assetid: b2442579-e559-4053-869f-9d96e4db202e
title: Threat Mitigation Techniques
ms.topic: article
ms.date: 05/31/2018
---

# Threat Mitigation Techniques

There are a number of threat-mitigation techniques available that you can use to better secure passwords. These techniques are implemented by using one or more of the following four, primary technologies.



| Technology                      | Description                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CryptoAPI                       | CryptoAPI provides a set of functions that help you apply cryptographic routines to target entities. CryptoAPI can provide hashes, digests, encryption, and decryption, to mention its primary functionality. CryptoAPI also has other features. To learn about cryptography and the CryptoAPI, see [Cryptography Essentials](/windows/desktop/SecCrypto/cryptography-essentials).           |
| Access control lists            | An [*access control list*](/windows/desktop/SecGloss/a-gly) (ACL) is a list of security protections that applies to an object. An object can be a file, process, event, or anything else that has a security descriptor. For more information on ACLs see [Access Control Lists](/windows/desktop/SecAuthZ/access-control-lists) (ACLs). |
| Data protection API             | The data protection API (DPAPI) provides the following four functions that you use to encrypt and decrypt sensitive data: [**CryptProtectData**](/windows/desktop/api/dpapi/nf-dpapi-cryptprotectdata), [**CryptUnprotectData**](/windows/desktop/api/dpapi/nf-dpapi-cryptunprotectdata), [**CryptProtectMemory**](/windows/desktop/api/dpapi/nf-dpapi-cryptprotectmemory), and [**CryptUnprotectMemory**](/windows/desktop/api/dpapi/nf-dpapi-cryptunprotectmemory).                  |
| Stored user names and passwords | Storage functionality that makes handling users' passwords and other credentials, such as private keys, easier, more consistent, and safer. For more information on this functionality, see [**CredUIPromptForCredentials**](/windows/desktop/api/wincred/nf-wincred-creduipromptforcredentialsa).                                                                                                         |



 

These technologies are not available on all operating systems. Therefore, the extent to which security can be improved depends on which operating systems are involved. Here are the technologies that are available in each operating system.


| Operating system | Technology | 
|------------------|------------|
| Windows Server 2003 and Windows XP | <ul><li>CryptoAPI</li><li>Access control lists</li><li>Data protection API</li><li>Stored user names and passwords</li></ul> | 
| Windows 2000 | <ul><li>CryptoAPI</li><li>Access control lists</li><li><a href="/windows/desktop/api/dpapi/nf-dpapi-cryptprotectdata"><strong>CryptProtectData</strong></a></li><li><a href="/windows/desktop/api/dpapi/nf-dpapi-cryptunprotectdata"><strong>CryptUnprotectData</strong></a></li></ul> | 




 

The following threat-mitigation techniques use one or more of the four technologies. Techniques that require the use of technologies that are not included in the operating system cannot be used.

## Getting Passwords from the User

When you allow the user to set up a password, force the use of strong passwords. For example, require that passwords be a minimum length such as eight characters or more. Passwords should also be required to include uppercase and lowercase letters, numbers, and other keyboard characters such as the dollar sign ($), exclamation point (!), or greater than (>).

After you get a password, use it quickly (using as little code as possible), and then erase all vestiges of the password. This minimizes the time available to an intruder to "trap" the password. The trade-off with this technique is the frequency with which the password must be retrieved from the user; however, the principle should be employed wherever possible. For information about how to properly get passwords, see [Asking the User for Credentials](asking-the-user-for-credentials.md).

Avoid providing "remember my password" user interface options. Often, users will demand to have this option. If you must provide it, then at minimum, ensure that the password gets saved in a secure fashion. For information, see the Storing Passwords section, later in this topic.

Limit password entry tries. After a certain number of tries without success, lock out the user for a certain length of time. Optionally, lengthen the response time for each try over a maximum. This technique is aimed at defeating a guessing attack.

## Storing Passwords

Never store passwords in plaintext (unencrypted). Encrypting passwords significantly increases their security. For information about storing encrypted passwords, see [**CryptProtectData**](/windows/desktop/api/dpapi/nf-dpapi-cryptprotectdata). For information about encrypting passwords in memory, see [**CryptProtectMemory**](/windows/desktop/api/dpapi/nf-dpapi-cryptprotectmemory). Store passwords in as few places as possible. The more places a password is stored, the greater the chance that an intruder might find it. Never store passwords in a webpage or in a web-based file. Storing passwords in a webpage or in a web-based file allows them to be easily compromised.

After you have encrypted a password and stored it, use secure ACLs to limit access to the file. Alternatively, you can store passwords and encryption keys on removable devices. Storing passwords and encryption keys on a removable media, such as a smart card, helps create a more secure system. After a password is retrieved for a given session, the card can be removed, thereby removing the possibility that an intruder can gain access to it.

 

 
