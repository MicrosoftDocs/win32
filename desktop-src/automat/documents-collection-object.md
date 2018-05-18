---
title: Documents Collection Object
description: If your application supports a multiple-document interface (MDI), you should provide a Documents collection object.
ms.assetid: '8c301453-ca38-480a-ba66-b1f340b9dc1d'
---

# Documents Collection Object

If your application supports a multiple-document interface (MDI), you should provide a Documents collection object. Use the name Documents for this collection, unless the name is inappropriate for the application.

The Documents collection object should have all of the following properties.



| Property name              | Return type             | Description                                                                                                                     |
|----------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **Application**<br/> | VT\_DISPATCH<br/> | Returns the Application object; read only. Required.<br/>                                                                 |
| **Count**<br/>       | VT\_I4<br/>       | Returns the number of items in the collection; read only. Required.<br/>                                                  |
| **\_NewEnum**<br/>   | VT\_DISPATCH<br/> | A special property that returns an enumerator object that implements [**IEnumVARIANT**](ienumvariant.md). Required.<br/> |
| **Parent**<br/>      | VT\_DISPATCH<br/> | Returns the parent of the Documents collection object; read only. Required.<br/>                                          |



 

The Documents collection object should have all of the following methods.



| Method name          | Return type                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Add**<br/>   | VT\_DISPATCH<br/>              | Creates a new document and adds it to the collection. Returns the document that was created. Required.<br/>                                                                                                                                                                                                                                                                                                                                |
| **Close**<br/> | VT\_EMPTY<br/>                 | Closes all documents in the collection. Required.<br/>                                                                                                                                                                                                                                                                                                                                                                                     |
| **Item**<br/>  | VT\_DISPATCH or VT\_EMPTY<br/> | Returns a Document object from the collection or returns VT\_EMPTY if the document does not exist. Takes an optional argument, *index*, which may be a string (VT\_BSTR) indicating the document name, a number (VT\_I4) indicating the ordered position within the collection, or either (VT\_VARIANT). If *index* is omitted, returns the Document collection. The **Item** method is the default member (DISPID\_VALUE). Required.<br/> |
| **Open**<br/>  | VT\_DISPATCH or VT\_EMPTY<br/> | Opens an existing document and adds it to the collection. Returns the document that was opened, or VT\_EMPTY if the object could not be opened. Takes one required argument, *filename*, and one optional argument, *password*. Both arguments have the type VT\_BSTR. Required.<br/>                                                                                                                                                      |



 

 

 





