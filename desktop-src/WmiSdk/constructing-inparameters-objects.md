---
description: An InParameters object contains the parameter list for calling provider methods when using an ExecMethod type of call.
ms.assetid: 8cc65129-1698-4ada-b493-672772c94045
ms.tgt_platform: multiple
title: Constructing InParameters Objects
ms.topic: article
ms.date: 05/31/2018
---

# Constructing InParameters Objects

An [**InParameters**](swbemmethod-inparameters.md) object contains the parameter list for calling provider methods when using an **ExecMethod** type of call. The [**SWbemObject.ExecMethod\_**](swbemobject-execmethod-.md), [**SWbemObject.ExecMethodAsync\_**](swbemobject-execmethodasync-.md), [**SWbemServices.ExecMethod**](swbemservices-execmethod.md), and [**SWbemServices.ExecMethodAsync**](swbemservices-execmethodasync.md) methods all require an **InParameters** object.

The following procedure describes how to construct an [**InParameters**](swbemmethod-inparameters.md) object.

**To construct the *objwbemInParams* parameter**

1.  Connect to WMI.
2.  Obtain the definition of the WMI class that defines the method you want to execute.
3.  Obtain an [**InParameters**](swbemmethod-inparameters.md) object specific to the WMI class method you want to execute.

    ```VB
    Set objInParam = objShare.Methods_("Create"). _
        inParameters.SpawnInstance_()
    ```

    

4.  Set the properties of the instance to whatever values are appropriate. Be sure to give values to the key properties in the WMI class that contains the method you want to execute.

    For example, if you want to set an input parameter named myinputparam to the value "abc" in an instance of [**InParameters**](swbemmethod-inparameters.md) called "INST", the code would look like this.

    ```VB
    INST.Properties_.Add ("myinputparam").Value = "abc".
    ```

    

5.  Execute the method and obtain the return status of the method you are executing.

The following code example illustrates setting up the [**InParameters**](swbemmethod-inparameters.md) object to create a new WMI object that represents a share. For more information about the [**OutParameters**](swbemmethod-outparameters.md) object, see [Parsing OutParameters Objects](parsing-outparameters-objects.md). This example returns a successful return value (0) if there is a folder named "Share" at the location "C:/Share". This example enables this folder to be shared with other users.


```VB
' Connect to WMI.
Set objServices = GetObject("winmgmts:root\cimv2")

' Obtain the definition of the WMI class that defines
' the method you want to execute.
Set objShare = objServices.Get("Win32_Share")

' Obtain an InParameters object specific
' to the WMI class method you want to execute.
Set objInParam = objShare.Methods_("Create"). _
    inParameters.SpawnInstance_()

' Set the properties of the instance to whatever
' values are appropriate.
objInParam.Properties_.Item("Access") = objSecDescriptor
objInParam.Properties_.Item("Description") = _
    "New share created by WMI script"
objInParam.Properties_.Item("Name") = "share"
objInParam.Properties_.Item("Path") = "C:\share"
objInParam.Properties_.Item("Type") = 0
'optional - default is 'max allowed'
objInParam.Properties_.Item("MaximumAllowed") = 100
'optional - default is no password
objInParam.Properties_.Item("Password") = "Password"

' Execute the method and obtain the return status. 
' The OutParameters object in objOutParams
' is created by the provider. 
Set objOutParams = objShare.ExecMethod_("Create", objInParam)    
wscript.echo objOutParams.ReturnValue
```



 

 



