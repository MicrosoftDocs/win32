---
description: You can use the methods and properties of the SWbemObject object to represent one Windows Management Instrumentation (WMI) class definition or object instance.
ms.assetid: d303ec1a-5e0c-4a5e-8ed3-ed353a138755
ms.tgt_platform: multiple
title: SWbemObject object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObject
- ISWbemObject
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObject object

You can use the methods and properties of the **SWbemObject** object to represent one Windows Management Instrumentation (WMI) class definition or object instance. This object cannot be created by the VBScript [CreateObject](/previous-versions//xzysf6hc(v=vs.85)) call.

This object supports two types of properties and methods. Those defined in this section are generic properties and methods that apply to all WMI objects. In addition, this object exposes the properties and methods of the underlying object as dynamic automation properties and methods of **SWbemObject**. The names and types of these properties and methods depend on the underlying WMI object. For more information about how these dynamic properties and methods are exposed, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md).

From the WMI client perspective, this object is always in-process. Write operations only affect the local copy of the object, and read operations always retrieve values from the local copy. Updates to WMI are performed only when entire objects are written using a call to the [**SWbemObject.Put\_**](swbemobject-put-.md) method. If you modify the properties or methods in an **SWbemObject** object, your changes are not written to WMI until you call **SWbemObject.Put\_**.

The generic method and property names defined in this section always end with a trailing underscore ("\_") to differentiate them from the dynamic WMI methods and properties of the underlying object.

