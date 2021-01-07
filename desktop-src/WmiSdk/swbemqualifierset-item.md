---
description: The Item method of the SWbemQualifierSet object returns a named SWbemQualifier object from the collection. This is the default method of this object.
ms.assetid: 5ed3a336-c06f-446d-85d4-243daddc82a5
ms.tgt_platform: multiple
title: SWbemQualifierSet.Item method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemQualifierSet.Item
- ISWbemQualifierSet.Item
- ISWbemQualifierSet.Item
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemQualifierSet.Item method

The **Item** method of the [**SWbemQualifierSet**](swbemqualifierset.md) object returns a named [**SWbemQualifier**](swbemqualifier.md) object from the collection. This is the default method of this object.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objQualifier = .Item( _
  ByVal strName, _
  [ ByVal iFlags ] _
)
```



## Parameters

<dl> <dt>

*strName* \[in\]
</dt> <dd>

Required. Name of the qualifier to retrieve.

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Reserved. The default value is 0 (zero).

</dd> </dl>

## Return value

If successful, the requested [**SWbemQualifier**](swbemqualifier.md) object is returned.

## Error codes

After completion of the **Item** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

The *iFlags* parameter was not valid.

</dd> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrNotFound** - 2147749890 (0x80041002)
</dt> <dd>

Specified qualifier does not exist.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemQualifierSet<br/>                                                     |
| IID<br/>                      | IID\_ISWbemQualifierSet<br/>                                                      |



## See also

<dl> <dt>

[**SWbemQualifierSet**](swbemqualifierset.md)
</dt> <dt>

[**SWbemQualifier**](swbemqualifier.md)
</dt> </dl>

 

 




