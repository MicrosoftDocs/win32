---
description: The classes used to hold registry data are defined with several standard qualifiers.
ms.assetid: d4786880-6c50-4e36-9a16-47de430e77a9
ms.tgt_platform: multiple
title: Defining a Registry Class With Qualifiers
ms.topic: article
ms.date: 05/31/2018
---

# Defining a Registry Class With Qualifiers

The classes used to hold registry data are defined with several standard qualifiers.

The following is a list of the standard qualifiers:

-   [Dynamic](standard-wmi-qualifiers.md) and [**Provider**](/windows/desktop/api/Provider/nl-provider-provider)

    You can attach the **Dynamic** qualifier to either a class or an instance. The **Dynamic** qualifier marks the class or instance as managed dynamically by a provider. When **Dynamic** appears on a class or instance, the [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) qualifier must also appear. The **Provider** qualifier identifies the particular provider that must manage the dynamic class or instance.

-   [ClassContext](standard-wmi-qualifiers.md)

    The **ClassContext** qualifier is attached to a class. It specifies the path to the registry key that contains the information the class represents.

    The **ClassContext** qualifier has the following format.

    ``` syntax
    MACHINE_NAME|Subtree\\KeyPath
    ```

    The value for KeyPath can be long if it includes keys with subkeys.

    The following example shows the **ClassContext** qualifier that contains the path to a particular computer transport device.

    ``` syntax
    Machine_Name|HKEY_LOCAL_MACHINE\\SOFTWARE\\MICROSOFT\\WBEM\\TRANSPORTS
    ```

The following template for a class definition illustrates the use of the **Dynamic**, [**Provider**](/windows/desktop/api/Provider/nl-provider-provider), and **ClassContext** qualifiers. The provider named by the **Provider** qualifier is the instance System Registry provider. Be aware that registry paths are case-insensitive, as are qualifier names.

``` syntax
[dynamic, provider("RegProv"), 
    ClassContext("local|hkey_local_machine\\software\\microsoft
    \\WBEM\\transports\\Network Transport Modules")]

class RegTrans
{
  [key] string  TransportsGUID;
  [PropertyContext("Name")] string Name;
  [PropertyContext("Independent")] uint32 Enabled;
};
```

Management applications can also use the System Registry provider to retrieve and modify registry data for a particular key.

 

 



