---
description: Protected Storage provides applications with an interface to store user data that must be kept secure or free from modification.
ms.assetid: '85c1a009-c4f7-4b5a-ad96-6845a4e80de9'
title: PStore
ms.topic: article
ms.date: 05/31/2018
---

# PStore

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

Protected Storage provides applications with an interface to store user data that must be kept secure or free from modification.

Units of data stored are called Items. The structure and content of the stored data is opaque to the Protected Storage system. Access to Items is subject to confirmation according to a user-defined Security Style, which specifies what confirmation is required to access the data, such as whether a password is required. In addition, access to Items is subject to an Access rule set. There is an Access rule for each Access Mode: for example, read/write. Access rule sets are composed of Access Clauses. Two kinds of Access Clauses are currently supported: Authenticode and Binary Check of caller. Typically at application setup time, a mechanism is provided to allow a new application to request from the user access to Items that may have been created previously by another application.

Items are uniquely identified by the combination of a Key, Type, Subtype, and Name. The Key is a constant that specifies whether the Item is global to this computer or associated only with this user. The Name is a string, generally chosen by the user. Type and Subtype are **GUID**s, generally specified by the application. Additional information about Types and Subtypes is kept in the system registry and include attributes such as Display Name and UI hints. For Subtypes, the parent Type is fixed and included in the system registry as an attribute. The Type group Items is used for a common purpose: for example, Payment or Identification. The Subtype group Items share a common data format.

## In this section

-   [**IEnumPStoreItems**](ienumpstoreitems.md)
-   [**IEnumPStoreProviders**](ienumpstoreproviders.md)
-   [**IEnumPStoreTypes**](ienumpstoretypes.md)
-   [**IPStore**](ipstore.md)
-   [**PStoreCreateInstance**](pstorecreateinstance.md)
-   [**PStoreEnumProviders**](pstoreenumproviders.md)
-   [**PStore Constants**](pstore-constants.md)
-   [**PStore Types**](pstore-types.md)

 

 
