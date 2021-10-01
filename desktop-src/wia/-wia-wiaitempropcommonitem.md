---
description: The following device property constants must be supported by all IWiaItem, IWiaItem2 and IWiaDrvItem Interface interfaces unless otherwise noted in their descriptions.
ms.assetid: ef48313e-4df4-4ccd-a085-f714100885a7
title: Common WIA Item Property Constants (Wiadef.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WIA_IPA_ACCESS_RIGHTS
- WIA_IPA_APP_COLOR_MAPPING
- WIA_IPA_BITS_PER_CHANNEL
- WIA_IPA_BUFFER_SIZE
- WIA_IPA_BYTES_PER_LINE
- WIA_IPA_CHANNELS_PER_PIXEL
- WIA_IPA_COLOR_PROFILE
- WIA_IPA_COMPRESSION
- WIA_IPA_DATATYPE
- WIA_IPA_DEPTH
- WIA_IPA_FILENAME_EXTENSION
- WIA_IPA_FORMAT
- WIA_IPA_FULL_ITEM_NAME
- WIA_IPA_GAMMA_CURVES
- WIA_IPA_ICM_PROFILE_NAME
- WIA_IPA_ITEM_CATEGORY
- WIA_IPA_ITEM_FLAGS
- WIA_IPA_ITEM_NAME
- WIA_IPA_ITEM_SIZE
- WIA_IPA_ITEM_TIME
- WIA_IPA_ITEMS_STORED
- WIA_IPA_MIN_BUFFER_SIZE
- WIA_IPA_NUMBER_OF_LINES
- WIA_IPA_PIXELS_PER_LINE
- WIA_IPA_PLANAR
- WIA_IPA_PREFERRED_FORMAT
- WIA_IPA_PROP_STREAM_COMPAT_ID
- WIA_IPA_RAW_BITS_PER_CHANNEL
- WIA_IPA_REGION_TYPE
- WIA_IPA_SUPPRESS_PROPERTY_PAGE
- WIA_IPA_TYMED
- WIA_IPA_UPLOAD_ITEM_SIZE
api_type: 
- HeaderDef
api_location: 
- wiadef.h
---

# Common WIA Item Property Constants

The following device property constants must be supported by all [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem), [**IWiaItem2**](-wia-iwiaitem2.md) and [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) interfaces unless otherwise noted in their descriptions.

The prefix "WIA\_IPA\_" indicates an item property for all devices and is the naming convention used in C/C++. For scripting purposes these constants use the prefix "Picture" and are part of the [WiaItemPropertyId](-wia-wiaitempropertyid.md) enumerated type. The corresponding member name from that script enumeration appears in parentheses next to the C/C++ constant name in the following list.



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
<td ><span id="WIA_IPA_ACCESS_RIGHTS"></span><span id="wia_ipa_access_rights"></span><dl> <dt><strong>WIA_IPA_ACCESS_RIGHTS</strong></dt> <dt>PictureAccessRights</dt> </dl></td>
<td >This flag controls access to the item as well as whether the item is deleted.<br/> Required for all WIA 2.0 items.<br/> Type: <strong>VT_I4</strong>; Read/Write or Read Only, depending on the item's ability to have its access rights changed; Valid values: WIA_PROP_FLAG<br/> The following table has the five flags that are valid with this property.<br/> 
<table>
<thead>
<tr class="header">
<th>Access Right</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_ITEM_READ</td>
<td>Item has read-only access.</td>
</tr>
<tr class="even">
<td>WIA_ITEM_WRITE</td>
<td>Item has write-only access.</td>
</tr>
<tr class="odd">
<td>WIA_ITEM_CAN_BE_DELETED</td>
<td>Item has delete-only access.</td>
</tr>
<tr class="even">
<td>WIA_ITEM_RD</td>
<td>WIA_ITEM_READ | WIA_ITEM_CAN_BE_DELETED</td>
</tr>
<tr class="odd">
<td>WIA_ITEM_RWD</td>
<td>WIA_ITEM_READ | WIA_ITEM_WRITE | WIA_ITEM_CAN_BE_DELETED</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_APP_COLOR_MAPPING"></span><span id="wia_ipa_app_color_mapping"></span><dl> <dt><strong>WIA_IPA_APP_COLOR_MAPPING</strong></dt> <dt>PictureAppColorMapping</dt> </dl></td>
<td ><p>This property is reserved by for future use and is not implemented at this time.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_BITS_PER_CHANNEL"></span><span id="wia_ipa_bits_per_channel"></span><dl> <dt><strong>WIA_IPA_BITS_PER_CHANNEL</strong></dt> <dt>PictureBitsPerChannel</dt> </dl></td>
<td ><p>Contains the number of bits per channel for the image. The minidriver creates and maintains this property.</p>
<p>Required for all WIA 2.0 acquisition-enabled or stored image items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_BUFFER_SIZE"></span><span id="wia_ipa_buffer_size"></span><dl> <dt><strong>WIA_IPA_BUFFER_SIZE</strong></dt> <dt>PictureBufferSize</dt> </dl></td>
<td ><p>Contains the size of the buffer, in bytes, used during a data transfer. The minidriver creates and maintains this property.</p>
<p>An application can read this property to determine the driver-specified buffer size for data transfers. The WIA service also reads this property to allocate memory for the minidriver during the data transfer</p>
<p>Optional for all transfer-enabled WIA 2.0 items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<div class="alert">
<blockquote>
[!Note]<br />
The <strong>WIA_IPA_BUFFER_SIZE</strong> property contains is the minimum amount of data an application can request at any given time. The larger the buffer size, the larger the requests to the device will be. This can make the device seem slow and unresponsive, can slow the overall system performance, and can consume excessive resources. Buffer sizes that are too small can slow performance of the data transfer by requiring many smaller requests. Choose a reasonable buffer size by considering the typical size of a data request to your device and balancing the number of requests against the size of those requests.
</blockquote>
</div>
<div>
 
</div></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_BYTES_PER_LINE"></span><span id="wia_ipa_bytes_per_line"></span><dl> <dt><strong>WIA_IPA_BYTES_PER_LINE</strong></dt> <dt>PictureBytesPerLine</dt> </dl></td>
<td ><p>Contains the number of bytes in one scan line of the image. The minidriver creates and maintains this property.</p>
<p>Optional for all WIA 2.0 items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_CHANNELS_PER_PIXEL"></span><span id="wia_ipa_channels_per_pixel"></span><dl> <dt><strong>WIA_IPA_CHANNELS_PER_PIXEL</strong></dt> <dt>PictureChannelsPerPixel</dt> </dl></td>
<td ><p>Contains the number of channels per pixel for the image. The minidriver creates and maintains this property.</p>
<p>Required for all WIA 2.0 acquisition-enabled or stored image items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_COLOR_PROFILE"></span><span id="wia_ipa_color_profile"></span><dl> <dt><strong>WIA_IPA_COLOR_PROFILE</strong></dt> <dt>PictureColorProfile</dt> </dl></td>
<td ><p>This property is reserved by for future use and is not implemented at this time.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_COMPRESSION"></span><span id="wia_ipa_compression"></span><dl> <dt><strong>WIA_IPA_COMPRESSION</strong></dt> <dt>PictureCompression</dt> </dl></td>
<td ><p>Contains the current compression type used. The minidriver creates and maintains this property.</p>
<p>An application reads this property to determine the image compression type or sets this property to configure the compression setting.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the constants that are valid with this property. The <strong>V</strong> symbol indicates that the constant is supported only in Windows Vista and later. (It is only available through the <a href="-wia-iwiaitem2.md"><strong>IWiaItem2</strong></a> interface.)</p>

<table>
<thead>
<tr class="header">
<th>Compression Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_COMPRESSION_NONE</td>
<td>No compression. See <strong>Note</strong> for more information.</td>
</tr>
<tr class="even">
<td>WIA_COMPRESSION_AUTO</td>
<td>Automatic compression mode. See <strong>Note</strong> for more information.</td>
</tr>
<tr class="odd">
<td>WIA_COMPRESSION_BI_RLE4</td>
<td>RLE4 compression</td>
</tr>
<tr class="even">
<td>WIA_COMPRESSION_BI_RLE8</td>
<td>RLE8 compression</td>
</tr>
<tr class="odd">
<td>WIA_COMPRESSION_G3</td>
<td>Group 3 compression</td>
</tr>
<tr class="even">
<td>WIA_COMPRESSION_G4</td>
<td>Group 4 compression</td>
</tr>
<tr class="odd">
<td>WIA_COMPRESSION_JPEG</td>
<td>JPEG compression.</td>
</tr>
<tr class="even">
<td>WIA_COMPRESSION_JBIG<strong>V</strong></td>
<td>JBIG compression.</td>
</tr>
<tr class="odd">
<td>WIA_COMPRESSION_JPEG2K<strong>V</strong></td>
<td>JPEG 2000 compression.</td>
</tr>
<tr class="even">
<td>WIA_COMPRESSION_PNG<strong>V</strong></td>
<td>PNG compression.</td>
</tr>
</tbody>
</table>

<p> </p>
<div class="alert">
<blockquote>
<p>[!Note]</p>
<p>When this property is WIA_COMPRESSION_NONE, and WIA_IPA_FORMAT is either WiaImgFmt_PDFA or WiaImgFmt_XPS; then WIA_COMPRESSION_NONE means that the compression mode is undefined and the scanner must decide on a mode.</p>
<p>WIA_COMPRESSION_AUTO is a new property value defined for the WIA_IPA_COMPRESSION property. This value is valid for all programmable image data source items, including the Flatbed and Feeder. When this value is supported by the WIA mini-driver, the WIA application client can set WIA_IPA_COMPRESSION in order to enable automatic compression mode detection at the device. WIA_COMPRESSION_AUTO can work with and without full auto-color being supported or enabled (WIA_DATA_AUTO and WIA_DEPTH_AUTO).</p>
<p>WIA_COMPRESSION_AUTO is most useful with transfer file formats that support multiple data types and bit depths, such as WiaImgFmt_RAW. For more information about transfer file formats, see WIA_IPA_FORMAT in this table.</p>
<p>It is opitonal for the WIA mini-driver to suport WIA_COMPRESSION_AUTO. When it is supported, the WIA mini-driver must never set it as the default value for WIA_IPA_COMPRESSION; only the WIA application can set this value.</p>
</blockquote>
</div>
<div>
 
</div></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_DATATYPE"></span><span id="wia_ipa_datatype"></span><dl> <dt><strong>WIA_IPA_DATATYPE</strong></dt> <dt>PictureDatatype</dt> </dl></td>
<td ><p>Contains the current data type setting for the device. The minidriver creates and maintains this property.</p>
<p>An application reads this property to determine the data type of the image. An application writes this property to set the current data type of the image about to be transferred.</p>
<p>This property is required for all WIA 2.0 items. It must be Read/Write for all WIA 2.0 acquisition enabled items and Read Only for WIA 2.0 storage items.</p>
<p>Type: <strong>VT_I4</strong>; Access for pre-Windows Vista operating systems: This property is Read Only for cameras and Read/Write for scanners; Access for Windows Vista and later: This property is Read Only for WIA_CATEGORY_FOLDER and WIA_CATEGORY_FINISHED_FILE items, and Read/Write for all other WIA 2.0 item categories; Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the six constants that are valid with when <strong>WIA_IPA_FORMAT</strong> is not set to WiaImgFmt_RAW.</p>

<table>
<thead>
<tr class="header">
<th>Data Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_DATA_AUTO</td>
<td>Valid for all programmable image data source items, including the Flatbed and Feeder. When this value is supported by the WIA mini-driver, the WIA application client can set WIA_IPA_DATATYPE in order to enable automatic color detection at the device. When WIA_DATA_AUTO is set, the WIA mini-driver must update WIA_IPA_DEPTH on the same item to WIA_DEPTH_AUTO (which must be a supported value if the device supports automatic color).<br/> This is an optional value, but it is required when WIA_DEPTH_AUTO is supported for WIA_IPA_DEPTH.<br/></td>
</tr>
<tr class="even">
<td>WIA_DATA_COLOR</td>
<td>Scan data is red, green, blue (RGB) color. The full color format is described using the following WIA properties: <strong>WIA_IPA_CHANNELS_PER_PIXEL</strong><br/> <strong>WIA_IPA_BITS_PER_CHANNEL</strong><br/> <strong>WIA_IPA_PLANAR</strong><br/> <strong>WIA_IPA_PIXELS_PER_LINE</strong><br/> <strong>WIA_IPA_BYTES_PER_LINE</strong><br/> <strong>WIA_IPA_NUMBER_OF_LINES</strong><br/></td>
</tr>
<tr class="odd">
<td>WIA_DATA_COLOR_DITHER</td>
<td>Same as WIA_DATA_COLOR except that the data is dithered using the currently selected dither pattern.</td>
</tr>
<tr class="even">
<td>WIA_DATA_COLOR_THRESHOLD</td>
<td>Same as WIA_DATA_COLOR except that the threshold value is used when scanning the data. Color values over the <a href="https://msdn.microsoft.com/library/ms796233.aspx">WIA_IPS_THRESHOLD</a> value are converted to full brightness; colors under this value are converted to black.</td>
</tr>
<tr class="odd">
<td>WIA_DATA_DITHER</td>
<td>Scan data is dithered using the currently selected dither pattern.</td>
</tr>
<tr class="even">
<td>WIA_DATA_GRAYSCALE</td>
<td>Scan data represents intensity. The palette is a fixed, equally-spaced gray scale with a depth specified by <a href="https://msdn.microsoft.com/library/ms795935.aspx">WIA_IPA_DEPTH</a> property.</td>
</tr>
<tr class="odd">
<td>WIA_DATA_THRESHOLD</td>
<td>The threshold is one bit per pixel of black-and-white data. Data over the current value of <a href="https://msdn.microsoft.com/library/ms796233.aspx">WIA_IPS_THRESHOLD</a> is converted to white; data under this value is converted to black.</td>
</tr>
</tbody>
</table>

<p> </p>
<p>The <strong>WIA_IPA_DATATYPE</strong> property is also used to describe the type of RAW data transfer to be used when the application sets WiaImgFmt_RAW. The driver should set the <strong>WIA_IPA_DATATYPE</strong> property to a list of allowed values from which the application can pick one.</p>
<p>If the device can be set to only a single value, create a <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> type, and place the valid value in it.</p>
<p>Check the <a href="https://msdn.microsoft.com/library/ms795935.aspx">WIA_IPA_DEPTH</a> property to determine the bit depth. This property usually contains a single value for cameras.</p>
<p>The following table lists the constants that are valid with <strong>WIA_IPA_DATATYPE</strong> when <strong>WIA_IPA_FORMAT</strong> is set to WiaImgFmt_RAW.</p>

<table>
<thead>
<tr class="header">
<th>Data Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_DATA_GRAYSCALE</td>
<td>Scan data represents intensity. The palette is a fixed, equally spaced grayscale with a depth specified by the <a href="https://msdn.microsoft.com/library/ms795935.aspx">WIA_IPA_DEPTH</a> property. <a href="https://msdn.microsoft.com/library/ms795495.aspx">WIA_IPA_RAW_BITS_PER_CHANNEL</a> must be set to 1.</td>
</tr>
<tr class="even">
<td>WIA_DATA_RAW_BGR</td>
<td>Scan data is in the BGR (blue-green-red) colorspace. The full color format is described using the followingWIAproperties: <a href="https://msdn.microsoft.com/library/ms796163.aspx">WIA_IPA_CHANNELS_PER_PIXEL</a><br/> <a href="https://msdn.microsoft.com/library/ms795997.aspx">WIA_IPA_BITS_PER_CHANNEL</a><br/> <a href="https://msdn.microsoft.com/library/ms796567.aspx">WIA_IPA_PIXELS_PER_LINE</a><br/> <a href="https://msdn.microsoft.com/library/ms796404.aspx">WIA_IPA_BYTES_PER_LINE</a><br/> <a href="https://msdn.microsoft.com/library/ms795916.aspx">WIA_IPA_NUMBER_OF_LINES</a><br/> <a href="https://msdn.microsoft.com/library/ms795495.aspx">WIA_IPA_RAW_BITS_PER_CHANNEL</a> must be set to 3.<br/></td>
</tr>
<tr class="odd">
<td>WIA_DATA_RAW_CMY</td>
<td>Scan data is in the cyan-magenta-yellow (CMY) colorspace. The full color format is described using the same WIA properties as in WIA_DATA_RAW_BGR. <a href="https://msdn.microsoft.com/library/ms795495.aspx">WIA_IPA_RAW_BITS_PER_CHANNEL</a> must be set to 3.<br/></td>
</tr>
<tr class="even">
<td>WIA_DATA_RAW_CMYK</td>
<td>Scan data is in the cyan-magenta-yellow-black (CMYK) colorspace. The full color format is described using the same WIA properties as in WIA_DATA_RAW_BGR. <a href="https://msdn.microsoft.com/library/ms795495.aspx">WIA_IPA_RAW_BITS_PER_CHANNEL</a> must be set to 4.<br/></td>
</tr>
<tr class="odd">
<td>WIA_DATA_RAW_RGB</td>
<td>Scan data is in the red-green-blue (RGB) colorspace. The full color format is described using the same WIA properties as in WIA_DATA_RAW_BGR. <a href="https://msdn.microsoft.com/library/ms795495.aspx">WIA_IPA_RAW_BITS_PER_CHANNEL</a> must be set to 3.<br/></td>
</tr>
<tr class="even">
<td>WIA_DATA_RAW_YUV</td>
<td>Scan data is in the luminance-blue difference-red difference (YUV) colorspace. The full color format is described using the same WIA properties as in WIA_DATA_RAW_BGR. <a href="https://msdn.microsoft.com/library/ms795495.aspx">WIA_IPA_RAW_BITS_PER_CHANNEL</a> must be set to 3.<br/></td>
</tr>
<tr class="odd">
<td>WIA_DATA_RAW_YUVK</td>
<td>Scan data is in the luminance-blue difference-red difference-black (YUVK) colorspace. The full color format is described using the same WIA properties as in WIA_DATA_RAW_BGR. <a href="https://msdn.microsoft.com/library/ms795495.aspx">WIA_IPA_RAW_BITS_PER_CHANNEL</a> must be set to 4.<br/></td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_DEPTH"></span><span id="wia_ipa_depth"></span><dl> <dt><strong>WIA_IPA_DEPTH</strong></dt> <dt>PictureDepth</dt> </dl></td>
<td ><p>WIA_IPA_DEPTH Contains the bit depth setting of an image. The minidriver creates and maintains this property.An application reads this property to determine the bit depth setting of the image. The application might also be able to set this value to the desired bit depth.</p>
<p>If the device can be set to only a single value, create a <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> type and place the valid value in it.</p>
<p>This property is required for all WIA 2.0 items. It must be Read/Write for all WIA 2.0 acquisition enabled items and Read Only for WIA 2.0 storage items.</p>
<p>Type: <strong>VT_I4</strong>; Access for pre-Windows Vista operating systems: Read/Write; Access for Windows Vista and later: This property is Read Only for WIA_CATEGORY_FOLDER and WIA_CATEGORY_FINISHED_FILE items, and Read/Write for all other WIA 2.0 item categories; Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>WIA_DEPTH_AUTO is defined as 0 bits per pixel, and it is a new property value defined for the WIA_IPA_DEPTH. This value is valid for all programmable image data source items, including the Flatbed and Feeder. When WIA_DEPTH_AUTO is supported by the WIA mini-driver, the WIA application client can set WIA_IPA_DEPTH to this value, to enable automatic color detection at the device. When WIA_DEPTH_AUTO is set, the WIA mini-driver must update WIA_IPA_DATATYPE on the same item to WIA_DATA_AUTO (which must be a supported value, if the device supports automatic color).</p>
<p>WIA_DEPTH_AUTO is an optional value, but it becomes required when WIA_DATA_AUTO is supported for WIA_IPA_DATATYPE.</p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_FILENAME_EXTENSION"></span><span id="wia_ipa_filename_extension"></span><dl> <dt><strong>WIA_IPA_FILENAME_EXTENSION</strong></dt> <dt>PictureFilenameExtension</dt> </dl></td>
<td ><p>Contains the file name extension for a particular file format. The minidriver creates and maintains this property.</p>
<p>Optional for all transfer-enabled WIA 2.0 items.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>The driver updates this property to reflect the current value of the <a href="https://msdn.microsoft.com/library/ms796440.aspx">WIA_IPA_FORMAT</a> property.</p>
<p>For example, if <strong>WIA_IPA_FORMAT</strong> is WiaImgFmt_JPEG, then <a href="-wia-property-attributes.md">WIA_IPA_FILENAME_EXTENSION</a> should be <strong>jpg</strong>. If <strong>WIA_IPA_FORMAT</strong> is WiaImgFmt_BMP, then WIA_IPA_FILENAME_EXTENSION should be BMP.</p>
<div class="alert">
<blockquote>
[!Note]<br />
The file name extension does not include the dot.
</blockquote>
</div>
<div>
 
</div>
<p>This property is recommended for drivers that support standard formats and is required for drivers that implement custom-defined formats. It informs the application of the correct file name extension to use during the transfer of privately formatted files. For example, if the A. Datum Corporation created a WIA driver that transferred a file in a new format, the company could specify an extension of &quot;adc&quot;. This allows applications to transfer data in that format to a file and to create a file name such as <em>myfile.adc</em>,which is useful to others who understand the new extension.</p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_FORMAT"></span><span id="wia_ipa_format"></span><dl> <dt><strong>WIA_IPA_FORMAT</strong></dt> <dt>PictureFormat</dt> </dl></td>
<td ><p>Contains the current format of the image about to be transferred.</p>
<p>An application reads this property to determine the format of the image that it is about to receive. An application writes this property to set the format. This property depends on the <a href="https://msdn.microsoft.com/library/ms795488.aspx">WIA_IPA_TYMED</a> property. The minidriver creates and maintains this property.</p>
<p>If the device can be set to only a single value, create a <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> type, and place the valid value in it.</p>
<p>Type: <strong>CLSID</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table lists the constants that are valid with this property. The asterisk * indicates that the constant is not supported in Windows Vista. (It is only available through the <a href="/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem"><strong>IWiaItem</strong></a> interface.) The double asterisk ** indicates that the constant is not supported in either Windows Server 2003 or Windows Vista. The <strong>V</strong> symbol indicates that the constant is supported only in Windows Vista and later. (It is only available through the <a href="-wia-iwiaitem2.md"><strong>IWiaItem2</strong></a> interface.)</p>

<table>
<thead>
<tr class="header">
<th>Format</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WiaAudFmt_AIFF</td>
<td>AIFF audio format</td>
</tr>
<tr class="even">
<td>WiaAudFmt_MP3</td>
<td>MP3 audio format</td>
</tr>
<tr class="odd">
<td>WiaAudFmt_WAV</td>
<td>WAV audio format</td>
</tr>
<tr class="even">
<td>WiaAudFmt_WMA</td>
<td>WMA audio format</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_ASF**</td>
<td>ASF video format</td>
</tr>
<tr class="even">
<td>WiaImgFmt_AVI**</td>
<td>AVI video format</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_BMP</td>
<td>Windows bitmap with a header file</td>
</tr>
<tr class="even">
<td>WiaImgFmt_CIFF*</td>
<td>Camera Image File format</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_DPOF</td>
<td>DPOF printing format</td>
</tr>
<tr class="even">
<td>WiaImgFmt_EMF</td>
<td>Extended Windows metafile</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_EXEC</td>
<td>Executable file</td>
</tr>
<tr class="even">
<td>WiaImgFmt_EXIF</td>
<td>Exchangeable File Format</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_FLASHPIX</td>
<td>FlashPix format</td>
</tr>
<tr class="even">
<td>WiaImgFmt_GIF</td>
<td>GIF image format</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_HTML</td>
<td>HTML format</td>
</tr>
<tr class="even">
<td>WiaImgFmt_ICO</td>
<td>Windows icon file format</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_JBIG<strong>V</strong></td>
<td>The Joint Bi-level Image Experts Group (JBIG) format.</td>
</tr>
<tr class="even">
<td>WiaImgFmt_JPEG</td>
<td>JPEG compressed format</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_JPEG2K</td>
<td>JPEG 2000 compressed format</td>
</tr>
<tr class="even">
<td>WiaImgFmt_JPEG2KX</td>
<td>JPEG 2000 compressed format</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_MEMORYBMP</td>
<td>Windows bitmap without a header file</td>
</tr>
<tr class="even">
<td>WiaImgFmt_PDFA<strong>V</strong></td>
<td>The PDF/A (ISO/CD 19005-1) format.</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_MPG**</td>
<td>MPEG video format</td>
</tr>
<tr class="even">
<td>WiaImgFmt_PHOTOCD</td>
<td>Eastman Kodak file format</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_PICT</td>
<td>Apple file format</td>
</tr>
<tr class="even">
<td>WiaImgFmt_PNG</td>
<td>W3C PNG format</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_RAW</td>
<td>Raw format for data transfers only</td>
</tr>
<tr class="even">
<td>WiaImgFmt_RAWRGB</td>
<td>Raw RGB format</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_RTF</td>
<td>Rich Text File format</td>
</tr>
<tr class="even">
<td>WiaImgFmt_SCRIPT</td>
<td>Script file</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_TIFF</td>
<td>Tag Image File Format</td>
</tr>
<tr class="even">
<td>WiaImgFmt_TXT</td>
<td>Text file</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_UNICODE16</td>
<td>UNICODE 16-bit encoding</td>
</tr>
<tr class="even">
<td>WiaImgFmt_WMF</td>
<td>Windows metafile</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_XML</td>
<td>XML file</td>
</tr>
<tr class="even">
<td>WiaImgFmt_XPS<strong>V</strong></td>
<td>XPS Package format</td>
</tr>
</tbody>
</table>

<p> </p>
<div class="alert">
<blockquote>
[!Note]<br />
When this property is either WiaImgFmt_PDFA or WiaImgFmt_XPS, and WIA_IPA_COMPRESSION is WIA_COMPRESSION_NONE; then the latter value means that the compression mode is undefined and the scanner must decide on a mode.
</blockquote>
</div>
<div>
 
</div></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_FULL_ITEM_NAME"></span><span id="wia_ipa_full_item_name"></span><dl> <dt><strong>WIA_IPA_FULL_ITEM_NAME</strong></dt> <dt>PictureFullItemName</dt> </dl></td>
<td ><p>Contains the full item name (the item name together with path information). The full item name is the same as the <em>bstrFullItemName</em> parameter of the <a href="https://msdn.microsoft.com/library/ms794649.aspx">wiasCreateDrvItem</a> service utility function. An application reads this property to determine which item it is currently using and where that item is located in the item tree. Each item should have a unique name. Applications commonly use the full item name to search for items in the item tree. The WIA service creates and maintains this property.</p>
<p>Required for all WIA 2.0 items.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_GAMMA_CURVES"></span><span id="wia_ipa_gamma_curves"></span><dl> <dt><strong>WIA_IPA_GAMMA_CURVES</strong></dt> <dt>PictureGammaCurves</dt> </dl></td>
<td ><p>This property is reserved for future use and is not implemented at this time.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_ICM_PROFILE_NAME"></span><span id="wia_ipa_icm_profile_name"></span><dl> <dt><strong>WIA_IPA_ICM_PROFILE_NAME</strong></dt> <dt>PictureIcmProfileName</dt> </dl></td>
<td ><p>Contains the ICM profile name that is needed to properly decode the image. An application reads this property to determine the ICM profile to use when processing the image. The WIA service creates and maintains this property based on the ICMProfiles entry in the driver installation file.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_ITEM_CATEGORY"></span><span id="wia_ipa_item_category"></span><dl> <dt><strong>WIA_IPA_ITEM_CATEGORY</strong></dt> <dt>PictureItemCategory</dt> </dl></td>
<td ><p>Supported only in Windows Vista and later.</p>
<p>WIA 2.0 items are grouped into categories that define how a <a href="-wia-iwiaitem2.md"><strong>IWiaItem2</strong></a> is to be treated or used. For example, If the item represents a feeder, then the application should expect it to contain the required document feeder properties and operate like a document feeder. If the item represents a finished file, then a WIA 2.0 application should treat it that way, assuming that the data is static and located on the device. (The rules for each item will be defined in their individual specification documents.)</p>
<p>Required for all WIA 2.0 items.</p>
<p>Type: <strong>VT_CLSID</strong>, Access: Read Only, Valid values: <a href="-wia-wia2-itemcategoryguids.md"><strong>Item Category GUIDs</strong></a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_ITEM_FLAGS"></span><span id="wia_ipa_item_flags"></span><dl> <dt><strong>WIA_IPA_ITEM_FLAGS</strong></dt> <dt>PictureItemFlags</dt> </dl></td>
<td ><p>Contains the descriptive flags for a WIA item. The item flags are the same as those in the <em>lObjectFlags</em> parameter of the <a href="https://msdn.microsoft.com/library/ms794649.aspx">wiasCreateDrvItem</a> service utility function. The WIA service creates and maintains this property.</p>
<p>An application reads this property to determine the item's descriptive flag values.</p>
<p>Type: <strong>VT_I4</strong> Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>The following table has the flags that are valid with this property. An asterisk * indicates that the flag is not supported in Windows Vista or later. (It is only available through the <a href="/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem"><strong>IWiaItem</strong></a> interface.) An double asterisk ** indicates that the flag is not supported in either Windows Server 2003 or Windows Vista or later. The <strong>V</strong> symbol indicates that the flag is supported only in Windows Vista and later. (It is only available through the <a href="-wia-iwiaitem2.md"><strong>IWiaItem2</strong></a> interface.)</p>

<table>
<thead>
<tr class="header">
<th>Flag</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WiaItemTypeAnalyze*</td>
<td>This item supports the <strong>IWiaItem::AnalyzeItem</strong> method (described in the Platform SDK documentation). This item also supports automatic child item generation. This capability is useful for region detection or page decomposition.</td>
</tr>
<tr class="even">
<td>WiaItemTypeAudio</td>
<td>This item supports audio. This flag is valid only for items that also have the <strong>WiaItemTypeFile</strong> flag set.</td>
</tr>
<tr class="odd">
<td>WiaItemTypeBurst*</td>
<td>For folders only. This flag indicates that the images in this folder were taken in a continuous time sequence.</td>
</tr>
<tr class="even">
<td>WiaItemTypeDeleted</td>
<td>This item is marked for deletion, this item has been deleted, this item does not exist, or the contents of this item are invalid.</td>
</tr>
<tr class="odd">
<td>WiaItemTypeDocument<strong>V</strong></td>
<td>This item is a document file in one of the document formats that the <strong>WIA_IPA_FORMAT</strong> property contains. (These formats include those for nonimage files, such as .txt, .htm, and .doc files.)</td>
</tr>
<tr class="even">
<td>WiaItemTypeDevice</td>
<td>This item represents a connected device.</td>
</tr>
<tr class="odd">
<td>WiaItemTypeDisconnected</td>
<td>This item represents a disconnected device.</td>
</tr>
<tr class="even">
<td>WiaItemTypeFile</td>
<td>The item supports file transfers.</td>
</tr>
<tr class="odd">
<td>WiaItemTypeFolder</td>
<td>The item is a folder.</td>
</tr>
<tr class="even">
<td>WiaItemTypeFree</td>
<td>The item is uninitialized or has been deleted.</td>
</tr>
<tr class="odd">
<td>WiaItemTypeGenerated</td>
<td>This item has been generated by an application or by the driver.</td>
</tr>
<tr class="even">
<td>WiaItemTypeHasAttachments*</td>
<td>This item supports attachments and currently contains attachments.</td>
</tr>
<tr class="odd">
<td>WiaItemTypeHPanorama*</td>
<td>This item represents a horizontal panoramic image. This flag is valid only for items that also have the <strong>WiaItemTypeFolder</strong> flag set.</td>
</tr>
<tr class="even">
<td>WiaItemTypeImage</td>
<td>The item is an image file. This flag is valid only for items that also have the <strong>WiaItemTypeFile</strong> flag set.</td>
</tr>
<tr class="odd">
<td>WiaItemTypeProgrammableDataSource<strong>V</strong></td>
<td>The item is a programmable data source and follows a set of predefined configuration rules, which are based on <strong>WIA_IPA_ITEM_CATEGORY</strong>.</td>
</tr>
<tr class="even">
<td>WiaItemTypeRoot<strong>V</strong></td>
<td>This item is the root item, which is the parent to all the feature items that the device supports.</td>
</tr>
<tr class="odd">
<td>WiaItemTypeStorage</td>
<td>This flag indicates additional storage for folders items. WIA drivers specify their items in terms of images and folders. No WIA properties exist that describe the characteristics of a storage item (such as remaining storage space, write speed, or type of media. Vendor-specific properties that expose this information can be added. These properties are accessible only to applications or extensions that are written to recognize them.</td>
</tr>
<tr class="even">
<td>WiaItemTypeTransfer</td>
<td>This item can be used to transfer data.</td>
</tr>
<tr class="odd">
<td>WiaItemTypeTwainCapabilityPassThrough</td>
<td>This type indicates that the WIA device is able to receive TWAIN capability data from the TWAIN compatibility layer. If this type is set, any TWAIN capability that is not understood by the TWAIN compatibility layer will be passed to theWIA driver. This is valid only for the root item.</td>
</tr>
<tr class="even">
<td>WiaItemTypeVideo**</td>
<td>This item supports streaming video.</td>
</tr>
<tr class="odd">
<td>WiaItemTypeVPanorama*</td>
<td>This item represents a vertical panoramic image. This flag is valid only for items that also have the <strong>WiaItemTypeFolder</strong> flag set.</td>
</tr>
</tbody>
</table>

<p> </p>
<p>Some of these flags are required or optional for WIA 2.0 items, according to the category of the item, as shown in this table.</p>

<table>
<thead>
<tr class="header">
<th>Category of Item</th>
<th>Required</th>
<th>Optional</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_CATEGORY_ROOT</td>
<td>WiaItemTypeRoot WiaItemTypeFolder</td>
<td>WiaItemTypeDevice WiaItemTypeDisconnected</td>
</tr>
<tr class="even">
<td>WIA_CATEGORY_FLATBED</td>
<td>WiaItemTypeProgrammableDataSource WiaItemTypeTransfer WiaItemTypeImage WiaItemTypeFile</td>
<td>WiaItemTypeFolder (If multiple scan regions items are supported, this flag is optional only for the WIA_CATEGORY_FLATBED root item.)</td>
</tr>
<tr class="odd">
<td>WIA_CATEGORY_FEEDER WIA_CATEGORY_FEEDER_FRONT WIA_CATEGORY_FEEDER_BACK</td>
<td>WiaItemTypeProgrammableDataSource WiaItemTypeTransfer WiaItemTypeImage WiaItemTypeFile</td>
<td>WiaItemTypeFolder (If WIA_CATEGORY_FEEDER_FRONT and WIA_CATEGORY_FEEDER_BACK items are present, then this flag is optional only for the WIA_CATEGORY_FEEDER root item.)</td>
</tr>
<tr class="even">
<td>WIA_CATEGORY_FILM (root)</td>
<td>WiaItemTypeProgrammableDataSource WiaItemTypeTransfer WiaItemTypeImage WiaItemTypeFile WiaItemTypeFolder</td>
<td>None</td>
</tr>
<tr class="odd">
<td>WIA_CATEGORY_FILM (children)</td>
<td>WiaItemTypeProgrammableDataSource WiaItemTypeTransfer WiaItemTypeImage WiaItemTypeFile</td>
<td>None</td>
</tr>
<tr class="even">
<td>WIA_CATEGORY_FOLDER</td>
<td>WiaItemTypeStorage WiaItemTypeFolder</td>
<td>WiaItemTypeDeleted</td>
</tr>
<tr class="odd">
<td>WIA_CATEGORY_FINISHED_FILE</td>
<td>WiaItemTypeFile WiaItemTypeTransfer</td>
<td>WiaItemTypeImage WiaItemTypeAudio WiaItemTypeDeleted</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_ITEM_NAME"></span><span id="wia_ipa_item_name"></span><dl> <dt><strong>WIA_IPA_ITEM_NAME</strong></dt> <dt>PictureItemName</dt> </dl></td>
<td ><p>Contains the item name. An application reads this property to determine which item it is currently using. Each item has a unique name. The WIA service creates and maintains this property.</p>
<p>Required for all WIA 2.0 items.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_ITEM_SIZE"></span><span id="wia_ipa_item_size"></span><dl> <dt><strong>WIA_IPA_ITEM_SIZE</strong></dt> <dt>PictureItemSize</dt> </dl></td>
<td ><p>Contains the current size, in bytes, of the data that is associated with the item. The minidriver creates and maintains this property.</p>
<p>Contains is the total size of the data being transferred. If this value is zero, it means that the minidriver has no information about the exact size of the data. (This is common for compressed data.) An application reads this value to determine the size of the acquisition before it takes place. The WIA service reads this property to assist in allocating memory for data transfers. For further information, see <a href="https://msdn.microsoft.com/library/ms792198.aspx">Transferring Data to a WIA Application</a> if the property is set to zero and TYMED is configured for a file transfer, the WIA service does not allocate any memory for the WIA minidriver.</p>
<p>Required for all transfer-enabled WIA 2.0 items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_ITEM_TIME"></span><span id="wia_ipa_item_time"></span><dl> <dt><strong>WIA_IPA_ITEM_TIME</strong></dt> <dt>PictureItemTime</dt> </dl></td>
<td ><p>Contains the time that the image was originally captured. The minidriver creates and maintains this property. This property should be reported as a vector of eight <strong>WORD</strong> values in the form of a SYSTEMTIME structure (described in the Platform SDK documentation).</p>
<p>Optional for all WIA 2.0 items.</p>
<p>Type: <strong>VT_UI2</strong> | <strong>VT_VECTOR</strong> Access: Read/Write or Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_ITEMS_STORED"></span><span id="wia_ipa_items_stored"></span><dl> <dt><strong>WIA_IPA_ITEMS_STORED</strong></dt> <dt>PictureItemItemsStored</dt> </dl></td>
<td ><p>Supported only in Windows Vista and later.</p>
<p>Specifies how many items are stored in the WIA_CATEGORY_FOLDER item.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_MIN_BUFFER_SIZE"></span><span id="wia_ipa_min_buffer_size"></span><dl> <dt><strong>WIA_IPA_MIN_BUFFER_SIZE</strong></dt> <dt>PictureMinBufferSize</dt> </dl></td>
<td ><p>Specifies the minimum buffer size that is used in data transfers. If the data transfer is performed through a callback mechanism, the property value can be as small as 64KB. However, if the transfer is to file, the property value is the number of bytes that are needed to transfer one page of data at a time. The minidriver creates and maintains this WIA property.</p>
<p>Optional for all transfer-enabled WIA 2.0 items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_NUMBER_OF_LINES"></span><span id="wia_ipa_number_of_lines"></span><dl> <dt><strong>WIA_IPA_NUMBER_OF_LINES</strong></dt> <dt>PictureNumberOfLines</dt> </dl></td>
<td ><p>Contains the number of lines contained in the image (the vertical height of the image in pixels). The minidriver creates and maintains this property.</p>
<p>Optional for all WIA 2.0 items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_PIXELS_PER_LINE"></span><span id="wia_ipa_pixels_per_line"></span><dl> <dt><strong>WIA_IPA_PIXELS_PER_LINE</strong></dt> <dt>PicturePixelsPerLine</dt> </dl></td>
<td ><p>Contains the number of pixels in each line of the image (the width of the image in pixels). The minidriver creates and maintains this property.</p>
<p>Optional for all WIA 2.0 items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_PLANAR"></span><span id="wia_ipa_planar"></span><dl> <dt><strong>WIA_IPA_PLANAR</strong></dt> <dt>PicturePlanar</dt> </dl></td>
<td ><p>This property is not supported in Windows Vista and later.</p>
<p>Contains image data packing options. The minidriver creates and maintains this property.</p>
<p>An application reads this property to determine the image packing options or sets the current image packing options.</p>
<p>Type: <strong>VT_I4</strong>; Access: Read/Write; Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a>. If the device can be set to only a single value, create a WIA_PROP_LIST type and place the valid value in it.</p>
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
<td>WIA_PACKED_PIXEL</td>
<td>Image data is in packed-pixel format.</td>
</tr>
<tr class="even">
<td>WIA_PLANAR</td>
<td>Image data is in planar format.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_PREFERRED_FORMAT"></span><span id="wia_ipa_preferred_format"></span><dl> <dt><strong>WIA_IPA_PREFERRED_FORMAT</strong></dt> <dt>PicturePreferredFormat</dt> </dl></td>
<td ><p>Contains the preferred format for images that this minidriver transfers. The minidriver creates and maintains this property.</p>
<p>Required for all transfer-enabled WIA 2.0 items.</p>
<p>Type: <strong>CLSID</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_PROP_STREAM_COMPAT_ID"></span><span id="wia_ipa_prop_stream_compat_id"></span><dl> <dt><strong>WIA_IPA_PROP_STREAM_COMPAT_ID</strong></dt> <dt>PicturePropStreamCompatId</dt> </dl></td>
<td ><p>Specifies a CLSID that represents a set of device property values. If a device driver implements this feature, applications use this property to determine if the device supports a set of values.</p>
<p>Type: <strong>CLSID</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the 12 constants that are valid with this property.</p>

<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WiaImgFmt_BMP</td>
<td>MicrosoftWindows bitmap with a header file</td>
</tr>
<tr class="even">
<td>WiaImgFmt_EMF</td>
<td>Extended Windows metafile</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_EXIF</td>
<td>Exchangeable File Format</td>
</tr>
<tr class="even">
<td>WiaImgFmt_FLASHPIX</td>
<td>FlashPix format</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_GIF</td>
<td>GIF image format</td>
</tr>
<tr class="even">
<td>WiaImgFmt_ICO</td>
<td>Windows icon file format</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_JPEG</td>
<td>JPEG compressed format</td>
</tr>
<tr class="even">
<td>WiaImgFmt_PHOTOCD</td>
<td>Eastman Kodak file format</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_PNG</td>
<td>W3C PNG format</td>
</tr>
<tr class="even">
<td>WiaImgFmt_MEMORYBMP</td>
<td>Windows bitmap without a header file</td>
</tr>
<tr class="odd">
<td>WiaImgFmt_TIFF</td>
<td>Tag Image File Format</td>
</tr>
<tr class="even">
<td>WiaImgFmt_WMF</td>
<td>Windows metafile</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_RAW_BITS_PER_CHANNEL"></span><span id="wia_ipa_raw_bits_per_channel"></span><dl> <dt><strong>WIA_IPA_RAW_BITS_PER_CHANNEL</strong></dt> <dt>PictureRawBitsPerChannel</dt> </dl></td>
<td ><p>Supported only in Windows Vista and later.</p>
<p>Contains the number of bits in each channel. This property should be reported as a vector of as many BYTE values as there are channels, where the first BYTE corresponds to the number of bits in the first channel, the second byte to the number of bits in the second channel and so on. There need to be as many entries as there are channels according to WIA_IPA_CHANNELS_PER_PIXEL. The driver sets that property when the application switches to WiaImgFmt_RAW. For the well-known subtypes, there are as many entries as listed in the table under WIA_IPA_RAW_SUBTYPE.</p>
<p>Type: <strong>VT_UI1</strong>|<strong>VT_VECTOR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_REGION_TYPE"></span><span id="wia_ipa_region_type"></span><dl> <dt><strong>WIA_IPA_REGION_TYPE</strong></dt> <dt>PictureRegionType</dt> </dl></td>
<td ><p>This property is reserved by for future use and is not implemented at this time.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_SUPPRESS_PROPERTY_PAGE"></span><span id="wia_ipa_suppress_property_page"></span><dl> <dt><strong>WIA_IPA_SUPPRESS_PROPERTY_PAGE</strong></dt> <dt>PictureSuppressPropertyPage</dt> </dl></td>
<td ><p>Specifies whether to suppress the general property pages for items on the device.</p>
<p>This property is available on Windows XP and later.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>The following table has the constants that are valid with this property. The asterisk * indicates that the constant is not valid with Windows Vista and later. (It is only available through the <a href="/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem"><strong>IWiaItem</strong></a> interface.)</p>

<table>
<thead>
<tr class="header">
<th>Constant</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_PROPPAGE_CAMERA_ITEM_GENERAL*</td>
<td>Suppress the general item property page for a camera.</td>
</tr>
<tr class="even">
<td>WIA_PROPPAGE_SCANNER_ITEM_GENERAL</td>
<td>Suppress the general item property page for a scanner.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_IPA_TYMED"></span><span id="wia_ipa_tymed"></span><dl> <dt><strong>WIA_IPA_TYMED</strong></dt> <dt>PictureTymed</dt> </dl></td>
<td ><p>This property contains the transfer method setting. The minidriver creates and maintains this property.</p>
<p>An application reads this property to determine the minidriver's method of data transfer.</p>
<p>Required for all transfer-enabled WIA 2.0 items.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid Values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the constants that are valid with this property. The asterisk * indicates constants that are not valid with Windows Vista and later. (They are only available through the <a href="/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem"><strong>IWiaItem</strong></a> interface.)</p>

<table>
<thead>
<tr class="header">
<th>Transfer Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TYMED_CALLBACK*</td>
<td>Transfer an image to memory, in bands.</td>
</tr>
<tr class="even">
<td>TYMED_MULTIPAGE_CALLBACK*</td>
<td>Transfer multiple images to memory, in bands.</td>
</tr>
<tr class="odd">
<td>TYMED_FILE</td>
<td>Transfer an image to a file.</td>
</tr>
<tr class="even">
<td>TYMED_MULTIPAGE_FILE</td>
<td>Transfer an image to a file.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td ><span id="WIA_IPA_UPLOAD_ITEM_SIZE"></span><span id="wia_ipa_upload_item_size"></span><dl> <dt><strong>WIA_IPA_UPLOAD_ITEM_SIZE</strong></dt> <dt>PictureItemUploadItemSize</dt> </dl></td>
<td ><p>Supported only in Windows Vista and later.</p>
<p>Specifies the number of bytes to upload for an item.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
</tbody>
</table>



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wiadef.h</dt> </dl> |



 

 




