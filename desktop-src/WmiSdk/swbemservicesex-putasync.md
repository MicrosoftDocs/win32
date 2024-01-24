---
description: Saves an object asynchronously to a namespace. When successful, this method sends an OnCompleted event to the SWbemSink object that is specified as an input parameter.
ms.assetid: 27da0c60-6dae-482d-a9bf-1aab016d3ae8
ms.tgt_platform: multiple
title: SWbemServicesEx.PutAsync method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemServicesEx.PutAsync
- ISWbemServicesEx.PutAsync
- ISWbemServicesEx.PutAsync
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemServicesEx.PutAsync method

The **PutAsync** method of the [**SWbemServicesEx**](swbemservicesex.md) object saves an object asynchronously to a namespace. When successful, this method sends an [**OnCompleted**](swbemsink-oncompleted.md) event to the [**SWbemSink**](swbemsink.md) object that is specified as an input parameter.

This method is called in the asynchronous mode. For more information, see [Calling a Method](calling-a-method.md).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemServicesEx.PutAsync( _
  ByVal objWbemSink, _
  ByVal ojbWbemObject, _
  [ ByVal iFlags ], _
  [ ByVal objWbemNamedValueSet ], _
  [ ByVal objWbemAsyncContext ] _
)
```



## Parameters

<dl> <dt>

*objWbemSink* 
</dt> <dd>

Required. Object sink that receives the objects asynchronously. Create a [**SWbemSink**](swbemsink.md) object to receive the objects.

</dd> <dt>

*ojbWbemObject* 
</dt> <dd>

Required. The new object to be put in the namespace. This may be a newly created object or a modified object.

</dd> <dt>

*iFlags* \[optional\]
</dt> <dd>

This parameter determines whether the call creates or updates the object and whether the call returns immediately. This parameter can accept the following values.

<dt>

<span id="wbemChangeFlagUpdateCompatible"></span><span id="wbemchangeflagupdatecompatible"></span><span id="WBEMCHANGEFLAGUPDATECOMPATIBLE"></span>

<span id="wbemChangeFlagUpdateCompatible"></span><span id="wbemchangeflagupdatecompatible"></span><span id="WBEMCHANGEFLAGUPDATECOMPATIBLE"></span>**wbemChangeFlagUpdateCompatible** (0 (0x0))


</dt> <dd>

Allows a class to be updated when there are no derived classes and no instances for the class. It also allows updates in all cases when the change is only to unimportant qualifiers, for example, the **Description** qualifier. This is the default behavior for this call, and is used for compatibility with previous versions of WMI. If the class has instances, the update fails.

</dd> <dt>

<span id="wbemChangeFlagUpdateSafeMode"></span><span id="wbemchangeflagupdatesafemode"></span><span id="WBEMCHANGEFLAGUPDATESAFEMODE"></span>

<span id="wbemChangeFlagUpdateSafeMode"></span><span id="wbemchangeflagupdatesafemode"></span><span id="WBEMCHANGEFLAGUPDATESAFEMODE"></span>**wbemChangeFlagUpdateSafeMode** (32 (0x20))


</dt> <dd>

Allows updates of classes even when there are child classes and the change does not cause conflicts with the child classes. Use this flag when adding a new property to a base class that is not mentioned previously in any of the child classes. If the class has instances, the update fails.

</dd> <dt>

<span id="wbemChangeFlagUpdateForceMode"></span><span id="wbemchangeflagupdateforcemode"></span><span id="WBEMCHANGEFLAGUPDATEFORCEMODE"></span>

<span id="wbemChangeFlagUpdateForceMode"></span><span id="wbemchangeflagupdateforcemode"></span><span id="WBEMCHANGEFLAGUPDATEFORCEMODE"></span>**wbemChangeFlagUpdateForceMode** (64 (0x40))


</dt> <dd>

This flag forces updates of classes when conflicting child classes exist. For example, this flag forces an update when a class qualifier is defined in a child class, and the base class tries to add the same qualifier in conflict with the existing one. In the force mode, this conflict is resolved by deleting the conflicting qualifier in the child class. If the class has instances, the update fails.

The use of the force mode to update a static class causes the deletion of all instances of that class. A forced update on a provider class does not delete instances of the class.

</dd> <dt>

<span id="wbemChangeFlagCreateOrUpdate"></span><span id="wbemchangeflagcreateorupdate"></span><span id="WBEMCHANGEFLAGCREATEORUPDATE"></span>

<span id="wbemChangeFlagCreateOrUpdate"></span><span id="wbemchangeflagcreateorupdate"></span><span id="WBEMCHANGEFLAGCREATEORUPDATE"></span>**wbemChangeFlagCreateOrUpdate** (0 (0x0))


</dt> <dd>

Causes the class or instance to be created if it does not exist, or overwritten if it exists already.

</dd> <dt>

<span id="wbemChangeFlagCreateOnly"></span><span id="wbemchangeflagcreateonly"></span><span id="WBEMCHANGEFLAGCREATEONLY"></span>

<span id="wbemChangeFlagCreateOnly"></span><span id="wbemchangeflagcreateonly"></span><span id="WBEMCHANGEFLAGCREATEONLY"></span>**wbemChangeFlagCreateOnly** (2 (0x2))


</dt> <dd>

Used for creation only. The call fails if the class or instance already exists.

</dd> <dt>

<span id="wbemChangeFlagUpdateOnly"></span><span id="wbemchangeflagupdateonly"></span><span id="WBEMCHANGEFLAGUPDATEONLY"></span>

<span id="wbemChangeFlagUpdateOnly"></span><span id="wbemchangeflagupdateonly"></span><span id="WBEMCHANGEFLAGUPDATEONLY"></span>**wbemChangeFlagUpdateOnly** (1 (0x1))


</dt> <dd>

Causes this call to update. The class or instance must exist for the call to be successful.

</dd> <dt>

<span id="wbemFlagReturnImmediately"></span><span id="wbemflagreturnimmediately"></span><span id="WBEMFLAGRETURNIMMEDIATELY"></span>

<span id="wbemFlagReturnImmediately"></span><span id="wbemflagreturnimmediately"></span><span id="WBEMFLAGRETURNIMMEDIATELY"></span>**wbemFlagReturnImmediately** (16 (0x10))


</dt> <dd>

Causes the call to return immediately.

</dd> <dt>

<span id="wbemFlagReturnWhenComplete"></span><span id="wbemflagreturnwhencomplete"></span><span id="WBEMFLAGRETURNWHENCOMPLETE"></span>

<span id="wbemFlagReturnWhenComplete"></span><span id="wbemflagreturnwhencomplete"></span><span id="WBEMFLAGRETURNWHENCOMPLETE"></span>**wbemFlagReturnWhenComplete** (0 (0x0))


</dt> <dd>

Causes this call to block until the query is complete. This flag calls the method in the synchronous mode.

</dd> <dt>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>**wbemFlagUseAmendedQualifiers** (131072 (0x20000))


</dt> <dd>

Causes WMI to write class amendment data and the base class definition. For more information, see [Localizing WMI Class Information](localizing-wmi-class-information.md).

</dd> </dl> </dd> <dt>

*objWbemNamedValueSet* \[optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that services the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> <dt>

*objWbemAsyncContext* \[optional\]
</dt> <dd>

An [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that returns to the object sink to identify the source of the original asynchronous call. Use this parameter to make multiple asynchronous calls using the same object sink. To use this parameter, create an **SWbemNamedValueSet** object and use the [**SWbemNamedValueSet.Add**](swbemnamedvalueset-add.md) method to add a value that identifies the asynchronous call you are making. This **SWbemNamedValueSet** object is returned to the object sink and the source of the call can be extracted using the [**SWbemNamedValueSet.Item**](swbemnamedvalueset-item.md) method. For more information, see [Calling a Method](calling-a-method.md).

</dd> </dl>

## Return value

This method does not return a value. If the call is successful, the [**OnObjectPut**](swbemsink-onobjectput.md) event of the supplied object sink receives an [**SWbemObjectPath**](swbemobjectpath.md) object, which contains the object path of the instance or class that is successfully committed to WMI.

## Error codes

After the completion of the **PutAsync** method, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

Current user does not have the permission to update an instance of the specified class.

</dd> <dt>

**wbemErrAlreadyExists** - 2147749913 (0x80041019)
</dt> <dd>

The **wbemChangeFlagCreateOnly** flag was specified, but the instance already exists.

</dd> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrIllegalNull** - 2147749898 (0x8004100A)
</dt> <dd>

A value of Null was specified for a property that cannot be Null. An example of such a property is one marked by a **Key**, **Indexed**, or **Not\_Null** qualifier.

</dd> <dt>

**wbemErrInvalidObject** - 2147749908 (0x80041014)
</dt> <dd>

The specified instance is not valid.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

A specified parameter is not valid.

</dd> <dt>

**wbemErrNotFound** - 2147749890 (0x80041002)
</dt> <dd>

The **wbemChangeFlagUpdateOnly** flag was specified, but the instance or class does not exist.

</dd> <dt>

**wbemErrIncompleteClass** - 2147749920 (0x80041020)
</dt> <dd>

Required properties for classes have not all been set.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> </dl>

## Remarks

This call returns immediately, and the results and status are returned to the caller through events delivered to the sink that is specified in *objWbemSink*. To handle each object when it arrives, create an *objWbemSink*.[**OnObjectReady**](swbemsink-onobjectready.md) event subroutine. Any processing done after all the objects arrive is done in a subroutine for the *objWbemSink*.[**OnCompleted**](swbemsink-oncompleted.md) event.

An asynchronous callback allows a non-authenticated user to provide data to the sink. This poses security risks to your scripts and applications. To eliminate the risks, see [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_ISWbemServicesEx<br/>                                                      |
| IID<br/>                      | IID\_ISWbemServicesEx<br/>                                                        |



 

