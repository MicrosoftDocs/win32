---
description: An association view class allows you to use ASSOCIATORS OF queries on classes that reside in different namespaces.
ms.assetid: 4af4fe1b-2b19-472e-8261-798b374ae57e
ms.tgt_platform: multiple
title: Associating Instances Between Namespaces
ms.topic: article
ms.date: 05/31/2018
---

# Associating Instances Between Namespaces

An association view class allows you to use [ASSOCIATORS OF](associators-of-statement.md) queries on classes that reside in different namespaces.

The following procedure describes how to associate instances between namespaces.

**To associate instances between namespaces**

1.  Begin your class definition with the [**Association**](meta-qualifiers.md) string qualifier.

    The **JoinOn**, [**Association**](meta-qualifiers.md), and **Union** qualifiers are mutually exclusive.

2.  Create the queries that define source instances used in the view class with the [**ViewSources**](viewsources-qualifier.md) qualifier.
3.  Define the names and location of the namespaces in which the source instances are located with the [**ViewSpaces**](viewspaces-qualifier.md) qualifier.
4.  Define the properties you want in your association view class with the [**PropertySources**](propertysources-qualifier.md) qualifier.

    If necessary, you can tag any of the properties as belonging to a source class by using the [**HiddenDefault**](qualifiers-specific-to-the-view-provider.md) qualifier.

5.  Tag any relevant properties with the **Direct** qualifier.

    The **Direct** qualifier prevents the View Provider from mapping the tagged association reference to a view reference.

The following code examples show how to create association view classes.

``` syntax
[union,
ViewSources {"SELECT * FROM Win32_OperatingSystem"},
    ViewSpaces {"\\\\.\\root\\cimv2"},
    dynamic, provider("MS_VIEW_INSTANCE_PROVIDER")
]
class Union_OS_For_AssociationExample
{
    [key, PropertySources{"Name"}]
    string Name;

    [PropertySources{"Version"}]
    string Version;

    [PropertySources{"BuildNumber"}]
    string BuildNumber;
};

[
Association,
ViewSources {"SELECT * FROM Win32_SystemOperatingSystem"}, 
ViewSpaces {"\\\\.\\root\\cimv2"},
dynamic, provider("MS_VIEW_INSTANCE_PROVIDER")
]
class Association_SystemViewOperatingSystem
{
    [Direct, key, PropertySources{"GroupComponent"}]
    Win32_ComputerSystem ref Computer;
    
    [key, PropertySources{"PartComponent"}]
    Union_OS_For_AssociationExample ref OperatingSystem;
};
```

 

 



