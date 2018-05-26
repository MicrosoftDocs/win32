---
title: Serialization
description: Serialization is the process of writing values in C data structures (structs, arrays, and primitive values) as an XML element. Deserialization is the reverse process.
ms.assetid: aa092156-30ae-4f8a-baa2-450f38a78153
keywords:
- Serialization Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Serialization

Serialization is the process of writing values in C data structures (structs, arrays, and primitive values) as an XML element. Deserialization is the reverse process.

## 

Serialization is the process of writing values in C data structures (structures, arrays, and primitive values) as an XML element. Deserialization is the reverse process.

Both processes rely on a description of the mapping between the C data structures and the XML.

![](images/xmlmapping.png)

To serialize a value, the application calls [**WsWriteElement**](/windows/win32/WebServices/nf-webservices-wswriteelement?branch=master), [**WsWriteAttribute**](/windows/win32/WebServices/nf-webservices-wswriteattribute?branch=master) or [**WsWriteType**](/windows/win32/WebServices/nf-webservices-wswritetype?branch=master).

To deserialize a value, the application calls [**WsReadElement**](/windows/win32/WebServices/nf-webservices-wsreadelement?branch=master), [**WsReadAttribute**](/windows/win32/WebServices/nf-webservices-wsreadattribute?branch=master) or [**WsReadType**](/windows/win32/WebServices/nf-webservices-wsreadtype?branch=master).

## Security

[XML Reader](xml-reader.md) is used in deserialization process. Refer to the security section in XML Reader for XML related security information.

The deserializer continues to deserialize data until it has completed reading the element being deserialized. Deserialization process fails when it encounter any XML document that does not conform to the description of the data being deserialized. At that point XML reader being used becomes invalid, and an error is returned.

By default deserialization is strict. Some conditions that cause deserialization to fail include but not limited to:

-   Expected elements is missing
-   Unexpected element fields appear between required elements
-   Extra element content after required fields, unless [**WS\_STRUCT\_IGNORE\_TRAILING\_ELEMENT\_CONTENT**](/windows/win32/WebServices/?branch=master)
-   Unexpected attributes, unless [**WS\_STRUCT\_IGNORE\_UNHANDLED\_ATTRIBUTES**](/windows/win32/WebServices/?branch=master) flag is specified
-   Unexpected data type value that is out of specified range
-   Count of repeating element is out of the specified range

Serializing large amount of data might cause excessive memory allocation and can cause denial of service attack. The user that is deserializing data must specify a Heap object to allocate the data, and the user can use the heap allocation limit to prevent memory allocation attack.

Range support for data types, including max length for string, max element count in array, etc. allows the user to control the maximum size for different data types. User can specify range in data description or schema to limit the maximum size of different data.

A string value containing an embedded zero is supported in the wire formats (text, binary, MTOM). When deserializing a string with an embedded zero, the user should use a counted string (WS\_STRING) so the zero will not confuse the calculation of the length of the string. If a string value containing an embedded zero is deserialized into a field that is expecting a zero-terminated string, an error is returned, and deserialization fails. If wsutil is used to generate data descriptions, /string:WS\_STRING option should be used if string with embedded zero is expected.

The following callbacks are used with serialization:

-   [**WS\_DURATION\_COMPARISON\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_duration_comparison_callback?branch=master)
-   [**WS\_READ\_TYPE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_read_type_callback?branch=master)
-   [**WS\_WRITE\_TYPE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_write_type_callback?branch=master)

The following enumerations are used with serialization:

-   [**WS\_FIELD\_MAPPING**](/windows/win32/WebServices/ne-webservices-ws_field_mapping?branch=master)
-   [**WS\_FIELD\_OPTIONS**](/windows/win32/WebServices/?branch=master)
-   [**WS\_READ\_OPTION**](/windows/win32/WebServices/ne-webservices-ws_read_option?branch=master)
-   [**WS\_TYPE**](/windows/win32/WebServices/ne-webservices-ws_type?branch=master)
-   [**WS\_TYPE\_MAPPING**](/windows/win32/WebServices/ne-webservices-ws_type_mapping?branch=master)
-   [**WS\_WRITE\_OPTION**](/windows/win32/WebServices/ne-webservices-ws_write_option?branch=master)

