---
description: Provides functionality for hashing a string.
ms.assetid: 893639c2-57b9-48f6-bf60-a21c3368ffeb
title: HashedData object
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- HashedData
api_type:
- COM
api_location:
- Capicom.dll
---

# HashedData object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**HashAlgorithm Class**](/previous-versions/windows/) in the [**System.Security.Cryptography**](/dotnet/api/system.security.cryptography?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

The **HashedData** object provides functionality for hashing a string.

## When to use

The **HashedData** object is used to perform the following tasks:

-   Specify the content string that contains the data to be hashed.
-   Apply a specified hash algorithm to the content string.

## Members

The **HashedData** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **HashedData** object has these methods.



| Method                          | Description                                        |
|:--------------------------------|:---------------------------------------------------|
| [**Hash**](hasheddata-hash.md) | Creates a hash of the specified string.<br/> |



 

### Properties

The **HashedData** object has these properties.



| Property                                             | Access type           | Description                                                                                                                                                                          |
|:-----------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Algorithm**](hasheddata-algorithm.md)<br/> | Read/write<br/> | Sets or retrieves the type of hashing algorithm used.<br/>                                                                                                                     |
| [**Value**](hasheddata-value.md)<br/>         | Read-only<br/>  | Retrieves the hashed data after successful calls to the [**Hash**](hasheddata-hash.md) method. The hash is returned in hexadecimal format. This is the default property.<br/> |



 

## Remarks

To create the hash of a large amount of data, call the [**Hash**](hasheddata-hash.md) method for each piece of data. The hash of each piece of data is concatenated to the [**Value**](hasheddata-value.md) property until the property is read. The contents of the **Value** property are reset when the property is read.

The **HashedData** object can be created, and it is safe for scripting. The ProgID for the **HashedData** object is "CAPICOM.HashedData.1".

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
