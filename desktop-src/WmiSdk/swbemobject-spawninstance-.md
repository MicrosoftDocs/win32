---
description: Use the SpawnInstance\_ method of the SWbemObject object to create a new instance of a class.
ms.assetid: 4761bdb2-455a-48c4-9e22-bfba6a1036ec
ms.tgt_platform: multiple
title: SWbemObject.SpawnInstance_ method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObject.SpawnInstance_
- ISWbemObject.SpawnInstance_
- ISWbemObject.SpawnInstance_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObject.SpawnInstance\_ method

Use the **SpawnInstance\_** method of the [**SWbemObject**](swbemobject.md) object to create a new instance of a class. The current object must be a class definition obtained from WMI via a method such as [**SWbemServices.Get**](swbemservices-get.md) or [**SWbemServices.ExecQuery**](swbemservices-execquery.md). Then, use this class definition to create new instances. Create each new instance locally within the process, and then call [**SWbemObject.Put\_**](swbemobject-put-.md) to actually create the instance within WMI.

> [!Note]  
> Spawning an instance from an instance is supported, but the returned instance is empty.

 

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objNewInstance = .SpawnInstance_( _
  [ ByVal iFlags ] _
)
```



## Parameters

<dl> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Reserved and must be zero if specified.

</dd> </dl>

## Return value

If successful, this call returns an [**SWbemObject**](swbemobject.md) object that contains a new instance of the class.

## Error codes

After the completion of the **SpawnInstance\_** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrIncompleteClass** - 2147749920 (0x80041020)
</dt> <dd>

Current object is not a valid class definition, and it cannot spawn new instances. Either it is incomplete, or it has not been registered with WMI using [**SWbemObject.Put\_**](swbemobject-put-.md).

</dd> <dt>

**wbemErrIllegalOperation** - 2147749918 (0x8004101E)
</dt> <dd>

Returned if this method is used on an instance instead of a class.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

Invalid parameter was specified.

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
| CLSID<br/>                    | CLSID\_SWbemObject<br/>                                                           |
| IID<br/>                      | IID\_ISWbemObject<br/>                                                            |



## See also

<dl> <dt>

[**SWbemObject**](swbemobject.md)
</dt> <dt>

[**SWbemObject.Put\_**](swbemobject-put-.md)
</dt> <dt>

[**SWbemServices.Get**](swbemservices-get.md)
</dt> </dl>

 

 




