---
description: Creates an enumerator that returns the instances of a specified class according to the user-specified selection criteria.
ms.assetid: 6465a981-f98e-4ece-a9b6-9da8ae618bc6
ms.tgt_platform: multiple
title: SWbemServices.InstancesOf method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemServices.InstancesOf
- ISWbemServices.InstancesOf
- ISWbemServices.InstancesOf
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemServices.InstancesOf method

The **InstancesOf** method of the [**SWbemServices**](swbemservices.md) object creates an enumerator that returns the instances of a specified class according to the user-specified selection criteria. This method implements a simple query. More complex queries may require the use of [**SWbemServices.ExecQuery**](swbemservices-execquery.md).

The method is called in the semisynchronous mode. For more information, see [Calling a Method](calling-a-method.md).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objWbemObjectSet = .InstancesOf( _
  ByVal strClass, _
  [ ByVal iFlags ], _
  [ ByVal objWbemNamedValueSet ] _
)
```



## Parameters

<dl> <dt>

*strClass* 
</dt> <dd>

Required. String that contains the name of the class for which instances are desired. This parameter cannot be blank.

</dd> <dt>

*iFlags* \[optional\]
</dt> <dd>

This parameter determines how detailed the call enumerates and if this call returns immediately. The default value for this parameter is **wbemFlagReturnImmediately**. This parameter can accept the following values.

<dt>

<span id="wbemFlagForwardOnly"></span><span id="wbemflagforwardonly"></span><span id="WBEMFLAGFORWARDONLY"></span>

<span id="wbemFlagForwardOnly"></span><span id="wbemflagforwardonly"></span><span id="WBEMFLAGFORWARDONLY"></span>****wbemFlagForwardOnly**** (32 (0x20))


</dt> <dd>

Causes a forward-only enumerator to be returned. Forward-only enumerators are generally much faster and use less memory than conventional enumerators, but they do not allow calls to [**SWbemObject.Clone\_**](swbemobject-clone-.md).

</dd> <dt>

<span id="wbemFlagBidirectional"></span><span id="wbemflagbidirectional"></span><span id="WBEMFLAGBIDIRECTIONAL"></span>

<span id="wbemFlagBidirectional"></span><span id="wbemflagbidirectional"></span><span id="WBEMFLAGBIDIRECTIONAL"></span>****wbemFlagBidirectional**** (0 (0x0))


</dt> <dd>

Causes WMI to retain pointers to objects of the enumeration until the client releases the enumerator.

</dd> <dt>

<span id="wbemFlagReturnImmediately"></span><span id="wbemflagreturnimmediately"></span><span id="WBEMFLAGRETURNIMMEDIATELY"></span>

<span id="wbemFlagReturnImmediately"></span><span id="wbemflagreturnimmediately"></span><span id="WBEMFLAGRETURNIMMEDIATELY"></span>****wbemFlagReturnImmediately**** (16 (0x10))


</dt> <dd>

Default value for this parameter. This flag causes the call to return immediately.

</dd> <dt>

<span id="wbemFlagReturnWhenComplete"></span><span id="wbemflagreturnwhencomplete"></span><span id="WBEMFLAGRETURNWHENCOMPLETE"></span>

<span id="wbemFlagReturnWhenComplete"></span><span id="wbemflagreturnwhencomplete"></span><span id="WBEMFLAGRETURNWHENCOMPLETE"></span>****wbemFlagReturnWhenComplete**** (0 (0x0))


</dt> <dd>

Causes this call to block until the query has completed. This flag calls the method in the synchronous mode.

</dd> <dt>

<span id="wbemQueryFlagShallow"></span><span id="wbemqueryflagshallow"></span><span id="WBEMQUERYFLAGSHALLOW"></span>

<span id="wbemQueryFlagShallow"></span><span id="wbemqueryflagshallow"></span><span id="WBEMQUERYFLAGSHALLOW"></span>****wbemQueryFlagShallow**** (1 (0x1))


</dt> <dd>

Forces the enumeration to include only immediate subclasses of the specified parent class.

</dd> <dt>

<span id="wbemQueryFlagDeep"></span><span id="wbemqueryflagdeep"></span><span id="WBEMQUERYFLAGDEEP"></span>

<span id="wbemQueryFlagDeep"></span><span id="wbemqueryflagdeep"></span><span id="WBEMQUERYFLAGDEEP"></span>****wbemQueryFlagDeep**** (0 (0x0))


</dt> <dd>

Default value for this parameter. This value forces the enumeration to include all classes in the hierarchy.

</dd> <dt>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>****wbemFlagUseAmendedQualifiers**** (131072 (0x20000))


</dt> <dd>

Causes WMI to return class amendment data with the base class definition. For more information, see [Localizing WMI Class Information](localizing-wmi-class-information.md).

</dd> </dl> </dd> <dt>

*objWbemNamedValueSet* \[optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that is servicing the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> </dl>

## Return value

If successful, the method returns an [**SWbemObjectSet**](swbemobjectset.md).

## Error codes

Upon the completion of the **InstancesOf** method, the **Err** object may contain one of the error codes in the following list.

> [!Note]  
> A returned enumerator with zero elements is not an error.

 

<dl> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

Current user does not have the permission to view instances of the specified class.

</dd> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error occurred.

</dd> <dt>

**wbemErrInvalidClass** - 2147749904 (0x80041010)
</dt> <dd>

Specified class is not valid.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

A specified parameter is not valid.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> </dl>

## Remarks

The **InstancesOf** method only works for class objects.

By default, InstancesOf performs a deep retrieval. That is, InstancesOf retrieves all instances of the managed resource you identify and all instances of all the subclasses defined beneath the target class. For example, the following script retrieves all of the resources modeled by all of the dynamic classes defined beneath the CIM\_Service abstract class.


```VB
strComputer = "."
Set objSWbemServices = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
Set colSWbemObjectSet = objSWbemServices.InstancesOf("CIM_Service")
For Each objSWbemObject In colSWbemObjectSet
    Wscript.Echo "Object Path: " & objSWbemObject.Path_.Path
Next
```



If you run this script, you will get information back. However, this information will not be limited to the services installed on a computer. Instead, it will include information from all child classes of [**CIM\_Service**](/windows/desktop/CIMWin32Prov/cim-service), including [**Win32\_SystemDriver**](/windows/desktop/CIMWin32Prov/win32-systemdriver) and [**Win32\_ApplicationService**](/previous-versions/windows/desktop/legacy/aa394068(v=vs.85)).

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

[**SWbemObjectSet**](swbemobjectset.md)
</dt> </dl>

 

