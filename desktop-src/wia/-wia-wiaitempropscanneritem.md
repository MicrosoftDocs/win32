---
description: The following constants specify the valid set of Windows Image Acquisition (WIA) scanner item properties.
ms.assetid: c7c5b10b-81e8-4a30-b20a-ea187724ddd4
title: Scanner WIA Item Property Constants (Wiadef.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WIA_IPS_AUTO_DESKEW
- WIA_IPS_BRIGHTNESS
- WIA_IPS_CONTRAST
- WIA_IPS_CUR_INTENT
- WIA_IPS_DESKEW_X
- WIA_IPS_DESKEW_Y
- WIA_IPS_DOCUMENT_HANDLING_SELECT
- WIA_IPS_FILM_NODE_NAME
- WIA_IPS_FILM_SCAN_MODE
- WIA_IPS_INVERT
- WIA_IPA_ITEMS_STORED
- WIA_IPS_LAMP
- WIA_IPS_LAMP_AUTO_OFF
- WIA_IPS_MAX_HORIZONTAL_SIZE
- WIA_IPS_MAX_VERTICAL_SIZE
- WIA_IPS_MIN_HORIZONTAL_SIZE
- WIA_IPS_MIN_VERTICAL_SIZE
- WIA_IPS_MIRROR
- WIA_IPS_OPTICAL_XRES
- WIA_IPS_OPTICAL_YRES
- WIA_IPS_ORIENTATION
- WIA_IPS_PAGE_SIZE
- WIA_IPS_PAGE_HEIGHT
- WIA_IPS_PAGE_WIDTH
- WIA_IPS_PAGES
- WIA_IPS_PHOTOMETRIC_INTERP
- WIA_IPS_PREVIEW
- WIA_IPS_PREVIEW_TYPE
- WIA_IPS_ROTATION
- WIA_IPS_SEGMENTATION
- WIA_IPS_SHEET_FEEDER_REGISTRATION
- WIA_IPS_SHOW_PREVIEW_CONTROL
- WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION
- WIA_IPS_THRESHOLD
- WIA_IPS_TRANSFER_CAPABILITIES
- WIA_IPA_UPLOAD_ITEM_SIZE
- WIA_IPS_WARM_UP_TIME
- WIA_IPS_XEXTENT
- WIA_IPS_XPOS
- WIA_IPS_XRES
- WIA_IPS_XSCALING
- WIA_IPS_YEXTENT
- WIA_IPS_YPOS
- WIA_IPS_YRES
- WIA_IPS_YSCALING
api_type: 
- HeaderDef
api_location: 
- wiadef.h
---

# Scanner WIA Item Property Constants

The following constants specify the valid set of Windows Image Acquisition (WIA) scanner item properties.

The prefix "WIA\_IPS\_" indicates an Item Property for Scanner devices and is the naming convention used in C/C++. For scripting purposes these constants use the prefix "ScannerPicture" and are part of the [WiaItemPropertyId](-wia-wiaitempropertyid.md) enumerated type. The corresponding member name from that script enumeration appears in parentheses next to the C/C++ constant name in the following list.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th >Constant/value</th>
<th >Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td ><span id="WIA_IPS_AUTO_DESKEW"></span><span id="wia_ips_auto_deskew"></span><dl> <dt><strong>WIA_IPS_AUTO_DESKEW</strong></dt> <dt>ScannerPictureAutoDeskew</dt> </dl></td>
<td ><blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
<br/> Turns automatic deskew on or off.<br/> Optional for WIA_CATEGORY_FEEDER only.<br/> Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a><br/> The following table has the constants that are valid with this property. 
<table>
<thead>
<tr class="header">
<th>Constant</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_AUTO_DESKEW_ON</td>
<td>Turn on automatic deskew.</td>
</tr>
<tr class="even">
<td>WIA_AUTO_DESKEW_OFF</td>
<td>Turn off automatic deskew.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_BRIGHTNESS"></span><span id="wia_ips_brightness"></span><dl> <dt><strong>WIA_IPS_BRIGHTNESS</strong></dt> <dt>ScannerPictureBrightness</dt> </dl></td>
<td ><p>The image brightness values available within the scanner.</p>
<p>Contains the current hardware brightness setting for the device. An application sets this property to the hardware's brightness value. The minidriver creates and maintains this property.</p>
<p>Values should be mapped in a range from -1000 through 1000, where 1000 corresponds to the maximum brightness, 0 corresponds to normal brightness, and -1000 corresponds to the minimum brightness.</p>
<p>Required for all items in the categories: WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FEEDER_FRONT, WIA_CATEGORY_FEEDER_BACK, and WIA_CATEGORY_FILM. Optional, but recommended, for WIA_CATEGORY_FINISHED_FILE items supporting previews.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_RANGE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_CONTRAST"></span><span id="wia_ips_contrast"></span><dl> <dt><strong>WIA_IPS_CONTRAST</strong></dt> <dt>ScannerPictureContrast</dt> </dl></td>
<td ><p>Contains the current hardware contrast setting for a device. An application sets this property to the hardware's contrast value. The minidriver creates and maintains this property.</p>
<p>Values should be mapped in a range from -1000 through 1000, where -1000 corresponds to the minimum contrast, 0 corresponds to normal contrast, and 1000 corresponds to the maximum contrast.</p>
<p>Required for all items in the categories: WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FEEDER_FRONT, WIA_CATEGORY_FEEDER_BACK, and WIA_CATEGORY_FILM. Optional, but recommended, for WIA_CATEGORY_FINISHED_FILE items supporting previews.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_RANGE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_CUR_INTENT"></span><span id="wia_ips_cur_intent"></span><dl> <dt><strong>WIA_IPS_CUR_INTENT</strong></dt> <dt>ScannerPictureCurIntent</dt> </dl></td>
<td ><p>Contains the current intent settings. The minidriver creates and maintains this property.</p>
<p>Required for all acquisition enabled items; that is, items in the categories: WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FEEDER_FRONT, WIA_CATEGORY_FEEDER_BACK, and WIA_CATEGORY_FILM. It is not supported for WIA_CATEGORY_FINISHED_FILE or WIA_CATEGORY_FOLDER items.</p>
<p>Type: <strong>VT_I4</strong> Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_FLAGS</a></p>
<p>The driver uses these to preset item properties based on an application's intended use of the image. This might include, for example, maximum quality, minimum size, and so on.</p>
<p>The driver chooses the bit depth, in dots per inch, and other settings that it determines are appropriate for the selected intent. It is up to the application to read the current settings to determine which properties were changed. An application sets this property to auto-set the WIA properties for specific acquisition intent. This property is required for all scanners.</p>
<p>An application sets this property to auto-set the WIA properties for specific acquisition intent</p>
<div class="alert">
<blockquote>
[!Note]<br />
The flags can be combined with a bitwise <strong>OR</strong> operator, but an image cannot be both grayscale and color.
</blockquote>
</div>
<div>
 
</div>
<p>This property is required for all scanners.</p>
<p>The following table contains the image-type flags and their definitions. These flags are used to set which type of image is intended: color, grayscale, and so on.</p>
<p></p>
<table>
<thead>
<tr class="header">
<th>Intended image type flags</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_INTENT_NONE</td>
<td>Default value. No intent is specified.</td>
</tr>
<tr class="even">
<td>WIA_INTENT_IMAGE_TYPE_COLOR</td>
<td>The application intends to prepare the device for a color scan.</td>
</tr>
<tr class="odd">
<td>WIA_INTENT_IMAGE_TYPE_GRAYSCALE</td>
<td>The application intends to prepare the device for a grayscale scan.</td>
</tr>
<tr class="even">
<td>WIA_INTENT_IMAGE_TYPE_TEXT</td>
<td>The application intends to prepare the device for scanning text.</td>
</tr>
<tr class="odd">
<td>WIA_INTENT_IMAGE_TYPE_MASK</td>
<td>Mask for all of the image-type flags.</td>
</tr>
</tbody>
</table>

<p> </p>
<p>The following table contains the quality and size flags and their definitions. These flags are used to set which level of quality is intended.</p>

<table>
<thead>
<tr class="header">
<th>Intended image size/quality flags</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_INTENT_MINIMIZE_SIZE</td>
<td>The application intends to prepare the device for scanning an image that result's in a small scan.</td>
</tr>
<tr class="even">
<td>WIA_INTENT_MAXIMIZE_QUALITY</td>
<td>The application intends to prepare the device for scanning a high-quality image.</td>
</tr>
<tr class="odd">
<td>WIA_INTENT_SIZE_MASK</td>
<td>This flag is a mask for all of the size/quality flags.</td>
</tr>
<tr class="even">
<td>WIA_INTENT_BEST_PREVIEW</td>
<td>The application intends to prepare the device for scanning a preview.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_DESKEW_X"></span><span id="wia_ips_deskew_x"></span><dl> <dt><strong>WIA_IPS_DESKEW_X</strong></dt> <dt>ScannerPictureDeskewX</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the number of pixels in the x-direction from WIA_IPS_XPOS to the x-coordinate of the uppermost corner of the image to be deskewed. Hence, it describes, in conjunction with WIA_IPS_DESKEW_Y, where the two upper corners of the skewed image are located within the bounding rectangle defined by WIA_IPS_XPOS, WIA_IPS_YPOS, WIA_IPS_XEXTENT and WIA_IPS_YEXTENT. his property is implemented by the scanner driver if it supports deskewing.</p>
<p>The valid values for WIA_IPS_DESKEW_X must be between 0 and (WIA_IPS_XEXTENT - 1). A value of 0 means that no deskew should be performed.</p>
<p>This property is optional for items of the categories WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, and WIA_CATEGORY_FILM; and it is not available for WIA_CATEGORY_FINISHED_FILE or WIA_CATEGORY_FOLDER items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: WIA_PROP_RANGE</p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_DESKEW_Y"></span><span id="wia_ips_deskew_y"></span><dl> <dt><strong>WIA_IPS_DESKEW_Y</strong></dt> <dt>ScannerPictureDeskewY</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the number of pixels in the y-direction from WIA_IPS_YPOS to the y-coordinate of the leftmost corner of the image to be deskewed. Hence, it describes, in conjunction with WIA_IPS_DESKEW_X, where the two upper corners of the skewed image are located within the bounding rectangle defined by WIA_IPS_XPOS, WIA_IPS_YPOS, WIA_IPS_XEXTENT and WIA_IPS_YEXTENT. This property is implemented by the scanner driver if it supports deskewing.</p>
<p>The valid values for WIA_IPS_DESKEW_Y must be between 0 and (WIA_IPS_YEXTENT - 1). A value of 0 means that no deskew should be performed.</p>
<p>This property is optional for items of the categories WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, and WIA_CATEGORY_FILM; and it is not available for WIA_CATEGORY_FINISHED_FILE or WIA_CATEGORY_FOLDER items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: WIA_PROP_RANGE</p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_DOCUMENT_HANDLING_SELECT"></span><span id="wia_ips_document_handling_select"></span><dl> <dt><strong>WIA_IPS_DOCUMENT_HANDLING_SELECT</strong></dt> <dt>ScannerPictureDocumentHandlingSelect</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the current scanner acquisition source and mode. The minidriver creates and maintains this property.</p>
<p>An application reads this property to determine the current acquisition source of the scanner or to write this property to set the source and mode of the scanner. In addition, applications use this property to enable and disable duplexer functionality.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_FLAG</a></p>
<p>The following table has the constants that are valid with this property. </p>
<table>
<thead>
<tr class="header">
<th>Flags</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DUPLEX</td>
<td>Scan using duplexer operations. Scan both document sides using common settings configured for the feeder item (WIA_CATEGORY_FEEDER). DUPLEX and ADVANCE_DUPLEX cannot both be set.</td>
</tr>
<tr class="even">
<td>ADVANCED_DUPLEX</td>
<td>Scan using individual settings configured for each child feeder item (WIA_CATEGORY_FEEDER_FRONT and WIA_CATEGORY_FEEDER_BACK). DUPLEX and ADVANCE_DUPLEX cannot both be set.</td>
</tr>
<tr class="odd">
<td>FRONT_FIRST</td>
<td>Scan the front of the document first. This value is valid when DUPLEX or ADVANCED_DUPLEX is set.</td>
</tr>
<tr class="even">
<td>BACK_FIRST</td>
<td>Scan the back of the document first. This value is valid when DUPLEX or ADVANCED_DUPLEX is set.</td>
</tr>
<tr class="odd">
<td>FRONT_ONLY</td>
<td>Scan the front only.</td>
</tr>
<tr class="even">
<td>BACK_ONLY</td>
<td>Scan the back only. This value is valid when DUPLEX or ADVANCED_DUPLEX is set.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_FILM_NODE_NAME"></span><span id="wia_ips_film_node_name"></span><dl> <dt><strong>WIA_IPS_FILM_NODE_NAME</strong></dt> <dt>ScannerPictureFilmNodeName</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Enables specification of a particular film scanning attachment when there is more than one.</p>
<p>This property is required for the WIA_CATEGORY_FILM items when there are multiple film scan items. If the device supports only one root scanner film item then this property is optional.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>Allowed values: The BSTR should be in the form of @ResourceBinary,-<ResourceID> to allow localization as this string would be exposed to the user through the film scanning UI.</p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_FILM_SCAN_MODE"></span><span id="wia_ips_film_scan_mode"></span><dl> <dt><strong>WIA_IPS_FILM_SCAN_MODE</strong></dt> <dt>ScannerPictureFilmScanMode</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Enables configuration of the current film scan.</p>
<p>This property is required for the WIA_CATEGORY_FILM item.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the constants that are valid with this property. </p>
<table>
<thead>
<tr class="header">
<th>Constant</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_FILM_COLOR_SLIDE</td>
<td>Scan for a color slide.</td>
</tr>
<tr class="even">
<td>WIA_FILM_COLOR_NEGATIVE</td>
<td>Scan for a color negative.</td>
</tr>
<tr class="odd">
<td>WIA_FILM_BW_NEGATIVE</td>
<td>Scan for a black and white negative.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_INVERT"></span><span id="wia_ips_invert"></span><dl> <dt><strong>WIA_IPS_INVERT</strong></dt> <dt>ScannerPictureInvert</dt> </dl></td>
<td ><p>Reserved for future use and is not implemented at this time.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_ITEMS_STORED"></span><span id="wia_ipa_items_stored"></span><dl> <dt><strong>WIA_IPA_ITEMS_STORED</strong></dt> <dt>ScannerPictureInvert</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Specifies how many items are stored in the WIA_CATEGORY_FOLDER item.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_LAMP"></span><span id="wia_ips_lamp"></span><dl> <dt><strong>WIA_IPS_LAMP</strong></dt> <dt>ScannerPictureLamp</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Turns the scanner lamp on or off.</p>
<p>Optional for the WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, and WIA_CATEGORY_FILM items and recommended for WIA_CATEGORY_FILM.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the constants that are valid with this property. </p>
<table>
<thead>
<tr class="header">
<th>Constant</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_LAMP_ON</td>
<td>Turn on the lamp.</td>
</tr>
<tr class="even">
<td>WIA_LAMP_OFF</td>
<td>Turn off the lamp.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_LAMP_AUTO_OFF"></span><span id="wia_ips_lamp_auto_off"></span><dl> <dt><strong>WIA_IPS_LAMP_AUTO_OFF</strong></dt> <dt>ScannerPictureLampAutoOff</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Sets the maximum time to keep the lamp on when the scanner is not being used.</p>
<p>Optional for the WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, and WIA_CATEGORY_FILM items and recommended for WIA_CATEGORY_FILM.</p>
<p>Type: <strong>VT_UI4</strong>, Access: Read/Write, Valid Values: 0 - 0xFFF seconds</p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_MAX_HORIZONTAL_SIZE"></span><span id="wia_ips_max_horizontal_size"></span><dl> <dt><strong>WIA_IPS_MAX_HORIZONTAL_SIZE</strong></dt> <dt>ScannerPictureMaxHorizontalSize</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Specifies the maximum width, in thousandths of an inch, that is scanned in the horizontal (X) axis at the current resolution. This may be the width of the sheet feeder or the scanning bed, according to the type of item.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_MAX_VERTICAL_SIZE"></span><span id="wia_ips_max_vertical_size"></span><dl> <dt><strong>WIA_IPS_MAX_VERTICAL_SIZE</strong></dt> <dt>ScannerPictureMaxVerticalSize</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Specifies the maximum height, in thousandths of an inch, that is scanned in the vertical (Y) axis at the current resolution. This may be the height of the sheet feeder or the scanning bed, according to the type of item.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_MIN_HORIZONTAL_SIZE"></span><span id="wia_ips_min_horizontal_size"></span><dl> <dt><strong>WIA_IPS_MIN_HORIZONTAL_SIZE</strong></dt> <dt>ScannerPictureMinHorizontalSize</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Specifies the minimum width, in thousandths of an inch, that is scanned in the horizontal (X) axis at the current resolution.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_MIN_VERTICAL_SIZE"></span><span id="wia_ips_min_vertical_size"></span><dl> <dt><strong>WIA_IPS_MIN_VERTICAL_SIZE</strong></dt> <dt>ScannerPictureMinVerticalSize</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Specifies the minimum height, in thousandths of an inch, that is scanned in the vertical (Y) axis at the current resolution.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_MIRROR"></span><span id="wia_ips_mirror"></span><dl> <dt><strong>WIA_IPS_MIRROR</strong></dt> <dt>ScannerPictureMirror</dt> </dl></td>
<td ><p>Reserved for future use and is not implemented at this time.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_OPTICAL_XRES"></span><span id="wia_ips_optical_xres"></span><dl> <dt><strong>WIA_IPS_OPTICAL_XRES</strong></dt> <dt>ScannerPictureOpticalXres</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Horizontal Optical Resolution. Highest supported horizontal optical resolution in DPI. This property is a single value. This is not a list of all resolutions that can be generated by the device. Rather, this is the resolution of the device's optics. The minidriver creates and maintains this property. This property is required for all items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_OPTICAL_YRES"></span><span id="wia_ips_optical_yres"></span><dl> <dt><strong>WIA_IPS_OPTICAL_YRES</strong></dt> <dt>ScannerPictureOpticalYres</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Vertical Optical Resolution. Highest supported vertical optical resolution in DPI. This property is a single value. This is not a list of all resolutions that are generated by the device. Rather, this is the resolution of the device's optics. The minidriver creates and maintains this property. This property is required for all items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_ORIENTATION"></span><span id="wia_ips_orientation"></span><dl> <dt><strong>WIA_IPS_ORIENTATION</strong></dt> <dt>ScannerPictureOrientation</dt> </dl></td>
<td ><p>Specifies the current orientation of the documents to be scanned. The minidriver creates and maintains this property.</p>
<p>An application sets this property to define the original orientation of a page or image to be acquired. For information on how to use WIA_IPS_ORIENTATION, see <strong>WIA_IPS_PAGE_SIZE</strong>.</p>
<div class="alert">
<blockquote>
[!Note]<br />
WIA_IPS_ORIENTATION refers to the position of the document to be scanned on the scanner bed or feeder. It is the orientation of the document relative to the direction of the scan. WIA_IPS_ROTATION refers to rotation that is applied to the image after it is scanned, just before the image is transferred to the application.
</blockquote>
</div>
<div>
 
</div>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the four constants that are valid with this property.</p>

<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PORTRAIT</td>
<td>0 degrees.</td>
</tr>
<tr class="even">
<td>LANDSCAPE</td>
<td>90-degree counter-clockwise rotation, relative to the PORTRAIT orientation.</td>
</tr>
<tr class="odd">
<td>ROT180</td>
<td>180-degree counter-clockwise rotation, relative to the PORTRAIT orientation.</td>
</tr>
<tr class="even">
<td>ROT270</td>
<td>270-degree counter-clockwise rotation, relative to the PORTRAIT orientation.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_PAGE_SIZE"></span><span id="wia_ips_page_size"></span><dl> <dt><strong>WIA_IPS_PAGE_SIZE</strong></dt> <dt>ScannerPicturePageSize</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the size of the page that is currently set to be scanned. An application sets this property to select the dimensions of the page to scan. The minidriver creates and maintains this property.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>For the constants that can be used with this property, see <a href="-wia-wia2-pagesizeconstants.md"><strong>WIA 2.0 Page Size Constants</strong></a>. Note these non-fixed sizes, in particular: </p>
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_PAGE_CUSTOM</td>
<td>Defined by the values of the <strong>WIA_IPS_PAGE_HEIGHT</strong> and <strong>WIA_IPS_PAGE_WIDTH</strong> properties.</td>
</tr>
<tr class="even">
<td>WIA_PAGE_AUTO</td>
<td>Page size is automatically determined by the device.</td>
</tr>
<tr class="odd">
<td>WIA_PAGE_CUSTOM_BASE</td>
<td>A custom page size whose dimensions are already known to the application and the device driver.</td>
</tr>
</tbody>
</table>

<p> </p>
<p>The value of the <strong>WIA_IPS_ORIENTATION</strong> property determines the orientation of the currently selected page. The <strong>WIA_IPS_PAGE_WIDTH</strong> and <strong>WIA_IPS_PAGE_HEIGHT</strong> properties report the page's dimensions, in thousandths of an inch. These properties must be in agreement with <strong>WIA_IPS_XEXTENT</strong> and <strong>WIA_IPS_YEXTENT</strong>, which contain the page's dimensions in pixels.</p>
<div class="alert">
<blockquote>
[!Note]<br />
Valid values of type WIA_PROP_LIST depend on valid settings of the <strong>WIA_IPS_ORIENTATION</strong> property. If, for example, the device cannot scan landscape-oriented documents with a WIA_PAGE_A4 setting, WIA_PAGE_A4 is not a valid value for the <strong>WIA_IPS_PAGE_SIZE</strong> property when <strong>WIA_IPS_ORIENTATION</strong> is set to LANDSCAPE.
</blockquote>
</div>
<div>
 
</div>
<p>If an application sets <strong>WIA_IPS_PAGE_SIZE</strong> to any value other than the three in the table above, the minidriver should adjust the values of <strong>WIA_IPS_PAGE_WIDTH</strong> and <strong>WIA_IPS_PAGE_HEIGHT</strong> to the page's dimensions in thousandths of an inch. It should also adjust the values of <strong>WIA_IPS_XEXTENT</strong> and <strong>WIA_IPS_YEXTENT</strong> to the page's dimensions in pixels.</p>
<p>If an extent setting (<strong>WIA_IPS_XEXTENT</strong> or <strong>WIA_IPS_YEXTENT</strong>) is changed to a value that does not match the current page size setting, the minidriver should change the value of the <strong>WIA_IPS_PAGE_SIZE</strong> property to WIA_PAGE_CUSTOM. The minidriver should also modify <a href="-wia-wiaitempropscannerdevice.md"><strong>WIA_IPS_PAGE_WIDTH</strong></a> or <strong>WIA_IPS_PAGE_HEIGHT</strong> in accordance with the new extent setting.</p>
<p>If <strong>WIA_IPS_ORIENTATION</strong> is set to LANDSCAPE, the extent settings will be exchanged relative to their usual values. For example, if an application sets <strong>WIA_IPS_PAGE_SIZE</strong> to WIA_PAGE_A4, the minidriver sets <strong>WIA_IPS_PAGE_WIDTH</strong> to 11692 and <strong>WIA_IPS_PAGE_HEIGHT</strong> to 8267. (The minidriver should also adjust <strong>WIA_IPS_XEXTENT</strong> and <strong>WIA_IPS_YEXTENT</strong> accordingly.)</p>
<div class="alert">
<blockquote>
[!Note]<br />
If <a href="-wia-wiaitempropscannerdevice.md"><strong>WIA_IPS_PAGE_SIZE</strong></a> is set to WIA_PAGE_CUSTOM, the orientation setting is not used to determine the extent dimensions of the page to be scanned.
</blockquote>
</div>
<div>
 
</div>
<p>The minidriver is responsible for ensuring that the <strong>WIA_IPS_ORIENTATION</strong> property is in agreement with the current selection area. If an application changes the value of <strong>WIA_IPS_ORIENTATION</strong> to one that is invalid for the currently selected page size, the minidriver should change the value of <strong>WIA_IPS_PAGE_SIZE</strong> to a page size that is supported by the new orientation value.</p>
<p>If an application sets the <strong>WIA_IPS_PAGE_SIZE</strong> property to WIA_PAGE_CUSTOM, the current selection area is not affected. The WIA minidriver should obtain the current image layout, starting from the current settings of the <strong>WIA_IPS_XPOS</strong> and <strong>WIA_IPS_YPOS</strong> properties. If the page size setting results in a selection area that is outside the scanner's bed, the minidriver must automatically adjust the values of the <strong>WIA_IPS_XPOS</strong> and <strong>WIA_IPS_YPOS</strong> properties to valid settings. If the <strong>WIA_IPS_PAGE_SIZE</strong> and <strong>WIA_IPS_ORIENTATION</strong> properties are set at the same time, and they are invalid when applied in combination, the minidriver should fail the application's settings by returning an error in the <a href="https://msdn.microsoft.com/library/ms794145.aspx">IWiaMiniDrv::drvValidateItemProperties</a>.</p>
<p>The following four examples show different <strong>WIA_IPS_PAGE_SIZE</strong> scenarios.</p>
<ol>
<li>The driver reports the settings.</li>
<li>An application sets the <strong>WIA_IPS_PAGE_SIZE</strong> property to WIA_PAGE_LETTER.</li>
<li>An application sets the <strong>WIA_IPS_ORIENTATION</strong> property to LANDSCAPE.</li>
<li>An application changes the <strong>WIA_IPS_XEXTENT</strong> property to a smaller value.</li>
</ol>
<p><strong>Example 1: The minidriver reports the settings</strong></p>
<p>In the following example, the minidriver sets a custom selection area before an application sets any WIA properties. In this case, the selection area represents the entire flatbed.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>WIA_IPS_PAGE_SIZE = WIA_PAGE_CUSTOM
WIA_IPS_PAGE_WIDTH = 11500
WIA_IPS_PAGE_HEIGHT = 14000
WIA_IPS_ORIENTATION = PORTRAIT
WIA_IPS_XPOS = 0
WIA_IPS_YPOS = 0
WIA_IPS_XEXTENT = 1150
WIA_IPS_YEXTENT = 1400
WIA_IPS_XRES = 100
WIA_IPS_YRES = 100</code></pre></td>
</tr>
</tbody>
</table>

</div>
<p><strong>Example 2: An application sets the</strong> <strong>WIA_IPS_PAGE_SIZE</strong>  <strong>property to WIA_PAGE_LETTER</strong></p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>WIA_IPS_PAGE_SIZE = WIA_PAGE_LETTER
WIA_IPS_PAGE_WIDTH = 8500
WIA_IPS_PAGE_HEIGHT = 11000
WIA_IPS_ORIENTATION = PORTRAIT
WIA_IPS_XPOS = 0
WIA_IPS_YPOS = 0
WIA_IPS_XEXTENT = 850
WIA_IPS_YEXTENT = 1100
WIA_IPS_XRES = 100
WIA_IPS_YRES = 100</code></pre></td>
</tr>
</tbody>
</table>

</div>
<p><strong>Example 3: An application sets the</strong> <strong>WIA_IPS_ORIENTATION</strong>  <strong>property to LANDSCAPE</strong></p>
<p>The physical bed must be able to acquire a page that was originally in landscape orientation.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>WIA_IPS_PAGE_SIZE = WIA_PAGE_LETTER
WIA_IPS_PAGE_HEIGHT = 11000
WIA_IPS_PAGE_WIDTH = 8500
WIA_IPS_ORIENTATION = LANDSCAPE
WIA_IPS_XPOS = 0
WIA_IPS_YPOS = 0
WIA_IPS_XEXTENT = 1100
WIA_IPS_YEXTENT = 850
WIA_IPS_XRES = 100
WIA_IPS_YRES = 100</code></pre></td>
</tr>
</tbody>
</table>

</div>
<p><strong>Example 4: An application changes the</strong> <strong>WIA_IPS_XEXTENT</strong> <strong>property to a smaller value</strong></p>
<p>In the following example, an application changes the <strong>WIA_IPS_XEXTENT</strong> property to 1000. The minidriver should assume that the new value contained in <strong>WIA_IPS_XEXTENT</strong> is no longer valid for the <strong>WIA_IPS_PAGE_SIZE</strong> property and should thus change <strong>WIA_IPS_PAGE_SIZE</strong> to WIA_PAGE_CUSTOM. The minidriver must also adjust <strong>WIA_IPS_PAGE_WIDTH</strong>.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>WIA_IPS_PAGE_SIZE = WIA_PAGE_CUSTOM
WIA_IPS_PAGE_HEIGHT = 10000
WIA_IPS_PAGE_WIDTH = 8500
WIA_IPS_ORIENTATION = LANDSCAPE
WIA_IPS_XPOS = 0
WIA_IPS_YPOS = 0
WIA_IPS_XEXTENT = 1000
WIA_IPS_YEXTENT = 850
WIA_IPS_XRES = 100
WIA_IPS_YRES = 100</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_PAGE_HEIGHT"></span><span id="wia_ips_page_height"></span><dl> <dt><strong>WIA_IPS_PAGE_HEIGHT</strong></dt> <dt>ScannerPicturePageHeight</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the height, in thousandths of an inch, of the currently selected page. The minidriver creates and maintains the <strong>WIA_IPS_PAGE_HEIGHT</strong> property. An application reads this property to determine the physical dimensions of the page being scanned. If the extent settings are different from the known page sizes, this property reports the height of the page whose <strong>WIA_IPS_PAGE_SIZE</strong> property is set to WIA_PAGE_CUSTOM (which is a value of the <strong>WIA_IPS_PAGE_SIZE</strong> property). <strong>WIA_IPS_PAGE_HEIGHT</strong> must be in sync with <strong>WIA_IPS_XEXTENT</strong>, which reports the height, in pixels, of the page to be scanned.</p>
<p>This property is required for WIA_CATEGORY_FEEDER items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_PAGE_WIDTH"></span><span id="wia_ips_page_width"></span><dl> <dt><strong>WIA_IPS_PAGE_WIDTH</strong></dt> <dt>ScannerPicturePageWidth</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the width of the current page selected, in thousandths of an inch. An application reads this property to determine the physical dimensions of the page being scanned. If the extent settings are different from known page sizes, this property reports the width of the page whose <strong>WIA_IPS_PAGE_SIZE</strong> property is set to WIA_PAGE_CUSTOM. <strong>WIA_IPS_PAGE_WIDTH</strong> must be in sync with the value of <strong>WIA_IPS_XEXTENT</strong>, which reports the width, in pixels, of the page to be scanned. The minidriver creates and maintains this property.</p>
<p>This property is required for WIA_CATEGORY_FEEDER items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_PAGES"></span><span id="wia_ips_pages"></span><dl> <dt><strong>WIA_IPS_PAGES</strong></dt> <dt>ScannerPicturePages</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the current number of pages to be acquired from an automatic document feeder. The minidriver creates and maintains this property.</p>
<p>Type: <strong>VT_I4</strong>; Access: Read/Write; Valid values: <a href="-wia-property-attributes.md">WIA_PROP_RANGE</a> This is zero through the maximum number of pages that the scanner can scan. The value is ALL_PAGES (= 0) if the scanner can scan continuously.</p>
<p>An application reads this property to determine the document feeder's page capacity. The application also sets this property to the number of pages it is going to scan.</p>
<div class="alert">
<blockquote>
[!Note]<br />
If duplex mode is enabled (<strong>WIA_IPS_DOCUMENT_HANDLING_SELECT</strong> is set to FEEDER | DUPLEX | ADVANCED_DUPLEX), <strong>WIA_IPS_PAGES</strong> is still equal to the number of pages to scan.
</blockquote>
</div>
<div>
 
</div>
<p>One sheet of paper will automatically contain two pages if DUPLEX is enabled, even if the back side of the page is blank.</p>
<p>Setting <strong>WIA_IPS_PAGES</strong> to 1 causes a scanner to process one side of the page. We recommend that, if a scanner is unable to scan only one side of a page while in duplex mode, you change the <strong>WIA_IPS_PAGES</strong> value for the Inc member of the Range member of the WIA_PROPERTY_INFO structure to 2. This value signals the application that it must request pages in multiples of two. A value of ALL_PAGES (= 0) means that <em>all</em> pages that are currently loaded into the document feeder are to be scanned.</p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_PHOTOMETRIC_INTERP"></span><span id="wia_ips_photometric_interp"></span><dl> <dt><strong>WIA_IPS_PHOTOMETRIC_INTERP</strong></dt> <dt>ScannerPicturePhotometricInterp</dt> </dl></td>
<td ><p>Contains the current setting for white and black pixels. The minidriver creates and maintains this property.</p>
<p>An application reads this value to determine the value of WHITE or BLACK (depending on what the application is doing).</p>
<p>Required for all acquisition enabled or stored items; that is, items in the categories: WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FEEDER_FRONT, WIA_CATEGORY_FEEDER_BACK, WIA_CATEGORY_FINISHED_FILE, and WIA_CATEGORY_FILM. It is not supported for WIA_CATEGORY_FOLDER items.</p>
<p>Type: <strong>VT_I4</strong>; Access: Read/Write; Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a>. If the device can be set to only a single value, create a WIA_PROP_LIST type, and place the valid value in it.</p>
<p>The following table has the two constants that are valid with this property.</p>

<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_PHOTO_WHITE_0</td>
<td>WHITE is 0, and BLACK is 1.</td>
</tr>
<tr class="even">
<td>WIA_PHOTO_WHITE_1</td>
<td>WHITE is 1, and BLACK is 0.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_PREVIEW"></span><span id="wia_ips_preview"></span><dl> <dt><strong>WIA_IPS_PREVIEW</strong></dt> <dt>ScannerPicturePreview</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Indicates the preview mode for a device. An application sets this property to place the device into a preview mode.</p>
<p>This property is required for the WIA_CATEGORY_FLATBED and WIA_CATEGORY_FILM items, optional for the WIA_CATEGORY_FEEDER item.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the constants that are valid with this property. </p>
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_FINAL_SCAN</td>
<td>The application will perform a final scan.</td>
</tr>
<tr class="even">
<td>WIA_PREVIEW_SCAN</td>
<td>The application will perform a preview scan.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_PREVIEW_TYPE"></span><span id="wia_ips_preview_type"></span><dl> <dt><strong>WIA_IPS_PREVIEW_TYPE</strong></dt> <dt>ScannerPicturePreviewType</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Specifies whether the existing preview image can be updated during an image preview (in response to a change in the WIA_IPA_DATATYPE or WIA_IPA_DEPTH properties).</p>
<p>This property is optional for all acquisition enabled items that support preview scans; that is, WIA_IPS_PREVIEW is supported with WIA_PREVIEW_SCAN. This includes items of types WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FEEDER_FRONT, WIA_CATEGORY_FEEDER_BACK, and WIA_CATEGORY_FILM.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>The following table has the constants that are valid with this property. </p>
<table>
<thead>
<tr class="header">
<th>Constant</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_ADVANCED_PREVIEW</td>
<td>Updating the existing image is possible.</td>
</tr>
<tr class="even">
<td>WIA_BASIC_PREVIEW</td>
<td>Another preview scan must be executed because updating the existing image is not possible.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_ROTATION"></span><span id="wia_ips_rotation"></span><dl> <dt><strong>WIA_IPS_ROTATION</strong></dt> <dt>ScannerPictureRotation</dt> </dl></td>
<td ><p>Contains the current rotation setting, if it is implemented. The minidriver creates and maintains this property.</p>
<p>An application sets this property to inform the driver how much (if at all) to rotate the image before the driver returns it to the application.</p>
<div class="alert">
<blockquote>
[!Note]<br />
WIA_IPS_ORIENTATION refers to the position of the document to be scanned on the scanner bed or feeder. It is the orientation of the document relative to the direction of the scan. WIA_IPS_ROTATION refers to rotation that is applied to the image after it is scanned, just before the image is transferred to the application.
</blockquote>
</div>
<div>
 
</div>
<p>The WIA minidriver is responsible for rotating the image data before sending it back to the application. The application is responsible for checking the image headers to see the newly rotated values.</p>
<p>Considerable confusion exists about resolving the effect of rotation on the current image's selection area (which is defined by the <strong>WIA_IPS_XPOS</strong>, <strong>WIA_IPS_YPOS</strong>, <strong>WIA_IPS_XEXTENT</strong> and <strong>WIA_IPS_YEXTENT</strong> properties).</p>
<p><em>Selection area</em> refers to the selected area on the physical scanner bed that an image is be acquired from. <strong>WIA_IPS_ROTATION</strong> does not modify the selection area. The driver applies a counterclockwise rotation according to <strong>WIA_IPS_ROTATION</strong> only after the driver has acquired the appropriate selection area. <strong>WIA_IPS_ROTATION</strong> does affect the dimensions of the output image, so these dimensions must be reflected in the resulting image's data header.</p>
<p>Optional for all acquisition enabled items; that is, items in the categories: WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FEEDER_FRONT, WIA_CATEGORY_FEEDER_BACK, and WIA_CATEGORY_FILM.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following rotation constants are defined.</p>

<table>
<thead>
<tr class="header">
<th>Constant</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PORTRAIT</td>
<td>The driver will not rotate the image.</td>
</tr>
<tr class="even">
<td>LANDSCAPE</td>
<td>TThe driver rotates the image 90 degrees counterclockwise.</td>
</tr>
<tr class="odd">
<td>ROT180</td>
<td>The driver rotates the image 180 degrees counterclockwise.</td>
</tr>
<tr class="even">
<td>ROT270</td>
<td>The driver rotates the image 270 degrees counterclockwise.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_SEGMENTATION"></span><span id="wia_ips_segmentation"></span><dl> <dt><strong>WIA_IPS_SEGMENTATION</strong></dt> <dt>ScannerPictureSegmentation</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Specifies whether the application should use the driver's segmentation filter for multi-region scanning. WIA_IPS_SEGMENTATION must be implemented for WIA_CATEGORY_FLATBED and WIA_CATEGORY_FILM items if they support either the creation of child items with a segmentation filter or if the driver itself creates child items for fixed frames.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>The following table has the two constants that are valid with this property.</p>

<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_USE_SEGMENTATION_FILTER</td>
<td>The application should use the segmentation filter for multi-region scanning.</td>
</tr>
<tr class="even">
<td>WIA_DONT_USE_SEGMENTATION_FILTER</td>
<td>The driver creates the child items itself for multi-region scanning. This is usually the case if the scanner uses fixed frames for this purpose.</td>
</tr>
</tbody>
</table>

<p> </p>
<div class="alert">
<blockquote>
[!Note]<br />
It is possible for a driver to come with a segmentation filter, but still have WIA_IPS_SEGMENTATION set to WIA_DONT_USE_SEGMENTATION_FILTER for one of its items (such as, the WIA_CATEGORY_FILM item). This could be the case if the scanner uses fixed frames for film scanning, but not for regular scanning from WIA_CATEGORY_FLATBED items.
</blockquote>
</div>
<div>
 
</div></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_SHEET_FEEDER_REGISTRATION"></span><span id="wia_ips_sheet_feeder_registration"></span><dl> <dt><strong>WIA_IPS_SHEET_FEEDER_REGISTRATION</strong></dt> <dt>ScannerPictureSheetFeederRegistration</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the registration, or alignment and edge detection, for documents that are placed on the flatbed. The minidriver creates and maintains this property. This property indicates how the sheet is horizontally positioned on the scanning head of a handheld or sheet-fed scanner. The property is used to predict where across the scan head a document is placed.</p>
<p>For scanners that support more than one scan head, this property is relative to the topmost scan head. This property is mandatory for sheet-fed, scroll-fed, and handheld scanners.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>The following table has the three constants that are valid with this property.</p>

<table>
<thead>
<tr class="header">
<th>Constant</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LEFT_JUSTIFIED</td>
<td>The sheet is positioned to the left with respect to the scanning head.</td>
</tr>
<tr class="even">
<td>CENTERED</td>
<td>The sheet is centered on the scanning head.</td>
</tr>
<tr class="odd">
<td>RIGHT_JUSTIFIED</td>
<td>The sheet is positioned to the right with respect to the scanning head.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_SHOW_PREVIEW_CONTROL"></span><span id="wia_ips_show_preview_control"></span><dl> <dt><strong>WIA_IPS_SHOW_PREVIEW_CONTROL</strong></dt> <dt>ScannerPictureShowPreviewControl</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Indicates whether an item needs a preview control displayed to the user. The minidriver creates and maintains this property.</p>
<p>Optional for all transfer enabled items. This is usually just items of the categories WIA_ITEM_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FILM, and WIA_CATEGORY_FINISHED_FILE.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>The following table has the constants that are valid with this property. </p>
<table>
<thead>
<tr class="header">
<th>Constant</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_SHOW_PREVIEW_CONTROL</td>
<td>Show a preview control to the user, because this device can perform a preview.</td>
</tr>
<tr class="even">
<td>WIA_DONT_SHOW_PREVIEW_CONTROL</td>
<td>Do not show a preview control to the user, because this device cannot perform a preview.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION"></span><span id="wia_ips_supports_child_item_creation"></span><dl> <dt><strong>WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION</strong></dt> <dt>ScannerPictureSupportsChildItemCreation</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Specifies whether the application (or the filters) can create child items under the current item.</p>
<p>Optional for all transfer enabled item categories: WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FILM and even WIA_CATEGORY_FOLDER. (If the storage won't support upload of new items then this property should be either unsupported or supported with the <strong>FALSE</strong> value.)</p>
<p>Items supporting WIA_IPS_SEGMENTATION and WIA_USE_SEGMENTATION_FILTER must also support WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION and have it set to <strong>TRUE</strong>.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <strong>TRUE</strong> and <strong>FALSE</strong></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_THRESHOLD"></span><span id="wia_ips_threshold"></span><dl> <dt><strong>WIA_IPS_THRESHOLD</strong></dt> <dt>ScannerPictureThreshold</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Specifies the grayscale value that determines whether a pixel will be converted to white or black when an image is converted to monochromatic. Pixels above the threshold become white. Pixels below the threshold become white.</p>
<p>This property is required for acquisition items that support 1-bpp scans and that have the WIA_IPA_DATATYPE property set to WIA_DATA_THRESHOLD.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_RANGE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_TRANSFER_CAPABILITIES"></span><span id="wia_ips_transfer_capabilities"></span><dl> <dt><strong>WIA_IPS_TRANSFER_CAPABILITIES</strong></dt> <dt>ScannerPictureTransferCapabilities</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Specifies whether the driver is capable of transferring multiple child items in single transfer call.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_FLAG</a></p>
<p>The only possible value for this property is WIA_TRANSFER_CHILDREN_SINGLE_SCAN. If this flag is set, then the driver is capable of transfering multiple child items in single transfer call. If the flag is not set, the WIA Service will walk through the child items recursively and then transfer each of those items.</p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_UPLOAD_ITEM_SIZE"></span><span id="wia_ipa_upload_item_size"></span><dl> <dt><strong>WIA_IPA_UPLOAD_ITEM_SIZE</strong></dt> <dt>ScannerPictureInvert</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Specifies the number of bytes to upload for the item.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_WARM_UP_TIME"></span><span id="wia_ips_warm_up_time"></span><dl> <dt><strong>WIA_IPS_WARM_UP_TIME</strong></dt> <dt>ScannerPictureWarmUpTime</dt> </dl></td>
<td ><p>Specifies the maximum warm-up time, in milliseconds, that the device needs before starting the scanning operation. The minidriver creates and maintains this property.</p>
<p>An application can read this property to determine the maximum warm-up time for this device. It can then present a &quot;waiting for the device to warm up&quot; dialog box, to let the user know that a wait or pause might occur before anything happens.</p>
<p>This property is required for all acquisition enabled items; that is, items in the categories: WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FEEDER_FRONT, WIA_CATEGORY_FEEDER_BACK, and WIA_CATEGORY_FILM.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_XEXTENT"></span><span id="wia_ips_xextent"></span><dl> <dt><strong>WIA_IPS_XEXTENT</strong></dt> <dt>ScannerPictureXextent</dt> </dl></td>
<td ><p>Contains the current width, in pixels, of the selected image to acquire. An application sets this property to mark the width of a selection area to acquire. This property must agree with the <a href="-wia-wiaitempropcommonitem.md"><strong>WIA_IPA_PIXELS_PER_LINE</strong></a> property. The minidriver creates and maintains this property.</p>
<p>Required for all acquisition enabled items; that is, items in the categories: WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FEEDER_FRONT, WIA_CATEGORY_FEEDER_BACK, and WIA_CATEGORY_FILM.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_RANGE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_XPOS"></span><span id="wia_ips_xpos"></span><dl> <dt><strong>WIA_IPS_XPOS</strong></dt> <dt>ScannerPictureXpos</dt> </dl></td>
<td ><p>Contains the x coordinate, in pixels, of the upper-left corner of the selected image. An application sets this property to mark the upper-left corner of the selection area. The minidriver creates and maintains this property.</p>
<p>Required for all acquisition enabled items; that is, items in the categories: WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FEEDER_FRONT, WIA_CATEGORY_FEEDER_BACK, WIA_CATEGORY_FINISHED_FILE, and WIA_CATEGORY_FILM. It is not supported for WIA_CATEGORY_FOLDER items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_RANGE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_XRES"></span><span id="wia_ips_xres"></span><dl> <dt><strong>WIA_IPS_XRES</strong></dt> <dt>ScannerPictureXres</dt> </dl></td>
<td ><p>Contains the current horizontal resolution, in pixels per inch, for the device. An application sets this property to set the horizontal resolution. The minidriver creates and maintains this property.</p>
<p>If the device can be set to only a single value, create a <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> type and place the valid value in it. This is also a case where one resolution setting depends on another resolution. (The vertical resolution can depend on the horizontal resolution.)</p>
<p>Required for all acquisition enabled items; that is, items in the categories: WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FEEDER_FRONT, WIA_CATEGORY_FEEDER_BACK, WIA_CATEGORY_FINISHED_FILE, and WIA_CATEGORY_FILM. It is not supported for WIA_CATEGORY_FOLDER items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write or Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_RANGE</a> or WIA_PROP_LIST</p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_XSCALING"></span><span id="wia_ips_xscaling"></span><dl> <dt><strong>WIA_IPS_XSCALING</strong></dt> <dt>ScannerPictureXscaling</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Sets the horizontal scaling, as a percentage, that may be applied to scanned images within the scanner device or its driver.</p>
<p>This property is optional for all acquisition enabled items; that is, items of types WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FEEDER_FRONT, WIA_CATEGORY_FEEDER_BACK, and WIA_CATEGORY_FILM.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write or Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> or WIA_PROP_RANGE.</p>
<p>Values can be from 1 to maximum VT_I4 (0xFFFF). For example, 100 means no scaling, 050 means scaling down to 50% of the orignal size, and 200 means scaling up to 200% of the original size.</p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_YEXTENT"></span><span id="wia_ips_yextent"></span><dl> <dt><strong>WIA_IPS_YEXTENT</strong></dt> <dt>ScannerPictureYextent</dt> </dl></td>
<td ><p>Contains the current height, in pixels, of the selected image to acquire. An application sets this property to mark the height of a selection area. This property must be agree with the value of the <a href="-wia-wiaitempropcommonitem.md"><strong>WIA_IPA_PIXELS_PER_LINE</strong></a> property. The minidriver creates and maintains this property.</p>
<p>Required for all acquisition enabled items; that is, items in the categories: WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FEEDER_FRONT, WIA_CATEGORY_FEEDER_BACK, and WIA_CATEGORY_FILM.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_RANGE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_YPOS"></span><span id="wia_ips_ypos"></span><dl> <dt><strong>WIA_IPS_YPOS</strong></dt> <dt>ScannerPictureYpos</dt> </dl></td>
<td ><p>Current y coordinate, in pixels, of the upper-left corner of the selected image. An application sets this property to mark the upper-left corner of the selection area. The minidriver creates and maintains this property.</p>
<p>Required for all acquisition enabled items; that is, items in the categories: WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FEEDER_FRONT, WIA_CATEGORY_FEEDER_BACK, WIA_CATEGORY_FINISHED_FILE, and WIA_CATEGORY_FILM. It is not supported for WIA_CATEGORY_FOLDER items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_RANGE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPS_YRES"></span><span id="wia_ips_yres"></span><dl> <dt><strong>WIA_IPS_YRES</strong></dt> <dt>ScannerPictureYres</dt> </dl></td>
<td ><p>Contains the current vertical resolution, in pixels per inch, for the device. An application sets this property to set the vertical resolution. The minidriver creates and maintains this property.</p>
<p>If the device can be set to only a single value, create a <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> type and place the valid value in it. This is also a case where one resolution setting depends on another resolution. (The horizontal resolution can depend on the vertical resolution.)</p>
<p>Required for all acquisition enabled items; that is, items in the categories: WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FEEDER_FRONT, WIA_CATEGORY_FEEDER_BACK, WIA_CATEGORY_FINISHED_FILE, and WIA_CATEGORY_FILM. It is not supported for WIA_CATEGORY_FOLDER items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write or Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_RANGE</a> or WIA_PROP_LIST</p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPS_YSCALING"></span><span id="wia_ips_yscaling"></span><dl> <dt><strong>WIA_IPS_YSCALING</strong></dt> <dt>ScannerPictureYscaling</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Sets the vertical scaling, as a percentage, that may be applied to scanned images within the scanner device or its driver.</p>
<p>This property is optional for all acquisition enabled items; that is, items of types WIA_CATEGORY_FLATBED, WIA_CATEGORY_FEEDER, WIA_CATEGORY_FEEDER_FRONT, WIA_CATEGORY_FEEDER_BACK, and WIA_CATEGORY_FILM.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write or Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> or WIA_PROP_RANGE.</p>
<p>Values can be from 1 to maximum VT_I4 (0xFFFF). For example, 100 means no scaling, 050 means scaling down to 50% of the orignal size, and 200 means scaling up to 200% of the original size.</p></td>
</tr>
</tbody>
</table>



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wiadef.h</dt> </dl> |



 

 




