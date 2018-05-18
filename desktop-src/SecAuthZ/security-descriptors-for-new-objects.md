---
Description: 'When you create a securable object, you can assign a security descriptor to the new object.'
ms.assetid: '5b276d27-31a4-4a83-83b0-c4044a427097'
title: Security Descriptors for New Objects
---

# Security Descriptors for New Objects

When you create a securable object, you can assign a [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) to the new object. The functions for creating securable objects, such as [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) or [**RegCreateKeyEx**](https://msdn.microsoft.com/library/windows/desktop/ms724844), have a parameter that points to the [**SECURITY\_ATTRIBUTES**](security-attributes.md) structure that can contain a pointer to the new object's security descriptor. For sample code that builds a security descriptor and then calls **RegCreateKeyEx** to assign the security descriptor to a new registry key, see [Creating a Security Descriptor for a New Object in C++](creating-a-security-descriptor-for-a-new-object-in-c--.md).

The system component or server that manages the object can store the specified or default security descriptor to make it a persistent attribute of the object. If an object's creator does not specify a security descriptor, the system uses inherited or default security information to create a security descriptor. You can use functions to change the information in an object's security descriptor.

Directory service objects, files, directories, registry keys, and desktops are securable objects that can have a parent object. When you create one of these objects, the system checks for inheritable ACEs in the security descriptor of the parent object. The system typically merges any inheritable ACEs into the ACLs of the new object's security descriptor. You can prevent a DACL or SACL from inheriting ACEs by setting the SE\_DACL\_PROTECTED or SE\_SACL\_PROTECTED bits in the security descriptor's control bits. For more information, see [ACE inheritance](ace-inheritance.md).

 

 



