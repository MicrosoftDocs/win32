---
description: SWbemServices.AssociatorsOf method - Returns a collection of objects (classes or instances) called endpoints that are associated with a specified object.
ms.assetid: a78e6701-6779-4a02-b811-23b2da4f4167
ms.tgt_platform: multiple
title: SWbemServices.AssociatorsOf method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemServices.AssociatorsOf
- ISWbemServices.AssociatorsOf
- ISWbemServices.AssociatorsOf
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemServices.AssociatorsOf method

The **AssociatorsOf** method of the [**SWbemServices**](swbemservices.md) object returns a collection of objects (classes or instances) called endpoints that are associated with a specified object. This method performs the same function that the ASSOCIATORS OF WQL query performs.

This method is called in the semisynchronous mode by default. For more information, see [Calling a Method](calling-a-method.md).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objWbemObjectSet = .AssociatorsOf( _
  ByVal strObjectPath, _
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

*strObjectPath* 
</dt> <dd>

Required. String that contains the object path of the source class or instance. For more information, see [Describing the Location of a WMI Object](describing-the-location-of-a-wmi-object.md).

</dd> <dt>

*strAssocClass* \[optional\]
</dt> <dd>

String that contains an association class. If specified, this parameter indicates that the returned endpoints must be associated with the source through the specified association class or a class that is derived from this association class.

</dd> <dt>

*strResultClass* \[optional\]
</dt> <dd>

String that contains a class name. If specified, this optional parameter indicates that the returned endpoints must belong to or be derived from the class specified in this parameter.

</dd> <dt>

*strResultRole* \[optional\]
</dt> <dd>

String that contains a property name. If specified, this parameter indicates that the returned endpoints must play a particular role in their association with the source object. The role is defined by the name of a specified property (which must be a reference property) of an association.

</dd> <dt>

*strRole* \[optional\]
</dt> <dd>

String that contains a property name. If specified, this parameter indicates that the returned endpoints must participate in an association with the source object in which the source object plays a particular role. The role is defined by the name of a specified property (which must be a reference property) of an association.

</dd> <dt>

*bClassesOnly* \[optional\]
</dt> <dd>

Boolean value that indicates whether a list of class names should be returned rather than actual instances of the classes. These are the classes to which the endpoint instances belong. The default value for this parameter is **FALSE**.

</dd> <dt>

*bSchemaOnly* \[optional\]
</dt> <dd>

Boolean value that indicates whether the query applies to the schema rather than the data. The default value for this parameter is **FALSE**. It can only be set to **TRUE** if the *strObjectPath* parameter specifies the object path of a class. When set to **TRUE**, the set of returned endpoints represent classes that are suitably associated with the source class in schema.

</dd> <dt>

*strRequiredAssocQualifier* \[optional\]
</dt> <dd>

String that contains a qualifier name. If specified, this parameter indicates that the returned endpoints must be associated with the source object through an association class that includes the specified qualifier.

</dd> <dt>

*strRequiredQualifier* \[optional\]
</dt> <dd>

String that contains a qualifier name. If specified, this parameter indicates that the returned endpoints must include the specified qualifier.

</dd> <dt>

*iFlags* \[optional\]
</dt> <dd>

Integer that specifies additional flags to the operation. The default value for this parameter is **wbemFlagReturnImmediately**, which calls the method in the semisynchronous mode. This parameter can accept the following values.

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

Causes this call to block until the query has completed. This flag calls the method in synchronous mode.

</dd> <dt>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>****wbemFlagUseAmendedQualifiers**** (131072 (0x20000))


</dt> <dd>

Causes WMI to return class amendment data along with the base class definition. For more information, see [Localizing WMI Class Information](localizing-wmi-class-information.md).

</dd> </dl> </dd> <dt>

*objwbemNamedValueSet* \[optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that is servicing the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> </dl>

## Return value

If the call is successful, an [**SWbemObjectSet**](swbemobjectset.md) object is returned.

## Error codes

After the completion of the **AssociatorsOf** method, the **Err** object may contain one of the error codes in the following list.

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

**wbemErrNotFound** - 2147749890 (0x80041002)
</dt> <dd>

Requested item was not found.

</dd> </dl>

## Remarks

The method retrieves the instances of managed resources that are associated with a specified resource through one or more association classes. You provide the object path for the originating endpoint, and AssociatorsOf returns the managed resources at the opposite endpoint. The AssociatorsOf method performs the same function that the ASSOCIATORS OF WQL query performs.

For more information about the ASSOCIATORS OF WQL query, source instances, and endpoints, see [ASSOCIATORS OF Statement](associators-of-statement.md).

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

[**SWbemObject.AssociatorsAsync\_**](swbemobject-associatorsasync-.md)
</dt> <dt>

[**SWbemServices.AssociatorsOfAsync**](swbemservices-associatorsofasync.md)
</dt> <dt>

[**SWbemObject.References\_**](swbemobject-references-.md)
</dt> <dt>

[**SWbemServices.ReferencesTo**](swbemservices-referencesto.md)
</dt> </dl>

 

 




