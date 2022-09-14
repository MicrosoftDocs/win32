---
description: You can use the System Registry Provider as either an instance or a property provider.
ms.assetid: 0a8198c0-57c1-4d96-9965-3867c8c0e738
ms.tgt_platform: multiple
title: Use the System Registry Provider as a Property Provider
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Use the System Registry Provider as a Property Provider

You can use the [System Registry Provider](/previous-versions/windows/desktop/regprov/system-registry-provider) as either an instance or a property provider.

If you choose to access the property provider interfaces, you must mark your WMI classes to indicate your intention.

**To use the system registry provider as a property provider**

-   Define your WMI class with the **DynProps**, [**Provider**](/windows/desktop/api/Provider/nl-provider-provider), and **PropertyContext** standard qualifiers.

    The **DynProps** qualifier identifies a class as having properties that are maintained by the property provider identified by the [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) qualifier. The **PropertyContext** qualifier specifies the name of the registry value to be stored by the property. The format of the **PropertyContext** qualifier is the same as the format of the **ClassContext** qualifier with additional *valuename* and *expression* values.

    ``` syntax
    MACHINE_NAME | Subtree\\KeyPath [|valuename [expression]]
    ```

    Both *valuename* and *expression* are optional. The *valuename* setting is only used if the registry value has a name. The *expression* is also optional and is used for resource descriptor data. For more information, see [Describing a Resource for the Registry](describing-a-resource-for-the-registry.md).

    The following code example shows how the class uses the System Registry provider as a property provider to maintain its nonkey properties.

    ``` syntax
    [DYNPROPS]
    class PropReg {

        [KEY]  STRING  MyKey;
        STRING Logging;
        STRING Events;
        uint32 Resource1;
    };

    [DYNPROPS]
    instance of PropReg
    {
      MyKey = "a";

      [PropertyContext("local|hkey_local_Machine\\software\\microsoft\\
       wbem\\cimom|Logging"), Dynamic, Provider("RegPropProv")]  Logging;

      [PropertyContext("local|hkey_local_Machine\\software\\microsoft\\
       wbem\\cimom|EnableEvents"), Dynamic, Provider("RegPropProv")]
       Events;

      [PropertyContext("local|hkey_local_Machine\\hardware\\
       ResourceMap\\Hardware Abstraction Layer\\PC Compatible Eisa/isa 
       hal|.raw(\"Internal\")(0)(0)(\"interrupt.vector\")"), Dynamic, 
       Provider("RegPropProv")]  Resource1;
    };
    ```

 

 
