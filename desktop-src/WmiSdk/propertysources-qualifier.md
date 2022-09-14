---
description: Every property in a view class must have a string array qualifier called PropertySources.
ms.assetid: df89680b-8ea7-4f38-81ba-c4132b944f37
ms.tgt_platform: multiple
title: PropertySources Qualifier
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PropertySources
api_type: 
- NA
api_location: 
---

# PropertySources Qualifier

Every property in a view class must have a string array qualifier called **PropertySources**. The **PropertySources** qualifier contains the name of the source class property or properties from which this view class property gets data. The order of the values in this array correspond to the order of the source classes defined for the [ViewSources qualifier](viewsources-qualifier.md). The following example shows how to define a property for a union view class that is the union of the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class from two different computers:


```mof
[PropertySources{"DeviceID", "DeviceID"},key] String Devname;
```



The first **DeviceID** property corresponds to the **DeviceID** property from the class in the first source query. The second **DeviceID** property is the **DeviceID** property from the class in the second source query.

When defining properties for join view classes, you must define a separate view property for each of the source class properties unless the source class properties are the basis of the join view class. The following example creates properties in a join view class on similar properties from the [**Win32\_Printer**](/windows/desktop/CIMWin32Prov/win32-printer) source class and the [**Win32\_PrinterConfiguration**](/windows/desktop/CIMWin32Prov/win32-printerconfiguration) source class:


```mof
[PropertySources{"VerticalResolution", ""}] Uint32 Vres;
[PropertySources{"", "YResolution"}] Uint32 Yres;
```



If the two source classes are being joined by a common property, you can only define a single view class property because the value of both source class properties is always the same. The following example shows how to join the [**Win32\_Printer**](/windows/desktop/CIMWin32Prov/win32-printer) class and the [**Win32\_PrinterConfiguration**](/windows/desktop/CIMWin32Prov/win32-printerconfiguration) by a common property value:


```mof
[PropertySources{"DeviceId", "DeviceName "}] String Name;
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[**Qualifiers Specific to the View Provider**](qualifiers-specific-to-the-view-provider.md)
</dt> </dl>

 

