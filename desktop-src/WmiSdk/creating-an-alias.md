---
description: An alias in WMI is a symbolic reference in either a class or a class instance located elsewhere in a Managed Object Format (MOF) file.
ms.assetid: bf4981dc-3aab-46c5-bf02-48132ccec8c2
ms.tgt_platform: multiple
title: Creating a WMI Alias
ms.topic: article
ms.date: 05/31/2018
---

# Creating a WMI Alias

An [*alias*](gloss-a.md) in WMI is a symbolic reference in either a class or a class instance located elsewhere in a Managed Object Format (MOF) file. The MOF compiler uses aliases to establish references between classes and instances. The compiler resolves aliases to the classes to which they refer, so alias names are not available in compiled code. As a result, client applications cannot refer to classes using aliases.

> [!Note]  
> WMI supports forward referencing but not circular aliases.

 

An alias has scope only within the MOF file in which you declare the alias. Therefore, you typically use an alias as a shortcut to a lengthy object path.

**To define an alias**

1.  Add the phrase "as $*aliasname*" to the instance or class declaration.
2.  Alias names follow the same rules as instance and class names, except that alias names must begin with a dollar sign ($). Underscores can appear in an alias name following the initial character.

The following code example describes how to use an alias in a class definition.

``` syntax
class MyClass as $MyClassAlias
{
};
instance of MyClass as $MyInstanceAlias
{
};
```

The following code examples describe how to use an alias as a symbolic reference to an object path. These examples declare two classes to describe a disk: the Disk class to indicate the drive letter and the DiskRef class to indicate the disk path. An alias is defined for the Disk class instance. This alias is used as the value for the PathToDisk property in the DiskRef instance.

``` syntax
class Disk {
    [key]  string    DriveLetter;
};

class DiskRef 
{
    [key]  string    MyKey;
    Disk   ref       PathToDisk;
};

instance of Disk as $DiskAlias 
{
    DriveLetter = "c";
};

instance of DiskRef
{
    MyKey      =  "hello";
    PathToDisk = $DiskAlias;
};
```

## Related topics

<dl> <dt>

[Creating a Class](creating-a-class.md)
</dt> </dl>

 

 



