---
description: The application must create the properties with a data type that maps to the registry data type.
ms.assetid: aa86565c-47eb-40d3-a533-03464cd1c6cd
ms.tgt_platform: multiple
title: Mapping a Registry Data Type to a WMI Data Type
ms.topic: article
ms.date: 05/31/2018
---

# Mapping a Registry Data Type to a WMI Data Type

The application must create the properties with a data type that maps to the registry data type. You do not need to specify the registry data type in the methods that create, get, or set registry values. However, the input parameter that contains the value must be in the correct WMI data type. For example, if an application receives **REG\_DWORD** data from the registry, the class that receives the data must include a **Uint32** property.

The following table lists the mapping between registry and WMI data types used in the [**StdRegProv**](/previous-versions/windows/desktop/regprov/stdregprov) methods.



| Registry data type      | WMI data type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **REG\_BINARY**         | **uint8** array<br/> An array of values that do not exceed 255 or hex FF. For example, the following Visual Basic Script code creates an array that fits this data type.<br/> `BinArray = Array(&H01, &Ha2)`<br/> The [**StdRegProv**](/previous-versions/windows/desktop/regprov/stdregprov) class method [**SetBinaryValue**](/previous-versions/windows/desktop/regprov/setbinaryvalue-method-in-class-stdregprov) requires the **REG\_BINARY** data type.<br/>                                                                                          |
| **REG\_DWORD**          | **uint32**, **sint32** or Visual Basic **integer**<br/> A single 32-bit value. The [**StdRegProv**](/previous-versions/windows/desktop/regprov/stdregprov) class methods [**GetDWORDValue**](/previous-versions/windows/desktop/regprov/getdwordvalue-method-in-class-stdregprov) and [**SetDWORDValue**](/previous-versions/windows/desktop/regprov/setdwordvalue-method-in-class-stdregprov) require the **REG\_DWORD** data type.<br/>                                                                                                                                                                  |
| **REG\_SZ**             | **string**<br/> The [**StdRegProv**](/previous-versions/windows/desktop/regprov/stdregprov) class method [**SetStringValue**](/previous-versions/windows/desktop/regprov/setstringvalue-method-in-class-stdregprov) requires the **REG\_SZ** data type.<br/>                                                                                                                                                                                                                                                                                                            |
| **REG\_QWORD**          | **uint64**.<br/> A single 64-bit value. The [**StdRegProv**](/previous-versions/windows/desktop/regprov/stdregprov) class methods [**GetQWORDValue**](/previous-versions/windows/desktop/regprov/getqwordvalue-method-in-class-stdregprov) and [**SetQWORDValue**](/previous-versions/windows/desktop/regprov/setqwordvalue-method-in-class-stdregprov) require the **REG\_QWORD** data type.<br/>                                                                                                                                                                                                         |
| **REG\_EXPAND\_SZ**     | **string**<br/> Expanded strings are special strings that represent system environment variables. For example, the following VBScript code creates a string that represents the **HKEY\_LOCAL\_USER** environment variable TEMP.<br/> `TEMP = "%USERPROFILE\LocalSettings\Temp%"`<br/> The [**StdRegProv**](/previous-versions/windows/desktop/regprov/stdregprov) class method [**SetExpandedStringValue**](/previous-versions/windows/desktop/regprov/setexpandedstringvalue-method-in-class-stdregprov) requires the **REG\_EXPAND\_SZ** data type.<br/> |
| **REG\_MULTI\_SZ**      | **string** array<br/> The Multistring data type contains multiple strings. For example, the following VBScript code creates an array that fits this data type.<br/> `MultiValue = Array("first", "second", "third")`<br/> The [**StdRegProv**](/previous-versions/windows/desktop/regprov/stdregprov) class method [**SetMultiStringValue**](/previous-versions/windows/desktop/regprov/setmultistringvalue-method-in-class-stdregprov) requires the **REG\_MULTI\_SZ** data type.<br/>                                                                     |
| **REG\_RESOURCE\_LIST** | As appropriate. For more information, see [Describing a Resource for the Registry](describing-a-resource-for-the-registry.md).<br/>                                                                                                                                                                                                                                                                                                                                                                    |



 

## Related topics

<dl> <dt>

[Defining Classes for the System Registry Provider](defining-classes-for-the-system-registry-provider.md)
</dt> </dl>

 

