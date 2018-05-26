---
Description: Default system stores, including MY, CA, and ROOT, are implemented as logical collection stores with a number of predefined physical stores as their member stores.
ms.assetid: 1d82b94b-4842-454a-aca4-823cd264ac52
title: Logical and Physical Stores
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Logical and Physical Stores

Default system stores, including MY, CA, and ROOT, are implemented as logical collection stores with a number of predefined physical stores as their member stores. The member physical stores of a system store are opened automatically when the system store is opened. A user can add additional physical stores to any system store collection. The CryptoAPI function [**CertRegisterPhysicalStore**](/windows/win32/Wincrypt/nf-wincrypt-certregisterphysicalstore?branch=master) adds a new physical store to a system store collection. [**CertUnregisterPhysicalStore**](/windows/win32/Wincrypt/nf-wincrypt-certunregisterphysicalstore?branch=master) disassociates a physical store from a logical system store. [**CertRegisterSystemStore**](/windows/win32/Wincrypt/nf-wincrypt-certregistersystemstore?branch=master) creates a new system store under a registry hKey, while [**CertUnregisterSystemStore**](/windows/win32/Wincrypt/nf-wincrypt-certunregistersystemstore?branch=master) removes a system store from the registry.

In CryptoAPI, system stores are logical stores with associated physical stores. All the certificates in an existing system store remain available, and the physical addition of new certificates is made in the physical stores that make up the logical system store.

Users who prefer to continue to use physical system stores and not convert to logical stores can open system stores with the CERT\_STORE\_PROV\_SYSTEM\_REGISTRY provider. This provider will continue to use each system store as a single, physical store.

The functions [**CertEnumSystemStoreLocation**](/windows/win32/Wincrypt/nf-wincrypt-certenumsystemstorelocation?branch=master), [**CertEnumSystemStore**](/windows/win32/Wincrypt/nf-wincrypt-certenumsystemstore?branch=master), and [**CertEnumPhysicalStore**](/windows/win32/Wincrypt/nf-wincrypt-certenumphysicalstore?branch=master) list system store locations, available system stores, and all physical stores that are members of a system store.

System stores can also be relocated. By default, a system store is opened relative to a registry subkey following a predefined pattern. For more information, see [System Store Locations](system-store-locations.md). Setting CERT\_SYSTEM\_STORE\_RELOCATE\_FLAG in the *dwFlags* parameter passed to [**CertOpenStore**](/windows/win32/Wincrypt/nf-wincrypt-certopenstore?branch=master) places a system store in the registry under a user-specified registry subkey instead of the predefined one.

 

 



