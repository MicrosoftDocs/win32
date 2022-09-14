---
description: Represents a WMI namespace.
ms.assetid: d5f0abc7-32cf-4d85-b5cd-5d60c991bcbc
ms.tgt_platform: multiple
title: '__Namespace class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __Namespace
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_Namespace class

The **\_\_Namespace** system class represents a WMI namespace.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __Namespace : __SystemClass
{
  string Name;
};
```

## Members

The **\_\_Namespace** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_Namespace** class has these properties.

<dl> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Key**](standard-qualifiers.md)
</dt> </dl>

Namespace name.

</dd> </dl>

## Remarks

The **\_\_Namespace** class is derived from [**\_\_SystemClass**](--systemclass.md), which has no properties.

You can use **\_\_Namespace** to identify, create, and delete child namespaces within the current working namespace for which you have an [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) object. Creating a new instance of **\_\_Namespace** within any working namespace creates a child namespace within the working namespace. Conversely, deleting an instance of **\_\_Namespace** removes the child namespace from the working namespace. Note that deleting a child namespace also deletes all of its classes and instances.

Enumerating instances of this class within any working namespace gives the available child namespaces.

For example, within the \\root namespace are two instances of **\_\_Namespace**. One has its **Name** property set to "Default," the other has **Name** set to "Cimv2." These instances represent the \\root\\default, and \\root\\cimv2 namespaces, respectively.

## Examples

The [List All WMI Namespaces](https://Gallery.TechNet.Microsoft.Com/4a8e84f1-4b52-452c-ae4f-e4e00e266257) VBScript example on the TechNet Gallery uses a recursive call to list all instances of the \_\_Namespace class on a system.

The following code sample retrieves all namespaces in PowerShell.


```PowerShell
get-wmiobject __namespace -namespace 'root' -list -recurse | format-table __namespace
```



The following code sample improves on the previous sample, and adds in additional information.


```PowerShell
# Set computer name 
$comp = "." 
 
# Get the name spaces on the local computer, and the local computer name 
$Namespace = get-wmiobject __namespace -namespace 'root' -list -recurse -computer $comp  
$hotsname = hostname 
 
# Display number of and names of the namespaces 
"{0} Namespaces on: {1}" -f $namespace.count, $hostname 
$NameSpace| sort __namespace  | Format-Table @{Expression = "__Namespace"; Label = "Namespace"}
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_SystemClass**](--systemclass.md)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> </dl>

 

 




