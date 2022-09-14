---
description: The Qualifiers\_ property of the SWbemObject object returns an SWbemQualifierSet object that is a collection of the qualifiers for the current class or instance. This property is read-only.
ms.assetid: 5ecae751-0d83-4ad6-9840-ef47f76b1ff6
ms.tgt_platform: multiple
title: SWbemObject.Qualifiers_ property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObject.Qualifiers_
- ISWbemObject.Qualifiers_
- ISWbemObject.get_Qualifiers_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObject.Qualifiers\_ property

The **Qualifiers\_** property of the [**SWbemObject**](swbemobject.md) object returns an [**SWbemQualifierSet**](swbemqualifierset.md) object that is a collection of the qualifiers for the current class or instance. This property is read-only.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read-only.

## Syntax


```VB
SWbemObject.Qualifiers_ As Object
```



## Property value

## Examples

The [List All the Qualifiers for a WMI Class](https://Gallery.TechNet.Microsoft.Com/fe7a7ae2-d9d9-4c0f-bbf5-c9c112e90983) VBScript code sample on TechNet Gallery uses the Qualifier\_ property to list the class qualifiers for a specified WMI class.

The [List All Abstract Classes in WMI](https://Gallery.TechNet.Microsoft.Com/2eb0a3ba-d825-432e-b011-7c6fe358707f) VBScript code sample on TechNet Gallery lists all WMI abstract classes defined in the root\\cimv2 namespace.

The [List All Dynamic Classes in WMI](https://Gallery.TechNet.Microsoft.Com/8352ca94-264c-43c7-9dda-258d65ac6c8c) VBScript code sample uses the Qualifier\_ property to list all WMI Dynamic classes (including Association classes) defined in the root\\cimv2 namespace.

The [Get-WritableWMIProperties.ps1](https://Gallery.TechNet.Microsoft.Com/816fb8b6-cdcf-4156-a9a3-a852ce1d2baa) PowerShell code sample on TechNet Gallery lists all writeable properties in the specified namespace.

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



 

 




