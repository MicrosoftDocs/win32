---
title: Using COM Objects in Windows Script Host
description: Microsoft Windows Script Host is a scripting utility you can use to run scripts within the base operating system.
ms.assetid: b13c1bdf-91ce-42a2-b66a-20d68952bb34
ms.topic: article
ms.date: 05/31/2018
---

# Using COM Objects in Windows Script Host

Microsoft Windows Script Host is a scripting utility you can use to run scripts within the base operating system. You can use Windows Script Host to automate common tasks and to create powerful macros and logon scripts. Windows Script Host comes with VBScript and JScript ActiveX scripting engines. Other software companies provide ActiveX scripting engines for languages such as PerlScript, PScript, Python, and others.

To use a COM object in a script run by Windows Script Host, you must first create an instance of the object. After a COM object has been created, you can then use it in scripts.

Windows Script Host consists of two applications. One runs scripts from the Windows desktop (`WScript.exe`); the other runs scripts from the command prompt (`CScript.exe`).

To run a script from the desktop, simply double-click a script file. Script files are text files. By convention, VBScript files have the extension `.vbs` and JScript files `.js`.

To run a script from the command prompt, run the `Cscript.exe` application with a command line such as the following:

```console
cscript "c:\\sample scripts\\chart.vbs"
```

where `c:\\sample scripts\\chart.vbs` is the path to the file containing the script.

You can print out a list of the parameters supported by Cscript.exe by entering the following command line:

```console
call cscript //?
```

To use a COM object in a script run by Windows Script Host, you must first create an instance of the object. In VBScript you can do this by calling the `CreateObject()` method. In JScript one can use either the `ActiveXObject` object or the `WScript.CreateObject()` method. The following example illustrates calling `CreateObject()` using VBScript:


```VB
Dim objXL
Set objXL = CreateObject("Excel.Application")
 
```



The following example illustrates creating an `ActiveXObject` object using JScript:


```JScript
var objXL = new ActiveXObject("Excel.Application");
 
```
Alternatively using `WScript.CreateObject()` method inside JScript:

```JScript
var objXL = WScript.CreateObject("Excel.Application");
```


After you have created an instance of the COM object, you can write script that uses the object, for example:


```VB
objXL.Visible = true;
 
```



In addition to the CreateObject method and ActiveXObject object, both VBScript and JScript provide the method GetObject, which returns an object instance.

## Related topics

<dl> <dt>

[Scripting with COM Objects](scripting-with-com-objects.md)
</dt> </dl>

 

 




