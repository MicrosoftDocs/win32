---
Description: Object-specific ACEs are supported for directory service (DS) objects. An object-specific ACE contains a pair of GUIDs that expand the ways in which the ACE can protect an object.
ms.assetid: 37d353c0-ac22-430f-b5f3-15deb69be24b
title: Object-specific ACEs
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Object-specific ACEs

Object-specific [*ACEs*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) are supported for directory service (DS) objects. An object-specific ACE contains a pair of GUIDs that expand the ways in which the ACE can protect an object.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>GUID</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ObjectType</strong></td>
<td>Identifies one of the following:
<ul>
<li>A type of child object. The ACE controls the right to create a specified type of child object. For more information, see [Controlling Child Object Creation in C++](controlling-child-object-creation-in-c--.md).</li>
<li>A property set or property. The ACE controls the right to read or write the property or property set. For more information, see [ACEs to Control Access to an Object's Properties](aces-to-control-access-to-an-object-s-properties.md).</li>
<li>An extended right. The ACE controls the right to perform the operation associated with the extended right.</li>
<li>A validated write. The ACE controls the right to perform certain write operations. These validated write permissions, defined and exposed in the ACL Editor, provide permissions for validated writes of properties rather than unchecked low-level writes of any value to a property that is granted with a &quot;write property&quot; permission.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>InheritedObjectType</strong></td>
<td>Indicates the type of child object that can inherit the ACE. Inheritance is also controlled by the inheritance flags in the [<strong>ACE_HEADER</strong>](/windows/win32/Winnt/ns-winnt-_ace_header?branch=master), as well as by any protection against inheritance placed on the child objects. For more information, see [ACE Inheritance](ace-inheritance.md).</td>
</tr>
</tbody>
</table>



 

Three types of object-specific ACEs are supported.

> [!Note]  
> System-alarm object ACEs are not currently supported.

 



| Type                      | Description                                                                                                                                                                                                                                       |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Access-denied object ACE  | Used in a DACL to deny a trustee access to a property or property set on the object, or to limit ACE inheritance to a specified type of child object. Uses the [**ACCESS\_DENIED\_OBJECT\_ACE**](/windows/win32/Winnt/ns-winnt-_access_denied_object_ace?branch=master) structure.         |
| Access-allowed object ACE | Used in a DACL to allow a trustee access to a property or property set on the object, or to limit ACE inheritance to a specified type of child object. Uses the [**ACCESS\_ALLOWED\_OBJECT\_ACE**](/windows/win32/Winnt/ns-winnt-_access_allowed_object_ace?branch=master) structure.      |
| System-audit object ACE   | Used in a SACL to log a trustee's attempts to access a property or property set on the object, or to limit ACE inheritance to a specified type of child object. Uses the [**SYSTEM\_AUDIT\_OBJECT\_ACE**](/windows/win32/Winnt/ns-winnt-_system_alarm_object_ace?branch=master) structure. |



 

Any ACL that contains an object-specific ACE must use the revision ACL\_REVISION\_DS.

 

 



