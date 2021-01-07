---
description: Retrieves an object, that is either a class definition or an instance, based on the object path.
ms.assetid: 3071aeb2-adab-47aa-a10c-9796766bb630
ms.tgt_platform: multiple
title: SWbemServices.Get method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemServices.Get
- ISWbemServices.Get
- ISWbemServices.Get
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemServices.Get method

The **Get** method of the [**SWbemServices**](swbemservices.md) object retrieves an object, that is either a class definition or an instance, based on the object path. This method retrieves only objects from the namespace that is associated with the current **SWbemServices** object.

The method is called in the synchronous mode. For more information, see [Calling a Method](calling-a-method.md).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objWbemObject = .Get( _
  [ ByVal strObjectPath ], _
  [ ByVal iFlags ], _
  [ ByVal objWbemNamedValueSet ] _
)
```



## Parameters

<dl> <dt>

*strObjectPath* \[optional\]
</dt> <dd>

String that contains the object path of the object to retrieve. If this value is empty, the empty object that is returned can become a new class. For more information, see [Describing the Location of a WMI Object](describing-the-location-of-a-wmi-object.md).

</dd> <dt>

*iFlags* \[optional\]
</dt> <dd>

Integer that determines the behavior of the query. This parameter can accept the following values.

<dt>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>****wbemFlagUseAmendedQualifiers**** (131072 (0x20000))


</dt> <dd>

Causes WMI to return class amendment data with the base class definition. For more information about amended qualifiers, see [Localizing WMI Class Information](localizing-wmi-class-information.md).

</dd> </dl> </dd> <dt>

*objWbemNamedValueSet* \[optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that is servicing the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> </dl>

## Return value

If successful, this method returns an [**SWbemObject**](swbemobject.md) object that represents the requested object.

## Error codes

Upon the completion of the **Get** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

Current user does not have the permission to access the object.

</dd> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

A specified parameter is not valid.

</dd> <dt>

**wbemErrInvalidObjectPath** - 2147749946 (0x8004103A)
</dt> <dd>

Specified path was not valid.

</dd> <dt>

**wbemErrNotFound** - 2147749890 (0x80041002)
</dt> <dd>

Requested object could not be found.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> </dl>

## Remarks

Unlike the [**ExecQuery**](/windows/desktop/api/Provider/nf-provider-provider-execquery) and [**InstancesOf**](swbemservices-instancesof.md) methods, the Get method always returns an [**SWbemObject**](swbemobject.md) representing a specific instance of a WMI-managed resource. To obtain a specific instance of a WMI-managed resource using the Get method, you must tell Get the instance to retrieve by passing the method the object path, as shown in the following script.


```VB
strComputer = "."
Set objSWbemServices = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
Set objSWbemObject = objSWbemServices.Get("Win32_Service.Name='Messenger'")
Wscript.Echo "Name:         " & objSWbemObject.Name        & vbCrLf & _
             "Display Name: " & objSWbemObject.DisplayName & vbCrLf & _
             "Start Mode:   " & objSWbemObject.StartMode   & vbCrLf & _
             "State:        " & objSWbemObject.State
```



You can use this method to obtain [*singleton*](gloss-s.md) objects, such as [**\_\_CIMOMIdentification**](--cimomidentification.md), which contains version information about the WMI installation that is running.

You can examine the repository with a viewing tool such as [CIM Studio](further-information.md) to verify that the new class and instance appear. For an example of removing a class and instance from the repository, see [**SWbemServices.Delete**](swbemservices-delete.md) or [**SWbemObject.Delete\_**](swbemobject-delete-.md).

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

[**SWbemObject**](swbemobject.md)
</dt> </dl>

 

 




