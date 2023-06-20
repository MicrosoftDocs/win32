---
title: Multicast Station Attributes
description: Multicast Station Attributes
ms.assetid: 24b81ccb-4030-49a4-802c-5b45f7dd5950
keywords:
- Windows Media Format SDK,attributes
- Advanced Systems Format (ASF),attributes
- ASF (Advanced Systems Format),attributes
- attributes,multicast station
- multicast station attributes
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Multicast Station Attributes

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When a file is streaming from a multicast station, the station can impose some attributes on the file. These attributes, listed in the following table, are not actually stored in the file and are only available when the file is streaming. They contain information about the station and would typically be identical for all content from the station.



| Multicast station attribute                 | Global identifier      | Data type             |
|---------------------------------------------|------------------------|-----------------------|
| [**NSC\_Address**](nsc-address.md)         | g\_wszWMNSCAddress     | **WMT\_TYPE\_STRING** |
| [**NSC\_Description**](nsc-description.md) | g\_wszWMNSCDescription | **WMT\_TYPE\_STRING** |
| [**NSC\_Email**](nsc-email.md)             | g\_wszWMNSCEmail       | **WMT\_TYPE\_STRING** |
| [**NSC\_Name**](nsc-name.md)               | g\_wszWMNSCName        | **WMT\_TYPE\_STRING** |
| [**NSC\_Phone**](nsc-phone.md)             | g\_wszWMNSCPhone       | **WMT\_TYPE\_STRING** |



 

## Related topics

<dl> <dt>

[**Attributes By Type**](attributes-by-type.md)
</dt> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




