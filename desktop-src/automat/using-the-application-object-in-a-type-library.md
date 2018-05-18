---
title: Using the Application Object in a Type Library
description: Describes how to use the Application object in a type library.
ms.assetid: '85e2f481-51a0-4090-9b7d-115623eb2525'
---

# Using the Application Object in a Type Library

If you use a type library, the Application object should be the object that has the [appobject](appobject.md) attribute. Because some ActiveX clients use the type information to allow unqualified access to the Application object's members, it is important to avoid overloading the Application object with too many members.

The Application object should have the properties listed in the following table. The **Application**, **FullName**, **Name**, *Parent*, and **Visible** properties are required; other properties are optional.



| Property name       | Return type             | Description                                                                                                                                                                              |
|---------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ActiveDocument**  | VT\_DISPATCH, VT\_EMPTY | Returns the active document object or VT\_EMPTY if none; read only.                                                                                                                      |
| **Application**     | VT\_DISPATCH            | Returns the Application object; read only. Required.                                                                                                                                     |
| **Caption**         | VT\_BSTR                | Sets or returns the title of the application window; read/write. Setting the Caption to VT\_EMPTY returns control to the application.                                                    |
| **DefaultFilePath** | VT\_BSTR                | Sets or returns the default path specification used by the application for opening files; read/write.                                                                                    |
| **Documents**       | VT\_DISPATCH            | Returns a collection object for the open documents; read only.                                                                                                                           |
| **FullName**        | VT\_BSTR                | Returns the file specification for the application, including path; read only. For example, C:\\Drawdir\\Scribble. Required. (See Comments section below.)                               |
| **Height**          | VT\_R4                  | Sets or returns the distance between the top and bottom edge of the main application window; read/write.                                                                                 |
| **Interactive**     | VT\_BOOL                | Sets or returns True if the application accepts actions from the user, otherwise False; read/write.                                                                                      |
| **Left**            | VT\_R4                  | Sets or returns the distance between the left edge of the physical screen and the main application window; read/write.                                                                   |
| **Name**            | VT\_BSTR                | Returns the name of the application, such as "Microsoft Excel"; read only. The **Name** property is the default member (DISPID\_VALUE) for the Application object. Required.             |
| **Parent**          | VT\_DISPATCH            | Returns the Application object; read only. Required.                                                                                                                                     |
| **Path**            | VT\_BSTR                | Returns the path specification for the application's executable file; read only. For example, C:\\Drawdir if the .exe file is C:\\Drawdir\\Scribble.exe. (See Comments section below.)   |
| **StatusBar**       | VT\_BSTR                | Sets or returns the text displayed in the status bar; read/write.                                                                                                                        |
| **Top**             | VT\_R4                  | Sets or returns the distance between the top edge of the physical screen and main application window; read/write.                                                                        |
| **Visible**         | VT\_BOOL                | Sets or returns whether the application is visible to the user; read/write. The default is False when the application is started with the **/Automation** command-line switch. Required. |
| **Width**           | VT\_R4                  | Sets or returns the distance between the left and right edges of the main application window; read/write.                                                                                |



 

## Comments

Properties or methods that disclose information about local directory structures or file systems can leave your system vulnerable to attack. Security precautions, such as authenticating callers, can help reduce the risk of revealing sensitive information.

The Application object should have the following methods. The **Quit** method is required; other methods are optional.



| Method name | Return type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Help**    | VT\_EMPTY   | Displays online Help. May take three optional arguments: *helpfile* (VT\_BSTR), *helpcontextID* (VT\_I4), and *helpstring* (VT\_BSTR). The *helpfile* argument specifies the Help file to display; if omitted, the main Help file for the application is displayed. The *helpcontextID* and *helpstring* arguments specify a Help context to display; only one of them can be supplied. If both are omitted, the default Help topic is displayed. |
| **Quit**    | VT\_EMPTY   | Exits the application and closes all open documents. Required.                                                                                                                                                                                                                                                                                                                                                                                    |
| **Repeat**  | VT\_EMPTY   | Repeats the previous action in the user interface.                                                                                                                                                                                                                                                                                                                                                                                                |
| **Undo**    | VT\_EMPTY   | Reverses the previous action in the user interface.                                                                                                                                                                                                                                                                                                                                                                                               |



 

 

 




