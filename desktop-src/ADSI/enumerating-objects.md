---
title: Enumerating Objects
description: To view the child object of a container, such as an organizational unit (OU), enumerate the container object.
ms.assetid: 06995281-d269-42ce-839f-2938a2f6af22
ms.tgt_platform: multiple
keywords:
- Enumerating Objects
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Objects

To view the child object of a container, such as an organizational unit (OU), enumerate the container object. To make an analogy to a file system, the child object would correspond to files in the directory, while the container, which is the parent object, would correspond to the directory itself. You may also use the enumerate operation when you want to get the parent object of an object.

When you enumerate an object, you actually bind to an object in the directory, and an [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) interface is returned on each object.

The following code example shows how to enumerate the children of a container.


```VB
Dim ou As IADs
' Bind to an object using its DN.
On Error GoTo Cleanup

Set ou = GetObject("LDAP://OU=Sales,DC=Fabrikam,DC=COM")

For each child in ou
    Debug.Print child.Name
Next

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If
    Set ou = Nothing
```



You can filter the types of objects returned from the enumeration. For example, to display only users and groups, use the following code example before the enumeration.


```VB
Ou.Filter = Array("user", "group")
```



If you have an object reference, you can get the object's parent using the [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) [**Parent**](iads-property-methods.md) property. The following code example shows how to bind to the parent object.


```VB
parentPath = obj.Parent
Set parent = GetObject(parentPath)
```



For more information, see [Enumerating ADSI Objects](enumerating-adsi-objects.md).

## Related topics

<dl> <dt>

[Searching for Objects](searching-for-objects.md)
</dt> </dl>

 

 




