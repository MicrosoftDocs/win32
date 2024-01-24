---
description: The ExecMethod\_ method of the SWbemObject object executes a method exported by a method provider.
ms.assetid: 39a8a6e7-b499-410a-8c27-d4a05d1a61b9
ms.tgt_platform: multiple
title: SWbemObject.ExecMethod_ method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObject.ExecMethod_
- ISWbemObject.ExecMethod_
- ISWbemObject.ExecMethod_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObject.ExecMethod\_ method

The **ExecMethod\_** method of the [**SWbemObject**](swbemobject.md) object executes a method exported by a method provider.

This method pauses while the method that is forwarded to the appropriate provider executes. The information and status are then returned. The provider rather than WMI implements the method.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objOutParams = .ExecMethod_( _
  ByVal strMethodName, _
  [ ByVal objwbemInParams ], _
  [ ByVal iFlags ], _
  [ ByVal objwbemNamedValueSet ] _
)
```



## Parameters

<dl> <dt>

*strMethodName* \[in\]
</dt> <dd>

Required. Name of the method for the object.

</dd> <dt>

*objwbemInParams* \[in, optional\]
</dt> <dd>

This is an [**SWbemObject**](swbemobject.md) object that contains the input parameters for the method being executed. By default, this parameter is undefined. For more information, see [Constructing InParameters Objects and Parsing OutParameters Objects](constructing-inparameters-objects-and-parsing-outparameters-objects.md).

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Reserved and must be set to 0 (zero) if specified.

</dd> <dt>

*objwbemNamedValueSet* \[in, optional\]
</dt> <dd>

Typically, it is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that is servicing the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> </dl>

## Return value

If this method is successful, an [**SWbemObject**](swbemobject.md) object returns. The returned object contains the out parameters and return value for the method being executed.

## Error codes

After the completion of the **ExecMethod\_** method, the **Err** object may contain one of the error codes in the following list.

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

This method is similar to [**SWbemServices.ExecMethod**](swbemservices-execmethod.md), but it operates directly on the object whose method is to be executed. For example, the following code example calls the [**StartService**](/windows/desktop/CIMWin32Prov/startservice-method-in-class-win32-service) provider method in [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service) and uses [direct access](manipulating-class-and-instance-information.md).


```VB
oService = GetObject("winmgmts:Win32_Service=Alerter")
iStatus = oService.StartService()
```



This version calls **SWbemObject.ExecMethod\_** to execute the [**StartService**](/windows/desktop/CIMWin32Prov/startservice-method-in-class-win32-service) method.


```VB
oService = GetObject("winmgmts:Win32_Service=Alerter")
Set outParam = process.ExecMethod_("StartService")
```



Use **SWbemObject.ExecMethod\_** as an alternative to direct access for executing a [*provider method*](gloss-p.md) in cases where it is not possible to execute a method directly. For example, you would use **SWbemObject.ExecMethod\_** with a scripting language that does not support output parameters if your method has out parameters. Otherwise, the recommended means of invoking a method is to use direct access.

-   The **SWbemObject.ExecMethod\_** method assumes the object represented by [**SWbemObject**](swbemobject.md) contains the method to execute. By contrast, [**SWbemServices.ExecMethod**](swbemservices-execmethod.md) requires an object path. Use **SWbemObject.ExecMethod\_** if you already have obtained the object whose method you want to execute.

## Examples

The following example shows the [**ExecMethod**](swbemservices-execmethod.md) method.The script creates a [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) object representing a process running Notepad. For more information about a script illustrating the same operations performed asynchronously, see [**SWbemObject.ExecMethodAsync\_**](swbemobject-execmethodasync-.md). For an example using direct access, see [**Create Method in Class Win32\_Process**](/windows/desktop/CIMWin32Prov/create-method-in-class-win32-process) . For an example of the same operation using an [**SWbemServices**](swbemservices.md) object, see **SWbemServices.ExecMethod**.


```VB
' Connect to WMI and obtain a Win32_Process object.
' This is also an SWbemObject object.
Set oProcess = GetObject("winmgmts:Win32_Process")

' Create the SWbemMethod.InParameters
' object to hold the input parameter needed
' for the Win32_Process.Create method call.
' The oProcess.Methods_("Create") call
' obtains a class object that defines
' the correct input parameters
' for the Win32_Process.Create call.
' The InParameters object is an 
' SWbemObject object so SWbemObject.SpawnInstance_
' can be called to create it.
Set oInParams = oProcess.Methods_("Create"). _
    InParameters.SpawnInstance_

' Specify the name of the process to be run.
oInParams.CommandLine = "Notepad.exe"
Set oOutParams = oProcess.ExecMethod_("Create", oInParams)

If oOutParams.ReturnValue = 0 Then
    wscript.echo "Create method executed successfully"
Else
' If the Create method failed to execute,
' an empty OutParameters object is returned. 
    If IsNull(oOutParams.ReturnValue) Then
        wscript.echo "Create method failed to execute."  
    Else
        wscript.echo "Create method executed but had error" _
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
| CLSID<br/>                    | CLSID\_SWbemObject<br/>                                                           |
| IID<br/>                      | IID\_ISWbemObject<br/>                                                            |



## See also

<dl> <dt>

[**SWbemObject**](swbemobject.md)
</dt> <dt>

[**SWbemObject.ExecMethodAsync\_**](swbemobject-execmethodasync-.md)
</dt> <dt>

[**SWbemServices.ExecMethod**](swbemservices-execmethod.md)
</dt> </dl>

 

