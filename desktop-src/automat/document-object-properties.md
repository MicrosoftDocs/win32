---
title: Document Object Properties
description: If the application is document based, it should provide a Document object named Document.
ms.assetid: '328b5040-5230-4916-94d9-cd585ec42034'
---

# Document Object Properties

If the application is document based, it should provide a Document object named Document. Use a different name only if Document is inappropriate (for example, if the application uses highly technical or otherwise specialized terminology within its user interface).

The Document object should have the properties listed in the table that follows. The properties **Application**, **FullName**, **Name**, **Parent**, **Path**, and **Saved** are required; other properties are optional.



| Property name              | Return type             | Description                                                                                                                                                                                                                                                                                                                               |
|----------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Application**<br/> | VT\_DISPATCH<br/> | Returns the Application object; read only. Required.<br/>                                                                                                                                                                                                                                                                           |
| **Author**<br/>      | VT\_BSTR<br/>     | Sets or returns summary information about the document's author; read/write.<br/>                                                                                                                                                                                                                                                   |
| **Comments**<br/>    | VT\_BSTR<br/>     | Sets or returns summary information comments for the document; read/write.<br/>                                                                                                                                                                                                                                                     |
| **FullName**<br/>    | VT\_BSTR<br/>     | Returns the file specification of the document, including the path; read only. Required. (See Comments section below.)<br/>                                                                                                                                                                                                         |
| **Keywords**<br/>    | VT\_BSTR<br/>     | Sets or returns summary information keywords associated with the document; read/write.<br/>                                                                                                                                                                                                                                         |
| **Name**<br/>        | VT\_BSTR<br/>     | Returns the file name of the document, not including the file's path specification; read only.<br/>                                                                                                                                                                                                                                 |
| **Parent**<br/>      | VT\_DISPATCH<br/> | Returns the **Parent** property of the Document object; read only. Required.<br/>                                                                                                                                                                                                                                                   |
| **Path**<br/>        | VT\_BSTR<br/>     | Returns the path specification for the document, not including the file name or file name extension; read only. Required. (See Comments section below.)<br/>                                                                                                                                                                        |
| **ReadOnly**<br/>    | VT\_BOOL<br/>     | Returns True if the file is read only, otherwise False; read only.<br/>                                                                                                                                                                                                                                                             |
| **Saved**<br/>       | VT\_BOOL<br/>     | Returns True if the document has never been saved, but has not changed since it was created. Returns True if it has been saved and has not changed since last saved. Returns False if it has never been saved and has changed since it was created; or if it was saved, but has changed since last saved. Read only; required.<br/> |
| **Subject**<br/>     | VT\_BSTR<br/>     | Sets or returns summary information about the subject of the document; read/write.<br/>                                                                                                                                                                                                                                             |
| **Title**<br/>       | VT\_BSTR<br/>     | Sets or returns summary information about the title of the document; read/write.<br/>                                                                                                                                                                                                                                               |



 

## Comments

Properties or methods that disclose information about local directory structures or file systems can leave your system vulnerable to attack. Security precautions, such as authenticating callers, can help reduce the risk of revealing sensitive information.

The Document object should have the methods listed in the following table. The methods **Activate**, **Close**, **Print**, **Save**, and **SaveAs** are required; other methods are optional.



| Method name                  | Return type          | Description                                                                                                                                                                                                                                                                                          |
|------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Activate** <br/>     | VT\_EMPTY<br/> | Activates the first window associated with the document. Required.<br/>                                                                                                                                                                                                                        |
| **Close** <br/>        | VT\_EMPTY<br/> | Closes all windows associated with the document and removes the document from the Documents collection. Required. Takes two optional arguments, *saveChanges* (VT\_BOOL) and *filename* (VT\_BSTR). The *filename* argument specifies the name of the file in which to save the document.<br/> |
| **NewWindow**<br/>     | VT\_EMPTY<br/> | Creates a new window for the document.<br/>                                                                                                                                                                                                                                                    |
| **Print**<br/>         | VT\_EMPTY<br/> | Prints the document. Required. Takes three optional arguments: *from* (VT\_I2), *to* (VT\_I2), and *copies* (VT\_I2). The *from* and *to* arguments specify the page range to print. The *copies* argument specifies the number of copies to print.<br/>                                       |
| **PrintOut**<br/>      | VT\_EMPTY<br/> | Same as **Print** method, but provides an easier way to use the method in Visual Basic, because **Print** is a Visual Basic keyword.<br/>                                                                                                                                                      |
| **PrintPreview**<br/>  | VT\_EMPTY<br/> | Previews the pages and page breaks of the document. Equivalent to clicking **Print Preview** on the **File** menu.<br/>                                                                                                                                                                        |
| **RevertToSaved**<br/> | VT\_EMPTY<br/> | Reverts to the last saved copy of the document, and discards any changes.<br/>                                                                                                                                                                                                                 |
| **Save**<br/>          | VT\_EMPTY<br/> | Saves changes to the file specified in the document's **FullName** property. Required.<br/>                                                                                                                                                                                                    |
| **SaveAs**<br/>        | VT\_EMPTY<br/> | Saves changes to a file. Required. Takes one optional argument, *filename* (VT\_BSTR). The *filename* argument can include an optional path specification.<br/>                                                                                                                                |



 

 

 





