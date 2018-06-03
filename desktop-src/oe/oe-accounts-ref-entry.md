---
title: Windows Mail Accounts Reference
description: This documentation provides accounts-related information about the set of interfaces for objects related to Windows Mail (formerly Outlook Express).
ms.assetid: 3a7d010a-0771-4234-a2fd-ea248bac71a8
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Mail Accounts Reference

This documentation provides accounts-related information about the set of interfaces for objects related to Windows Mail (formerly Outlook Express).

New applications should not use this set of interfaces and schemas. These interfaces and schemas exist for backward compatibility with legacy applications. These interfaces and schemas will be unavailable in the future.

### Interfaces



| Topic                                                         | Contents                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IImnAccount**](oe-iimnaccount.md)                         | Do not use. Represents the base Internet Mail and News (IMN) account object.<br/>                                                                                                                                                                                             |
| [**IImnAccountManager**](oe-iimnaccountmanager.md)           | Do not use. This object allows a client to create, open, delete, and enumerate accounts.<br/>                                                                                                                                                                                 |
| [**IImnAccountManager2**](oe-iimnaccountmanager2.md)         | Do not use. Extends [**IImnAccountManager**](oe-iimnaccountmanager.md).<br/>                                                                                                                                                                                                 |
| [**IImnAdviseAccount**](oe-iimnadviseaccount.md)             | Do not use. When a method in the account manager is called that deletes, modifies or changes a default account, notifications are generated. A client can hook all notifications by implementing the simple [**IImnAdviseAccount**](oe-iimnadviseaccount.md) interface.<br/> |
| [**IImnAdviseMigrateServer**](oe-iimnadvisemigrateserver.md) | Do not use. Used to receive notification when an account is migrated.<br/>                                                                                                                                                                                                    |
| [**IImnEnumAccounts**](oe-iimnenumaccounts.md)               | Do not use. Used to enumerate IMN accounts.<br/>                                                                                                                                                                                                                              |
| [**IPropertyContainer**](oe-ipropertycontainer.md)           | Do not use. Gets and sets values of account properties. <br/>                                                                                                                                                                                                                 |



 

### Enums



| Topic                                   | Contents                                                                                    |
|-----------------------------------------|---------------------------------------------------------------------------------------------|
| [**ACCTTYPE**](oe-accttype.md)         | Do not use. Defines the various account types.<br/>                                   |
| [**PROPTYPE**](oe-proptype.md)         | Do not use. Defines the data type of a property. <br/>                                |
| [**SMTPAUTHTYPE**](oe-smtpauthtype.md) | Do not use. Defines Simple Mail Transport Protocol (SMTP) authentication types. <br/> |



 

### Structures



| Topic                                   | Contents                                                                                        |
|-----------------------------------------|-------------------------------------------------------------------------------------------------|
| [**ACCTLISTINFO**](oe-acctlistinfo.md) | Do not use. Contains information about an account list for display in a dialog box. <br/> |
| [**ACTX**](oe-actx.md)                 | Do not use. Contains account information. <br/>                                           |



 

### Constants



| Topic                                                             | Contents                                                                                                                                    |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**Account Flags**](oe-account-flags.md)                         | Do not use. Account type flag values that can be set and their meaning. <br/>                                                         |
| [**Account Initialization**](oe-account-init.md)                 | Do not use. Account initialization type values that can be set, and their meaning. <br/>                                              |
| [**Connection Types**](oe-connection-types.md)                   | Do not use. Connection type values that can be set, and their meaning. <br/>                                                          |
| [**IMAP Dirty Flags**](oe-imap-dirty-flags.md)                   | Do not use. Internet Message Access Protocol (IMAP) special folders list dirty flag values that can be set, and their meaning. <br/>  |
| [**LDAP Authentication Types**](oe-ldap-authentication-types.md) | Do not use. Lightweight Directory Access Protocol (LDAP) authentication type values that can be set, and their meaning. <br/>         |
| [**LDAP NTDS Types**](oe-ldap-ntds-types.md)                     | Do not use. LDAP NTDS type values that can be set. <br/>                                                                              |
| [**LDAP Paged Result Support Types**](oe-ldap-presult-types.md)  | Do not use. For convenience, query results may be broken into pages. The following LDAP paged result support types are defined: <br/> |
| [**NNTP Post Format Types**](oe-nntp-post-format-types.md)       | Do not use. Network News Transport Protocol (NNTP) posting format type values that can be set, and their meaning. <br/>               |
| [**NNTP User Information Types**](oe-nntp-user-info-types.md)    | Do not use. NNTP user information type values that can be set, and their meaning. <br/>                                               |
| [**Server Types**](oe-server-types.md)                           | Do not use. Server type values that can be set and their meaning. <br/>                                                               |



 

 

 





