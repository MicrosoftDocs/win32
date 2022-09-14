---
description: Active Directory provides the account database that the Key Distribution Center (KDC) uses to obtain information about security principals in the domain.
ms.assetid: 560ef22c-dd4f-49f8-9e15-a45dbf17df01
title: Account Database
ms.topic: article
ms.date: 05/31/2018
---

# Account Database

Active Directory provides the account database that the [*Key Distribution Center*](/windows/desktop/SecGloss/k-gly) (KDC) uses to obtain information about [*security principals*](/windows/desktop/SecGloss/s-gly) in the domain. Each principal is represented by an account object in the directory. The [*encryption*](/windows/desktop/SecGloss/e-gly) key used in communicating with a user, computer, or service is stored as an attribute of the account object of that security principal.

Only domain controllers are Active Directory servers. Each domain controller keeps a writable copy of the directory, so accounts can be created, passwords reset, and group membership modified at any domain controller. Changes made to one replica of the directory are automatically propagated to all other replicas. Windows replicates the information store for the Active Directory using a proprietary multiple-master replication protocol that uses a secure remote procedure call connection between replication partners. The connection uses the [*Kerberos authentication protocol*](/windows/desktop/SecGloss/k-gly) to provide mutual [*authentication*](/windows/desktop/SecGloss/a-gly) and encryption.

Physical storage of account data is managed by the [Directory System Agent](/windows/desktop/AD/directory-system-agent), a protected process integrated with the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) on the domain controller. Clients of the directory service are never given direct access to the data store. Any client that wants access to directory information must connect to the Directory System Agent and then search for, read, and write directory objects and their attributes.

Requests to access an object or attribute in the directory are subject to validation by Windows access control mechanisms. Like file and folder objects in the NTFS file system, objects in the Active Directory are protected by [*access control lists*](/windows/desktop/SecGloss/a-gly) (ACLs) that specify who can access the object and in what way. Unlike files and folders, however, Active Directory objects have an ACL for each of their attributes. Thus attributes for sensitive account information can be protected by more restrictive permissions than those granted for other attributes of the account.

The most sensitive information about an account is of course its password. Although the password attribute of an account object stores an encryption key derived from a password, not the password itself, this key is just as useful to an intruder. Therefore, access to the password attribute of an account object is granted only to the account holder, never to anyone else, not even administrators. Only processes with Trusted Computing Base privilege—processes running in the security [*context*](/windows/desktop/SecGloss/c-gly) of the LSA—are allowed to read or change password information.

To hinder an offline attack by someone with access to the backup tape of a domain controller, the password attribute of an account object is further protected by a second encryption using a system key. This encryption key can be stored on removable media so that it can be safeguarded separately, or it can be stored on the domain controller but protected by a dispersal mechanism. Administrators are given the option to choose where the system key is stored and which of several algorithms is used to encrypt password attributes.

 

 