Note that **SWbemObject** cannot be created using the VBScript [**GetObject**](https://msdn.microsoft.com/library/e9waz863(v=VS.71).aspx).method. If you want to create a new, empty class use [**SWbemServices.Get**](swbemservices-get.md) with an empty path parameter. This call returns an empty **SWbemObject** object that can become a class. You can then supply a class name for the [**Class**](swbemobjectpath-class.md) property of the [**SWbemObjectPath**](swbemobjectpath.md) object returned by the [**Path\_**](swbemobject-path-.md) call. Add properties to the new class by the [**Properties\_**](swbemobject-properties-.md) method. To create an instance, call **GetObject** on the new class.

The following code example shows how to obtain a new class and add a property to it. The **SWbemObject** object that represents the class must be written back to the WMI repository by a call to [**Put\_**](swbemobject-put-.md).


```VB
wbemCimtypeString = 8
Set objSWbemService = GetObject("Winmgmts:root\default")
Set objClass = objSWbemService.Get()
objClass.Path_.Class = "NewClass"

' Add a property
' String property
objClass.Properties_.add "PropertyName", wbemCimtypeString  
' Make the property a key property 
objClass.Properties_("PropertyName").Qualifiers_.add "key", true

' Write the new class to the root\default namespace in the repository
Set objClassPath = objClass.Put_
WScript.Echo objClassPath.Path

'Create an instance of the new class using SWbemObject.SpawnInstance
Set objNewInst = GetObject( _
    "Winmgmts:root\default:NewClass").Spawninstance_

objNewInst.PropertyName = "My Instance"

' Write the instance into the repository
Set objInstancePath = objNewInst.Put_
WScript.Echo objInstancePath.Path

```



You can examine the repository with a viewing tool such as [CIM Studio](further-information.md) to verify that the new class and instance appear. For an example of removing a class and instance from the repository, see [**SWbemServices.Delete**](swbemservices-delete.md) or [**SWbemObject.Delete\_**](swbemobject-delete-.md).

## Members

The **SWbemObject** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SWbemObject** object has these methods.



| Method                                                        | Description                                                                                             |
|:--------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|
| [**Associators\_**](swbemobject-associators-.md)             | Retrieves the associators of the object.<br/>                                                     |
| [**AssociatorsAsync\_**](swbemobject-associatorsasync-.md)   | Asynchronously retrieves the associators of the object.<br/>                                      |
| [**Clone\_**](swbemobject-clone-.md)                         | Makes a copy of the current object.<br/>                                                          |
| [**CompareTo\_**](swbemobject-compareto-.md)                 | Tests two objects for equality.<br/>                                                              |
| [**Delete\_**](swbemobject-delete-.md)                       | Deletes the object from WMI.<br/>                                                                 |
| [**DeleteAsync\_**](swbemobject-deleteasync-.md)             | Asynchronously deletes the object from WMI.<br/>                                                  |
| [**ExecMethod\_**](swbemobject-execmethod-.md)               | Executes a method exported by a method provider.<br/>                                             |
| [**ExecMethodAsync\_**](swbemobject-execmethodasync-.md)     | Asynchronously executes a method exported by a method provider.<br/>                              |
| [**GetObjectText\_**](swbemobject-getobjecttext-.md)         | Retrieves the textual representation of the object (MOF syntax).<br/>                             |
| [**Instances\_**](swbemobject-instances-.md)                 | Returns a collection of instances of the object (which must be a WMI class).<br/>                 |
| [**InstancesAsync\_**](swbemobject-instancesasync-.md)       | Asynchronously returns a collection of instances of the object (which must be a WMI class).<br/>  |
| [**Put\_**](swbemobject-put-.md)                             | Creates or updates the object in WMI.<br/>                                                        |
| [**PutAsync\_**](swbemobject-putasync-.md)                   | Asynchronously creates or updates the object in WMI.<br/>                                         |
| [**References\_**](swbemobject-references-.md)               | Returns references to the object.<br/>                                                            |
| [**ReferencesAsync\_**](swbemobject-referencesasync-.md)     | Asynchronously returns references to the object.<br/>                                             |
| [**SpawnDerivedClass\_**](swbemobject-spawnderivedclass-.md) | Creates a new derived class from the current object (which must be a WMI class).<br/>             |
| [**SpawnInstance\_**](swbemobject-spawninstance-.md)         | Creates a new instance from the current object.<br/>                                              |
| [**Subclasses\_**](swbemobject-subclasses-.md)               | Returns a collection of subclasses of the object (which must be a WMI class).<br/>                |
| [**SubclassesAsync\_**](swbemobject-subclassesasync-.md)     | Asynchronously returns a collection of subclasses of the object (which must be a WMI class).<br/> |



 

### Properties

The **SWbemObject** object has these properties.



| Property                                                   | Access type          | Description                                                                                                                                |
|:-----------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| [**Derivation\_**](swbemobject-derivation-.md)<br/> | Read-only<br/> | Contains an array of strings that describes the derivation hierarchy for the class.<br/>                                             |
| [**Methods\_**](swbemobject-methods-.md)<br/>       | Read-only<br/> | An [**SWbemMethodSet**](swbemmethodset.md) object that is the collection of methods for this object.<br/>                           |
| [**Path\_**](swbemobject-path-.md)<br/>             | Read-only<br/> | Contains an [**SWbemObjectPath**](swbemobjectpath.md) object that represents the object path of the current class or instance.<br/> |
| [**Properties\_**](swbemobject-properties-.md)<br/> | Read-only<br/> | An [**SWbemPropertySet**](swbempropertyset.md) object that is the collection of properties for this object.<br/>                    |
| [**Qualifiers\_**](swbemobject-qualifiers-.md)<br/> | Read-only<br/> | An [**SWbemQualifierSet**](swbemqualifierset.md) object that is the collection of qualifiers for this object.<br/>                  |
| [**Security\_**](swbemobject-security-.md)<br/>     | Read-only<br/> | Contains an [**SWbemSecurity**](swbemsecurity.md) object used to read or change the security settings.<br/>                         |



 

## Examples

The [List All the Properties and Methods for a WMI Class](https://Gallery.TechNet.Microsoft.Com/f0666124-3b67-4254-8ff1-3b75ae15776d) VBScript code sample on TechNet Gallery uses the SWbemObject to list all of the methods and properties for a specified WMI class.

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

[**SWbemObjectEx**](swbemobjectex.md)
</dt> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

