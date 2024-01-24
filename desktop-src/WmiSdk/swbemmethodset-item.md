---
description: The Item method of the SWbemMethodSet object returns a named SWbemMethod object from the collection.
ms.assetid: 4c1bbecc-b38b-4869-9c8c-b9321536b23e
ms.tgt_platform: multiple
title: SWbemMethodSet.Item method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemMethodSet.Item
- ISWbemMethodSet.Item
- ISWbemMethodSet.Item
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemMethodSet.Item method

The **Item** method of the [**SWbemMethodSet**](swbemmethodset.md) object returns a named [**SWbemMethod**](swbemmethod.md) object from the collection.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objMethod = .Item( _
  ByVal strName, _
  [ ByVal iFlags ] _
)
```



## Parameters

<dl> <dt>

*strName* \[in\]
</dt> <dd>

Required. Name of the method to retrieve.

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Reserved. The default value is 0.

</dd> </dl>

## Return value

If successful, the requested [**SWbemMethod**](swbemmethod.md) object returns.

## Error codes

Upon completion of the **Item** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

The *iFlags* parameter was not valid.

</dd> <dt>

**wbemErrFailed** - 2147749894
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrNotFound** - 2147749890 (0x80041002)
</dt> <dd>

The specified method does not exist.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemMethodSet<br/>                                                        |
| IID<br/>                      | IID\_ISWbemMethodSet<br/>                                                         |



## See also

<dl> <dt>

[**SWbemMethodSet**](swbemmethodset.md)
</dt> <dt>

[**SWbemMethod**](swbemmethod.md)
</dt> </dl>

 

 




