---
title: StandardType element
description: Specifies the numeric, logical or character data type.
ms.assetid: 'FAEBDCA3-F502-4E88-AA72-5858F1F2F91D'
keywords: ["StandardType element Access Execution Engine"]
topic_type:
- apiref
api_name:
- StandardType
api_type:
- Schema
---

# StandardType element

Specifies the numeric, logical or character data type.

## Usage

``` syntax
<StandardType>
  child elements
</StandardType>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                | Description                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Boolean**](boolean.md)<br/>                  | The data type is Boolean (value of **true** and **false**).<br/> <br/>                                                                                                                                                                                                 |
| [**Byte**](byte.md)<br/>                        | The data type is an unsigned integer value between 0 and 255.<br/> <br/>                                                                                                                                                                                               |
| [**Char**](char.md)<br/>                        | The data type is a character whose integer representation is between 0 and 65535.<br/> <br/>                                                                                                                                                                           |
| [**DateTime**](datetime.md)<br/>                | The data type is an instant in time, typically expressed as a date and time of day, for example "6/15/2009 1:45:30 PM".<br/> <br/>                                                                                                                                     |
| [**DirectoryPath**](directorypath.md)<br/>      | The data type is a directory path.<br/> <br/>                                                                                                                                                                                                                          |
| [**Double**](double.md)<br/>                    | The data type is a double-precision 64-but floating point number whose values range from -1.7976931348623157E+308 to 1.7976931348623157E+308, as well as positive or negative zero, **PositiveInfinity**, **NegativeInfinity**, and not a number (**NaN**).<br/> <br/> |
| [**Duration**](duration.md)<br/>                | The data type is a time interval<br/> <br/>                                                                                                                                                                                                                            |
| [**FilePath**](filepath--standardtype-.md)<br/> | The data type is a file path.<br/> <br/>                                                                                                                                                                                                                               |
| [**Int16**](int16.md)<br/>                      | The data type is an integer value between -32768 and 32767.<br/> <br/>                                                                                                                                                                                                 |
| [**Int32**](int32.md)<br/>                      | The data type is an integer value between -2,147,483,648 and 2,147,483,647.<br/> <br/>                                                                                                                                                                                 |
| [**Int64**](int64.md)<br/>                      | The data type is an integer value between and -9,223,372,036,854,775,808 and 9,223,372,036,854,775,807.<br/> <br/>                                                                                                                                                     |
| [**SByte**](sbyte.md)<br/>                      | The data type is an integer value between -128 and 127.<br/> <br/>                                                                                                                                                                                                     |
| [**Single**](single.md)<br/>                    | The data type is a single-precision 32-but floating point number whose values range from -3.402823e38 to 3.402823e38, as well as positive or negative zero, **PositiveInfinity**, **NegativeInfinity**, and not a number (**NaN**).<br/> <br/>                         |
| [**String**](string.md)<br/>                    | The data type is a character string.<br/> <br/>                                                                                                                                                                                                                        |
| [**TimeSpan**](timespan.md)<br/>                | The data type is a time interval.<br/> <br/>                                                                                                                                                                                                                           |
| [**UInt16**](uint16.md)<br/>                    | The data type is an unsigned integer value between 0 and 65535.<br/> <br/>                                                                                                                                                                                             |
| [**UInt32**](uint32.md)<br/>                    | The data type is an unsigned integer value between 0 and 4,294,967,295.<br/> <br/>                                                                                                                                                                                     |
| [**UInt64**](uint64.md)<br/>                    | The data type is an unsigned integer value between 0 and 18,446,744,073,709,551,615.<br/> <br/>                                                                                                                                                                        |



### Child element sequence

``` syntax
StringInt16Int32Int64UInt16UInt32UInt64ByteSByteSingleDoubleBooleanCharDateTimeDurationTimeSpanFilePathDirectoryPath
```

## Parent elements



| Element                                                       | Description                                                                          |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**MetricDefinition**](metricdefinition.md)<br/>       | This element describes the metrics produced by an assessment.<br/> <br/> |
| [**ParameterDefinition**](parameterdefinition.md)<br/> | Information that fully describes an assessment parameter. <br/> <br/>    |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



 

 





