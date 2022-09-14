---
title: Editing Metadata Attributes
description: Editing Metadata Attributes
ms.assetid: 96c979e2-c616-45e3-9c60-a24f03e29dc4
keywords:
- Windows Media Format SDK,editing metadata attributes
- Advanced Systems Format (ASF),editing metadata attributes
- ASF (Advanced Systems Format),editing metadata attributes
- metadata,editing attributes
ms.topic: article
ms.date: 05/31/2018
---

# Editing Metadata Attributes

Editing metadata attributes is very similar to setting new ones. Instead of using [**IWMHeaderInfo3::AddAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo3-addattribute), use [**IWMHeaderInfo3::ModifyAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo3-modifyattribute). **ModifyAttribute** is identical to **AddAttribute** except that you do not specify an attribute name, and the index number is an input parameter instead of an output.

You can use stream number 0xFFFF to specify an attribute to modify using its global index.

## Related topics

<dl> <dt>

[**Working with Metadata**](working-with-metadata.md)
</dt> </dl>

 

 




