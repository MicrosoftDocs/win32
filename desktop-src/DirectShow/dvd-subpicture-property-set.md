---
description: DVD Subpicture properties control the color, contrast, and output of the subpicture display.
ms.assetid: ddbfb65c-7630-4e9f-8013-c5d65c62c628
title: DVD Subpicture Property Set (Dvdmedia.h)
ms.topic: reference
ms.date: 05/31/2018
---

# DVD Subpicture Property Set

DVD Subpicture properties control the color, contrast, and output of the subpicture display.

The following information presents the necessary constants and data types to use for this property set in calls to [**IKsPropertySet**](ikspropertyset.md) methods. It provides values for the **GUID** (*guidPropSet*), property ID (*dwPropID*), and property data type (*pPropData*) parameters.



| Label | Value |
|-------------------|----------------------------|
| Property Set GUID | AM\_KSPROPSETID\_DvdSubPic |



 



| Property ID                           | Description                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AM\_PROPERTY\_DVDSUBPIC\_COMPOSIT\_ON | Set-only property that enables or disables subpicture display. DirectShow defines the **AM\_PROPERTY\_COMPOSIT\_ON** Boolean data type for this property, as well as PAM\_PROPERTY\_COMPOSIT\_ON as a pointer to this data type. **TRUE** indicates display the subpicture, **FALSE** indicates disable it. See the WDM portion of the Windows DDK for more information. |
| AM\_PROPERTY\_DVDSUBPIC\_HLI          | Set-only property that specifies a rectangle of subpicture or screen whose color or contrast will be changed. Data type is [**AM\_PROPERTY\_SPHLI**](/previous-versions/windows/desktop/api/Dvdmedia/ns-dvdmedia-am_property_sphli). See Remarks.                                                                                                                                                                                |
| AM\_PROPERTY\_DVDSUBPIC\_PALETTE      | Sets the palette for a subpicture. Data type is [**AM\_PROPERTY\_SPPAL**](/previous-versions/windows/desktop/api/Dvdmedia/ns-dvdmedia-am_property_sppal).                                                                                                                                                                                                                                                                        |



 

## Remarks

The **AM\_PROPERTY\_DVDSUBPIC\_HLI** property is set-only. It specifies a rectangle of subpicture or screen whose color or contrast will be changed. This differs from the DVD-Video specification, in that the Microsoft DVD navigator parses all button and keyboard information and passes only one highlight rectangle to the subpicture decoder at any given time. As a result, highlight information is sent to the decoder more often than it is present in the DVD stream.

The highlight information arrives asynchronously to the data stream. The decoder uses the highlight Start and End time stamps to correlate the highlight information to the relevant subpicture information, if any. If the decoder has not received any subpicture stream information for the requested time stamps, the decoder assumes that the highlight information is stand-alone and does not apply to a subpicture. In this case, the decoder assumes the color and contrast information is all the same color.

The data is not entirely in DVD disc format. Microsoft provides an additional structure of type [**AM\_PROPERTY\_SPHLI**](/previous-versions/windows/desktop/api/Dvdmedia/ns-dvdmedia-am_property_sphli) that is passed as the parameter to this property. This structure describes the currently selected button from the DVD highlight information.

The DVD navigator processes all keystroke information and sends new highlight information each time a button state changes. The information describes only one mode of one button at a time. It includes a display rectangle in pixel coordinates of the screen, or a display of the subpicture, if present. The structure also contains color and contrast information, but only for the present state of the currently selected button. The format is defined in the DVD specification.

Highlight information contains Start and End time stamps. These are in the same units as other time stamps, with two exceptions: A Start time stamp of 0xFFFFFFFF means the highlight property is effective upon receipt, and an End time stamp of 0xFFFFFFFF means the highlight property is valid until next highlight received.

The HLISS field is as defined in the DVD specification. A value of zero indicates that all highlights are invalid and the decoder should disable all highlights.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdmedia.h</dt> </dl> |



## See also

<dl> <dt>

[Property Sets](property-sets.md)
</dt> </dl>

 

 




