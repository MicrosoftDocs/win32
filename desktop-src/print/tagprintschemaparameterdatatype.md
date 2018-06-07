---
Description: The PrintSchemaParameterDataType enumeration identifies the allowed data types for the Print Schema parameter.
ms.assetid: 3276C273-C950-4DC9-B338-E6E7E30DEB77
title: PrintSchemaParameterDataType enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# PrintSchemaParameterDataType enumeration

The PrintSchemaParameterDataType enumeration identifies the allowed data types for the Print Schema parameter.

## Syntax


```C++
typedef enum tagPrintSchemaParameterDataType { 
  PrintSchemaParameterDataType_Integer        = 0,
  PrintSchemaParameterDataType_NumericString,
  PrintSchemaParameterDataType_String
} PrintSchemaParameterDataType;
```



## Constants

<dl> <dt>

<span id="PrintSchemaParameterDataType_Integer"></span><span id="printschemaparameterdatatype_integer"></span><span id="PRINTSCHEMAPARAMETERDATATYPE_INTEGER"></span>**PrintSchemaParameterDataType\_Integer**
</dt> <dd>

Integer data type. This maps to the Print Schema’s IntegerParamType parameters.

</dd> <dt>

<span id="PrintSchemaParameterDataType_NumericString"></span><span id="printschemaparameterdatatype_numericstring"></span><span id="PRINTSCHEMAPARAMETERDATATYPE_NUMERICSTRING"></span>**PrintSchemaParameterDataType\_NumericString**
</dt> <dd>

String data type with only numeric chars allowed. This maps to the Print Schema’s StringParamType parameters, with UnitType = “numeric”.

</dd> <dt>

<span id="PrintSchemaParameterDataType_String"></span><span id="printschemaparameterdatatype_string"></span><span id="PRINTSCHEMAPARAMETERDATATYPE_STRING"></span>**PrintSchemaParameterDataType\_String**
</dt> <dd>

String data type with arbitrary chars allowed. This maps to the Print Schema’s StringParamType parameters, with UnitType not equal to “numeric”.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaParameterDefinition::DataType**](-iprintschemaparameterdefinition-datatype.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PrintSchemaParameterDataType%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





