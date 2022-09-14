---
description: The simplest way of creating a namespace is to use Managed Object Format (MOF) code to create the namespace inside the current directory. The current directory is defined when you log on.
ms.assetid: 2b83cd96-079f-4178-9e5a-68ede3a92066
ms.tgt_platform: multiple
title: Creating a Child Namespace with MOF Code
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Child Namespace with MOF Code

The simplest way of creating a namespace is to use Managed Object Format (MOF) code to create the namespace inside the current directory. The current directory is defined when you log on.

The following procedure describes how to create a child namespace using MOF code.

**To create a child namespace using MOF code**

1.  Create an instance of the [**\_\_Namespace**](--namespace.md) class.

    The following code example shows how to create a child namespace.

    ``` syntax
    instance of __Namespace 
    {
        Name = "MyNamespace";
    };
    ```

2.  If you want to require the user to make an encrypted connection to the namespace, use the **RequiresEncryption** qualifier. For more information, see [Requiring an Encrypted Connection to a Namespace](requiring-an-encrypted-connection-to-a-namespace.md).

    The following code example shows how to require an encrypted connection.

    ``` syntax
    instance of __Namespace 
    {
        Name = "MyNamespace";
        [RequiresEncryption(TRUE)] 
        instance of __MyNamespace { };
    };
    ```

3.  If you want to set a security descriptor on the namespace rather than using the default namespace security, use the **NamespaceSecuritySDDL** qualifier. For more information, see [Setting Namespace Security When the Namespace is Created](setting-namespace-security-when-the-namespace-is-created.md).

    The following code example shows how to set a security descriptor on the namespace.

    ``` syntax
    #pragma namespace("\\\\.\\root\\MyNamespace")

    [NamespaceSecuritySDDL ("O:AUG:AUD:(A;CI;0x00060033;;;WD)")]
    Instance of __Namespace
    {
      Name = "MyNamespace";
    };
    ```

4.  Compile and load the [**\_\_Namespace**](--namespace.md) instance using the [mofcomp](mofcomp.md) utility or the [**IMofCompiler**](/windows/desktop/api/Wbemcli/nn-wbemcli-imofcompiler) interface. Both mofcomp and the **IMofCompiler** interface automatically load the namespace into the current directory. For more information, see [Compiling MOF Files](compiling-mof-files.md).

## Related topics

<dl> <dt>

[**Standard WMI Qualifiers**](standard-wmi-qualifiers.md)
</dt> </dl>

 

 



