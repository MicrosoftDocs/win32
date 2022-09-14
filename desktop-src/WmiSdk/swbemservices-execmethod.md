---
description: SWbemServices.ExecMethod method - Executes a method that is exported by a method provider.
ms.assetid: 2637efdc-fde5-4a44-a41f-67e0fb0df19d
ms.tgt_platform: multiple
title: SWbemServices.ExecMethod method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemServices.ExecMethod
- ISWbemServices.ExecMethod
- ISWbemServices.ExecMethod
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemServices.ExecMethod method

The **ExecMethod** method of the [**SWbemServices**](swbemservices.md) object executes a method that is exported by a method provider. This method blocks while the method that is forwarded to the appropriate provider executes. The information and status are then returned. The provider, rather than WMI, implements the method.

This method is called in the synchronous mode. For more information, see [Calling a Method](calling-a-method.md).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objOutParams = .ExecMethod( _
  ByVal strObjectPath, _
  ByVal strMethodName, _
  [ ByVal objWbemInParams ], _
  [ ByVal iFlags ], _
  [ ByVal objWbemNamedValueSet ] _
)
```



## Parameters

<dl> <dt>

*strObjectPath* 
</dt> <dd>

Required. String that contains the object path of the object for which the method is executed. For more information, see [Describing the Location of a WMI Object](describing-the-location-of-a-wmi-object.md).

</dd> <dt>

*strMethodName* 
</dt> <dd>

Required. Name of the method for the object.

</dd> <dt>

*objWbemInParams* \[optional\]
</dt> <dd>

An [**SWbemObject**](swbemobject.md) object that contains the input parameters for the method being executed. By default, this parameter is undefined. For more information, see [Constructing InParameters Objects and Parsing OutParameters Objects](constructing-inparameters-objects-and-parsing-outparameters-objects.md).

</dd> <dt>

*iFlags* \[optional\]
</dt> <dd>

Reserved. This value must be zero.

</dd> <dt>

*objWbemNamedValueSet* \[optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that is servicing the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> </dl>

## Return value

If the method is successful, an [**SWbemObject**](swbemobject.md) object is returned. The returned object contains the out parameters and return value for the method that is being executed.

## Error codes

After the completion of the **ExecMethod** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidClass** - 2147749904 (0x80041010)
</dt> <dd>

Specified class was not valid.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

A specified parameter is not valid.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> <dt>

**wbemErrInvalidMethod** - 2147749934 (0x8004102E)
</dt> <dd>

Requested method was not available.

</dd> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

Current user was not authorized to execute the method.

</dd> </dl>

## Remarks

Use **SWbemServices.ExecMethod** as an alternative to direct access for executing a [*provider method*](gloss-p.md) in cases where it is not possible to execute a method directly. The **ExecMethod** method allows you to obtain output parameters, if the provider supplies them, with a scripting language that does not support output parameters. Otherwise, the recommended means of invoking a method is to use direct access. For more information, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md).

For example, the following code example that calls the [**StartService**](/windows/desktop/CIMWin32Prov/startservice-method-in-class-win32-service) provider method in [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service) uses direct access.


```VB
oService = GetObject("winmgmts:Win32_Service=Alerter")
iStatus = oService.StartService()
```



This example calls **SWbemServices.ExecMethod** to execute the [**StartService**](/windows/desktop/CIMWin32Prov/startservice-method-in-class-win32-service) method. Note that an object path is required because **SWbemServices.ExecMethod** is not operating on the object already, unlike [**SWbemObject.ExecMethod**](swbemobject-execmethod-.md).


```VB
Set WbemServices = GetObject("winmgmts:")
Set oService = GetObject("winmgmts:Win32_Service='Alerter'")
Set oPath = GetObject("winmgmts:Win32_Service='Alerter'").Path_
WbemServices.ExecMethod oPath, "StartService"
```



The **SWbemServices.ExecMethod** method requires an object path. If the script already holds an [**SWbemObject**](swbemobject.md) object, use the [**SWbemObject.ExecMethod**](swbemobject-execmethod-.md) method.

## Examples

The following example shows the **ExecMethod** method. The script creates a [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) object that represents a process that is running Notepad. It shows the setting up of an [**InParameters**](swbemmethod-inparameters.md) object and how to obtain results from an [**OutParameters**](swbemmethod-outparameters.md) object. For a script that shows the same operations performed asynchronously, see [**SWbemServices.ExecMethodAsync**](swbemservices-execmethodasync.md). For an example of using direct access, see [Create Method in Class Win32\_Process](/windows/desktop/CIMWin32Prov/create-method-in-class-win32-process). For an example of the same operation using an [**SWbemObject**](swbemobject.md), see [**SWbemObject.ExecMethod**](swbemobject-execmethod-.md).


```VB
' Connect to WMI
set Services = getobject("winmgmts:root\cimv2")

' Obtain the class definition object of a Win32_Process object.
Set oProcess = Services.Get("Win32_Process")

' Create the SWbemMethod.InParameters object
' to hold the input parameter needed
' for the Win32_Process.Create method call.
' The oProcess.Methods_("Create") call
' obtains obtains a class object that
' defines the correct input parameters
' for the Win32_Process.Create call.
' The InParameters object is an 
' SWbemObject object so SWbemObject.SpawnInstance_ 
'can be called to create it.

Set oInParams = _
    oProcess.Methods_("Create").InParameters.SpawnInstance_
oInParams.CommandLine = "Notepad.exe"

'Call SWbemServices.ExecMethod with the WMI path Win32_Process
Set oOutParams = _
    Services.ExecMethod( "Win32_Process", "Create", oInParams)

If oOutParams.ReturnValue = 0 Then
    wscript.echo "Create method executed successfully."
Else
' If the Create method failed to execute,
' an empty OutParameters object is returned. 
    If IsNull(oOutParams.ReturnValue) Then
        wscript.echo "Create method failed to execute."  
    Else
        wscript.echo "Create method executed" _
            & " but had error " _
            & "0x" & hex(oOutParams.ReturnValue)
    End If
End If
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemServices<br/>                                                         |
| IID<br/>                      | IID\_ISWbemServices<br/>                                                          |



## See also

<dl> <dt>

[**SWbemServices**](swbemservices.md)
</dt> <dt>

[**SWbemObject.ExecMethod\_**](swbemobject-execmethod-.md)
</dt> <dt>

[Calling a Provider Method](calling-a-provider-method.md)
</dt> <dt>

[Manipulating Class and Instance Information](manipulating-class-and-instance-information.md)
</dt> </dl>

 

