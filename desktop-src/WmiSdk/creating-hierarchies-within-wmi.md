---
description: WMI namespace is a programming object that defines the scope for a set of classes and instances. WMI provider classes must be defined inside a namespace.
ms.assetid: a00f26e6-bb81-45bc-a530-9346a074bb3c
ms.tgt_platform: multiple
title: Creating Hierarchies Within WMI
ms.topic: article
ms.date: 05/31/2018
---

# Creating Hierarchies Within WMI

[*WMI namespace*](gloss-n.md) is a programming object that defines the scope for a set of classes and instances. WMI provider classes must be defined inside a namespace.

Namespaces describe different managed environments, such as the SMS environment. Because the classes and instances of a schema define the components of a managed environment, each new schema requires a new namespace. For example, the root\\cimv2 namespace contains the classes and instances defined in the Win32 schema as well as the parent Common Information Model (CIM) classes from which the Win32 schema inherits. CIM classes are defined by the Distributed Management Task Force ([DMTF](https://www.dmtf.org/home)).

> [!Note]  
> To ensure that all of your WMI class definitions for managed objects are restored to the [*WMI repository*](gloss-w.md) if WMI has a failure and restarts, use the [**\#pragma autorecover**](pragma-autorecover.md) preprocessor instruction in your [*Managed Object Format (MOF)*](gloss-m.md) file.

 

WMI defines a namespace as an instance of the [**\_\_Namespace**](--namespace.md) system class or any class that derives from **\_\_Namespace**. The **\_\_Namespace** system class has a single property called **Name**, which must be unique within the scope of the parent namespace. The **Name** property must also contain a string that begins with a letter. All other characters in the string can be letters, digits, or underscores. All characters are case-insensitive.

In addition to determining the unique name for a child namespace, the parent WMI namespace can protect the static instances of your classes from accidental modification by other providers. For example, you may find it convenient to nest a new namespace under an existing namespace for another provider. However, the original provider may try to update all class instances to match up with a new schema. In doing so, the original provider may delete all sub-children in a namespace. While this may be an appropriate action for the target namespace, it may affect unrelated class instances in a child namespace (i.e., your own provider classes).

Therefore, it is generally recommended that you create and register your namespace as separate from namespaces that you do not directly control. This is especially true if your classes derive only from general CIM classes or other classes from your company. Your namespace can be under the **Root** namespace, such as the following:

**Root/myCompany/myProduct**

In contrast, if your new class derives from the class of another provider, you may need to store your class in a sub-namespace of that provider. Note that this exposes your new class to accidental deletion by the original provider.

WMI provides several different ways to create a namespace:

-   [Creating a Child Namespace with MOF Code](creating-a-child-namespace-with-mof-code.md)
-   [Creating a Sibling Namespace with MOF Code](creating-a-sibling-namespace-with-mof-code.md)
-   [Creating a Namespace with the WMI API](creating-a-namespace-with-the-wmi-api.md)

## Related topics

<dl> <dt>

[Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md)
</dt> </dl>

 

 



