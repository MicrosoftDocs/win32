---
description: Use the SpawnDerivedClass\_ method of the SWbemObject object to create a derived class object from the current object. The object must be a class definition that becomes the parent class of the spawned object.
ms.assetid: 1b5aaea7-50f4-40bd-ab2a-f4ff55cc22fc
ms.tgt_platform: multiple
title: SWbemObject.SpawnDerivedClass_ method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObject.SpawnDerivedClass_
- ISWbemObject.SpawnDerivedClass_
- ISWbemObject.SpawnDerivedClass_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObject.SpawnDerivedClass\_ method

Use the **SpawnDerivedClass\_** method of the [**SWbemObject**](swbemobject.md) object to create a derived class object from the current object. The object must be a class definition that becomes the parent class of the spawned object.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objNewClass = .SpawnDerivedClass_( _
  [ ByVal iFlags ] _
)
```



## Parameters

<dl> <dt>

*iFlags* \[optional\]
</dt> <dd>

Reserved and must be 0 (zero) if specified.

</dd> </dl>

## Return value

If the call is successful, the [**SWbemObject**](swbemobject.md) object contains the new class definition object. No object returns when there is an error.

## Error codes

After the completion of the **SpawnDerivedClass\_** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrIllegalOperation** - 2147749918 (0x8004101E)
</dt> <dd>

User requested an illegal operation, such as spawning a class from an instance.

</dd> <dt>

**wbemErrIncompleteClass** - 2147749920 (0x80041020)
</dt> <dd>

Source class was not completely defined or registered with WMI, so a new derived class is not permitted.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> </dl>

## Remarks

The object that is returned automatically becomes a subclass of the current object. This behavior cannot be overridden. There is no other method by which you can create derived classes.

You cannot create a derived class from a class that is local to your own client process. Before use this method to create a derived class, you must create the base class. To create the base class, call [**SWbemObject.Put\_**](swbemobject-put-.md), and retrieve the base class using [**SWbemServices.Get**](swbemservices-get.md).

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



 

 




