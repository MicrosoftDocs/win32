---
title: Vector object
description: Contains a collection of values of the same type. It is used throughout the library in many different ways. The Vector object can be created using WIA.Vector as the ProgID in a call to CreateObject.
ms.assetid: '1411191e-a4b5-4960-bc02-f52093e65171'
keywords: ["Vector object WIA Automation", "Vector object WIA Automation , described"]
topic_type:
- apiref
api_name:
- Vector
api_location:
- Wiaaut.h
api_type:
- COM
---

# Vector object

Contains a collection of values of the same type. It is used throughout the library in many different ways. The **Vector** object can be created using `WIA.Vector` as the ProgID in a call to [CreateObject](http://msdn.microsoft.com/library/7t9k08y5(VS.71).aspx).

## Members

The **Vector** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Vector** object has these methods.



| Method                                                 | Description                                                                                                                                                                                                                                                                         |
|:-------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add (Vector)**](-wiaaut-ivector-add.md)            | Inserts a new element into the **Vector** collection before the specified *Index* if *Index* is not 0. If *Index* is 0, this method appends a new element to the **Vector** collection.<br/>                                                                                  |
| [**Clear**](-wiaaut-ivector-clear.md)                 | Removes all elements from the **Vector**.<br/>                                                                                                                                                                                                                                |
| [**Remove (Vector)**](-wiaaut-ivector-remove.md)      | Removes the designated element.<br/>                                                                                                                                                                                                                                          |
| [**SetFromString**](-wiaaut-ivector-setfromstring.md) | Stores the **String** value into the **Vector** of bytes including the terminating null character. Value might be truncated unless *Resizable* is True. The string is stored as an ANSI string unless *Unicode* is True, in which case it is stored as a Unicode string.<br/> |



 

### Properties

The **Vector** object has these properties.



| Property                                                           | Access type           | Description                                                                                                                                                                                                                                                               |
|:-------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BinaryData**](-wiaaut-ivector-binarydata.md)<br/>        | Read/write<br/> | Sets or retrieves the **Vector** of bytes as an array of bytes.<br/>                                                                                                                                                                                                |
| [**Count (Vector)**](-wiaaut-ivector-count.md)<br/>         | Read-only<br/>  | Retrieves the number of members in the **Vector**.<br/>                                                                                                                                                                                                             |
| [**Date**](-wiaaut-ivector-date.md)<br/>                    | Read/write<br/> | Sets or retrieves the **Vector** of integers from a date.<br/>                                                                                                                                                                                                      |
| [**ImageFile (Vector)**](-wiaaut-ivector-imagefile.md)<br/> | Read-only<br/>  | Retrieves the image file thumbnail of an [**ImageFile**](-wiaaut-imagefile.md) object, the RGB data thumbnail of an [**Item**](-wiaaut-item.md) object, or creates an **ImageFile** object from raw ARGB data. Retrieves an **ImageFile** object on success.<br/> |
| [**Item (Vector)**](-wiaaut-ivector-item.md)<br/>           | Read/write<br/> | Sets or retrieves the specified item in the **Vector** by position.<br/>                                                                                                                                                                                            |
| [**Picture**](-wiaaut-ivector-picture.md)<br/>              | Read-only<br/>  | Retrieves a Visual Basic picture object. <br/>                                                                                                                                                                                                                      |
| [**String**](-wiaaut-ivector-string.md)<br/>                | Read-only<br/>  | Retrieves a **Vector** of bytes as a **String**.<br/>                                                                                                                                                                                                               |



 

## Remarks

Note that the **Vector** object provides special accessor properties and methods to make it easier to access or manipulate the elements contained in a **Vector** object. For more information, see the reference page for the specific property or method .

For example code, see [Create and Initialize a Vector Object](-wiaaut-shared-samples.md#create-and-initialize-a-vector-object) in Shared Samples.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**SubTypeValues**](-wiaaut-iproperty-subtypevalues.md)

[**FileData**](-wiaaut-iimagefile-filedata.md)

[**ARGBData**](-wiaaut-iimagefile-argbdata.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**ARGBData**](-wiaaut-iimagefile-argbdata.md)
</dt> <dt>

[**FileData**](-wiaaut-iimagefile-filedata.md)
</dt> <dt>

[**SubTypeValues**](-wiaaut-iproperty-subtypevalues.md)
</dt> </dl>

 

 





