---
title: ServiceInfo Element
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The ServiceInfo element is the main element for the ServiceInfo.xml document.
ms.assetid: d2f9e642-143e-405d-8588-c78e4355b9b9
keywords:
- ServiceInfo Element Windows Media Player
topic_type:
- apiref
api_name:
- ServiceInfo Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# ServiceInfo Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **ServiceInfo** element is the main element for the ServiceInfo.xml document.

``` syntax
<ServiceInfo
    Version = 1.00
    Key = "service key"
    ContentPartner = "true|false"
/>
```

## Attributes



| Term                                                                                                                                             | Description                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Version__optional_"></span><span id="version__optional_"></span><span id="VERSION__OPTIONAL_"></span>**Version** (optional)<br/> | Version of the ServiceInfo.xml file. Version 1.00 is supported for Windows Media Player.<br/>                                                                                                                                                            |
| <span id="Key__required_"></span><span id="key__required_"></span><span id="KEY__REQUIRED_"></span>**Key** (required)<br/>                 | The service key string that uniquely identifies the online store.<br/>                                                                                                                                                                                   |
| <span id="ContentPartner"></span><span id="contentpartner"></span><span id="CONTENTPARTNER"></span>**ContentPartner**<br/>                 | Indicates whether the online store is a type 1 store. A value of "true" indicates that the store is a type 1 store. A value of "false" indicates that the store is not a type 1 store; that is, it is a type 2 store. The default value is "false".<br/> |



 

## Parent/Child Elements



| Hierarchy       | Element                                                                                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parent elements | None                                                                                                                                                                               |
| Child elements  | **AlbumInfo**, **BuyCD**, **Color**, **Description**, **FriendlyName**, **HTMLView**, **Image**, **InfoCenter**, **Install**, **ServiceTask1**, **ServiceTask2**, **ServiceTask3** |



 

## Remarks

The following table details the parameters sent with the URL request. Others may be present for legacy compatibility purposes. The request will also include any parameters you specified using the ServiceExtra command-line parameter of Windows Media Player setup.



| Name         | Value                                                                                                                                                               |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *geoid*      | Windows geographical location ID. The location ID is specified by the user in the **Location** area of the Regional and Language Options settings in Control Panel. |
| *locale*     | Windows Media Player locale ID.                                                                                                                                     |
| *userlocale* | Windows locale ID. The locale is specified by the user in the **Standards and Formats** area of the Regional and Language Options settings in Control Panel.        |
| *version*    | Windows Media Player version number using the following format: 10.0.x.xxxx or 11.0.x.xxxx.                                                                         |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------|
| Version<br/> | Windows Media Player 10 or later.<br/> |



## See also

<dl> <dt>

[**Example ServiceInfo Document for a Type 1 Online Store**](example-serviceinfo-document-for-a-type-1-online-store.md)
</dt> <dt>

[**Example ServiceInfo Document for a Type 2 Online Store**](example-serviceinfo-document-for-a-type-2-online-store.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> </dl>

 

 





