---
title: Getting Started with ASP for ADSI
description: ADSI can be used to access directory data using an ASP page. This can be a convenient way to run administration tasks and queries from a webpage or provide information to employees on an intranet.
ms.assetid: 2007257c-6c4e-415e-9ab5-e65d8d9e5dd4
ms.tgt_platform: multiple
keywords:
- ASP ADSI
- ADSI, ASP Pages
- ADSI, ASP Pages, ASP Code Example
ms.topic: article
ms.date: 05/31/2018
---

# Getting Started with ASP for ADSI

ADSI can be used to access directory data using an ASP page. This can be a convenient way to run administration tasks and queries from a webpage or provide information to employees on an intranet.

One advantage of using ADSI with ASP is that you can create a richer user experience because you can use Visual Basic to create an ADSI application and offer it to a user through a standard webpage. For example, you could create a webpage that enables employees to enter the last name of an employee and get back a phone number for that employee, or create a form that allows employees to update personal information in a company human resources database.

ASP code starts with '<%' and ends with '%>'. You can add ADSI code as VBScript or Visual Basic.

To create an ASP page, you can use a webpage editor, Notepad or other text editor, or the Microsoft Visual Studio .NET development system.

Before you run your ASP page, set up your application or IIS server according to the instructions found in [Authentication Issues for ADSI with ASP](authentication-issues-for-adsi-with-asp.md).

## A Simple ASP Sample: Enumerating Objects in a Container

Using a webpage editor, create a new html page which accepts the distinguished name of a container object. Enter the following code example.


```HTML
<html>
<body>

<form method="POST" action="https://localhost/Enum.asp" ID="Form1">
<p>Distinguished name of container:<input type="text" name="inpContainer" size="100" ID="Text2"></p>
<p><input type="SUBMIT" value="GO" ID="Submit1" NAME="Submit1"></p>
</form>

</body>
</html>
```



This page can now accept a container name that is passed to it and use ADSI to enumerate objects in the container.

Create a new ASP page called Enum.asp and enter the following code example. Save this page at the root of the local web server.


```VB
<%@ Language=VBScript %>
<%
' Get the inputs.
containerName = Request.Form("inpContainer")
' Validate compName before using.

If Not ("" = containerName) Then
  ' Bind to the object.
  adsPath = "LDAP://" & containerName
  Set comp = GetObject(adsPath)

  ' Write the ADsPath of each of the child objects.
  Response.Write("<p>Enumeration:</p>")
  For Each obj in comp
    Response.Write(obj.ADsPath + "<BR>")
  Next
End If
%>
```



 

 




