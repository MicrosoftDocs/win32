---
description: A data object has the following syntax definition.
ms.assetid: e636c2eb-3c11-45bf-ab0b-a14ec878742c
title: Data (X file format)
ms.topic: article
ms.date: 05/31/2018
---

# Data (X file format, binary encoding)

A data object has the following syntax definition.


```
object                : identifier optional_name TOKEN_OBRACE
                            optional_class_id
                            data_parts_list
                            TOKEN_CBRACE

data_parts_list       : data_part
                      | data_parts_list data_part

data_part             : data_reference
                      | object
                      | number_list
                      | float_list
                      | string_list

number_list           : TOKEN_INTEGER_LIST

float_list            : TOKEN_FLOAT_LIST

string_list           : string_list_1 list_separator

string_list_1         : string
                      | string_list_1 list_separator string

list_separator        : comma
                      | semicolon

string                : token_string

identifier            : name
                      | primitive_type

data_reference        : TOKEN_OBRACE name optional_class_id TOKEN_CBRACE
```



Note that in number\_list and float\_list data in binary files, TOKEN\_COMMA and TOKEN\_SEMICOLON are not used. The comma and semicolon are used in string\_list data. Also note that you can only use data\_reference for optional data members.

## Related topics

<dl> <dt>

[Binary Encoding](binary-encoding.md)
</dt> </dl>

 

 



