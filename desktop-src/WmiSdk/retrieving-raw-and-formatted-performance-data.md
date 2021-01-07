---
description: The following topic describes how to retrieve the on-line programming documentation for a dynamically-created raw or formatted data object.
ms.assetid: B3CD7E2C-9FCF-42FB-8713-01A696E905B0
ms.tgt_platform: multiple
title: Retrieving Documentation for Raw and Formatted Performance Data Objects
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Documentation for Raw and Formatted Performance Data Objects

The following topic describes how to retrieve the on-line programming documentation for a dynamically-created raw or formatted data object.

WMI contains a number of objects that track performance. Classes derived from [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) contain raw, or "uncooked" performance data, and are supported by the [Performance Counter provider](performance-counter-provider.md). In contrast, classes derived from [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata) contain "cooked", or formatted data, and are supported by the [Formatted Performance Data Provider](formatted-performance-data-provider.md).

However, both providers support a number of dynamically-created child classes. Because the properties are added at run-time, these classes may contain undocumented properties. You can use the following code to identify what properties a given dynamically-created class has.

**To retrieve a description of a dynamically-created class**

1.  Create an instance of the item, and set the amended qualifier to true.

    ```PowerShell
    $osClass = New-Object System.Management.ManagementClass Win32_ClassNameHere  
    $osClass.Options.UseAmendedQualifiers = $true
    ```

    

2.  Retrieve the properties of the class.

    ```PowerShell
    $properties = $osClass.Properties  
    "This class has {0} properties as follows:" -f $properties.count
    ```

    

3.  Display the properties.

    ```PowerShell
    foreach ($property in $properties) {  
    "Property Name: {0}" -f $property.Name  
    "Description:   {0}" -f $($property.Qualifiers["Description"].Value)  
    "Type:          {0}" -f $property.Type  
    "-------"
    }
    ```

    

The following code retrieves the property descriptions for the specified [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata) object.


```PowerShell
$osClass = New-Object System.Management.ManagementClass Win32_PerfFormattedData_APPPOOLCountersProvider_APPPOOLWAS  
$osClass.Options.UseAmendedQualifiers = $true  
  
# Get the Properties in the class  
$properties = $osClass.Properties  
"This class has {0} properties as follows:" -f $properties.count  
  
  
# display the Property name, description, type, qualifiers and instance values  
  
foreach ($property in $properties) {  
"Property Name: {0}" -f $property.Name  
"Description:   {0}" -f $($property.Qualifiers["Description"].Value)  
"Type:          {0}" -f $property.Type  
"-------"  
}
```



 

 
