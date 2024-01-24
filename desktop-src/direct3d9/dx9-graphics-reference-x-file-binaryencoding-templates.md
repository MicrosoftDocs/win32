---
description: A template has the following syntax definition.
ms.assetid: 77eb739d-8da3-4481-8dd1-f9f2f0eda136
title: Templates (X file format)
ms.topic: article
ms.date: 05/31/2018
---

# Templates (X file format, binary encoding)

A template has the following syntax definition.


```
template              : TOKEN_TEMPLATE name TOKEN_OBRACE
                            class_id
                            template_parts
                            TOKEN_CBRACE

template_parts        : template_members_part TOKEN_OBRACKET
                        template_option_info
                        TOKEN_CBRACKET
                      | template_members_list

template_members_part : /* Empty */
                      | template_members_list

template_option_info  : ellipsis
                      | template_option_list

template_members_list :    template_members
                      | template_members_list template_members

template_members      : primitive
                      | array
                      | template_reference

primitive             : primitive_type optional_name TOKEN_SEMICOLON

array                 : TOKEN_ARRAY array_data_type name dimension_list
                        TOKEN_SEMICOLON

template_reference    : name optional_name YT_SEMICOLON

primitive_type        : TOKEN_WORD
                      | TOKEN_DWORD
                      | TOKEN_FLOAT
                      | TOKEN_DOUBLE
                      | TOKEN_CHAR
                      | TOKEN_UCHAR
                      | TOKEN_SWORD
                      | TOKEN_SDWORD
                      | TOKEN_LPSTR
                      | TOKEN_UNICODE
                      | TOKEN_CSTRING

array_data_type       : primitive_type
                      | name

dimension_list        : dimension
                      | dimension_list dimension

dimension             : TOKEN_OBRACKET dimension_size TOKEN_CBRACKET

dimension_size        : TOKEN_INTEGER
                      | name

template_option_list  : template_option_part
                      | template_option_list template_option_part

template_option_part  : name optional_class_id

name                  : TOKEN_NAME

optional_name         : /* Empty */
                      | name

class_id              : TOKEN_GUID

optional_class_id     : /* Empty */
                      | class_id

ellipsis              : TOKEN_DOT TOKEN_DOT TOKEN_DOT
```



## Related topics

<dl> <dt>

[Binary Encoding](binary-encoding.md)
</dt> </dl>

 

 



