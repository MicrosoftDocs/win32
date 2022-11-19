---
description: This section describes a set of Windows helper functions used with IPropertyBag objects.
ms.assetid: 4ef85855-7eb6-43ec-bf29-1223eaf1a0cc
title: Property Bag Functions
ms.topic: article
ms.date: 05/31/2018
---

# Property Bag Functions

This section describes a set of Windows helper functions used with [**IPropertyBag**](/windows/win32/api/oaidl/nn-oaidl-ipropertybag) objects.



| Topic                                                                       | Contents                                                                                                                     |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [**PSPropertyBag\_Delete**](/windows/win32/api/propsys/nf-propsys-pspropertybag_delete)                     | Deletes a property from a property bag.<br/>                                                                           |
| [**PSPropertyBag\_ReadBOOL**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readbool)                 | Reads the **BOOL** data value of a property in a property bag.<br/>                                                    |
| [**PSPropertyBag\_ReadBSTR**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readbstr)                 | Reads a **BSTR** data value from a property in a property bag.<br/>                                                    |
| [**PSPropertyBag\_ReadDWORD**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readdword)               | Reads a **DWORD** data value from property in a property bag.<br/>                                                     |
| [**PSPropertyBag\_ReadGUID**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readguid)                 | Reads the GUID data value from a property in a property bag.<br/>                                                      |
| [**PSPropertyBag\_ReadInt**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readint)                   | Reads an **int** data value from a property in a property bag.<br/>                                                    |
| [**PSPropertyBag\_ReadLONG**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readlong)                 | Reads a **LONG** data value from a property in a property bag.<br/>                                                    |
| [**PSPropertyBag\_ReadPOINTL**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readpointl)             | Retrieves the property coordinates stored in a [**POINTL**](/windows/win32/api/windef/ns-windef-pointl) structure of a specified property bag.<br/>    |
| [**PSPropertyBag\_ReadPOINTS**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readpoints)             | Retrieves the property coordinates stored in a [**POINTS**](/windows/win32/api/windef/ns-windef-points) structure of a specified property bag.<br/>    |
| [**PSPropertyBag\_ReadPropertyKey**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readpropertykey)   | Reads the property key of a property in a specified property bag.<br/>                                                 |
| [**PSPropertyBag\_ReadRECTL**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readrectl)               | Retrieves the coordinates of a rectangle stored in a property contained in a specified property bag.<br/>              |
| [**PSPropertyBag\_ReadSHORT**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readshort)               | Reads the **SHORT** data value of a property in a property bag.<br/>                                                   |
| [**PSPropertyBag\_ReadStr**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readstr)                   | Reads the **string** data value of a property in a property bag.<br/>                                                  |
| [**PSPropertyBag\_ReadStrAlloc**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readstralloc)         | Reads a **string** data value from a property in a property bag and allocates memory for the string that is read.<br/> |
| [**PSPropertyBag\_ReadStream**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readstream)             | Reads the data stream stored in a given property contained in a specified property bag.<br/>                           |
| [**PSPropertyBag\_ReadType**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readtype)                 | Reads the type of data value of a property that is stored in a property bag.<br/>                                      |
| [**PSPropertyBag\_ReadULONGLONG**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readulonglong)       | Reads a **ULONGLONG** data value from a property in a property bag.<br/>                                               |
| [**PSPropertyBag\_ReadUnknown**](/windows/win32/api/propsys/nf-propsys-pspropertybag_readunknown)           | Reads a given property of an unknown data value in a property bag.<br/>                                                |
| [**PSPropertyBag\_WriteBOOL**](/windows/win32/api/propsys/nf-propsys-pspropertybag_writebool)               | Sets the **BOOL** data value of a property in a property bag.<br/>                                                     |
| [**PSPropertyBag\_WriteBSTR**](/windows/win32/api/propsys/nf-propsys-pspropertybag_writebstr)               | Sets a **BSTR** data value from a property in a property bag.<br/>                                                     |
| [**PSPropertyBag\_WriteDWORD**](/windows/win32/api/propsys/nf-propsys-pspropertybag_writedword)             | Sets a **DWORD** data value from property in a property bag.<br/>                                                      |
| [**PSPropertyBag\_WriteGUID**](/windows/win32/api/propsys/nf-propsys-pspropertybag_writeguid)               | Sets the GUID data value from a property in a property bag.<br/>                                                       |
| [**PSPropertyBag\_WriteInt**](/windows/win32/api/propsys/nf-propsys-pspropertybag_writeint)                 | Sets an **int** data value from a property in a property bag.<br/>                                                     |
| [**PSPropertyBag\_WriteLONG**](/windows/win32/api/propsys/nf-propsys-pspropertybag_writelong)               | Sets a **LONG** data value from a property in a property bag.<br/>                                                     |
| [**PSPropertyBag\_WritePOINTL**](/windows/win32/api/propsys/nf-propsys-pspropertybag_writepointl)           | Stores the property coordinates stored in a [**POINTL**](/windows/win32/api/windef/ns-windef-pointl) structure of a specified property bag.<br/>       |
| [**PSPropertyBag\_WritePOINTS**](/windows/win32/api/propsys/nf-propsys-pspropertybag_writepoints)           | Stores the property coordinates stored in a [**POINTS**](/windows/win32/api/windef/ns-windef-points) structure of a specified property bag.<br/>       |
| [**PSPropertyBag\_WritePropertyKey**](/windows/win32/api/propsys/nf-propsys-pspropertybag_writepropertykey) | Sets the property key of a property in a specified property bag.<br/>                                                  |
| [**PSPropertyBag\_WriteRECTL**](/windows/win32/api/propsys/nf-propsys-pspropertybag_writerectl)             | Stores the coordinates of a rectangle stored in a property contained in a specified property bag.<br/>                 |
| [**PSPropertyBag\_WriteSHORT**](/windows/win32/api/propsys/nf-propsys-pspropertybag_writeshort)             | Sets the **SHORT** data value of a property in a property bag.<br/>                                                    |
| [**PSPropertyBag\_WriteStr**](/windows/win32/api/propsys/nf-propsys-pspropertybag_writestr)                 | Sets the **string** data value of a property in a property bag.<br/>                                                   |
| [**PSPropertyBag\_WriteStream**](/windows/win32/api/propsys/nf-propsys-pspropertybag_writestream)           | Sets the data stream stored in a given property contained in a specified property bag.<br/>                            |
| [**PSPropertyBag\_WriteULONGLONG**](/windows/win32/api/propsys/nf-propsys-pspropertybag_writeulonglong)     | Sets a **ULONGLONG** data value from a property in a property bag.<br/>                                                |
| [**PSPropertyBag\_WriteUnknown**](/windows/win32/api/propsys/nf-propsys-pspropertybag_writeunknown)         | Sets a given property of an unknown data value in a property bag.<br/>                                                 |



 

## Related topics

<dl> <dt>

[PROPVARIANT and VARIANT Functions](./functions-propvarutil.md)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 
