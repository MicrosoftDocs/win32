---
description: Returns an SWbemObjectPath object that contains the path of the object to which the data was written.
ms.assetid: 1a9a718d-875d-4102-9d9d-3d10be162f58
ms.tgt_platform: multiple
title: SWbemServicesEx.Put method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemServicesEx.Put
- ISWbemServicesEx.Put
- ISWbemServicesEx.Put
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemServicesEx.Put method

The **Put** method of the [**SWbemServicesEx**](swbemservicesex.md) object saves the object to the namespace bound to the object and returns an [**SWbemObjectPath**](swbemobjectpath.md) object that contains the path of the object to which the data was written.

This method is called in the semisynchronous mode. For more information, see [Calling a Method](calling-a-method.md).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objObjectPath = .Put( _
  ByVal objWbemObject, _
  [ ByVal iFlags ], _
  [ ByVal objWbemNamedValueSet ] _
)
```



## Parameters

<dl> <dt>

*objWbemObject* 
</dt> <dd>

Required. The new object to be put in the namespace. This can be either a newly created object or a modified object.

</dd> <dt>

*iFlags* \[optional\]
</dt> <dd>

This parameter determines if the call creates or updates the object and if the call returns immediately. This parameter can accept the following values.

<dt>

<span id="wbemChangeFlagUpdateCompatible"></span><span id="wbemchangeflagupdatecompatible"></span><span id="WBEMCHANGEFLAGUPDATECOMPATIBLE"></span>

<span id="wbemChangeFlagUpdateCompatible"></span><span id="wbemchangeflagupdatecompatible"></span><span id="WBEMCHANGEFLAGUPDATECOMPATIBLE"></span>**wbemChangeFlagUpdateCompatible** (0 (0x0))


</dt> <dd>

Allows a class to be updated if there are no derived classes and there are no instances for that class. It also allows updates in all cases if the change is only to unimportant qualifiers (for example, the **Description** qualifier). This is the default behavior for this call and is used for compatibility with previous versions of WMI. If the class has instances, the update fails.

</dd> <dt>

<span id="wbemChangeFlagUpdateSafeMode"></span><span id="wbemchangeflagupdatesafemode"></span><span id="WBEMCHANGEFLAGUPDATESAFEMODE"></span>

<span id="wbemChangeFlagUpdateSafeMode"></span><span id="wbemchangeflagupdatesafemode"></span><span id="WBEMCHANGEFLAGUPDATESAFEMODE"></span>**wbemChangeFlagUpdateSafeMode** (32 (0x20))


</dt> <dd>

Allows updates of classes even if there are child classes, when the change does not cause any conflicts with child classes. You can use this flag when adding a new property to a base class that was not previously mentioned in any of the child classes. If the class has instances, the update fails.

</dd> <dt>

<span id="wbemChangeFlagUpdateForceMode"></span><span id="wbemchangeflagupdateforcemode"></span><span id="WBEMCHANGEFLAGUPDATEFORCEMODE"></span>

<span id="wbemChangeFlagUpdateForceMode"></span><span id="wbemchangeflagupdateforcemode"></span><span id="WBEMCHANGEFLAGUPDATEFORCEMODE"></span>**wbemChangeFlagUpdateForceMode** (64 (0x40))


</dt> <dd>

This flag forces updates of classes when conflicting child classes exist. For example, this flag forces an update if a class qualifier was defined in a child class, and the base class tries to add the same qualifier in conflict with the existing one. In the force mode, this conflict is resolved by deleting the conflicting qualifier in the child class. If the class has instances, the update fails.

The use of the force mode to update a static class causes the deletion of all instances of that class. A forced update on a provider class does not delete instances of the class.

</dd> <dt>

<span id="wbemChangeFlagCreateOrUpdate"></span><span id="wbemchangeflagcreateorupdate"></span><span id="WBEMCHANGEFLAGCREATEORUPDATE"></span>

<span id="wbemChangeFlagCreateOrUpdate"></span><span id="wbemchangeflagcreateorupdate"></span><span id="WBEMCHANGEFLAGCREATEORUPDATE"></span>**wbemChangeFlagCreateOrUpdate** (0 (0x0))


</dt> <dd>

Causes the class or instance to be created if it does not exist, or overwritten if it already exists.

</dd> <dt>

<span id="wbemChangeFlagCreateOnly"></span><span id="wbemchangeflagcreateonly"></span><span id="WBEMCHANGEFLAGCREATEONLY"></span>

<span id="wbemChangeFlagCreateOnly"></span><span id="wbemchangeflagcreateonly"></span><span id="WBEMCHANGEFLAGCREATEONLY"></span>**wbemChangeFlagCreateOnly** (2 (0x2))


</dt> <dd>

Used for creation only. The call fails if the class or instance already exists.

</dd> <dt>

<span id="wbemChangeFlagUpdateOnly"></span><span id="wbemchangeflagupdateonly"></span><span id="WBEMCHANGEFLAGUPDATEONLY"></span>

<span id="wbemChangeFlagUpdateOnly"></span><span id="wbemchangeflagupdateonly"></span><span id="WBEMCHANGEFLAGUPDATEONLY"></span>**wbemChangeFlagUpdateOnly** (1 (0x1))


</dt> <dd>

Causes this call to only do an update. The class or instance must exist for the call to be successful.

</dd> <dt>

<span id="wbemFlagReturnImmediately"></span><span id="wbemflagreturnimmediately"></span><span id="WBEMFLAGRETURNIMMEDIATELY"></span>

<span id="wbemFlagReturnImmediately"></span><span id="wbemflagreturnimmediately"></span><span id="WBEMFLAGRETURNIMMEDIATELY"></span>**wbemFlagReturnImmediately** (16 (0x10))


</dt> <dd>

Causes the call to return immediately.

</dd> <dt>

<span id="wbemFlagReturnWhenComplete"></span><span id="wbemflagreturnwhencomplete"></span><span id="WBEMFLAGRETURNWHENCOMPLETE"></span>

<span id="wbemFlagReturnWhenComplete"></span><span id="wbemflagreturnwhencomplete"></span><span id="WBEMFLAGRETURNWHENCOMPLETE"></span>**wbemFlagReturnWhenComplete** (0 (0x0))


</dt> <dd>

Causes this call to block until the operation has completed. This flag calls the method in the synchronous mode.

</dd> <dt>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>**wbemFlagUseAmendedQualifiers** (131072 (0x20000))


</dt> <dd>

Causes WMI to write class amendment data as well as the base class definition. For more information, see [Localizing WMI Class Information](localizing-wmi-class-information.md).

</dd> </dl> </dd> <dt>

*objWbemNamedValueSet* \[optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that services the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> </dl>

## Return value

If the call is successful, an [**SWbemObjectPath**](swbemobjectpath.md) object is returned. This object contains the object path of the instance or class that has been successfully committed to WMI.

## Error codes

After the completion of the **Put** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

Current user does not have the permission for the operation.

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

A value of **NULL** was specified for a property that cannot be **NULL**. An example of such a property is one marked by a [**Key**](standard-qualifiers.md), **Indexed**, or **Not\_Null** qualifier.

</dd> <dt>

**wbemErrInvalidObject** - 2147749908 (0x80041014)
</dt> <dd>

The specified object is not valid.

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



 

 




