---
description: The SWbemProperty object represents a single WMI property of a managed object. This object cannot be created by the VBScript CreateObject call.
ms.assetid: 2ddcfffa-a7b4-4fd6-926d-411de27f6212
ms.tgt_platform: multiple
title: SWbemProperty object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemProperty
- ISWbemProperty
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemProperty object

The **SWbemProperty** object represents a single WMI property of a managed object. This object cannot be created by the VBScript [CreateObject](creating-an-object-using-vbscript.md) call.

## Members

The **SWbemProperty** object has these types of members:

-   [Properties](#properties)

### Properties

The **SWbemProperty** object has these properties.



| Property                                                     | Access type           | Description                                                                                                                   |
|:-------------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------------------------------------------|
| [**CIMType**](swbemproperty-cimtype.md)<br/>          | Read-only<br/>  | Type of this property.<br/>                                                                                             |
| [**IsArray**](swbemproperty-isarray.md)<br/>          | Read-only<br/>  | Boolean value that indicates if this property has an array type.<br/>                                                   |
| [**IsLocal**](swbemproperty-islocal.md)<br/>          | Read-only<br/>  | Boolean value that indicates if this property is local.<br/>                                                            |
| [**Name**](swbemproperty-name.md)<br/>                | Read-only<br/>  | Name of this WMI property.<br/>                                                                                         |
| [**Origin**](swbemproperty-origin.md)<br/>            | Read-only<br/>  | Contains the originating class of this property.<br/>                                                                   |
| [**Qualifiers\_**](swbemproperty-qualifiers-.md)<br/> | Read-only<br/>  | An [**SWbemQualifierSet**](swbemqualifierset.md) object, which is the collection of qualifiers for this property.<br/> |
| [**Value**](swbemproperty-value.md)<br/>              | Read/write<br/> | Actual value of this property. This is the default automation property of this object.<br/>                             |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemProperty<br/>                                                         |
| IID<br/>                      | IID\_ISWbemProperty<br/>                                                          |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

 




