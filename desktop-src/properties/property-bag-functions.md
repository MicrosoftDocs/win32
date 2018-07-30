---
Description: This section describes a set of Windows helper functions used with IPropertyBag objects.
ms.assetid: 4ef85855-7eb6-43ec-bf29-1223eaf1a0cc
title: Property Bag Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Property Bag Functions

This section describes a set of Windows helper functions used with [**IPropertyBag**](https://msdn.microsoft.com/library/Aa768196(v=VS.85).aspx) objects.



| Topic                                                                       | Contents                                                                                                                     |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [**PSPropertyBag\_Delete**](https://msdn.microsoft.com/library/Ee845049(v=VS.85).aspx)                     | Deletes a property from a property bag.<br/>                                                                           |
| [**PSPropertyBag\_ReadBOOL**](https://msdn.microsoft.com/library/Ee845050(v=VS.85).aspx)                 | Reads the **BOOL** data value of a property in a property bag.<br/>                                                    |
| [**PSPropertyBag\_ReadBSTR**](https://msdn.microsoft.com/library/Ee845051(v=VS.85).aspx)                 | Reads a **BSTR** data value from a property in a property bag.<br/>                                                    |
| [**PSPropertyBag\_ReadDWORD**](https://msdn.microsoft.com/library/Ee845052(v=VS.85).aspx)               | Reads a **DWORD** data value from property in a property bag.<br/>                                                     |
| [**PSPropertyBag\_ReadGUID**](https://msdn.microsoft.com/library/Ee845053(v=VS.85).aspx)                 | Reads the GUID data value from a property in a property bag.<br/>                                                      |
| [**PSPropertyBag\_ReadInt**](https://msdn.microsoft.com/library/Ee845054(v=VS.85).aspx)                   | Reads an **int** data value from a property in a property bag.<br/>                                                    |
| [**PSPropertyBag\_ReadLONG**](https://msdn.microsoft.com/library/Ee845055(v=VS.85).aspx)                 | Reads a **LONG** data value from a property in a property bag.<br/>                                                    |
| [**PSPropertyBag\_ReadPOINTL**](https://msdn.microsoft.com/library/Ee845056(v=VS.85).aspx)             | Retrieves the property coordinates stored in a [**POINTL**](https://msdn.microsoft.com/en-us/library/Dd162807(v=VS.85).aspx) structure of a specified property bag.<br/>    |
| [**PSPropertyBag\_ReadPOINTS**](https://msdn.microsoft.com/library/Ee845057(v=VS.85).aspx)             | Retrieves the property coordinates stored in a [**POINTS**](https://msdn.microsoft.com/en-us/library/Dd162808(v=VS.85).aspx) structure of a specified property bag.<br/>    |
| [**PSPropertyBag\_ReadPropertyKey**](https://msdn.microsoft.com/library/Ee845058(v=VS.85).aspx)   | Reads the property key of a property in a specified property bag.<br/>                                                 |
| [**PSPropertyBag\_ReadRECTL**](https://msdn.microsoft.com/library/Ee845059(v=VS.85).aspx)               | Retrieves the coordinates of a rectangle stored in a property contained in a specified property bag.<br/>              |
| [**PSPropertyBag\_ReadSHORT**](https://msdn.microsoft.com/library/Ee845060(v=VS.85).aspx)               | Reads the **SHORT** data value of a property in a property bag.<br/>                                                   |
| [**PSPropertyBag\_ReadStr**](https://msdn.microsoft.com/library/Ee845061(v=VS.85).aspx)                   | Reads the **string** data value of a property in a property bag.<br/>                                                  |
| [**PSPropertyBag\_ReadStrAlloc**](https://msdn.microsoft.com/library/Ee845062(v=VS.85).aspx)         | Reads a **string** data value from a property in a property bag and allocates memory for the string that is read.<br/> |
| [**PSPropertyBag\_ReadStream**](https://msdn.microsoft.com/library/Ee845063(v=VS.85).aspx)             | Reads the data stream stored in a given property contained in a specified property bag.<br/>                           |
| [**PSPropertyBag\_ReadType**](https://msdn.microsoft.com/library/Ee845064(v=VS.85).aspx)                 | Reads the type of data value of a property that is stored in a property bag.<br/>                                      |
| [**PSPropertyBag\_ReadULONGLONG**](https://msdn.microsoft.com/library/Ee845065(v=VS.85).aspx)       | Reads a **ULONGLONG** data value from a property in a property bag.<br/>                                               |
| [**PSPropertyBag\_ReadUnknown**](https://msdn.microsoft.com/library/Ee845066(v=VS.85).aspx)           | Reads a given property of an unknown data value in a property bag.<br/>                                                |
| [**PSPropertyBag\_WriteBOOL**](https://msdn.microsoft.com/library/Ee845067(v=VS.85).aspx)               | Sets the **BOOL** data value of a property in a property bag.<br/>                                                     |
| [**PSPropertyBag\_WriteBSTR**](https://msdn.microsoft.com/library/Ee845068(v=VS.85).aspx)               | Sets a **BSTR** data value from a property in a property bag.<br/>                                                     |
| [**PSPropertyBag\_WriteDWORD**](https://msdn.microsoft.com/library/Ee845069(v=VS.85).aspx)             | Sets a **DWORD** data value from property in a property bag.<br/>                                                      |
| [**PSPropertyBag\_WriteGUID**](https://msdn.microsoft.com/library/Ee845070(v=VS.85).aspx)               | Sets the GUID data value from a property in a property bag.<br/>                                                       |
| [**PSPropertyBag\_WriteInt**](https://msdn.microsoft.com/library/Ee845071(v=VS.85).aspx)                 | Sets an **int** data value from a property in a property bag.<br/>                                                     |
| [**PSPropertyBag\_WriteLONG**](https://msdn.microsoft.com/library/Ee845072(v=VS.85).aspx)               | Sets a **LONG** data value from a property in a property bag.<br/>                                                     |
| [**PSPropertyBag\_WritePOINTL**](https://msdn.microsoft.com/library/Ee845073(v=VS.85).aspx)           | Stores the property coordinates stored in a [**POINTL**](https://msdn.microsoft.com/en-us/library/Dd162807(v=VS.85).aspx) structure of a specified property bag.<br/>       |
| [**PSPropertyBag\_WritePOINTS**](https://msdn.microsoft.com/library/Ee845074(v=VS.85).aspx)           | Stores the property coordinates stored in a [**POINTS**](https://msdn.microsoft.com/en-us/library/Dd162808(v=VS.85).aspx) structure of a specified property bag.<br/>       |
| [**PSPropertyBag\_WritePropertyKey**](https://msdn.microsoft.com/library/Ee845075(v=VS.85).aspx) | Sets the property key of a property in a specified property bag.<br/>                                                  |
| [**PSPropertyBag\_WriteRECTL**](https://msdn.microsoft.com/library/Ee845076(v=VS.85).aspx)             | Stores the coordinates of a rectangle stored in a property contained in a specified property bag.<br/>                 |
| [**PSPropertyBag\_WriteSHORT**](https://msdn.microsoft.com/library/Ee845077(v=VS.85).aspx)             | Sets the **SHORT** data value of a property in a property bag.<br/>                                                    |
| [**PSPropertyBag\_WriteStr**](https://msdn.microsoft.com/library/Ee845078(v=VS.85).aspx)                 | Sets the **string** data value of a property in a property bag.<br/>                                                   |
| [**PSPropertyBag\_WriteStream**](https://msdn.microsoft.com/library/Ee845079(v=VS.85).aspx)           | Sets the data stream stored in a given property contained in a specified property bag.<br/>                            |
| [**PSPropertyBag\_WriteULONGLONG**](https://msdn.microsoft.com/library/Ee845080(v=VS.85).aspx)     | Sets a **ULONGLONG** data value from a property in a property bag.<br/>                                                |
| [**PSPropertyBag\_WriteUnknown**](https://msdn.microsoft.com/library/Ee845081(v=VS.85).aspx)         | Sets a given property of an unknown data value in a property bag.<br/>                                                 |



 

## Related topics

<dl> <dt>

[PROPVARIANT and VARIANT Functions](https://msdn.microsoft.com/library/Bb762286(v=VS.85).aspx)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 




