---
title: The Font Object
description: The standard font object supports a number of read-write properties as well as a set of methods through its IFont interface.
ms.assetid: d56c2f8a-498e-4b70-a0d8-ff562c00ed8e
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# The Font Object

The system provides a standard implementation of the font object. The standard font object supports a number of read-write properties as well as a set of methods through its [**IFont**](https://msdn.microsoft.com/library/windows/desktop/ms680673) interface. The standard font object implementation exposes an event interface, **IFontEventsDisp**.

The standard font object has the following properties:



| Property name                | Return type             | Description                                                                                                      |
|------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------|
| **Application**<br/>   | VT\_DISPATCH<br/> | Returns the Application object; read only.<br/>                                                            |
| **Bold**<br/>          | VT\_BOOL<br/>     | Sets or returns True if the font is bold, otherwise False; read/write.<br/>                                |
| **Charset**<br/>       | VT\_I2<br/>       | The character set used in the font, such as ANSI\_CHARSET, DEFAULT\_CHARSET, or SYMBOL\_CHARSET.<br/>      |
| **Italic** <br/>       | VT\_BOOL<br/>     | Sets or returns True if the font is italic; otherwise False, read/write.<br/>                              |
| **Name**<br/>          | VT\_BSTR<br/>     | Returns the name of the font; read only.<br/>                                                              |
| **Parent**<br/>        | VT\_DISPATCH<br/> | Returns the parent of the Font object; read only.<br/>                                                     |
| **Size**<br/>          | VT\_CY<br/>       | Sets or returns the point size of the font; read/write.<br/>                                               |
| **Strikethrough**<br/> | VT\_BOOL<br/>     | Sets or returns True if the font appears with a line running through it, otherwise False; read/write.<br/> |
| **Underline**<br/>     | VT\_BOOL<br/>     | Sets or returns True if the font is italic otherwise False, read/write. <br/>                              |
| **Weight**<br/>        | VT\_I2<br/>       | The boldness or weight of the font.<br/>                                                                   |



 

The standard font object implementation exposes a new event interface, **IFontEventsDisp**. This event contains **FontChanged**, which notifies the font object that its font resource has changed:



| Event name                                           | Description                                                                                                                                                                                                                                                                                                          |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **FontChanged**(*PropertyName* as String)<br/> | This event is contained in the **IFontEventsDisp** interface. The event is called whenever a property of the font object is changed. The *PropertyName* parameter will contain the English name of the property that has been changed in Visual Basic or the DISPID of the changed property in C and C++.<br/> |



 

For more information on font object properties, see [**IFont**](https://msdn.microsoft.com/library/windows/desktop/ms680673).

For more information on **IFontDisp**, see [**IFontDisp**](https://msdn.microsoft.com/library/windows/desktop/ms692695).

 

 





