---
description: Provides properties and methods that you can use to choose, manage, and use certificate stores and the certificates in those stores.
ms.assetid: 'de4eecf7-c03b-4733-ac29-d5b26b873dba'
title: Store object
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Store
api_type:
- COM
api_location:
- Capicom.dll
---

# Store object

\[The **Store** object is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Store Class**](/dotnet/api/system.security.cryptography.x509certificates.x509store?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace.\]

The **Store** object provides properties and methods that you can use to choose, manage, and use [*certificate stores*](../secgloss/c-gly.md) and the certificates in those stores. CAPICOM can use Current-User, Local-Machine, memory, and Active Directory stores. Also, stores support smart card–based certificate stores. Developers should be aware that some methods may fail with some stores if operations are attempted for which the user does not have rights.

## Members

The **Store** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Store** object has these methods.



| Method                         | Description                                                                                                                                                                                                      |
|:-------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](store-add.md)       | Adds a [**Certificate**](certificate.md) object to the open certificate store.<br/>                                                                                                                       |
| [**Close**](store-close.md)   | Closes an open certificate store.<br/> **CAPICOM 2.0.0.3 and earlier:** The [**Close**](store-close.md) method is not supported.<br/>                                                               |
| [**Delete**](store-delete.md) | Deletes the certificate store represented by the current [**Store**](certificate.md) object.<br/> **CAPICOM 2.0.0.3 and earlier:** The [**Delete**](store-delete.md) method is not supported.<br/> |
| [**Export**](store-export.md) | Exports the store of an encoded [*BLOB*](../secgloss/b-gly.md).<br/>                                                                                                       |
| [**Import**](store-import.md) | Imports a previously exported store.<br/>                                                                                                                                                                  |
| [**Load**](store-load.md)     | Imports [**Certificate**](certificate.md) objects from a file into the store.<br/>                                                                                                                        |
| [**Open**](store-open.md)     | Opens a certificate store.<br/>                                                                                                                                                                            |
| [**Remove**](store-remove.md) | Removes a [**Certificate**](certificate.md) object from an open store.<br/>                                                                                                                               |



 

### Properties

The **Store** object has these properties.



| Property                                              | Access type          | Description                                                                                                                                                                                           |
|:------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Certificates**](store-certificates.md)<br/> | Read-only<br/> | Retrieves the [**Certificates**](certificates.md) collection of the store. This is the default property.<br/>                                                                                  |
| [**Location**](store-location.md)<br/>         | Read-only<br/> | Retrieves the location of the certificate store that this object represents.<br/> **CAPICOM 2.0.0.3 and earlier:** The [**Location**](store-location.md) property is not supported.<br/> |
| [**Name**](store-name.md)<br/>                 | Read-only<br/> | Retrieves the name of the certificate store that this object represents.<br/> **CAPICOM 2.0.0.3 and earlier:** The [**Name**](store-name.md) property is not supported.<br/>             |



 

## Remarks

The **Store** object can be created, and it is safe for scripting. The ProgID for the **Store** object is CAPICOM.Store.2.

**CAPICOM 1.*x*:** The ProgID for the **Store** object is CAPICOM.Store.1.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 
