---
description: Provides the COM-standard enumeration methods for the IPStore interface.
ms.assetid: f5290e6c-8752-4380-9210-c96a87f000ba
title: IEnumPStoreItems interface (Pstore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEnumPStoreItems
api_type: 
- COM
api_location: 
- Pstorec.dll
---

# IEnumPStoreItems interface

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

Provides the COM-standard enumeration methods for the [**IPStore**](ipstore.md) interface.

## Members

The **IEnumPStoreItems** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IEnumPStoreItems** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumPStoreItems** interface has these methods.



| Method                                  | Description                                                                                        |
|:----------------------------------------|:---------------------------------------------------------------------------------------------------|
| [**Clone**](ienumpstoreitems-clone.md) | Creates another enumerator that contains the same enumeration state as the current one.<br/> |
| [**Next**](ienumpstoreitems-next.md)   | Gets the next specified data item in the enumeration sequence.<br/>                          |
| [**Reset**](ienumpstoreitems-reset.md) | Resets to the beginning of the enumeration sequence.<br/>                                    |
| [**Skip**](ienumpstoreitems-skip.md)   | Skips the specified data item in the enumeration sequence.<br/>                              |



 

## Remarks

It is necessary to free each item after enumerating it. The enumerator object must also be released when it is no longer being used.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl>    |
| DLL<br/>    | <dl> <dt>Pstorec.dll</dt> </dl> |



 

 
