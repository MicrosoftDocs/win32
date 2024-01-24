---
description: An SWbemMethodSet object is a collection of SWbemMethod objects. Items are retrieved using the Item method. For more information, see Accessing a Collection. This object cannot be created by the VBScript CreateObject call.
ms.assetid: 0ca2601f-ed40-472e-b4f2-eee750c8c8d1
ms.tgt_platform: multiple
title: SWbemMethodSet object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemMethodSet
- ISWbemMethodSet
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemMethodSet object

An **SWbemMethodSet** object is a collection of [**SWbemMethod**](swbemmethod.md) objects. Items are retrieved using the [**Item**](swbemmethodset-item.md) method. For more information, see [Accessing a Collection](accessing-a-collection.md). This object cannot be created by the VBScript **CreateObject** call.

> [!Note]  
> In this version of the API, write access to method information is not supported. If you want to define methods or modify existing method definitions, you can define the method changes in a MOF file and submit the changes using the MOF Compiler. Alternatively, use the WMI COM API.

 

## Members

The **SWbemMethodSet** object has these types of members:

-   [Methods](#swbemmethodset-object)
-   [Properties](#properties)

### Methods

The **SWbemMethodSet** object has these methods.



| Method                              | Description                                                                                                                                  |
|:------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| [**Item**](swbemmethodset-item.md) | Retrieves an [**SWbemMethod**](swbemmethod.md) object from the collection. This is the default automation method of this object.<br/> |



 

### Properties

The **SWbemMethodSet** object has these properties.



| Property                                         | Access type          | Description                                       |
|:-------------------------------------------------|:---------------------|:--------------------------------------------------|
| [**Count**](swbemmethodset-count.md)<br/> | Read-only<br/> | The number of items in the collection.<br/> |



 

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

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

 




