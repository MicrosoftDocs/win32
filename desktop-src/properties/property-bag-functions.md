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

This section describes a set of Windows helper functions used with [**IPropertyBag**](https://www.bing.com/search?q=**IPropertyBag**) objects.



| Topic                                                                       | Contents                                                                                                                     |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [**PSPropertyBag\_Delete**](https://www.bing.com/search?q=**PSPropertyBag\_Delete**)                     | Deletes a property from a property bag.<br/>                                                                           |
| [**PSPropertyBag\_ReadBOOL**](https://www.bing.com/search?q=**PSPropertyBag\_ReadBOOL**)                 | Reads the **BOOL** data value of a property in a property bag.<br/>                                                    |
| [**PSPropertyBag\_ReadBSTR**](https://www.bing.com/search?q=**PSPropertyBag\_ReadBSTR**)                 | Reads a **BSTR** data value from a property in a property bag.<br/>                                                    |
| [**PSPropertyBag\_ReadDWORD**](https://www.bing.com/search?q=**PSPropertyBag\_ReadDWORD**)               | Reads a **DWORD** data value from property in a property bag.<br/>                                                     |
| [**PSPropertyBag\_ReadGUID**](https://www.bing.com/search?q=**PSPropertyBag\_ReadGUID**)                 | Reads the GUID data value from a property in a property bag.<br/>                                                      |
| [**PSPropertyBag\_ReadInt**](https://www.bing.com/search?q=**PSPropertyBag\_ReadInt**)                   | Reads an **int** data value from a property in a property bag.<br/>                                                    |
| [**PSPropertyBag\_ReadLONG**](https://www.bing.com/search?q=**PSPropertyBag\_ReadLONG**)                 | Reads a **LONG** data value from a property in a property bag.<br/>                                                    |
| [**PSPropertyBag\_ReadPOINTL**](https://www.bing.com/search?q=**PSPropertyBag\_ReadPOINTL**)             | Retrieves the property coordinates stored in a [**POINTL**](https://msdn.microsoft.com/587d36c8-e81c-4256-af25-af2a82727e8d) structure of a specified property bag.<br/>    |
| [**PSPropertyBag\_ReadPOINTS**](https://www.bing.com/search?q=**PSPropertyBag\_ReadPOINTS**)             | Retrieves the property coordinates stored in a [**POINTS**](https://msdn.microsoft.com/d36bc846-c538-4a37-bb5d-c75d41a3c7cc) structure of a specified property bag.<br/>    |
| [**PSPropertyBag\_ReadPropertyKey**](https://www.bing.com/search?q=**PSPropertyBag\_ReadPropertyKey**)   | Reads the property key of a property in a specified property bag.<br/>                                                 |
| [**PSPropertyBag\_ReadRECTL**](https://www.bing.com/search?q=**PSPropertyBag\_ReadRECTL**)               | Retrieves the coordinates of a rectangle stored in a property contained in a specified property bag.<br/>              |
| [**PSPropertyBag\_ReadSHORT**](https://www.bing.com/search?q=**PSPropertyBag\_ReadSHORT**)               | Reads the **SHORT** data value of a property in a property bag.<br/>                                                   |
| [**PSPropertyBag\_ReadStr**](https://www.bing.com/search?q=**PSPropertyBag\_ReadStr**)                   | Reads the **string** data value of a property in a property bag.<br/>                                                  |
| [**PSPropertyBag\_ReadStrAlloc**](https://www.bing.com/search?q=**PSPropertyBag\_ReadStrAlloc**)         | Reads a **string** data value from a property in a property bag and allocates memory for the string that is read.<br/> |
| [**PSPropertyBag\_ReadStream**](https://www.bing.com/search?q=**PSPropertyBag\_ReadStream**)             | Reads the data stream stored in a given property contained in a specified property bag.<br/>                           |
| [**PSPropertyBag\_ReadType**](https://www.bing.com/search?q=**PSPropertyBag\_ReadType**)                 | Reads the type of data value of a property that is stored in a property bag.<br/>                                      |
| [**PSPropertyBag\_ReadULONGLONG**](https://www.bing.com/search?q=**PSPropertyBag\_ReadULONGLONG**)       | Reads a **ULONGLONG** data value from a property in a property bag.<br/>                                               |
| [**PSPropertyBag\_ReadUnknown**](https://www.bing.com/search?q=**PSPropertyBag\_ReadUnknown**)           | Reads a given property of an unknown data value in a property bag.<br/>                                                |
| [**PSPropertyBag\_WriteBOOL**](https://www.bing.com/search?q=**PSPropertyBag\_WriteBOOL**)               | Sets the **BOOL** data value of a property in a property bag.<br/>                                                     |
| [**PSPropertyBag\_WriteBSTR**](https://www.bing.com/search?q=**PSPropertyBag\_WriteBSTR**)               | Sets a **BSTR** data value from a property in a property bag.<br/>                                                     |
| [**PSPropertyBag\_WriteDWORD**](https://www.bing.com/search?q=**PSPropertyBag\_WriteDWORD**)             | Sets a **DWORD** data value from property in a property bag.<br/>                                                      |
| [**PSPropertyBag\_WriteGUID**](https://www.bing.com/search?q=**PSPropertyBag\_WriteGUID**)               | Sets the GUID data value from a property in a property bag.<br/>                                                       |
| [**PSPropertyBag\_WriteInt**](https://www.bing.com/search?q=**PSPropertyBag\_WriteInt**)                 | Sets an **int** data value from a property in a property bag.<br/>                                                     |
| [**PSPropertyBag\_WriteLONG**](https://www.bing.com/search?q=**PSPropertyBag\_WriteLONG**)               | Sets a **LONG** data value from a property in a property bag.<br/>                                                     |
| [**PSPropertyBag\_WritePOINTL**](https://www.bing.com/search?q=**PSPropertyBag\_WritePOINTL**)           | Stores the property coordinates stored in a [**POINTL**](https://msdn.microsoft.com/587d36c8-e81c-4256-af25-af2a82727e8d) structure of a specified property bag.<br/>       |
| [**PSPropertyBag\_WritePOINTS**](https://www.bing.com/search?q=**PSPropertyBag\_WritePOINTS**)           | Stores the property coordinates stored in a [**POINTS**](https://msdn.microsoft.com/d36bc846-c538-4a37-bb5d-c75d41a3c7cc) structure of a specified property bag.<br/>       |
| [**PSPropertyBag\_WritePropertyKey**](https://www.bing.com/search?q=**PSPropertyBag\_WritePropertyKey**) | Sets the property key of a property in a specified property bag.<br/>                                                  |
| [**PSPropertyBag\_WriteRECTL**](https://www.bing.com/search?q=**PSPropertyBag\_WriteRECTL**)             | Stores the coordinates of a rectangle stored in a property contained in a specified property bag.<br/>                 |
| [**PSPropertyBag\_WriteSHORT**](https://www.bing.com/search?q=**PSPropertyBag\_WriteSHORT**)             | Sets the **SHORT** data value of a property in a property bag.<br/>                                                    |
| [**PSPropertyBag\_WriteStr**](https://www.bing.com/search?q=**PSPropertyBag\_WriteStr**)                 | Sets the **string** data value of a property in a property bag.<br/>                                                   |
| [**PSPropertyBag\_WriteStream**](https://www.bing.com/search?q=**PSPropertyBag\_WriteStream**)           | Sets the data stream stored in a given property contained in a specified property bag.<br/>                            |
| [**PSPropertyBag\_WriteULONGLONG**](https://www.bing.com/search?q=**PSPropertyBag\_WriteULONGLONG**)     | Sets a **ULONGLONG** data value from a property in a property bag.<br/>                                                |
| [**PSPropertyBag\_WriteUnknown**](https://www.bing.com/search?q=**PSPropertyBag\_WriteUnknown**)         | Sets a given property of an unknown data value in a property bag.<br/>                                                 |



 

## Related topics

<dl> <dt>

[PROPVARIANT and VARIANT Functions](https://www.bing.com/search?q=PROPVARIANT+and+VARIANT+Functions)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 




