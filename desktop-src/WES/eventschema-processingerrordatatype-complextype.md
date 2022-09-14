---
title: ProcessingErrorDataType Complex Type
description: Defines an error that occurred while rendering the event data for the event.
ms.assetid: fd1cc78c-1da5-43c5-8c4b-8abe7e1dc1e1
keywords:
- ProcessingErrorDataType complex type EventLog
topic_type:
- apiref
api_name:
- ProcessingErrorDataType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ProcessingErrorDataType Complex Type

Defines an error that occurred while rendering the event data for the event. This can occur if the event data does not match the event data template definition in the manifest.

``` syntax
<xs:complexType name="ProcessingErrorDataType">
    <xs:sequence>
        <xs:element name="ErrorCode"
            type="unsignedInt"
         />
        <xs:element name="DataItemName"
            type="string"
         />
        <xs:element name="EventPayload"
            type="hexBinary"
         />
        <xs:any
            processContents="lax"
            minOccurs="0"
            maxOccurs="unbounded"
            namespace="##other"
         />
    </xs:sequence>
    <xs:anyAttribute
        processContents="lax"
        namespace="##other"
     />
</xs:complexType>
```

## Child elements



| Element                                                                          | Type        | Description                                                                          |
|----------------------------------------------------------------------------------|-------------|--------------------------------------------------------------------------------------|
| [**DataItemName**](eventschema-dataitemname-processingerrordatatype-element.md) | string      | The name of the event data item that caused the error.<br/>                    |
| [**ErrorCode**](eventschema-errorcode-processingerrordatatype-element.md)       | unsignedInt | The error code of the error that occurred while rendering the event data.<br/> |
| [**EventPayload**](eventschema-eventpayload-processingerrordatatype-element.md) | hexBinary   | A binary blob that contains the entire event data.<br/>                        |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





