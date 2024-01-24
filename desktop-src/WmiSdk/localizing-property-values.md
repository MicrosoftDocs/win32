---
description: The CIM schema localization model provides a mechanism for localizing qualifiers. It does not support direct localization of property values.
ms.assetid: a88bd873-7132-45b6-831e-64f9bb254c6e
ms.tgt_platform: multiple
title: Localizing Property Values
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Localizing Property Values

The CIM schema localization model provides a mechanism for localizing qualifiers. It does not support direct localization of property values.

In some cases, however, the string properties values in the static instances can be replaced by an enumerated integer type and a value map can be defined for the property in the class definition. In these cases, the **Values** qualifier should be localized. Using enumeration qualifiers is the primary mechanism for localizing property values. Any other forms of property value localization are not supported.

The following example shows how static properties can be localized using partial value maps with regular expressions. In this example, the predefined subset of values is initialized in the schema using static instances. The rest of the values are provided dynamically.

``` syntax
[abstract]
class DataGroup
{
   [key] string GUID;
   [Description("data group display name"): Amended,
                     ValueMap{"Logical Disk",
                     "CPU Utilization", ".+"}]
                     string GroupDisplayName;
   [ValueMap{"Monitors percentage of disk free space",
                  "Monitors percentage CPU utilization", ".+"}] 
                   string GroupDescription;
};

[static, Description ("pre-configured parameters") :amended]
class InitialGroup : DataGroup {
};

[dynamic, provider("HMProvider"),
    Description ("user-defined parameters") :amended]
class UserDefionedGroup : DataGroup {
};

instance of InitialGroup {
   GUID = "abc";
   GroupDisplayName = "Logical Disk";
   GroupDescription = "Monitors percentage of disk free space";
};

instance of InitialGroup {
   GUID = "def";
   GroupDisplayName = "CPU Utilization";
   GroupDescription = "Monitors percentage CPU utilization";
};
```

For more information, see [Localizing Static Properties](localizing-static-properties.md).

 

 



