---
description: The Associators\_ method of the SWbemObject object returns a collection of objects (classes or instances) that are associated with the current object.
ms.assetid: 79f01853-c649-4cbe-b2fa-cff38fb4b733
ms.tgt_platform: multiple
title: SWbemObject.Associators_ method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObject.Associators_
- ISWbemObject.Associators_
- ISWbemObject.Associators_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObject.Associators\_ method

The **Associators\_** method of the [**SWbemObject**](swbemobject.md) object returns a collection of objects (classes or instances) that are associated with the current object. These returned objects are called endpoints. This method performs the same function that the ASSOCIATORS OF WQL query performs.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objWbemObjectSet = .Associators_( _
  [ ByVal strAssocClass ], _
  [ ByVal strResultClass ], _
  [ ByVal strResultRole ], _
  [ ByVal strRole ], _
  [ ByVal bClassesOnly ], _
  [ ByVal bSchemaOnly ], _
  [ ByVal strRequiredAssocQualifier ], _
  [ ByVal strRequiredQualifier ], _
  [ ByVal iFlags ], _
  [ ByVal objwbemNamedValueSet ] _
)
```



## Parameters

<dl> <dt>

*strAssocClass* \[in, optional\]
</dt> <dd>

String that contains an association class. If specified, this parameter indicates that the returned endpoints must be associated with the source through the specified association class or a class derived from this association class.

</dd> <dt>

*strResultClass* \[in, optional\]
</dt> <dd>

String that contains a class name. If specified, this parameter indicates that the returned endpoints must belong to or be derived from the class specified in this parameter.

</dd> <dt>

*strResultRole* \[in, optional\]
</dt> <dd>

String that contains a property name. If specified, this parameter indicates that the returned endpoints must play a particular role in their association with the source object. The role is defined by the name of a specified property (which must be a reference property) of an association.

</dd> <dt>

*strRole* \[in, optional\]
</dt> <dd>

String that contains a property name. If specified, this parameter indicates that the returned endpoints must participate in an association with the source object in which the source object plays a particular role. The role is defined by the name of a specified property (which must be a reference property) of an association.

</dd> <dt>

*bClassesOnly* \[in, optional\]
</dt> <dd>

Boolean value that indicates whether a list of class names should be returned rather than actual instances of the classes. These are the classes to which the endpoint instances belong. The default value for this parameter is **FALSE**.

</dd> <dt>

*bSchemaOnly* \[in, optional\]
</dt> <dd>

This is a Boolean value that indicates whether the query applies to the schema rather than the data. The default value for this parameter is **FALSE**. It can only be set to **TRUE** if the object on which this method is invoked is a class. When set to **TRUE**, the set of returned endpoints represent classes that are suitably associated with the source class in the schema.

</dd> <dt>

*strRequiredAssocQualifier* \[in, optional\]
</dt> <dd>

String that contains a qualifier name. This parameter, if specified, indicates that the returned endpoints must be associated with the source object through an association class that includes the specified qualifier.

</dd> <dt>

*strRequiredQualifier* \[in, optional\]
</dt> <dd>

String that contains a qualifier name. This parameter, if specified, indicates that the returned endpoints must include the specified qualifier.

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Integer specifying additional flags to the operation. The default for this parameter is **wbemFlagReturnImmediately**, which directs the call to return immediately rather than wait until the query has completed. This parameter can accept the following values.

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

Causes the call to return immediately.

</dd> <dt>

<span id="wbemFlagReturnWhenComplete"></span><span id="wbemflagreturnwhencomplete"></span><span id="WBEMFLAGRETURNWHENCOMPLETE"></span>

<span id="wbemFlagReturnWhenComplete"></span><span id="wbemflagreturnwhencomplete"></span><span id="WBEMFLAGRETURNWHENCOMPLETE"></span>****wbemFlagReturnWhenComplete**** (0 (0x0))


</dt> <dd>

Causes this call to block until the query has completed.

</dd> <dt>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>****wbemFlagUseAmendedQualifiers**** (131072 (0x20000))


</dt> <dd>

Causes WMI to return class amendment data with the base class definition. Including this flag makes the localized description qualifier text available for classes, properties and methods. For more information about amended qualifiers, see [Localizing WMI Class Information](localizing-wmi-class-information.md).

</dd> </dl> </dd> <dt>

*objwbemNamedValueSet* \[in, optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that is servicing the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> </dl>

## Return value

If the call is successful, an [**SWbemObjectSet**](swbemobjectset.md) object is returned.

## Error codes

After completion of the **Associators\_** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

The current user does not have permission to view one or more of the classes returned by the call.

</dd> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

A specified parameter is not valid.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894
</dt> <dd>

Not enough memory to complete the operation.

</dd> </dl>

## Remarks

For more information about the ASSOCIATORS OF associated WQL query, source instances, and endpoints, see [ASSOCIATORS OF Statement](associators-of-statement.md).

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

[**SWbemObject.References\_**](swbemobject-references-.md)
</dt> <dt>

[**SWbemServices.AssociatorsOf**](swbemservices-associatorsof.md)
</dt> <dt>

[**SWbemServices.ReferencesTo**](swbemservices-referencesto.md)
</dt> </dl>

 

 