The following functions are used with serialization:

-   [**WsReadAttribute**](/windows/win32/WebServices/nf-webservices-wsreadattribute?branch=master)
-   [**WsReadElement**](/windows/win32/WebServices/nf-webservices-wsreadelement?branch=master)
-   [**WsReadType**](/windows/win32/WebServices/nf-webservices-wsreadtype?branch=master)
-   [**WsWriteAttribute**](/windows/win32/WebServices/nf-webservices-wswriteattribute?branch=master)
-   [**WsWriteElement**](/windows/win32/WebServices/nf-webservices-wswriteelement?branch=master)
-   [**WsWriteType**](/windows/win32/WebServices/nf-webservices-wswritetype?branch=master)

The following structures are used with serialization:

-   [**WS\_ATTRIBUTE\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_attribute_description?branch=master)
-   [**WS\_BOOL\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_bool_description?branch=master)
-   [**WS\_BYTES\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_bytes_description?branch=master)
-   [**WS\_BYTE\_ARRAY\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_byte_array_description?branch=master)
-   [**WS\_CHAR\_ARRAY\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_char_array_description?branch=master)
-   [**WS\_CUSTOM\_TYPE\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_custom_type_description?branch=master)
-   [**WS\_DATETIME\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_datetime_description?branch=master)
-   [**WS\_DECIMAL\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_decimal_description?branch=master)
-   [**WS\_DEFAULT\_VALUE**](/windows/win32/WebServices/ns-webservices-_ws_default_value?branch=master)
-   [**WS\_DOUBLE\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_double_description?branch=master)
-   [**WS\_DURATION\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_duration_description?branch=master)
-   [**WS\_ELEMENT\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_element_description?branch=master)
-   [**WS\_ENDPOINT\_ADDRESS\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_endpoint_address_description?branch=master)
-   [**WS\_ENUM\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_enum_description?branch=master)
-   [**WS\_ENUM\_VALUE**](/windows/win32/WebServices/ns-webservices-_ws_enum_value?branch=master)
-   [**WS\_FAULT\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_fault_description?branch=master)
-   [**WS\_FIELD\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_field_description?branch=master)
-   [**WS\_FLOAT\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_float_description?branch=master)
-   [**WS\_GUID\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_guid_description?branch=master)
-   [**WS\_INT16\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_int16_description?branch=master)
-   [**WS\_INT32\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_int32_description?branch=master)
-   [**WS\_INT64\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_int64_description?branch=master)
-   [**WS\_INT8\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_int8_description?branch=master)
-   [**WS\_ITEM\_RANGE**](/windows/win32/WebServices/ns-webservices-_ws_item_range?branch=master)
-   [**WS\_STRING\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_string_description?branch=master)
-   [**WS\_STRUCT\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_struct_description?branch=master)
-   [**WS\_TIMESPAN\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_timespan_description?branch=master)
-   [**WS\_UINT16\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_uint16_description?branch=master)
-   [**WS\_UINT32\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_uint32_description?branch=master)
-   [**WS\_UINT64\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_uint64_description?branch=master)
-   [**WS\_UINT8\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_uint8_description?branch=master)
-   [**WS\_UNION\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_union_description?branch=master)
-   [**WS\_UNION\_FIELD\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_union_field_description?branch=master)
-   [**WS\_UNIQUE\_ID\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_unique_id_description?branch=master)
-   [**WS\_UTF8\_ARRAY\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_utf8_array_description?branch=master)
-   [**WS\_VOID\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_void_description?branch=master)
-   [**WS\_WSZ\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_wsz_description?branch=master)
-   [**WS\_XML\_QNAME\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_xml_qname_description?branch=master)
-   [**WS\_XML\_STRING\_DESCRIPTION**](/windows/win32/WebServices/ns-webservices-_ws_xml_string_description?branch=master)

 

 




