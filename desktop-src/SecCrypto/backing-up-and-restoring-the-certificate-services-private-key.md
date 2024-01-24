---
description: You cannot use the Certadm.dll's backup and restore functions to back up the Certificate Services private keys.
ms.assetid: 27ee8caa-8f5e-46dc-b55d-afde5471507e
title: Backing Up and Restoring the Certificate Services Private Key
ms.topic: article
ms.date: 05/31/2018
---

# Backing Up and Restoring the Certificate Services Private Key

You cannot use the Certadm.dll's backup and restore functions to back up the Certificate Services [*private keys*](../secgloss/p-gly.md). Private keys cannot be backed up by these functions because these functions are intended to backup and restore the Certificate Services database (and related files), and this database does not contain any private keys (even for self-issued certificates).

To back up a Certificate Services private key, use the Certification Authority MMC snap-in, or the certutil command (with -backup or -backupkey specified). Backing up the private key with the Certification Authority MMC snap-in or certutil results in the private key being written to PKCS \#12 file. Even though this PKCS \#12 file is password-protected, it should be considered extremely sensitive and must be stored securely; the password to the PKCS \#12 file should also be guarded from unauthorized persons.

Similarly, private keys cannot be restored by the Certificate Services backup and restore functions. A Certificate Services backup key contained in a PKCS \#12 file can be restored by the Certification Authority MMC snap-in, or by the certutil command (specifying the -restore or -restorekey verbs); note that the person performing the restore operation will need to know the password for the PKCS \#12 file.

There are only two cases in which a Certificate Services private key must be backed up. The first case is after the installation of Certificate Services. The second case is after any renewal operation of the Certificate Services certificate.

 

 
