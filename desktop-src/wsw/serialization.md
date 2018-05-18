---
title: Serialization
description: Serialization is the process of writing values in C data structures (structs, arrays, and primitive values) as an XML element. Deserialization is the reverse process.
ms.assetid: 'aa092156-30ae-4f8a-baa2-450f38a78153'
keywords: ["Serialization Web Services for Windows", "WWSAPI", "WWS"]
---

# Serialization

Serialization is the process of writing values in C data structures (structs, arrays, and primitive values) as an XML element. Deserialization is the reverse process.

## 

Serialization is the process of writing values in C data structures (structures, arrays, and primitive values) as an XML element. Deserialization is the reverse process.

Both processes rely on a description of the mapping between the C data structures and the XML.

![](images/xmlmapping.png)

To serialize a value, the application calls [**WsWriteElement**](wswriteelement.md), [**WsWriteAttribute**](wswriteattribute.md) or [**WsWriteType**](wswritetype.md).

To deserialize a value, the application calls [**WsReadElement**](wsreadelement.md), [**WsReadAttribute**](wsreadattribute.md) or [**WsReadType**](wsreadtype.md).

## Security

[XML Reader](xml-reader.md) is used in deserialization process. Refer to the security section in XML Reader for XML related security information.

The deserializer continues to deserialize data until it has completed reading the element being deserialized. Deserialization process fails when it encounter any XML document that does not conform to the description of the data being deserialized. At that point XML reader being used becomes invalid, and an error is returned.

By default deserialization is strict. Some conditions that cause deserialization to fail include but not limited to:

-   Expected elements is missing
-   Unexpected element fields appear between required elements
-   Extra element content after required fields, unless [**WS\_STRUCT\_IGNORE\_TRAILING\_ELEMENT\_CONTENT**](ws-struct-options.md)
-   Unexpected attributes, unless [**WS\_STRUCT\_IGNORE\_UNHANDLED\_ATTRIBUTES**](ws-struct-options.md) flag is specified
-   Unexpected data type value that is out of specified range
-   Count of repeating element is out of the specified range

Serializing large amount of data might cause excessive memory allocation and can cause denial of service attack. The user that is deserializing data must specify a Heap object to allocate the data, and the user can use the heap allocation limit to prevent memory allocation attack.

Range support for data types, including max length for string, max element count in array, etc. allows the user to control the maximum size for different data types. User can specify range in data description or schema to limit the maximum size of different data.

A string value containing an embedded zero is supported in the wire formats (text, binary, MTOM). When deserializing a string with an embedded zero, the user should use a counted string (WS\_STRING) so the zero will not confuse the calculation of the length of the string. If a string value containing an embedded zero is deserialized into a field that is expecting a zero-terminated string, an error is returned, and deserialization fails. If wsutil is used to generate data descriptions, /string:WS\_STRING option should be used if string with embedded zero is expected.

The following callbacks are used with serialization:

-   [**WS\_DURATION\_COMPARISON\_CALLBACK**](ws-duration-comparison-callback.md)
-   [**WS\_READ\_TYPE\_CALLBACK**](ws-read-type-callback.md)
-   [**WS\_WRITE\_TYPE\_CALLBACK**](ws-write-type-callback.md)

The following enumerations are used with serialization:

-   [**WS\_FIELD\_MAPPING**](ws-field-mapping.md)
-   [**WS\_FIELD\_OPTIONS**](ws-field-options.md)
-   [**WS\_READ\_OPTION**](ws-read-option.md)
-   [**WS\_TYPE**](ws-type.md)
-   [**WS\_TYPE\_MAPPING**](ws-type-mapping.md)
-   [**WS\_WRITE\_OPTION**](ws-write-option.md)

The following functions are used with serialization:

