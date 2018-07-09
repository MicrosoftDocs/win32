---
title: FilterListType Complex Type
description: Defines a list of filters that an ETW controller can pass to your provider to further limit the events that it writes.
ms.assetid: 27f7b150-1264-4a12-858e-b0b0dff5baa7
keywords:
- FilterListType complex type EventLog
topic_type:
- apiref
api_name:
- FilterListType
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# FilterListType Complex Type

Defines a list of filters that an ETW controller can pass to your provider to further limit the events that it writes.

``` syntax
<xs:complexType name="FilterListType">
    <xs:sequence>
        <xs:element name="filter"
            type="FilterType"
            minOccurs="0"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element    | Type                                                             | Description                   |
|------------|------------------------------------------------------------------|-------------------------------|
| **filter** | [**FilterType**](eventmanifestschema-filtertype-complextype.md) | A list of filters.<br/> |



## Remarks

An ETW controller is an application that calls the [**StartTrace**](https://msdn.microsoft.com/library/windows/desktop/aa364117) function to create an ETW session. For details, see [Controlling Event Tracing Sessions](https://msdn.microsoft.com/library/windows/desktop/aa363694). The controller can use the [**TdhEnumerateProviderFilters**](https://msdn.microsoft.com/library/windows/desktop/dd392324) function to enumerate the filters that you define. The controller can then pass one or more of the filters when it calls the [**EnableTraceEx2**](https://msdn.microsoft.com/library/windows/desktop/dd392305) function to enable your provider. Your provider receives the filters, along with the rest of the enable parameters, in your [*EnableCallback*](https://msdn.microsoft.com/library/windows/desktop/aa363707) callback function.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 





