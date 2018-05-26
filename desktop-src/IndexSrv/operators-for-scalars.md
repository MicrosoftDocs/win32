---
title: Operators for Scalars
description: Operators for Scalars
ms.assetid: e44d8dd7-a323-41ff-a3b6-84104b4e4160
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Operators for Scalars

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following list describes the operators for scalars.

<dl> <dt>

<span id="DBOP_scalar_parameter"></span><span id="dbop_scalar_parameter"></span><span id="DBOP_SCALAR_PARAMETER"></span>DBOP\_scalar\_parameter
</dt> <dd>

Scalar parameter, named by a string. The name must be unique within all parameters for the command, including the parameters of SQL commands in textual nodes in the same command tree. This operator does not take any input and produces scalar output.

</dd> <dt>

<span id="DBOP_scalar_function"></span><span id="dbop_scalar_function"></span><span id="DBOP_SCALAR_FUNCTION"></span>DBOP\_scalar\_function
</dt> <dd>

A scalar function identified by name, globally unique identifier (GUID), etc., similar to a column name. The number of arguments (inputs) depends on the function; it produces scalar output.

</dd> <dt>

<span id="DBOP_plus__DBOP_minus__DBOP_times__DBOP_over__DBOP_div__DBOP_modulo__DBOP_power"></span><span id="dbop_plus__dbop_minus__dbop_times__dbop_over__dbop_div__dbop_modulo__dbop_power"></span><span id="DBOP_PLUS__DBOP_MINUS__DBOP_TIMES__DBOP_OVER__DBOP_DIV__DBOP_MODULO__DBOP_POWER"></span>DBOP\_plus, DBOP\_minus, DBOP\_times, DBOP\_over, DBOP\_div, DBOP\_modulo, DBOP\_power
</dt> <dd>

Standard arithmetic. "div" always returns an integer result, such that "(a div b) times b plus a modulo b == a" for all nonzero values for b. These operators require two scalar inputs and produce a scalar result.

</dd> <dt>

<span id="DBOP_like__DBOP_sounds_like"></span><span id="dbop_like__dbop_sounds_like"></span><span id="DBOP_LIKE__DBOP_SOUNDS_LIKE"></span>DBOP\_like, DBOP\_sounds\_like
</dt> <dd>

Regular expression matching. These operators require two string inputs. For DBOP\_like, the operator node includes a globally unique identifier (GUID) for the language or system whose regular expression syntax is to be used. Fixed GUIDs are assigned for SQL, MS-DOS,‹ OFS,› and Messaging Application Programming Interface (MAPI). Boolean result. The DBOP\_like node uses the [**DBLIKE**](dblike.md) structure to hold the GUID and a weight.

</dd> <dt>

<span id="DBOP_like_any__DBOP_like_all"></span><span id="dbop_like_any__dbop_like_all"></span><span id="DBOP_LIKE_ANY__DBOP_LIKE_ALL"></span>DBOP\_like\_any, DBOP\_like\_all
</dt> <dd>

Regular expression matching. These operators take a scalar first input and a table-valued second input and produce a Boolean output.

</dd> <dt>

<span id="DBOP_is_INVALID__DBOP_is_TRUE__DBOP_is_FALSE"></span><span id="dbop_is_invalid__dbop_is_true__dbop_is_false"></span><span id="DBOP_IS_INVALID__DBOP_IS_TRUE__DBOP_IS_FALSE"></span>DBOP\_is\_INVALID, DBOP\_is\_TRUE, DBOP\_is\_FALSE
</dt> <dd>

SQL's tests on predicates. These operators take one scalar input and produce a Boolean result.

</dd> <dt>

<span id="DBOP_overlaps__DBOP_case_condition__DBOP_case_value__DBOP_nullif__DBOP_cast__DBOP_coalesce__DBOP_position__DBOP_extract__DBOP_char_length__DBOP_octet_length__DBOP_bit_length__DBOP_substring__DBOP_upper__DBOP_lower__DBOP_trim__DBOP_translate__DBOP_convert__DBOP_string_concat__DBOP_current_date__DBOP_current_time__DBOP_current_timestamp"></span><span id="dbop_overlaps__dbop_case_condition__dbop_case_value__dbop_nullif__dbop_cast__dbop_coalesce__dbop_position__dbop_extract__dbop_char_length__dbop_octet_length__dbop_bit_length__dbop_substring__dbop_upper__dbop_lower__dbop_trim__dbop_translate__dbop_convert__dbop_string_concat__dbop_current_date__dbop_current_time__dbop_current_timestamp"></span><span id="DBOP_OVERLAPS__DBOP_CASE_CONDITION__DBOP_CASE_VALUE__DBOP_NULLIF__DBOP_CAST__DBOP_COALESCE__DBOP_POSITION__DBOP_EXTRACT__DBOP_CHAR_LENGTH__DBOP_OCTET_LENGTH__DBOP_BIT_LENGTH__DBOP_SUBSTRING__DBOP_UPPER__DBOP_LOWER__DBOP_TRIM__DBOP_TRANSLATE__DBOP_CONVERT__DBOP_STRING_CONCAT__DBOP_CURRENT_DATE__DBOP_CURRENT_TIME__DBOP_CURRENT_TIMESTAMP"></span>DBOP\_overlaps, DBOP\_case\_condition, DBOP\_case\_value, DBOP\_nullif, DBOP\_cast, DBOP\_coalesce, DBOP\_position, DBOP\_extract, DBOP\_char\_length, DBOP\_octet\_length, DBOP\_bit\_length, DBOP\_substring, DBOP\_upper, DBOP\_lower, DBOP\_trim, DBOP\_translate, DBOP\_convert, DBOP\_string\_concat, DBOP\_current\_date, DBOP\_current\_time, DBOP\_current\_timestamp
</dt> <dd></dd> </dl>

 

 