-   [**WsReadAttribute**](wsreadattribute.md)
-   [**WsReadElement**](wsreadelement.md)
-   [**WsReadType**](wsreadtype.md)
-   [**WsWriteAttribute**](wswriteattribute.md)
-   [**WsWriteElement**](wswriteelement.md)
-   [**WsWriteType**](wswritetype.md)

The following structures are used with serialization:

-   [**WS\_ATTRIBUTE\_DESCRIPTION**](ws-attribute-description.md)
-   [**WS\_BOOL\_DESCRIPTION**](ws-bool-description.md)
-   [**WS\_BYTES\_DESCRIPTION**](ws-bytes-description.md)
-   [**WS\_BYTE\_ARRAY\_DESCRIPTION**](ws-byte-array-description.md)
-   [**WS\_CHAR\_ARRAY\_DESCRIPTION**](ws-char-array-description.md)
-   [**WS\_CUSTOM\_TYPE\_DESCRIPTION**](ws-custom-type-description.md)
-   [**WS\_DATETIME\_DESCRIPTION**](ws-datetime-description.md)
-   [**WS\_DECIMAL\_DESCRIPTION**](ws-decimal-description.md)
-   [**WS\_DEFAULT\_VALUE**](ws-default-value.md)
-   [**WS\_DOUBLE\_DESCRIPTION**](ws-double-description.md)
-   [**WS\_DURATION\_DESCRIPTION**](ws-duration-description.md)
-   [**WS\_ELEMENT\_DESCRIPTION**](ws-element-description.md)
-   [**WS\_ENDPOINT\_ADDRESS\_DESCRIPTION**](ws-endpoint-address-description.md)
-   [**WS\_ENUM\_DESCRIPTION**](ws-enum-description.md)
-   [**WS\_ENUM\_VALUE**](ws-enum-value.md)
-   [**WS\_FAULT\_DESCRIPTION**](ws-fault-description.md)
-   [**WS\_FIELD\_DESCRIPTION**](ws-field-description.md)
-   [**WS\_FLOAT\_DESCRIPTION**](ws-float-description.md)
-   [**WS\_GUID\_DESCRIPTION**](ws-guid-description.md)
-   [**WS\_INT16\_DESCRIPTION**](ws-int16-description.md)
-   [**WS\_INT32\_DESCRIPTION**](ws-int32-description.md)
-   [**WS\_INT64\_DESCRIPTION**](ws-int64-description.md)
-   [**WS\_INT8\_DESCRIPTION**](ws-int8-description.md)
-   [**WS\_ITEM\_RANGE**](ws-item-range.md)
-   [**WS\_STRING\_DESCRIPTION**](ws-string-description.md)
-   [**WS\_STRUCT\_DESCRIPTION**](ws-struct-description.md)
-   [**WS\_TIMESPAN\_DESCRIPTION**](ws-timespan-description.md)
-   [**WS\_UINT16\_DESCRIPTION**](ws-uint16-description.md)
-   [**WS\_UINT32\_DESCRIPTION**](ws-uint32-description.md)
-   [**WS\_UINT64\_DESCRIPTION**](ws-uint64-description.md)
-   [**WS\_UINT8\_DESCRIPTION**](ws-uint8-description.md)
-   [**WS\_UNION\_DESCRIPTION**](ws-union-description.md)
-   [**WS\_UNION\_FIELD\_DESCRIPTION**](ws-union-field-description.md)
-   [**WS\_UNIQUE\_ID\_DESCRIPTION**](ws-unique-id-description.md)
-   [**WS\_UTF8\_ARRAY\_DESCRIPTION**](ws-utf8-array-description.md)
-   [**WS\_VOID\_DESCRIPTION**](ws-void-description.md)
-   [**WS\_WSZ\_DESCRIPTION**](ws-wsz-description.md)
-   [**WS\_XML\_QNAME\_DESCRIPTION**](ws-xml-qname-description.md)
-   [**WS\_XML\_STRING\_DESCRIPTION**](ws-xml-string-description.md)

 

 




