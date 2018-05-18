---
title: ImageProcess object
description: Manages the Filter chain. An ImageProcess object can be created using \ 0034;WIA.ImageProcess \ 0034; as the ProgID in a call to CreateObject.
ms.assetid: '98594336-34d1-4184-a1a4-fbdb71c17f00'
keywords: ["ImageProcess object WIA Automation", "ImageProcess object WIA Automation , described"]
topic_type:
- apiref
api_name:
- ImageProcess
api_location:
- Wiaaut.h
api_type:
- COM
---

# ImageProcess object

Manages the [**Filter**](-wiaaut-filter.md) chain. An **ImageProcess** object can be created using "WIA.ImageProcess" as the ProgID in a call to [CreateObject](http://msdn.microsoft.com/library/7t9k08y5(VS.71).aspx).

## Members

The **ImageProcess** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ImageProcess** object has these methods.



| Method                                       | Description                                                                     |
|:---------------------------------------------|:--------------------------------------------------------------------------------|
| [**Apply**](-wiaaut-iimageprocess-apply.md) | Applies filters to an [**ImageFile**](-wiaaut-imagefile.md) object.<br/> |



 

### Properties

The **ImageProcess** object has these properties.



| Property                                                                           | Access type          | Description                                                                     |
|:-----------------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------|
| [**FilterInfos (ImageProcess)**](-wiaaut-iimageprocess-filterinfos.md)<br/> | Read-only<br/> | Retrieves a collection of all available filters.<br/>                     |
| [**Filters (ImageProcess)**](-wiaaut-iimageprocess-filters.md)<br/>         | Read-only<br/> | Retrieves a collection of the filters to be applied in this process.<br/> |



 

## Remarks

Note that the **ImageProcess** object contains the [**FilterInfos (ImageProcess)**](-wiaaut-iimageprocess-filterinfos.md) collection of all available filters, the [**Filters (ImageProcess)**](-wiaaut-iimageprocess-filters.md) collection of those filters to be applied to an [**ImageFile**](-wiaaut-imagefile.md), and the [**Apply**](-wiaaut-iimageprocess-apply.md) method to apply those Filters to an **ImageFile**.

For example code, see [Convert Filter: Create a Compressed JPEG File from Another File](-wiaaut-howto-use-filters.md#convert-filter-create-a-compressed-jpeg-file-from-another-file).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Apply**](-wiaaut-iimageprocess-apply.md)
</dt> </dl>

 

 





