---
description: WMI provides a variety of techniques to retrieve and manipulate WMI class and instance information, using Microsoft PowerShell, Visual&\#160;Basic Scripting Edition (VBScript) and C++.
ms.assetid: 682cbe12-1487-4681-8d2f-4caf21cb068a
ms.tgt_platform: multiple
title: Manipulating Class and Instance Information
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Manipulating Class and Instance Information

WMI provides a variety of techniques to retrieve and manipulate WMI class and instance information, using Microsoft PowerShell, Visual Basic Scripting Edition (VBScript) and C++.

The following table lists the topics that discuss the techniques to retrieve and manipulate WMI class and instance information.



| Topic                                                                                  | Description                                                                                                                                                                       |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Retrieving WMI Class or Instance Data](retrieving-class-or-instance-data.md)         | Retrieve and set data from and to the WMI information repository.                                                                                                                 |
| [Modifying an Instance Property](modifying-an-instance-property.md)                   | Change the information in the instance after it is retrieved.                                                                                                                     |
| [Changing the Inheritance of an Instance](changing-the-inheritance-of-an-instance.md) | Change the parent class of an instance.                                                                                                                                           |
| [Modifying a Method](modifying-a-method.md)                                           | Modify the parameters of an instance.                                                                                                                                             |
| [Enumerating WMI](enumerating-wmi.md)                                                 | Enumerate WMI objects.                                                                                                                                                            |
| [Querying WMI](querying-wmi.md)                                                       | Query WMI objects.                                                                                                                                                                |
| [Calling a Method](calling-a-method.md)                                               | Use associated methods created by Microsoft or other third-party developers to further manipulate WMI objects, or else directly affect the object that the WMI object represents. |
| [Accessing a Collection](accessing-a-collection.md)                                   | Enumerate collections in script.                                                                                                                                                  |



 

## Manipulating Data Using VBScript

You can use direct access to access the WMI properties of a WMI class or instance directly on an [**SWbemObject**](swbemobject.md), rather than through the property [collection](accessing-a-collection.md) of that object. You can also execute methods on that object in the native style of the programming language rather than using the [**SWbemServices.ExecMethod**](swbemservices-execmethod.md) call. For example, the [**Create**](/windows/desktop/CIMWin32Prov/create-method-in-class-win32-process) method in [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) had three parameters in Windows 2000 but has four parameters in Windows Server 2003.

Using direct access, you can treat WMI properties and methods as if they were automation properties and methods of [**SWbemObject**](swbemobject.md).

The following example shows how you can access a property.


```VB
VolumeName = MyDisk.Properties_("VolumeName")
```



The following example shows how you can access a property when you have direct access.


```VB
VolumeName = MyDisk.VolumeName
```



Chaining of objects is also acceptable.

The following example shows how to access a property of an object that is embedded in another object.


```VB
value = MyComputer.MyDisk.VolumeName
```



The following example shows how to access a property with array subscript notation.


```VB
valueOfElement = MyDisk.MyArrayProperty(3)
```



The following VBScript code example shows how to spawn an instance of the input parameters to the [**Create**](/windows/desktop/CIMWin32Prov/create-method-in-class-win32-process) method in the [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) class as an [**SWbemObject**](swbemobject.md), populate the input properties, and then execute the **Create** method using [**SWbemServices.ExecMethod**](swbemservices-execmethod.md).

The [**SWbemObject.Methods\_**](swbemobject-methods-.md) property returns an [**SWbemMethodSet**](swbemmethodset.md) collection of the [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) methods. The members of the method set are [**SWbemMethod**](swbemmethod.md) objects and [**SWbemMethod.InParameters**](swbemmethod-inparameters.md) returns the input parameters for the [**Create**](/windows/desktop/CIMWin32Prov/create-method-in-class-win32-process) method. The required *CommandLine* input parameter is set to "calc.exe". The method is then executed by [**SWbemServices.ExecMethod**](swbemservices-execmethod.md), resulting in the launch of a calc.exe process.


```VB
set Services = GetObject("winmgmts:root\cimv2")
Set obj = Services.Get("Win32_Process")
Set objIns = obj.Methods_("Create").InParameters.SpawnInstance_
objIns.CommandLine = "calc.exe"
Set objOut = Services.ExecMethod("Win32_Process", "Create", objIns)
MsgBox "Return value = " & objOut.returnvalue & VBCRLF & "Process ID = " & objOut.processid
```



The following code example shows how to perform the previous operation using direct access.


```VB
set Services = GetObject("winmgmts:root\cimv2")
Set Obj = Services.Get("Win32_Process")
returnvalue = Obj.create("calc.exe",,,processid)
MsgBox "Return value = " & returnvalue & VBCRLF & "Process ID = " & processid
```



For more information, see [Calling a Provider Method](calling-a-provider-method.md) and [Scripting with SWbemObject](scripting-with-swbemobject.md).

 

 
