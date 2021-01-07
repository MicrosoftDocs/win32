---
description: Another way of creating a namespace is to use Managed Object Format (MOF) code to create a sibling namespace. A sibling namespace is a namespace that does not exist as a child of the current namespace.
ms.assetid: 1a3f8569-e725-4158-9a2b-b440b9247925
ms.tgt_platform: multiple
title: Creating a Sibling Namespace with MOF Code
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Creating a Sibling Namespace with MOF Code

Another way of creating a namespace is to use Managed Object Format (MOF) code to create a sibling namespace. A sibling namespace is a namespace that does not exist as a child of the current namespace.

The following procedure describes how to create a sibling namespace with MOF code.

**To create a sibling namespace with MOF code**

1.  Insert the [**\#pragma namespace**](pragma-namespace.md) command into your MOF code prior to the namespace declaration.

    The [**\#pragma namespace**](pragma-namespace.md) command instructs WMI where to create the instances following the directive.

2.  Create an instance of the [**\_\_Namespace**](--namespace.md) class.
3.  Compile your code with the [mofcomp](mofcomp.md) utility or the [**IMofCompiler**](/windows/desktop/api/Wbemcli/nn-wbemcli-imofcompiler) interface.

    For more information, see [Compiling MOF Files](compiling-mof-files.md).

The following MOF code example describes how to create a namespace as a sibling to the "Root\\CIMv2" namespace.

``` syntax
#pragma namespace("\\\\.\\Root")

instance of __Namespace 
{
    Name = "MyNamespace";
};
```

 

 



