---
description: The Item method of the SWbemObjectSet object gets an SWbemObject from the collection.
ms.assetid: da91683c-9895-4110-9f51-c340a0c52aec
ms.tgt_platform: multiple
title: SWbemObjectSet.Item method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObjectSet.Item
- ISWbemObjectSet.Item
- ISWbemObjectSet.Item
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObjectSet.Item method

The **Item** method of the [**SWbemObjectSet**](swbemobjectset.md) object gets an [**SWbemObject**](swbemobject.md) from the collection.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objWbemObject = .Item( _
  ByVal strObjectPath _
)
```



## Parameters

<dl> <dt>

*strObjectPath* 
</dt> <dd>

Required. Relative path of the object to retrieve from the collection. Example: Win32\_LogicalDisk="C:"

</dd> </dl>

## Return value

If successful, the requested [**SWbemObject**](swbemobject.md) object returns.

## Error codes

Upon completion of the **Item** method, the **Err** object may contain one of the error codes below.

<dl> <dt>

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

The **Item** method can require a lot of processor time because complete enumeration by the provider of the elements of the set is required to return the result.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemObjectSet<br/>                                                        |
| IID<br/>                      | IID\_ISWbemObjectSet<br/>                                                         |



 

 




