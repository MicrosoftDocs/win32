---
description: Accessing an Unnamed Registry Value
ms.assetid: 1095da4c-8b9f-4674-9801-f2d25c4f372b
ms.tgt_platform: multiple
title: Accessing an Unnamed Registry Value
ms.topic: article
ms.date: 05/31/2018
---

# Accessing an Unnamed Registry Value

The default, or unnamed value of a registry key is shown as (Default) or \<No Name> in the Regedit registry editor. You can use the System Registry provider to access an unnamed registry key. Similarly, you can also use the System Registry provider to access bitmap descriptions, which are defined as unnamed values.

The following procedure describes how to retrieve an unnamed registry value.

**To retrieve an unnamed registry value**

1.  Define a property and set the **PropertyContext** qualifier of that property to an empty string.

    The following code example shows how the class defines properties to hold values for the key specified by the **ClassContext** qualifier. The default value is stored in the **Default** property.

    ``` syntax
    [dynamic, 
     provider("RegProv"), 
     ClassContext("local|hkey_local_machine\\software\\"
     "microsoft\\Active Setup\\Installed Components")]

    class RegTrans{
      [key] String Transports="";
      [PropertyContext("")] String Default;
      [PropertyContext("ComponentId")] String ComponentID;
      [PropertyContext("Locale")] String Locale;
    };
    ```

    The Transports key does not use the unnamed value, so compilation of this MOF file does not produce any value for the **Default** property unless a registry editing tool is used to change the unnamed value.

2.  For a bitmap file, define a property and set the **PropertyContext** of that property.

    The following code example shows how to define a property.

    ```mof
    Local|hkey_classes_root\\.bmp
    ```

    

 

 



