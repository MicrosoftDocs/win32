---
description: Returns a collection of all association classes or instances that refer to a specific source class or instance.
ms.assetid: 33425b1c-13f5-4c3d-8f8a-2922f3e95264
ms.tgt_platform: multiple
title: SWbemServices.ReferencesTo method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemServices.ReferencesTo
- ISWbemServices.ReferencesTo
- ISWbemServices.ReferencesTo
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemServices.ReferencesTo method

The **ReferencesTo** method of the [**SWbemServices**](swbemservices.md) object returns a collection of all association classes or instances that refer to a specific source class or instance. This method performs the same function that the [REFERENCES OF](references-of-statement.md) WQL query performs.

This method is called in the semisynchronous mode. For more information, see [Calling a Method](calling-a-method.md).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objWbemObjectSet = .ReferencesTo( _
  ByVal strObjectPath, _
  [ ByVal strResultClass ], _
  [ ByVal strRole ], _
  [ ByVal bClassesOnly ], _
  [ ByVal bSchemaOnly ], _
  [ ByVal strRequiredQualifier ], _
  [ ByVal iFlags ], _
  [ ByVal objWbemNamedValueSet ] _
)
```



## Parameters

<dl> <dt>

*strObjectPath* 
</dt> <dd>

Required. String that contains the object path of the source for this method. For more information, see [Describing the Location of a WMI Object](describing-the-location-of-a-wmi-object.md).

</dd> <dt>

*strResultClass* \[optional\]
</dt> <dd>

String that contains a class name. If specified, this parameter indicates that the returned association objects must belong to or be derived from the class that is specified in this parameter.

</dd> <dt>

*strRole* \[optional\]
</dt> <dd>

String that contains a property name. If specified, this parameter indicates that the returned association objects must be limited to those in which the source object plays a specific role. The role is defined by the name of a specified property (which must be a reference property) of an association.

</dd> <dt>

*bClassesOnly* \[optional\]
</dt> <dd>

Boolean value that indicates whether or not a list of class names should be returned rather than actual instances of the classes. These are the classes to which the association objects belong. The default value for this parameter is **FALSE**.

</dd> <dt>

*bSchemaOnly* \[optional\]
</dt> <dd>

Boolean value that indicates whether or not the query applies to the schema rather than the data. The default value for this parameter is **FALSE**. It can only be set to **TRUE** if the *strObjectPath* parameter specifies the object path of a class. When set to **TRUE**, the set of returned endpoints represents classes that are suitably associated with the source class in the schema.

</dd> <dt>

*strRequiredQualifier* \[optional\]
</dt> <dd>

String that contains a qualifier name. If specified, this parameter indicates that the returned association objects must include the specified qualifier.

</dd> <dt>

*iFlags* \[optional\]
</dt> <dd>

Integer that specifies additional flags to the operation. The default for this parameter is **wbemFlagReturnImmediately**, which directs the call to return immediately rather than wait until the query has completed. This parameter can accept the following values.

<dt>

<span id="wbemFlagForwardOnly"></span><span id="wbemflagforwardonly"></span><span id="WBEMFLAGFORWARDONLY"></span>

<span id="wbemFlagForwardOnly"></span><span id="wbemflagforwardonly"></span><span id="WBEMFLAGFORWARDONLY"></span>****wbemFlagForwardOnly**** (32 (0x20))


</dt> <dd>

Causes a forward-only enumerator to be returned. Forward-only enumerators are generally much faster and use less memory than conventional enumerators, but they do not allow calls to [**SWbemObject.Clone\_**](swbemobject-clone-.md).

</dd> <dt>

<span id="wbemFlagBidirectional"></span><span id="wbemflagbidirectional"></span><span id="WBEMFLAGBIDIRECTIONAL"></span>

<span id="wbemFlagBidirectional"></span><span id="wbemflagbidirectional"></span><span id="WBEMFLAGBIDIRECTIONAL"></span>****wbemFlagBidirectional**** (0 (0x0))


</dt> <dd>

Causes Windows Management Instrumentation (WMI) to retain pointers to objects of the enumeration until the client releases the enumerator.

</dd> <dt>

<span id="wbemFlagReturnImmediately"></span><span id="wbemflagreturnimmediately"></span><span id="WBEMFLAGRETURNIMMEDIATELY"></span>

<span id="wbemFlagReturnImmediately"></span><span id="wbemflagreturnimmediately"></span><span id="WBEMFLAGRETURNIMMEDIATELY"></span>****wbemFlagReturnImmediately**** (16 (0x10))


</dt> <dd>

Causes the call to return immediately.

</dd> <dt>

<span id="wbemFlagReturnWhenComplete"></span><span id="wbemflagreturnwhencomplete"></span><span id="WBEMFLAGRETURNWHENCOMPLETE"></span>

<span id="wbemFlagReturnWhenComplete"></span><span id="wbemflagreturnwhencomplete"></span><span id="WBEMFLAGRETURNWHENCOMPLETE"></span>****wbemFlagReturnWhenComplete**** (0 (0x0))


</dt> <dd>

Causes this call to block until the query has completed. This flag calls the method in the synchronous mode.

</dd> <dt>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>****wbemFlagUseAmendedQualifiers**** (131072 (0x20000))


</dt> <dd>

Causes WMI to return class amendment data along with the base class definition. For more information, see [Localizing WMI Class Information](localizing-wmi-class-information.md).

</dd> </dl> </dd> <dt>

*objWbemNamedValueSet* \[optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that is servicing the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> </dl>

## Return value

If the method is successful, the method returns an [**SWbemObjectSet**](swbemobjectset.md) object.

## Error codes

After the completion of the **ReferencesTo** method, the **Err** object may contain one of the error codes in the following list.

> [!Note]  
> A returned collection with zero elements is not an error.

 

<dl> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

Current user does not have the permission to view one or more of the classes returned by the call.

</dd> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

Invalid parameter was specified.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> <dt>

**wbemFlagUseAmendedQualifiers** - 131072 (0x20000)
</dt> <dd>

Causes WMI to return class amendment data with the base class definition.

</dd> </dl>

## Remarks

For more information about the REFERENCES OF associated WQL query, source instances, and association objects, see [ASSOCIATORS OF Statement](associators-of-statement.md).

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

[**SWbemObject.Associators\_**](swbemobject-associators-.md)
</dt> <dt>

[**SWbemObject.References\_**](swbemobject-references-.md)
</dt> <dt>

[**SWbemServices.AssociatorsOf**](swbemservices-associatorsof.md)
</dt> </dl>

 

 




