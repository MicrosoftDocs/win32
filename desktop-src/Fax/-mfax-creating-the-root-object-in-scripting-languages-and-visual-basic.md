---
Description: The code examples provided here demonstrate how to create a root object in scripting languages and Microsoft Visual Basic.
ms.assetid: 9bbdfffa-cbea-49f1-863c-6fb0f982c914
title: Creating the Root Object in Scripting Languages and Visual Basic
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating the Root Object in Scripting Languages and Visual Basic

The code examples provided here demonstrate how to create a root object in scripting languages and Microsoft Visual Basic.

## VBScript

To create a root object in Microsoft Visual Basic Scripting Edition (VBScript), use the [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function.


```
Set objFaxServer = CreateObject("FaxComEx.FaxServer")
```



or, for the [**FaxDocument**](-mfax-faxdocument.md) object


```
Set objFaxDocument = CreateObject ("FaxComEx.FaxDocument")
```



## JScript

To create a root object in Microsoft JScript, use the [ActiveXObject Object](http://msdn.microsoft.com/library/en-us/jscript7/html/jsobjActiveXObject.asp) function.


```
objFaxServer = new ActiveXObject  ("FaxServer");
```



or, for the [**FaxDocument**](-mfax-faxdocument.md) object


```
objFaxDocument = new ActiveXObject  ("FaxDocument");
```



## Visual Basic

To create the root object in Visual Basic use the following:


```
Dim objFaxServer As New FAXCOMEXLib.FaxServer
```



or


```
Dim objFaxServer as FAXCOMEXLib.FaxServer
Set objFaxServer = New FAXCOMEXLib.FaxServer
```



For the [**FaxDocument**](-mfax-faxdocument.md) object


```
Dim objFaxDocument As New FAXCOMEXLib.FaxDocument
```



or


```
Dim objFaxDocument as FAXCOMEXLib.FaxDocument
Set objFaxDocument = New FAXCOMEXLib.FaxDocument
```



[**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) is also available to Visual Basic programmers and so, alternatively, the following can be used.


```
Dim objFaxServer As New FAXCOMEXLib.FaxServer
Set objFaxServer = CreateObject("FaxComEx.FaxServer")
```



or, for the [**FaxDocument**](-mfax-faxdocument.md) object


```
Dim objFaxServer As New FAXCOMEXLib.FaxServer
Set objFaxServer = CreateObject("FaxDocument")
```



If you want to make use of the fax events supplied in the [**IFaxServerNotify**](-mfax-ifaxservernotify.md) interface, use the following syntax.


```
Dim WithEvents objFaxServer As FAXCOMEXLib.FaxServer
Set objFaxServer = CreateObject("FaxComEx.FaxServer")
```



Creation of a root object is the first step in all fax service scripts. If you are using Visual Basic, you must have the **Microsoft Fax Service Extended COM Type Library** selected as a project reference to create this object. Select the library in the **Project References** menu of the Visual Basic editor.

 

 



