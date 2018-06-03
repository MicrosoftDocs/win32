---
title: MetricThresholdValueValueType enumeration
description: Provides values for the value type, which is the value of element MetricThresholdValue/ValueType.
ms.assetid: 1637EAB3-BED3-4154-99C6-7E8036744EA9
keywords:
- MetricThresholdValueValueType enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- MetricThresholdValueValueType
api_location:
- AxeRuntime.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# MetricThresholdValueValueType enumeration

Provides values for the value type, which is the value of element **MetricThresholdValue/ValueType**.

## Syntax


```C++
enum MetricThresholdValueValueType {
  MetricThresholdValueValueType_NotSet        = 0, 
  MetricThresholdValueValueTypeString, 
  MetricThresholdValueValueTypeInt, 
  MetricThresholdValueValueTypeInt16, 
  MetricThresholdValueValueTypeInt32, 
  MetricThresholdValueValueTypeInt64, 
  MetricThresholdValueValueTypeUInt16, 
  MetricThresholdValueValueTypeUInt32, 
  MetricThresholdValueValueTypeUInt64, 
  MetricThresholdValueValueTypeByte, 
  MetricThresholdValueValueTypeSByte, 
  MetricThresholdValueValueTypeSingle, 
  MetricThresholdValueValueTypeDouble, 
  MetricThresholdValueValueTypeFloat, 
  MetricThresholdValueValueTypeBool, 
  MetricThresholdValueValueTypeBoolean, 
  MetricThresholdValueValueTypeChar, 
  MetricThresholdValueValueTypeDateTime, 
  MetricThresholdValueValueTypeDuration, 
  MetricThresholdValueValueTypeTimeSpan, 
  MetricThresholdValueValueTypeFilePath, 
  MetricThresholdValueValueTypeDirectoryPath, 
  MetricThresholdValueValueType_Max 

};
```



## Constants

<dl> <dt>

<span id="MetricThresholdValueValueType_NotSet"></span><span id="metricthresholdvaluevaluetype_notset"></span><span id="METRICTHRESHOLDVALUEVALUETYPE_NOTSET"></span>**MetricThresholdValueValueType\_NotSet**
</dt> <dd>

No value type has been set.

</dd> <dt>

<span id="MetricThresholdValueValueTypeString"></span><span id="metricthresholdvaluevaluetypestring"></span><span id="METRICTHRESHOLDVALUEVALUETYPESTRING"></span>**MetricThresholdValueValueTypeString**
</dt> <dd>

The data type is a character string.

</dd> <dt>

<span id="MetricThresholdValueValueTypeInt"></span><span id="metricthresholdvaluevaluetypeint"></span><span id="METRICTHRESHOLDVALUEVALUETYPEINT"></span>**MetricThresholdValueValueTypeInt**
</dt> <dd>

The data type is an integer value between -2,147,483,648 and 2,147,483,647.

</dd> <dt>

<span id="MetricThresholdValueValueTypeInt16"></span><span id="metricthresholdvaluevaluetypeint16"></span><span id="METRICTHRESHOLDVALUEVALUETYPEINT16"></span>**MetricThresholdValueValueTypeInt16**
</dt> <dd>

The data type is an integer value between -32768 and 32767.

</dd> <dt>

<span id="MetricThresholdValueValueTypeInt32"></span><span id="metricthresholdvaluevaluetypeint32"></span><span id="METRICTHRESHOLDVALUEVALUETYPEINT32"></span>**MetricThresholdValueValueTypeInt32**
</dt> <dd>

The data type is an integer value between -2,147,483,648 and 2,147,483,647.

</dd> <dt>

<span id="MetricThresholdValueValueTypeInt64"></span><span id="metricthresholdvaluevaluetypeint64"></span><span id="METRICTHRESHOLDVALUEVALUETYPEINT64"></span>**MetricThresholdValueValueTypeInt64**
</dt> <dd>

The data type is an integer value between and -9,223,372,036,854,775,808 and 9,223,372,036,854,775,807.

</dd> <dt>

<span id="MetricThresholdValueValueTypeUInt16"></span><span id="metricthresholdvaluevaluetypeuint16"></span><span id="METRICTHRESHOLDVALUEVALUETYPEUINT16"></span>**MetricThresholdValueValueTypeUInt16**
</dt> <dd>

The data type is an unsigned integer value between 0 and 65535.

</dd> <dt>

<span id="MetricThresholdValueValueTypeUInt32"></span><span id="metricthresholdvaluevaluetypeuint32"></span><span id="METRICTHRESHOLDVALUEVALUETYPEUINT32"></span>**MetricThresholdValueValueTypeUInt32**
</dt> <dd>

The data type is an unsigned integer value between 0 and 4,294,967,295.

</dd> <dt>

<span id="MetricThresholdValueValueTypeUInt64"></span><span id="metricthresholdvaluevaluetypeuint64"></span><span id="METRICTHRESHOLDVALUEVALUETYPEUINT64"></span>**MetricThresholdValueValueTypeUInt64**
</dt> <dd>

The data type is an unsigned integer value between 0 and 18,446,744,073,709,551,615.

</dd> <dt>

<span id="MetricThresholdValueValueTypeByte"></span><span id="metricthresholdvaluevaluetypebyte"></span><span id="METRICTHRESHOLDVALUEVALUETYPEBYTE"></span>**MetricThresholdValueValueTypeByte**
</dt> <dd>

