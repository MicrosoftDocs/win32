---
description: If you attempt to remove more than one item in a collection, you may find that some items are not removed.
ms.assetid: 7c82321e-059f-497c-8561-33c3e9306d41
ms.tgt_platform: multiple
title: Removing Multiple Items from a WMI Collection
ms.topic: article
ms.date: 05/31/2018
---

# Removing Multiple Items from a WMI Collection

If you attempt to remove more than one item in a collection, you may find that some items are not removed. You cannot iterate a collection while removing items, because when you remove an element from a collection, the collection pointer is moved on to the next element. For example, an attempt to remove all of the items from a collection results in the removal of every other item. You may see this problem when you are removing items with the [**SWbemQualifierSet.Remove**](swbemqualifierset-remove.md) or [**SWbemPropertySet.Remove**](swbempropertyset-remove.md) methods. You can avoid this problem by looping through the collection and putting the names of the items to remove in an array. You then can loop through the array and delete the items named in the array. The collections, such as [**SWbemNamedValueSet**](swbemnamedvalueset.md), [**SWbemPrivilegeSet**](swbemprivilegeset.md), and [**SWbemRefresher**](swbemrefresher.md), also have a method that deletes all items in the refresher container.

The following script illustrates how to remove several items from a collection.


```VB
Const WBEM_CIMTYPE_STRING = 8    ' Value for string data type
Dim names()
Redim names (0)
set objSWbemService = GetObject("winmgmts:root\default")
set objClass = ObjSWbemService.Get()

Wscript.Echo "Creating class NewClass"
objClass.Path_.Class = "NewClass"
For i = 1 to 5
    objClass.Properties_.Add "Prop" & i, WBEM_CIMTYPE_STRING
Next
objClass.Put_
Getprops()

' Get all the property names in an array
For Each oprop in objClass.properties_
    Redim Preserve names(Ubound(names)+1)
    names(Ubound(names)-1) = oprop.name
Next
Wscript.Echo "Remove first 3 properties using array of names:"

For i = Lbound(names) to Ubound(names)-1
    If (i < 3) Then
       Wscript.Echo "Removing " & names(i)
       objClass.Properties_.Remove names(i)
    End If
Next

objClass.Put_
Wscript.Echo "Result:"
Getprops()

Sub Getprops()
    Wscript.Echo "Number of properties = " _
        & objClass.Properties_.Count
    For Each oprop in objClass.Properties_
        Wscript.Echo oprop.name
    Next
End Sub
```



You cannot remove properties and qualifiers in a class instance or derived class that has inherited properties. Such a deletion attempt raises an error and the property or qualifier is not removed; instead, WMI resets the property or qualifier to the default value. In the case of a derived class with inherited properties, WMI resets the inherited property to the default value of the property in the parent class.

For more information, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md), [Accessing a Collection](accessing-a-collection.md), and [Removing a Single Item from a Collection](removing-a-single-item-from-a-collection.md).

 

 



