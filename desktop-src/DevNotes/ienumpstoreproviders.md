---
Description: Provides COM-standard enumeration methods for the IPStore interface.
ms.assetid: d4c0482c-a751-4d41-bcd1-326878fdcf16
title: IEnumPStoreProviders interface
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IEnumPStoreProviders interface

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](security.cryptprotectdata) and [**CryptUnprotectData**](security.cryptunprotectdata) functions.\]

Provides COM-standard enumeration methods for the [**IPStore**](ipstore.md) interface.

## Members

The **IEnumPStoreProviders** interface inherits from the [**IUnknown**](com.iunknown) interface. **IEnumPStoreProviders** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumPStoreProviders** interface has these methods.



| Method                                      | Description                                                                                        |
|:--------------------------------------------|:---------------------------------------------------------------------------------------------------|
| [**Clone**](ienumpstoreproviders-clone.md) | Creates another enumerator that contains the same enumeration state as the current one.<br/> |
| [**Next**](ienumpstoreproviders-next.md)   | Gets the next specified provider in the enumeration sequence.<br/>                           |
| [**Reset**](ienumpstoreproviders-reset.md) | Resets to the beginning of the enumeration sequence.<br/>                                    |
| [**Skip**](ienumpstoreproviders-skip.md)   | Skips the specified provider in the enumeration sequence.<br/>                               |



 

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl>    |
| DLL<br/>    | <dl> <dt>Pstorec.dll</dt> </dl> |



 

 




