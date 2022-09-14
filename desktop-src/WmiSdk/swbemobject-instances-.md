---
description: The Instances\_ method of the SWbemObject object creates an enumerator that returns the instances of the current class object. This method implements a simple query. More complex queries may require the use of SWbemServices.ExecQuery.
ms.assetid: 30402d7d-f7cb-43b5-96b5-a8a76144e32d
ms.tgt_platform: multiple
title: SWbemObject.Instances_ method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObject.Instances_
- ISWbemObject.Instances_
- ISWbemObject.Instances_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObject.Instances\_ method

The **Instances\_** method of the [**SWbemObject**](swbemobject.md) object creates an enumerator that returns the instances of the current class object. This method implements a simple query. More complex queries may require the use of [**SWbemServices.ExecQuery**](swbemservices-execquery.md).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objWbemObjectSet = .Instances_( _
  [ ByVal iFlags ], _
  [ ByVal objwbemNamedValueSet ] _
)
```



## Parameters

<dl> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Integer that determines the behavior of the call. This parameter can accept the following values.

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

<span id="wbemFlagReturnWhenComplete"></span><span id="wbemflagreturnwhencomplete"></span><span id="WBEMFLAGRETURNWHENCOMPLETE"></span>****wbemFlagReturnWhenComplete**** ( 0 (0x0))


</dt> <dd>

Causes this call to block until the query has completed.

</dd> <dt>

<span id="wbemQueryFlagShallow"></span><span id="wbemqueryflagshallow"></span><span id="WBEMQUERYFLAGSHALLOW"></span>

<span id="wbemQueryFlagShallow"></span><span id="wbemqueryflagshallow"></span><span id="WBEMQUERYFLAGSHALLOW"></span>****wbemQueryFlagShallow**** (1 (0x1))


</dt> <dd>

Forces the enumeration to include only immediate subclasses of the specified parent class.

</dd> <dt>

<span id="wbemQueryFlagDeep"></span><span id="wbemqueryflagdeep"></span><span id="WBEMQUERYFLAGDEEP"></span>

<span id="wbemQueryFlagDeep"></span><span id="wbemqueryflagdeep"></span><span id="WBEMQUERYFLAGDEEP"></span>****wbemQueryFlagDeep**** (0 (0x0))


</dt> <dd>

Default for this parameter. This value forces the enumeration to include all classes in the hierarchy.

</dd> <dt>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>****wbemFlagUseAmendedQualifiers**** (131072 (0x20000))


</dt> <dd>

Causes WMI to return class amendment data with the base class definition.

</dd> </dl> </dd> <dt>

*objwbemNamedValueSet* \[in, optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that is servicing the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> </dl>

## Return value

If the method is successful, an [**SWbemObjectSet**](swbemobjectset.md) object returns.

## Error codes

After the completion of the **Instances\_** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

Current user does not have permission to view instances of the specified class.

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

The **Instances\_** method only works for class objects. It is not an error for the returned collection to have zero elements. The default behavior for this method is [*semisynchronous*](gloss-s.md) because of the default *IFlags* value **wbemFlagReturnImmediately**.

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

[**SWbemObjectSet**](swbemobjectset.md)
</dt> </dl>

 

 




