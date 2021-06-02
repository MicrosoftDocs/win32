---
description: CNG provides a model for private key storage that allows adapting to the current and future demands of creating applications that use cryptography features such as public or private key encryption, as well as the demands of the storage of key material.
ms.assetid: 95e5750f-fdc5-41f3-a4ce-9593a7081e95
title: Key Storage and Retrieval
ms.topic: article
ms.date: 05/31/2018
---

# Key Storage and Retrieval

-   [Key Storage Architecture](#key-storage-architecture)
-   [Key Types](#key-types)
-   [Supported Algorithms](#supported-algorithms)
-   [Key Directories and Files](#key-directories-and-files)

## Key Storage Architecture

CNG provides a model for private key storage that allows adapting to the current and future demands of creating applications that use cryptography features such as public or private key encryption, as well as the demands of the storage of key material. The key storage router is the central routine in this model and is implemented in Ncrypt.dll. An application accesses the key storage providers (KSPs) on the system through the key storage router, which conceals details, such as key isolation, from both the application and the storage provider itself. The following illustration shows the design and function of the CNG key isolation architecture.

![cng key storage provider](images/cng-key-storage-provider.png)

To comply with common criteria (CC) requirements, the long-lived keys must be isolated so that they are never present in the application process. CNG currently supports the storage of asymmetric private keys by using the Microsoft software KSP that is included with Windows Server 2008 and Windows Vista and installed by default.

Key isolation is enabled by default in Windows Server 2008 and Windows Vista. The key isolation feature is not available on platforms prior to these. Also, third party KSPs are not loaded in the key isolation service (LSA process). Only the Microsoft KSP is loaded in the key isolation service.

The LSA process is used as the key isolation process to maximize performance. All access to private keys goes through the key storage router, which exposes a comprehensive set of functions for managing and using private keys.

CNG stores the public portion of the stored key separately from the private portion. The public portion of a key pair is also maintained in the key isolation service and is accessed by using local remote procedure call (LRPC). The key storage router uses LRPC when calling into the key isolation process. All access to private keys goes through the private key router and is audited by CNG.

As described above, a wide range of hardware storage devices can be supported. In each case, the interface to all of these storage devices is identical. It includes functions to perform various private key operations as well as functions that pertain to key storage and management.

CNG provides a set of APIs that are used to create, store, and retrieve cryptographic keys. For a list of these APIs, see [CNG Key Storage Functions](cng-key-storage-functions.md).

## Key Types

CNG supports the following key types:

-   Diffie-Hellman public and private keys.
-   Digital Signature Algorithm (DSA, FIPS 186-2) public and private keys.
-   RSA (PKCS \#1) public and private keys.
-   Several legacy (CryptoAPI) public and private keys.
-   Elliptic Curve Cryptography public and private keys.

## Supported Algorithms

CNG supports the following key algorithms.

| Algorithm | Key/hash length (bits)             |
|-----------|------------------------------------|
| RSA       | 512 to 16384, in 64 bit increments |
| DH        | 512 to 16384, in 64 bit increments |
| DSA       | 512 to 1024, in 64 bit increments  |
| ECDSA     | P-256, P-384, P-521 (NIST Curves)  |
| ECDH      | P-256, P-384, P-521 (NIST Curves)  |
| MD2       | 128                                |
| MD4       | 128                                |
| MD5       | 128                                |
| SHA-1     | 160                                |
| SHA-256   | 256                                |
| SHA-384   | 384                                |
| SHA-512   | 512                                |



 

## Key Directories and Files

The Microsoft legacy CryptoAPI CSPs store private keys in the following directories.

| Key type                | Directories                                                                                                                                                 |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User private            | %APPDATA%\\Microsoft\\Crypto\\RSA\\*User SID*\\<br/>%APPDATA%\\Microsoft\\Crypto\\DSS\\*User SID*\\<br/>                                                   |
| Local system private    | %ALLUSERSPROFILE%\\Application Data\\Microsoft\\Crypto\\RSA\\S-1-5-18\\<br/>%ALLUSERSPROFILE%\\Application Data\\Microsoft\\Crypto\\DSS\\S-1-5-18\\<br/>   |
| Local service private   | %ALLUSERSPROFILE%\\Application Data\\Microsoft\\Crypto\\RSA\\S-1-5-19\\<br/>%ALLUSERSPROFILE%\\Application Data\\Microsoft\\Crypto\\DSS\\S-1-5-19\\<br/>   |
| Network service private | %ALLUSERSPROFILE%\\Application Data\\Microsoft\\Crypto\\RSA\\S-1-5-20\\<br/>%ALLUSERSPROFILE%\\Application Data\\Microsoft\\Crypto\\DSS\\S-1-5-20\\<br/>   |
| Shared private          | %ALLUSERSPROFILE%\\Application Data\\Microsoft\\Crypto\\RSA\\MachineKeys<br/>%ALLUSERSPROFILE%\\Application Data\\Microsoft\\Crypto\\DSS\\MachineKeys<br/> |



 

CNG stores private keys in the following directories.

| Key type                | Directory                                                          |
|-------------------------|--------------------------------------------------------------------|
| User private            | %APPDATA%\\Microsoft\\Crypto\\Keys                                 |
| Local system private    | %ALLUSERSPROFILE%\\Application Data\\Microsoft\\Crypto\\SystemKeys |
| Local service private   | %WINDIR%\\ServiceProfiles\\LocalService                            |
| Network service private | %WINDIR%\\ServiceProfiles\\NetworkService                          |
| Shared private          | %ALLUSERSPROFILE%\\Application Data\\Microsoft\\Crypto\\Keys       |



 

The following are some of the differences between the CryptoAPI and CNG key containers.

-   CNG uses different file names for key files than key files that are created by the Rsaenh.dll and Dssenh.dll legacy CSPs. The legacy key files also have the .key extension, but CNG key files do not have the .key extension.
-   CNG fully supports Unicode key container names; CNG uses a hash of the Unicode container name, whereas CryptoAPI uses a hash of the ANSI container name.
-   CNG is more flexible with regard to RSA key pairs. For example, CNG supports public exponents larger than 32-bits in length, and it supports keys in which p and q are different lengths.
-   In CryptoAPI, the key container file is stored in a directory whose name is the textual equivalent of the user's SID. This is no longer the case in CNG, which removes the difficulty of moving users from one domain to another without losing all of their private keys.
-   The CNG KSP and key names are limited to **MAX\_PATH** Unicode characters. The CryptoAPI CSP and key names are limited to **MAX\_PATH** ANSI characters.
-   CNG offers the capability of user-defined key properties. Users can create and associate custom properties with keys, and have them stored with persisted keys.

When persisting a key, CNG can create two files. The first file contains the private key in the new CNG format and is always created. This file is not usable by the legacy CryptoAPI CSPs. The second file contains the same private key in the legacy CryptoAPI key container. The second file conforms to the format and location used by Rsaenh.dll. Creation of the second file only occurs if the **NCRYPT\_WRITE\_KEY\_TO\_LEGACY\_STORE\_FLAG** flag is specified when the [**NCryptFinalizeKey**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptfinalizekey) function is called to finalize an RSA key. This feature is not supported for DSA and DH keys.

When an application attempts to open an existing persisted key, CNG first attempts to open the native CNG file. If this file does not exist, then CNG attempts to locate a matching key in the legacy CryptoAPI key container.

When you move or copy CryptoAPI keys from a source machine to a target machine with Windows User State Migration Tool (USMT), CNG will fail to access the keys on the target machine. To access such migrated keys, you must use the CryptoAPI.

 

 




