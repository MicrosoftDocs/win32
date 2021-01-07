---
description: An SWbemPropertySet object is a collection of SWbemProperty objects.
ms.assetid: 0edad17b-facc-4885-9ce4-561ca6f57a66
ms.tgt_platform: multiple
title: SWbemPropertySet object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemPropertySet
- ISWbemPropertySet
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemPropertySet object

An **SWbemPropertySet** object is a collection of [**SWbemProperty**](swbemproperty.md) objects. You can add items to the collection using the [**Add**](swbempropertyset-add.md) method, retrieve items from the collection using the [**Item**](swbempropertyset-item.md) method, and remove items from the collection using the [**Remove**](swbempropertyset-remove.md) method. For more information, see [Accessing a Collection](accessing-a-collection.md). This object cannot be created by the VBScript [CreateObject](creating-an-object-using-vbscript.md) call.

The [**SWbemProperty**](swbemproperty.md) objects that make up an **SWbemPropertySet** collection are used to describe the properties of a single WMI class or instance.

## Members

The **SWbemPropertySet** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SWbemPropertySet** object has these methods.



| Method                                    | Description                                                                                                                     |
|:------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](swbempropertyset-add.md)       | Adds an [**SWbemProperty**](swbemproperty.md) object to the **SWbemPropertySet** collection.<br/>                        |
| [**Item**](swbempropertyset-item.md)     | Gets a named [**SWbemProperty**](swbemproperty.md) from the collection. This is the default method for this object.<br/> |
| [**Remove**](swbempropertyset-remove.md) | Deletes an [**SWbemProperty**](swbemproperty.md) object from the collection.<br/>                                        |



 

### Properties

The **SWbemPropertySet** object has these properties.



| Property                                           | Access type          | Description                                                            |
|:---------------------------------------------------|:---------------------|:-----------------------------------------------------------------------|
| [**Count**](swbempropertyset-count.md)<br/> | Read-only<br/> | The number of items in the **SWbemPropertySet** collection.<br/> |



 

## Examples

The following VBScript sample demonstrates how [**SWbemPropertySet.Remove**](swbempropertyset-remove.md) can return **wbemErrResetToDefault** if the property is overridden.


```VB
on error resume next 

'Create a keyed class with a defaulted property
set service = GetObject("Winmgmts:")
set emptyclass = service.Get
emptyclass.path_.class = "REMOVETEST00"
set prop = emptyclass.properties_.add ("p", 19)

prop.qualifiers_.add "key", true
emptyclass.properties_.add ("q", 19).Value = 12

emptyclass.put_

'create an instance and override the property
set instance = service.get ("RemoveTest00").spawninstance_

instance.properties_("q").Value = 24
instance.properties_("p").Value = 1
instance.put_

'retrieve the instance and remove the property
set instance = service.get ("removetest00=1")
set property = instance.properties_ ("q")

WScript.echo "Overridden value of property is [24]:", property.value
WScript.echo ""

instance.properties_.remove "q"
set property = instance.properties_ ("q")
WScript.echo "Value of property after removal is [12]:", property.value
WScript.echo ""

if err <> 0 then
 WScript.Echo "0x" & Hex(Err.Number), Err.Description, Err.Source
end if
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemPropertySet<br/>                                                      |
| IID<br/>                      | IID\_ISWbemPropertySet<br/>                                                       |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

 




