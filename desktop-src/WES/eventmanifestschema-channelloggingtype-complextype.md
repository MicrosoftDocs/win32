---
title: ChannelLoggingType Complex Type
description: Defines the properties of the log file that backs the channel, such as its capacity and whether it is sequential or circular. | ChannelLoggingType Complex Type
ms.assetid: 58da75dd-d303-4a57-8c9b-5fde575c3cbb
keywords:
- ChannelLoggingType complex type EventLog
topic_type:
- apiref
api_name:
- ChannelLoggingType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ChannelLoggingType Complex Type

Defines the properties of the log file that backs the channel, such as its capacity and whether it is sequential or circular.

``` syntax
<xs:complexType name="ChannelLoggingType">
    <xs:sequence
        minOccurs="0"
    >
        <xs:element name="autoBackup"
            type="boolean"
            minOccurs="0"
         />
        <xs:element name="retention"
            type="boolean"
            default="0"
            minOccurs="0"
         />
        <xs:element name="maxSize"
            type="UInt64Type"
            default="1048576"
            minOccurs="0"
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



| Element                                                                         | Type                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**autoBackup**](eventmanifestschema-autobackup-channelloggingtype-element.md) | boolean                                                           | Determines whether to create a new log file when the current log file reaches its maximum size. Set to **true** to request that the service create a new file when the log file reaches its maximum size; otherwise, **false**. You can set [**autoBackup**](eventmanifestschema-autobackup-channelloggingtype-element.md) to **true** only if [**retention**](eventmanifestschema-retention-channelloggingtype-element.md) is set to **true**. The default is **false**.<br/> There is no limit to the number of backup files that the service can create (limited only by available disk space). The backup file names are of the form Archive-*channelName*-*timestamp*.evtx and are located in %windir%\\System32\\winevt\\Logs folder.<br/> |
| [**maxSize**](eventmanifestschema-maxsize-channelloggingtype-element.md)       | [**UInt64Type**](eventmanifestschema-hexint64type-simpletype.md) | The maximum size, in bytes, of the log file. The default (and minimum) value is 1 MB. If the physical log size is less than the configured maximum size and additional space is required in the log to store events, the service will allocate another block of space even if the resulting physical size of the log will be larger than the configured maximum size. The service allocates blocks of 1 MB so the physical size could grow to up to 1 MB larger than the configured max size. <br/>                                                                                                                                                                                                                                                      |
| [**retention**](eventmanifestschema-retention-channelloggingtype-element.md)   | boolean                                                           | Determines whether the log file is a sequential or circular log file. Set to **true** for a sequential log file and **false** for a circular log file. The default is **false** for Admin and Operational channel types and **true** for Analytic and Debug channel types.<br/> To query a circular log, you must first disable the channel.<br/>                                                                                                                                                                                                                                                                                                                                                                                                  |



## Remarks

You can specify the **maxSize** attribute for any channel type.

You can specify the **autoBackup** attribute only for Admin and Operational channel types.

You can set the **retention** attribute to false (circular logging) for Admin and Operational channel types. You can set the **retention** attribute to false (circular logging) for Analytic and Debug channel types but to view the events in the Windows Event Viewer, you will need to first disable the channel. Note that when you enable the channel again, the events are removed from the channel.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