The data type is an unsigned integer value between 0 and 255.

</dd> <dt>

<span id="MetricThresholdValueValueTypeSByte"></span><span id="metricthresholdvaluevaluetypesbyte"></span><span id="METRICTHRESHOLDVALUEVALUETYPESBYTE"></span>**MetricThresholdValueValueTypeSByte**
</dt> <dd>

The data type is an integer value between -128 and 127.

</dd> <dt>

<span id="MetricThresholdValueValueTypeSingle"></span><span id="metricthresholdvaluevaluetypesingle"></span><span id="METRICTHRESHOLDVALUEVALUETYPESINGLE"></span>**MetricThresholdValueValueTypeSingle**
</dt> <dd>

The data type is a single-precision 32-but floating point number whose values range from -3.402823e38 to 3.402823e38, as well as positive or negative zero, **PositiveInfinity**, **NegativeInfinity**, and not a number (**NaN**).

</dd> <dt>

<span id="MetricThresholdValueValueTypeDouble"></span><span id="metricthresholdvaluevaluetypedouble"></span><span id="METRICTHRESHOLDVALUEVALUETYPEDOUBLE"></span>**MetricThresholdValueValueTypeDouble**
</dt> <dd>

The data type is a double-precision 64-but floating point number whose values range from -1.7976931348623157E+308 to 1.7976931348623157E+308, as well as positive or negative zero, **PositiveInfinity**, **NegativeInfinity**, and not a number (**NaN**).

</dd> <dt>

<span id="MetricThresholdValueValueTypeFloat"></span><span id="metricthresholdvaluevaluetypefloat"></span><span id="METRICTHRESHOLDVALUEVALUETYPEFLOAT"></span>**MetricThresholdValueValueTypeFloat**
</dt> <dd>

The data type is a single-precision 32-but floating point number whose values range from -3.402823e38 to 3.402823e38, as well as positive or negative zero, **PositiveInfinity**, **NegativeInfinity**, and not a number (**NaN**).

</dd> <dt>

<span id="MetricThresholdValueValueTypeBool"></span><span id="metricthresholdvaluevaluetypebool"></span><span id="METRICTHRESHOLDVALUEVALUETYPEBOOL"></span>**MetricThresholdValueValueTypeBool**
</dt> <dd>

The data type is Boolean (value of **true** and **false**).

</dd> <dt>

<span id="MetricThresholdValueValueTypeBoolean"></span><span id="metricthresholdvaluevaluetypeboolean"></span><span id="METRICTHRESHOLDVALUEVALUETYPEBOOLEAN"></span>**MetricThresholdValueValueTypeBoolean**
</dt> <dd>

The data type is Boolean (value of **true** and **false**).

</dd> <dt>

<span id="MetricThresholdValueValueTypeChar"></span><span id="metricthresholdvaluevaluetypechar"></span><span id="METRICTHRESHOLDVALUEVALUETYPECHAR"></span>**MetricThresholdValueValueTypeChar**
</dt> <dd>

The data type is a character whose integer representation is between 0 and 65535.

</dd> <dt>

<span id="MetricThresholdValueValueTypeDateTime"></span><span id="metricthresholdvaluevaluetypedatetime"></span><span id="METRICTHRESHOLDVALUEVALUETYPEDATETIME"></span>**MetricThresholdValueValueTypeDateTime**
</dt> <dd>

The data type is an instant in time, typically expressed as a date and time of day, for example "6/15/2009 1:45:30 PM".

</dd> <dt>

<span id="MetricThresholdValueValueTypeDuration"></span><span id="metricthresholdvaluevaluetypeduration"></span><span id="METRICTHRESHOLDVALUEVALUETYPEDURATION"></span>**MetricThresholdValueValueTypeDuration**
</dt> <dd>

The data type is a time interval.

</dd> <dt>

<span id="MetricThresholdValueValueTypeTimeSpan"></span><span id="metricthresholdvaluevaluetypetimespan"></span><span id="METRICTHRESHOLDVALUEVALUETYPETIMESPAN"></span>**MetricThresholdValueValueTypeTimeSpan**
</dt> <dd>

The data type is a time interval.

</dd> <dt>

<span id="MetricThresholdValueValueTypeFilePath"></span><span id="metricthresholdvaluevaluetypefilepath"></span><span id="METRICTHRESHOLDVALUEVALUETYPEFILEPATH"></span>**MetricThresholdValueValueTypeFilePath**
</dt> <dd>

The data type is a file path.

</dd> <dt>

<span id="MetricThresholdValueValueTypeDirectoryPath"></span><span id="metricthresholdvaluevaluetypedirectorypath"></span><span id="METRICTHRESHOLDVALUEVALUETYPEDIRECTORYPATH"></span>**MetricThresholdValueValueTypeDirectoryPath**
</dt> <dd>

The data type is a directory path.

</dd> <dt>

<span id="MetricThresholdValueValueType_Max"></span><span id="metricthresholdvaluevaluetype_max"></span><span id="METRICTHRESHOLDVALUEVALUETYPE_MAX"></span>**MetricThresholdValueValueType\_Max**
</dt> <dd>

Invalid data type specification (the value of this member is one larger than the largest valid member).

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |



 

 





