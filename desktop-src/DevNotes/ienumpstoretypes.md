---
Description: Provides COM-standard enumeration methods for the IPStore interface.
ms.assetid: a90bc5cf-ca42-4007-a57b-be9c59d9552a
title: IEnumPStoreTypes interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IEnumPStoreTypes interface

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](https://msdn.microsoft.com/765a68fd-f105-49fc-a738-4a8129eb0770) and [**CryptUnprotectData**](https://msdn.microsoft.com/54eab3b0-d341-47c6-9c32-79328d7a7155) functions.\]

Provides COM-standard enumeration methods for the [**IPStore**](ipstore.md) interface.

## Members

The **IEnumPStoreTypes** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IEnumPStoreTypes** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumPStoreTypes** interface has these methods.



| Method                                  | Description                                                                                        |
|:----------------------------------------|:---------------------------------------------------------------------------------------------------|
| [**Clone**](ienumpstoretypes-clone.md) | Creates another enumerator that contains the same enumeration state as the current one.<br/> |
| [**Next**](ienumpstoretypes-next.md)   | Gets the next specified provider type in the enumeration sequence.<br/>                      |
| [**Reset**](ienumpstoretypes-reset.md) | Resets to the beginning of the enumeration sequence.<br/>                                    |
| [**Skip**](ienumpstoretypes-skip.md)   | Skips the specified provider type in the enumeration sequence.<br/>                          |



 

## Remarks

The enumerator object must be released when it is no longer being used.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl>    |
| DLL<br/>    | <dl> <dt>Pstorec.dll</dt> </dl> |



 

 




