---
description: Windows Image Acquisition (WIA) hardware devices have property values that are stored in the Windows registry.
ms.assetid: 78caa3af-927b-4143-9e88-4b5c918d00a4
title: Scanner Device Property Constants (Wiadef.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WIA_DPS_DEVICE_ID
- WIA_DPS_DITHER_PATTERN_DATA
- WIA_DPS_DITHER_SELECT
- WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES
- WIA_DPS_DOCUMENT_HANDLING_SELECT
- WIA_DPS_DOCUMENT_HANDLING_STATUS
- WIA_DPS_ENDORSER_CHARACTERS
- WIA_DPS_ENDORSER_STRING
- WIA_DPS_FILTER_SELECT
- WIA_DPS_GLOBAL_IDENTITY
- WIA_DPS_HORIZONTAL_BED_REGISTRATION
- WIA_DPS_HORIZONTAL_BED_SIZE
- WIA_DPS_HORIZONTAL_SHEET_FEED_SIZE
- WIA_DPS_MAX_SCAN_TIME
- WIA_DPS_MIN_HORIZONTAL_SHEET_FEED_SIZE
- WIA_DPS_MIN_VERTICAL_SHEET_FEED_SIZE
- WIA_DPS_OPTICAL_XRES
- WIA_DPS_OPTICAL_YRES
- WIA_DPS_ORIENTATION
- WIA_DPS_PAD_COLOR
- WIA_DPS_PAGE_HEIGHT
- WIA_DPS_PAGE_SIZE
- WIA_DPS_PAGE_WIDTH
- WIA_DPS_PAGES
- WIA_DPS_PLATEN_COLOR
- WIA_DPS_PREVIEW
- WIA_DPS_SCAN_AHEAD_PAGES
- WIA_DPS_SCAN_AVAILABLE_ITEM
- WIA_DPS_SERVICE_ID
- WIA_DPS_SHEET_FEEDER_REGISTRATION
- WIA_DPS_SHOW_PREVIEW_CONTROL
- WIA_DPS_USER_NAME
- WIA_DPS_VERTICAL_BED_REGISTRATION
- WIA_DPS_VERTICAL_BED_SIZE
- WIA_DPS_VERTICAL_SHEET_FEED_SIZE
api_type: 
- HeaderDef
api_location: 
- wiadef.h
---

# Scanner Device Property Constants

Windows Image Acquisition (WIA) hardware devices have property values that are stored in the Windows registry. For more information, see [**Common Device Property Constants**](-wia-wiaitempropcommondevice.md). The following device property constants, with their associated strings, are specific to digital image scanners.

The prefix "WIA\_DPS\_" indicates a Device Property for Scanner devices and is the naming convention used in C/C++. For scripting purposes these constants use the prefix "ScannerDevice" and are part of the [WiaItemPropertyId](-wia-wiaitempropertyid.md) enumerated type. The corresponding member name from that script enumeration appears in parentheses next to the C/C++ constant name in the following list.



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
<td ><span id="WIA_DPS_DEVICE_ID"></span><span id="wia_dps_device_id"></span><dl> <dt><strong>WIA_DPS_DEVICE_ID</strong></dt> <dt>ScannerDeviceDeviceId</dt> </dl></td>
<td ><blockquote>
[!Note]<br />
This property is supported only on Windows Vista and later.
</blockquote>
<br/> Contains a unique function instance identifier for a web services scanner device. This identifier represents the web service on the scanner device with which the WIA mini-driver is communicating. No assumptions about the form of this identifier should be made. The WIA mini-driver creates and maintains this property. <br/> WIA applications can use the value of WIA_DPS_DEVICE_ID to find, using the Function Discovery API, the function instance object representing the web services scanner device used in the current WIA 2.0 session.<br/> Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a><br/></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_DITHER_PATTERN_DATA"></span><span id="wia_dps_dither_pattern_data"></span><dl> <dt><strong>WIA_DPS_DITHER_PATTERN_DATA</strong></dt> </dl></td>
<td >Reserved, do not use.<br/> Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a><br/></td>
</tr>
<tr class="odd">
<td ><span id="WIA_DPS_DITHER_SELECT"></span><span id="wia_dps_dither_select"></span><dl> <dt><strong>WIA_DPS_DITHER_SELECT</strong></dt> </dl></td>
<td >Reserved, do not use.<br/> Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a><br/></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES"></span><span id="wia_dps_document_handling_capabilities"></span><dl> <dt><strong>WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES</strong></dt> <dt>ScannerDeviceDocumentHandlingCapabilities</dt> </dl></td>
<td >Contains the capabilities of the scanner. The minidriver creates and maintains this property. <br/> An application reads this property to determine whether the scanner has a flatbed, document feeder, or duplexer installed. This property is also used to further define the installed features.<br/> Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a><br/> The following table describes the constants that are valid with Windows 7 only.<br/> 
<table>
<thead>
<tr class="header">
<th>Flags</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AUTO_SOURCE</td>
<td>The scanner has an automatic document handler installed.</td>
</tr>
</tbody>
</table>

<p> </p>
<p>The following table describes the constants that are valid with Windows 7 and Windows Vista only.</p>
<p></p>
<table>
<thead>
<tr class="header">
<th>Flags</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADVANCED_DUP</td>
<td>The device supports advanced duplex scan configuration. Use WIA_IPS_DUPLEX_SETTINGS to switch between using basic and advanced duplex configurations.</td>
</tr>
<tr class="even">
<td>DETECT_FILM_TPA</td>
<td>The scanner can detect when the transparency/film adapter is ready to scan.</td>
</tr>
<tr class="odd">
<td>DETECT_STOR</td>
<td>The scanner can detect when there are documents in the internal storage.</td>
</tr>
<tr class="even">
<td>FILM_TPA</td>
<td>The scanner is equipped with a transparency/film scanning adapter.</td>
</tr>
<tr class="odd">
<td>STOR</td>
<td>The scanner is equipped with an internal image storage device.</td>
</tr>
</tbody>
</table>

<p> </p>
<p>The following table describes the constants that are valid with Windows XP or later.</p>
<p></p>
<table>
<thead>
<tr class="header">
<th>Flags</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DETECT_FEED</td>
<td>The scanner can detect a document in the feeder.</td>
</tr>
<tr class="even">
<td>DETECT_FLAT</td>
<td>The scanner can detect a document on the flatbed platen.</td>
</tr>
<tr class="odd">
<td>DETECT_SCAN</td>
<td>The scanner can detect a document in the feeder only by scanning.</td>
</tr>
<tr class="even">
<td>DUP</td>
<td>The scanner has a duplexer.</td>
</tr>
<tr class="odd">
<td>FEED</td>
<td>The scanner has an automatic document handler installed.</td>
</tr>
<tr class="even">
<td>FLAT</td>
<td>The scanner has a flatbed platen.</td>
</tr>
</tbody>
</table>

<p> </p>
<p>The following table describes the constants that are valid with Windows XP only. These values have been deprecated for Windows 7 and Windows Vista and should not be used.</p>
<p></p>
<table>
<thead>
<tr class="header">
<th>Flags</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DETECT_DUP</td>
<td>The scanner can detect a duplex scan request from the user.</td>
</tr>
<tr class="even">
<td>DETECT_DUP_AVAIL</td>
<td>The scanner can tell when the duplexer is installed.</td>
</tr>
<tr class="odd">
<td>DETECT_FEED_AVAIL</td>
<td>The scanner can tell when the automatic document feeder is installed.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_DPS_DOCUMENT_HANDLING_SELECT"></span><span id="wia_dps_document_handling_select"></span><dl> <dt><strong>WIA_DPS_DOCUMENT_HANDLING_SELECT</strong></dt> <dt>ScannerDeviceDocumentHandlingSelect</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported in Windows Vista and later. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_DOCUMENT_HANDLING_SELECT</strong></a>.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the current scanner acquisition source and mode.The minidriver creates and maintains this property.</p>
<p>An application reads this property to determine the current acquisition source of the scanner or to write this property to set the source and mode of the scanner. In addition, applications use this property to enable and disable duplexer functionality.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_FLAG</a></p>
<p>The following table has the ten constants that are valid with this property. </p>
<table>
<thead>
<tr class="header">
<th>Flags</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FEEDER</td>
<td>Scan using the document feeder.</td>
</tr>
<tr class="even">
<td>FLATBED</td>
<td>Scan using the flatbed.</td>
</tr>
<tr class="odd">
<td>DUPLEX</td>
<td>Scan using duplexer operations.</td>
</tr>
<tr class="even">
<td>AUTO_ADVANCE</td>
<td>Enables automatic feeding of the next document after a scan.</td>
</tr>
<tr class="odd">
<td>FRONT_FIRST</td>
<td>Scan the front of the document first. This value is valid when DUPLEX is set.</td>
</tr>
<tr class="even">
<td>BACK_FIRST</td>
<td>Scan the back of the document first. This value is valid when DUPLEX is set.</td>
</tr>
<tr class="odd">
<td>FRONT_ONLY</td>
<td>Scan the front only. This value is valid when DUPLEX is set.</td>
</tr>
<tr class="even">
<td>BACK_ONLY</td>
<td>Scan the back only. This value is valid when DUPLEX is set.</td>
</tr>
<tr class="odd">
<td>NEXT_PAGE</td>
<td>Scan the next page of the document.</td>
</tr>
<tr class="even">
<td>PREFEED</td>
<td>Enable pre-feed mode. Pre-position next document while scanning.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_DOCUMENT_HANDLING_STATUS"></span><span id="wia_dps_document_handling_status"></span><dl> <dt><strong>WIA_DPS_DOCUMENT_HANDLING_STATUS</strong></dt> <dt>ScannerDeviceDocumentHandlingStatus</dt> </dl></td>
<td ><p>Contains current state of the scanner's installed flatbed, document feeder, or duplexer. The minidriver creates and maintains this property.</p>
<p>An application reads this property to determine whether the scanner device is ready to be used. This is an ideal way to check whether paper is in the feeder prior to acquiring an image.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>The following table has the constants that are valid with this property.An asterisk * indicates that the flag is not supported in Windows Vista or later. The <strong>V</strong> symbol indicates that the flag is supported only in Windows Vista and later. </p>
<table>
<thead>
<tr class="header">
<th>Flags</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FEED_READY</td>
<td>The flatbed is ready for use.</td>
</tr>
<tr class="even">
<td>FLAT_READY</td>
<td>The scanner has a document on the flatbed platen.</td>
</tr>
<tr class="odd">
<td>DUP_READY</td>
<td>The duplexer is enabled and ready to be used.</td>
</tr>
<tr class="even">
<td>FLAT_COVER_UP</td>
<td>The flat bed cover is up.</td>
</tr>
<tr class="odd">
<td>PATH_COVER_UP</td>
<td>The paper path is covered up and is preventing proper operation.</td>
</tr>
<tr class="even">
<td>PAPER_JAM</td>
<td>A document is jammed in the document feeder.</td>
</tr>
<tr class="odd">
<td>FILM_TPA_READY<strong>V</strong></td>
<td>The transparency adapter is installed and ready for use.</td>
</tr>
<tr class="even">
<td>STORAGE_READY<strong>V</strong></td>
<td>The internal storage device is ready.</td>
</tr>
<tr class="odd">
<td>STORAGE_FULL<strong>V</strong></td>
<td>The storage is full, no upload operations possible.</td>
</tr>
<tr class="even">
<td>MULTIPLE_FEED<strong>V</strong></td>
<td>A multiple feed condition occurred (usually with a PAPER_JAM).</td>
</tr>
<tr class="odd">
<td>DEVICE_ATTENTION<strong>V</strong></td>
<td>There is an error that requires user intervention on the device.</td>
</tr>
<tr class="even">
<td>LAMP_ERR<strong>V</strong></td>
<td>The scanner is not ready due to a lamp problem.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_DPS_ENDORSER_CHARACTERS"></span><span id="wia_dps_endorser_characters"></span><dl> <dt><strong>WIA_DPS_ENDORSER_CHARACTERS</strong></dt> <dt>ScannerDeviceEndorserCharacters</dt> </dl></td>
<td ><p>Contains all the valid characters that an application can use to create valid endorser strings. An endorser is a printer installed on a scanner that imprints a text message on every page scanned. The minidriver should validate the setting of the <strong>WIA_DPS_ENDORSER_STRING</strong> property against the valid character set in this property. The minidriver creates and maintains this property.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_ENDORSER_STRING"></span><span id="wia_dps_endorser_string"></span><dl> <dt><strong>WIA_DPS_ENDORSER_STRING</strong></dt> <dt>ScannerDeviceEndorserString</dt> </dl></td>
<td ><p>Contains a string that is to be endorsed (in other words, printed) on each page that the minidriver scans. An application sets this property using the valid character set that is reported in the <strong>WIA_DPS_ENDORSER_CHARACTERS</strong> property. The minidriver should endorse documents only if a string is set in this property. An empty string means that the endorser functionality is disabled.</p>
<p>Because it is the driver's responsibility to interpret the endorser string, your driver can use special characters in <strong>WIA_DPS_ENDORSER_STRING</strong>. However, only your applications would understand these characters.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>A driver supporting the <strong>WIA_DPS_ENDORSER_STRING</strong> property must support the following list of tokens. </p>
<table>
<thead>
<tr class="header">
<th>Token</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>$DATE$</td>
<td>The date in the form YYYY/MM/DD.</td>
</tr>
<tr class="even">
<td>$DAY$</td>
<td>The day in the form DD.</td>
</tr>
<tr class="odd">
<td>$MONTH$</td>
<td>The month of the year in the form MM.</td>
</tr>
<tr class="even">
<td>$PAGE_COUNT$</td>
<td>The number of pages transferred.</td>
</tr>
<tr class="odd">
<td>$TIME$</td>
<td>The time of day in the form HH:MM:SS.</td>
</tr>
<tr class="even">
<td>$YEAR$</td>
<td>The year in the form YYYY.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_DPS_FILTER_SELECT"></span><span id="wia_dps_filter_select"></span><dl> <dt><strong>WIA_DPS_FILTER_SELECT</strong></dt> </dl></td>
<td ><p>Reserved, do not use.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_GLOBAL_IDENTITY"></span><span id="wia_dps_global_identity"></span><dl> <dt><strong>WIA_DPS_GLOBAL_IDENTITY</strong></dt> <dt>ScannerDeviceGlobalIdentity</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only on Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the SOAP address of a web services scanner device. The WIA 2.0 mini-driver creates and maintains this property.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_DPS_HORIZONTAL_BED_REGISTRATION"></span><span id="wia_dps_horizontal_bed_registration"></span><dl> <dt><strong>WIA_DPS_HORIZONTAL_BED_REGISTRATION</strong></dt> <dt>ScannerDeviceHorizontalBedRegistration</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported with Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the registration, or horizontal alignment, for documents placed on the flatbed. The minidriver creates and maintains this property.</p>
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
<td>The paper is left justified.</td>
</tr>
<tr class="even">
<td>CENTERED</td>
<td>The paper is centered.</td>
</tr>
<tr class="odd">
<td>RIGHT_JUSTIFIED</td>
<td>The paper is right justified.</td>
</tr>
</tbody>
</table>

<p> </p>
<p><strong>See Also</strong></p>
<p><strong>WIA_DPS_VERTICAL_BED_REGISTRATION</strong></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_HORIZONTAL_BED_SIZE"></span><span id="wia_dps_horizontal_bed_size"></span><dl> <dt><strong>WIA_DPS_HORIZONTAL_BED_SIZE</strong></dt> <dt>ScannerDeviceHorizontalBedSize</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported with Windows Vista and later. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_MAX_HORIZONTAL_SIZE</strong></a>.
</blockquote>
</div>
<div>
 
</div>
<p>Specifies the maximum width, in thousandths of an inch, that is scanned in the horizontal (X) axis from the platen of a flatbed scanner at the current resolution. This property also applies to automatic document feeders that move sheets to the platen of a flatbed scanner for scanning. This property is mandatory for scanners that have a platen. Other scanner types will instead implement the <strong>WIA_DPS_HORIZONTAL_SHEET_FEED_SIZE</strong> property.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_DPS_HORIZONTAL_SHEET_FEED_SIZE"></span><span id="wia_dps_horizontal_sheet_feed_size"></span><dl> <dt><strong>WIA_DPS_HORIZONTAL_SHEET_FEED_SIZE</strong></dt> <dt>ScannerDeviceHorizontalSheetFeedSize</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported with Windows Vista and later. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_MAX_HORIZONTAL_SIZE</strong></a>.
</blockquote>
</div>
<div>
 
</div>
<p>Specifies the maximum width, in thousandths of an inch, that is scanned in the horizontal (X) axis from a handheld or sheet feed scanner at the current resolution. This property also applies to automatic document feeders that scan without moving sheets to the platen of a flatbed scanner. This property is mandatory for sheet-fed, scroll-fed, and hand-held scanners.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_MAX_SCAN_TIME"></span><span id="wia_dps_max_scan_time"></span><dl> <dt><strong>WIA_DPS_MAX_SCAN_TIME</strong></dt> <dt>ScannerDeviceMaxScanTime</dt> </dl></td>
<td ><p>Contains the maximum time to scan a single page with the current property settings, in milliseconds. An application reads this property to estimate the time it will take to scan a page. This is helpful when determining the conditions of a device that has stopped responding. The minidriver creates and maintains this property. This property is required for all scanners.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_DPS_MIN_HORIZONTAL_SHEET_FEED_SIZE"></span><span id="wia_dps_min_horizontal_sheet_feed_size"></span><dl> <dt><strong>WIA_DPS_MIN_HORIZONTAL_SHEET_FEED_SIZE</strong></dt> <dt>ScannerDeviceMinHorizontalSheetFeedSize</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported with Windows Vista and later. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_MIN_HORIZONTAL_SIZE</strong></a>.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the physical horizontal dimensions of the smallest page that the scanner's document feeder can scan, in thousandths of an inch. The minidriver creates and maintains this property.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p><strong>See Also</strong></p>
<p><strong>WIA_DPS_MIN_VERTICAL_SHEET_FEED_SIZE</strong></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_MIN_VERTICAL_SHEET_FEED_SIZE"></span><span id="wia_dps_min_vertical_sheet_feed_size"></span><dl> <dt><strong>WIA_DPS_MIN_VERTICAL_SHEET_FEED_SIZE</strong></dt> <dt>ScannerDeviceMinVerticalSheetFeedSize</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported with Windows Vista and later. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_MIN_VERTICAL_SIZE</strong></a>.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the physical vertical dimensions of the smallest page that the scanner's document feeder can scan, in thousandths of an inch. The minidriver creates and maintains this property.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p><strong>See Also</strong></p>
<p><strong>WIA_DPS_MIN_HORIZONTAL_SHEET_FEED_SIZE</strong></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_DPS_OPTICAL_XRES"></span><span id="wia_dps_optical_xres"></span><dl> <dt><strong>WIA_DPS_OPTICAL_XRES</strong></dt> <dt>ScannerDeviceOpticalXres</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported by Windows Vista. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_OPTICAL_XRES</strong></a>.
</blockquote>
</div>
<div>
 
</div>
<p>Horizontal Optical Resolution. Highest supported horizontal optical resolution in DPI. This property is a single value. This is not a list of all resolutions that can be generated by the device. Rather, this is the resolution of the device's optics. The minidriver creates and maintains this property. This property is required for all scanners.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_OPTICAL_YRES"></span><span id="wia_dps_optical_yres"></span><dl> <dt><strong>WIA_DPS_OPTICAL_YRES</strong></dt> <dt>ScannerDeviceOpticalYres</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported by Windows Vista. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_OPTICAL_YRES</strong></a>.
</blockquote>
</div>
<div>
 
</div>
<p>Vertical Optical Resolution. Highest supported vertical optical resolution in DPI. This property is a single value. This is not a list of all resolutions that are generated by the device. Rather, this is the resolution of the device's optics. The minidriver creates and maintains this property. This property is required for all scanners.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_DPS_ORIENTATION"></span><span id="wia_dps_orientation"></span><dl> <dt><strong>WIA_DPS_ORIENTATION</strong></dt> <dt>ScannerDeviceOrientation</dt> </dl></td>
<td ><p>Contains the current orientation setting.The minidriver creates and maintains this property.</p>
<p>An application sets the <strong>WIA_DPS_ORIENTATION</strong> property to define the original orientation of a page or image to be acquired. For information on how to use WIA_DPS_ORIENTATION, see <strong>WIA_DPS_PAGE_SIZE</strong></p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the four constants that are valid with this property.</p>

<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Defination</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LANDSCAPE</td>
<td>90-degree counter-clockwise rotation, relative to the PORTRAIT orientation.</td>
</tr>
<tr class="even">
<td>PORTRAIT</td>
<td>0 degrees.</td>
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

<p> </p>
<p><strong>See Also</strong></p>
<p><a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_ROTATION</strong></a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_PAD_COLOR"></span><span id="wia_dps_pad_color"></span><dl> <dt><strong>WIA_DPS_PAD_COLOR</strong></dt> <dt>ScannerDevicePadColor</dt> </dl></td>
<td ><p>Color used to pad when there is not enough image data to fill a requested buffer. This property is implemented for scanners that pad the buffer. This property is optional for all scanners. The minidriver creates and maintains this property.</p>
<p>Type: <strong>VT_UI1</strong> | <strong>VT_VECTOR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>The format of the color information is <a href="/windows/win32/api/wingdi/ns-wingdi-rgbquad">RGBQUAD</a>.</p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_DPS_PAGE_HEIGHT"></span><span id="wia_dps_page_height"></span><dl> <dt><strong>WIA_DPS_PAGE_HEIGHT</strong></dt> <dt>ScannerDevicePageHeight</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported by Windows Vista. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_PAGE_HEIGHT</strong></a>.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the height, in thousandths of an inch, of the currently selected page. The minidriver creates and maintains the <strong>WIA_DPS_PAGE_HEIGHT</strong> property. An application reads this property to determine the physical dimensions of the page being scanned. If the extent settings are different from the known page sizes, this property reports the height of the page whose <strong>WIA_DPS_PAGE_SIZE</strong> property is set to WIA_PAGE_CUSTOM (which is a value of the <strong>WIA_DPS_PAGE_SIZE</strong> property). <strong>WIA_DPS_PAGE_HEIGHT</strong> must be in sync with <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_XEXTENT</strong></a>, which reports the height, in pixels, of the page to be scanned.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_PAGE_SIZE"></span><span id="wia_dps_page_size"></span><dl> <dt><strong>WIA_DPS_PAGE_SIZE</strong></dt> <dt>ScannerDevicePageSize</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported by Windows Vista. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_PAGE_SIZE</strong></a>.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the size of the page that is currently selected to be scanned. To select the dimensions of the page to scan, an application sets this property. The minidriver creates and maintains this property.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the three constants that are valid with this property. </p>
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_PAGE_A4</td>
<td>8267 X 11692 (PORTRAIT orientation)</td>
</tr>
<tr class="even">
<td>WIA_PAGE_CUSTOM</td>
<td>Defined by the values of the <strong>WIA_DPS_PAGE_HEIGHT</strong> and <strong>WIA_DPS_PAGE_WIDTH</strong> properties</td>
</tr>
<tr class="odd">
<td>WIA_PAGE_LETTER</td>
<td>8500 X 11000 (PORTRAIT orientation)</td>
</tr>
</tbody>
</table>

<p> </p>
<p>The value of the <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_ORIENTATION</strong></a> property determines the orientation of the currently selected page. The <strong>WIA_DPS_PAGE_WIDTH</strong> and <strong>WIA_DPS_PAGE_HEIGHT</strong> properties report the page's dimensions, in thousandths of an inch. Note that these properties must be in agreement with <strong>WIA_IPS_XEXTENT</strong> and <strong>WIA_IPS_YEXTENT</strong>, which contain the page's dimensions in pixels. Valid values of type WIA_PROP_LIST should depend on valid settings of the <strong>WIA_IPS_ORIENTATION</strong> property. If the device cannot scan landscape-oriented documents with a WIA_PAGE_A4 setting, WIA_PAGE_A4 should not appear in the list of valid values for the <strong>WIA_DPS_PAGE_SIZE</strong> property when <strong>WIA_IPS_ORIENTATION</strong> is set to LANSCAPE.</p>
<p>If an application sets <strong>WIA_DPS_PAGE_SIZE</strong> to any value other than WIA_PAGE_CUSTOM, the minidriver should adjust the values of <strong>WIA_DPS_PAGE_WIDTH</strong> and <strong>WIA_DPS_PAGE_HEIGHT</strong> to the page's dimensions in thousandths of an inch. It should also adjust the values of <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_XEXTENT</strong></a> and <strong>WIA_IPS_YEXTENT</strong> to the page's dimensions in pixels.</p>
<p>If an extent setting (<a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_XEXTENT</strong></a> or <strong>WIA_IPS_YEXTENT</strong>) is changed to a value that does not match the current page-size setting, the minidriver should change the value of the <strong>WIA_DPS_PAGE_SIZE</strong> property to WIA_PAGE_CUSTOM. The minidriver should also modify <strong>WIA_DPS_PAGE_WIDTH</strong> or <strong>WIA_DPS_PAGE_HEIGHT</strong> in accordance with the new extent setting.</p>
<p>If <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_ORIENTATION</strong></a> is set to LANSCAPE, the extent settings will be &quot;flipped.&quot; For example, if an application sets <strong>WIA_DPS_PAGE_SIZE</strong> to WIA_PAGE_A4, the minidriver should set <strong>WIA_DPS_PAGE_WIDTH</strong> to 11692 and <strong>WIA_DPS_PAGE_HEIGHT</strong> to 8267. (The minidriver should also set <strong>WIA_IPS_XEXTENT</strong> and <strong>WIA_IPS_YEXTENT</strong> accordingly.) Note that if <strong>WIA_DPS_PAGE_SIZE</strong> is set to WIA_PAGE_CUSTOM, the orientation setting is not used to determine the extent dimensions of the page to be scanned.</p>
<p>The minidriver is responsible for ensuring that the <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_ORIENTATION</strong></a> property is in agreement with the current selection area. If an application changes the value of <strong>WIA_IPS_ORIENTATION</strong> to one that is invalid for the currently selected page size, the minidriver should change the value of <strong>WIA_DPS_PAGE_SIZE</strong> to a page size that is supported by the new orientation value.</p>
<p>If an application sets the <strong>WIA_DPS_PAGE_SIZE</strong> property to WIA_PAGE_CUSTOM, the current selection area is not affected. The WIA minidriver should obtain the current image layout, starting from the current settings of the <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_XPOS</strong></a> and <strong>WIA_IPS_YPOS</strong> properties. If the page-size setting results in a selection area that is outside the scanner's bed, the minidriver must automatically adjust the values of the <strong>WIA_IPS_XPOS</strong> and <strong>WIA_IPS_YPOS</strong> properties to valid settings. If the <strong>WIA_DPS_PAGE_SIZE</strong> and <strong>WIA_IPS_ORIENTATION</strong> properties are set at the same time, and they are invalid when applied in combination, the minidriver should fail the application's settings by returning an error in the <a href="https://msdn.microsoft.com/library/ms794145.aspx">IWiaMiniDrv::drvValidateItemProperties</a>. .</p>
<p>The following four examples show different <strong>WIA_DPS_PAGE_SIZE</strong> scenarios.</p>
<ol>
<li>The driver reports the settings.</li>
<li>An application sets the <strong>WIA_DPS_PAGE_SIZE</strong> property to WIA_PAGE_LETTER.</li>
<li>An application sets the <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_ORIENTATION</strong></a> property to LANSCAPE.</li>
<li>An application changes the <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_XEXTENT</strong></a> property to a smaller value.</li>
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
<td><pre><code>WIA_DPS_PAGE_SIZE = WIA_PAGE_CUSTOM
WIA_DPS_PAGE_WIDTH = 11500
WIA_DPS_PAGE_HEIGHT = 14000
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
<p><strong>Example 2: An application sets the</strong> <strong>WIA_DPS_PAGE_SIZE</strong>  <strong>property to WIA_PAGE_LETTER</strong></p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>WIA_DPS_PAGE_SIZE = WIA_PAGE_LETTER
WIA_DPS_PAGE_WIDTH = 8500
WIA_DPS_PAGE_HEIGHT = 11000
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
<p><strong>Example 3: An application sets the</strong> <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_ORIENTATION</strong></a>  <strong>property to LANSCAPE</strong></p>
<p>The physical bed must be able to acquire a page that was originally in landscape orientation.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>WIA_DPS_PAGE_SIZE = WIA_PAGE_LETTER
WIA_DPS_PAGE_HEIGHT = 11000
WIA_DPS_PAGE_WIDTH = 8500
WIA_IPS_ORIENTATION = LANSCAPE
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
<p><strong>Example 4: An application changes the</strong> <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_XEXTENT</strong></a>  <strong>property to a smaller value</strong></p>
<p>In the following example, an application changes the <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_XEXTENT</strong></a> property to 1000. The minidriver should assume that the new value contained in <strong>WIA_IPS_XEXTENT</strong> is no longer valid for the <strong>WIA_DPS_PAGE_SIZE</strong> property and should thus change <strong>WIA_DPS_PAGE_SIZE</strong> to WIA_PAGE_CUSTOM. The minidriver must also adjust <strong>WIA_DPS_PAGE_WIDTH</strong>.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>WIA_DPS_PAGE_SIZE = WIA_PAGE_CUSTOM
WIA_DPS_PAGE_HEIGHT = 10000
WIA_DPS_PAGE_WIDTH = 8500
WIA_IPS_ORIENTATION = LANSCAPE
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
<td ><span id="WIA_DPS_PAGE_WIDTH"></span><span id="wia_dps_page_width"></span><dl> <dt><strong>WIA_DPS_PAGE_WIDTH</strong></dt> <dt>ScannerDevicePageWidth</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported by Windows Vista. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_PAGE_WIDTH</strong></a>.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the width of the current page selected, in thousandths of an inch. An application reads this property to determine the physical dimensions of the page being scanned. If the extent settings are different from known page sizes, this property reports the width of the page whose <strong>WIA_DPS_PAGE_SIZE</strong> property is set to WIA_PAGE_CUSTOM. <strong>WIA_DPS_PAGE_WIDTH</strong> must be in sync with the value of <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_XEXTENT</strong></a>, which reports the width, in pixels, of the page to be scanned. The minidriver creates and maintains this property.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_PAGES"></span><span id="wia_dps_pages"></span><dl> <dt><strong>WIA_DPS_PAGES</strong></dt> <dt>ScannerDevicePages</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported by Windows Vista. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_PAGES</strong></a>.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the current number of pages to be acquired from an automatic document feeder. The minidriver creates and maintains this property.</p>
<p>Type: <strong>VT_I4</strong>; Access: Read/Write; Valid values: <a href="-wia-property-attributes.md">WIA_PROP_RANGE</a> (zero through the maximum number of pages that the document feeder can hold)</p>
<p>An application reads this property to determine the document feeder's page capacity. The application also sets this property to the number of pages it is going to scan.</p>
<div class="alert">
<blockquote>
[!Note]<br />
If duplex mode is enabled (<strong>WIA_DPS_DOCUMENT_HANDLING_SELECT</strong> is set to FEEDER | DUPLEX ), <strong>WIA_DPS_PAGES</strong> is still equal to the number of pages to scan.
</blockquote>
</div>
<div>
 
</div>
<p>One sheet of paper will automatically contain two pages if DUPLEX is enabled, even if the back side of the page is blank.</p>
<p>Setting <strong>WIA_DPS_PAGES</strong> to 1 causes a scanner to process one of the sides of the page. It is recommended that if a scanner is unable to scan only one side of a page while in duplex mode, the <strong>WIA_DPS_PAGES</strong> valid value for the Inc member of the WIA_PROPERTY_INFO structure should be changed to 2. This value signals the application that it must request pages in multiples of two. A value of zero means that <em>all</em> pages that are currently loaded into the document feeder are to be scanned.</p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_DPS_PLATEN_COLOR"></span><span id="wia_dps_platen_color"></span><dl> <dt><strong>WIA_DPS_PLATEN_COLOR</strong></dt> <dt>ScannerDevicePlatenColor</dt> </dl></td>
<td ><p>Specifies the color of the platen in back of the sheet to be scanned. This property is optional for scanners that have a platen. The minidriver creates and maintains this property.</p>
<p>Type: <strong>VT_UI1</strong> | <strong>VT_VECTOR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>The format of the color information is <a href="/windows/win32/api/wingdi/ns-wingdi-rgbquad">RGBQUAD</a>.</p></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_PREVIEW"></span><span id="wia_dps_preview"></span><dl> <dt><strong>WIA_DPS_PREVIEW</strong></dt> <dt>ScannerDevicePreview</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported by Windows Vista. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_PREVIEW</strong></a>.
</blockquote>
</div>
<div>
 
</div>
<p>Indicates the preview mode for a device. An application sets this property to place the device into a preview mode.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the two constants that are valid with this property. </p>
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
<tr class="odd">
<td ><span id="WIA_DPS_SCAN_AHEAD_PAGES"></span><span id="wia_dps_scan_ahead_pages"></span><dl> <dt><strong>WIA_DPS_SCAN_AHEAD_PAGES</strong></dt> <dt>ScannerDeviceScanAheadPages</dt> </dl></td>
<td ><p>Contains a value that indicates whether the scanner will cache pages in a scanner buffer before sending them to the application.</p>
<p>A value of zero disables scan ahead and no pages will be scanned ahead. Doing normal data transfers on the buffered scan-ahead item retrieves the buffered pages. WIA properties cannot be changed during a scan-ahead operation. This property is optional.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_RANGE</a> of zero to the maximum number of pages that the document feeder can hold.</p></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_SCAN_AVAILABLE_ITEM"></span><span id="wia_dps_scan_available_item"></span><dl> <dt><strong>WIA_DPS_SCAN_AVAILABLE_ITEM</strong></dt> <dt>ScannerDeviceScanAvailableItem</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows 7 and later.
</blockquote>
</div>
<div>
 
</div>
<p>Indicates the input source (flatbed, automatic document feeder, or fil-scanning adapter) to scan from, or the storage location to transfer data from.</p>
<p>A scan event notifies the application that the user has initiated a scan, but the event does not supply the name of the WIA item that represents the input source. The application's event handler can query the root item's WIA_DPS_SCAN_AVAILABLE_ITEM property to get the name of the input source item.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_RANGE</a> of zero to the maximum number of pages that the document feeder can hold.</p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_DPS_SERVICE_ID"></span><span id="wia_dps_service_id"></span><dl> <dt><strong>WIA_DPS_SERVICE_ID</strong></dt> <dt>ScannerDeviceServiceId</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the Service ID of a Web Services scanner device. The WIA 2.0 mini-driver creates and maintains this property.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_SHEET_FEEDER_REGISTRATION"></span><span id="wia_dps_sheet_feeder_registration"></span><dl> <dt><strong>WIA_DPS_SHEET_FEEDER_REGISTRATION</strong></dt> <dt>ScannerDeviceSheetFeederRegistration</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported with Windows Vista and later. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_SHEET_FEEDER_REGISTRATION</strong></a>.
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
<tr class="odd">
<td ><span id="WIA_DPS_SHOW_PREVIEW_CONTROL"></span><span id="wia_dps_show_preview_control"></span><dl> <dt><strong>WIA_DPS_SHOW_PREVIEW_CONTROL</strong></dt> <dt>ScannerDeviceShowPreviewControl</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported by Windows Vista. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_SHOW_PREVIEW_CONTROL</strong></a>.
</blockquote>
</div>
<div>
 
</div>
<p>Indicates whether an item needs a preview control displayed to the user. The minidriver creates and maintains this property.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>The following table has the two constants that are valid with this property. </p>
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
<tr class="even">
<td ><span id="WIA_DPS_USER_NAME"></span><span id="wia_dps_user_name"></span><dl> <dt><strong>WIA_DPS_USER_NAME</strong></dt> <dt>ScannerDeviceUserName</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is supported only by Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Used by the WIA service to inform the mini-driver about the user account name (including the network domain name when applicable) of the session in which the current WIA application is running.</p>
<p>This is a root item property, managed by the WIA service.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_DPS_VERTICAL_BED_REGISTRATION"></span><span id="wia_dps_vertical_bed_registration"></span><dl> <dt><strong>WIA_DPS_VERTICAL_BED_REGISTRATION</strong></dt> <dt>ScannerDeviceVerticalBedRegistration</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported with Windows Vista and later.
</blockquote>
</div>
<div>
 
</div>
<p>Contains the registration, or vertical alignment and edge detection, for documents placed on the flatbed. The minidriver creates and maintains this property.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>The following table has the three constants that are valid with this property.. </p>
<table>
<thead>
<tr class="header">
<th>Constant</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TOP_JUSTIFIED</td>
<td>The paper is top justified.</td>
</tr>
<tr class="even">
<td>CENTERED</td>
<td>The paper is centered.</td>
</tr>
<tr class="odd">
<td>BOTTOM_JUSTIFIED</td>
<td>The paper is bottom justified.</td>
</tr>
</tbody>
</table>

<p> </p>
<p><strong>See Also</strong>.</p>
<p><strong>WIA_DPS_HORIZONTAL_BED_REGISTRATION</strong></p></td>
</tr>
<tr class="even">
<td ><span id="WIA_DPS_VERTICAL_BED_SIZE"></span><span id="wia_dps_vertical_bed_size"></span><dl> <dt><strong>WIA_DPS_VERTICAL_BED_SIZE</strong></dt> <dt>ScannerDeviceVerticalBedSize</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported with Windows Vista and later. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_MAX_VERTICAL_SIZE</strong></a>.
</blockquote>
</div>
<div>
 
</div>
<p>Specifies the maximum height, in thousandths of an inch, that is scanned in the vertical (Y) axis from the platen of a flatbed scanner at the current resolution. This property also applies to automatic document feeders, that move sheets to the platen of a flatbed scanner for scanning. This property is mandatory for scanners that have a platen. Other scanner types will instead implement the <strong>WIA_DPS_VERTICAL_SHEET_FEED_SIZE</strong> property.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td ><span id="WIA_DPS_VERTICAL_SHEET_FEED_SIZE"></span><span id="wia_dps_vertical_sheet_feed_size"></span><dl> <dt><strong>WIA_DPS_VERTICAL_SHEET_FEED_SIZE</strong></dt> <dt>ScannerDeviceVerticalSheetFeedSize</dt> </dl></td>
<td ><div class="alert">
<blockquote>
[!Note]<br />
This property is not supported with Windows Vista and later. Use <a href="-wia-wiaitempropscanneritem.md"><strong>WIA_IPS_MAX_VERTICAL_SIZE</strong></a>.
</blockquote>
</div>
<div>
 
</div>
<p>Specifies the maximum height, in thousandths of an inch, that is scanned in the vertical (Y) axis from a handheld or sheet feed scanner at the current resolution. This property also applies to automatic document feeders that scan without moving sheets to the platen of a flatbed scanner. This property is mandatory for sheet-fed scanners. Scroll-fed and hand-held scanners should not implement this property.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
</tbody>
</table>



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wiadef.h</dt> </dl> |



 

 
