---
Description: 'The MxdcGetPDEVAdjustment function is exported by a printer interface DLL and supplies printer configuration data for the Microsoft XPS Document Converter (MXDC).'
ms.assetid: '4839337b-0328-4919-8f49-d7847743845c'
title: MxdcGetPDEVAdjustment function
---

# MxdcGetPDEVAdjustment function

The `MxdcGetPDEVAdjustment` function is exported by a printer interface DLL and supplies printer configuration data for the Microsoft XPS Document Converter (MXDC).

## Syntax


```C++
HRESULT MxdcGetPDEVAdjustment(
  _In_           HANDLE                    hPrinter,
  _In_           ULONG                     cbDevMode,
  _In_     const DEVMODE                   *pDevMode,
  _In_           ULONG                     cbIn,
  _In_opt_ const VOID                      *pvIn,
  _In_           ULONG                     cbPrintPropertiesCollection,
  _Inout_        PrintPropertiesCollection *pOut
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

The handle of the currently instantiated printer.

</dd> <dt>

*cbDevMode* \[in\]
</dt> <dd>

The size of the [**DEVMODE**](display.devmodew) structure, in bytes, including the driver's private DEVMODE data.

</dd> <dt>

*pDevMode* \[in\]
</dt> <dd>

A copy of the DEVMODE structure that the MXDC received. The printer interface DLL uses information from this structure to return the requested data.

</dd> <dt>

*cbIn* \[in\]
</dt> <dd>

An input parameter that designates the size of the *pvIn* parameter, in bytes. This parameter is currently not used and its value is zero.

</dd> <dt>

*pvIn* \[in, optional\]
</dt> <dd>

A parameter that consists of data that is sent to the printer interface DLL from the MXDC. This parameter is currently not used and its value is **NULL**.

</dd> <dt>

*cbPrintPropertiesCollection* \[in\]
</dt> <dd>

The size of the [PrintPropertiesCollection](print.xps_driver_document_events) data structure, in bytes.

</dd> <dt>

*pOut* \[in, out\]
</dt> <dd>

The **PrintPropertiesCollection** data structure from which the printer interface's DLL gets the requested data. This structure is defined in WinSpool.h. The requested fields might be pre-filled with the MXDC's default data. The printer interface DLL must ignore the fields that it does not understand.

</dd> </dl>

## Return value

`MxdcGetPDEVAdjustment` should return one of the following values.



| Return code                                                                               | Description                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The printer interface DLL successfully returned an adjusted imageable area, compression type, or DPI based on the given DEVMODE structure. The MXDC will validate the returned imageable area and then use it to populate the [**GDIINFO**](display.gdiinfo) structure to the respective fields.<br/>                                                          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The `MxdcGetPDEVAdjustment` function is not implemented by the printer interface. The printer interface must not modify the fields that it does not support. The MXDC defaults to its current defaults. For the imageable area case, MXDC defaults to using the physical page size. For the compression option, MXDC defaults to medium JPEG compression.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | For this value or any other failure values, the MXDC returns -1 to the [**DrvEnablePDEV**](display.drvenablepdev) function, catches the internal exception, and sets a flag to fail and end the print job.<br/>                                                                                                                                                |



 

## Remarks

The `MxdcGetPDEVAdjustment` function is implemented by the hardware vendor. The MXDC calls this function to obtain printer configuration data in the form of a [*property bag*](wdkgloss.p#wdkgloss-property-bag) that includes the following data:

<dl> <dt>

<span id="Imageable_area"></span><span id="imageable_area"></span><span id="IMAGEABLE_AREA"></span>Imageable area
</dt> <dd>

The corner coordinates of the area in which a printer can lay down ink, as determined by the design of the printer and the selected paper size.

</dd> <dt>

<span id="Image_compression_type"></span><span id="image_compression_type"></span><span id="IMAGE_COMPRESSION_TYPE"></span>Image compression type
</dt> <dd>

The file format of an image, either JPEG or PNG, and the level of compression for JPEG images.

</dd> <dt>

<span id="Dots_per_inch_resolution"></span><span id="dots_per_inch_resolution"></span><span id="DOTS_PER_INCH_RESOLUTION"></span>Dots per inch resolution
</dt> <dd>

The resolution of an image in dots per inch (DPI). If the printer interface DLL does not support this field, MXDC defaults to a device-independent resolution that the **dmPrintQuality** field of the [**DEVMODEW**](display.devmodew) structure sets.

</dd> </dl>

MXDC enables the printer interface DLL to adjust DPI through the `MxdcGetPDEVAdjustment` function only if the print job's **dmPrintQuality** field has a value that is less than or equal to 0. If the DPI value is not adjusted, MXDC maps negative **dmPrintQuality** values to the following resolutions.



| GDI name(Wingdi.h)       | GDI value(Wingdi.h) | MXDC default interpretation(dots per inch) |
|--------------------------|---------------------|--------------------------------------------|
| DMRES\_HIGH<br/>   | -4<br/>       | 2400<br/>                            |
| DMRES\_MEDIUM<br/> | -3<br/>       | 1200<br/>                            |
| DMRES\_LOW<br/>    | -2<br/>       | 600<br/>                             |
| DMRES\_DRAFT<br/>  | -1<br/>       | 400<br/>                             |



 

> [!Note]  
> The name of the MXDC property that stores the MXDC default DPI value is L"MxdcDotsPerInch".

 

The following table lists the MXDC's property types and property-bag fields for the properties.



| Property(propertyName)                 | Property Type(ePropertyValue)  | Property-bag fields                                                                                                                                                                                                           |
|----------------------------------------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| L"MxdcImageableArea"<br/>        | kPropertyTypeBuffer<br/> | PrintPropertiesCollection::propertiesCollection\[i\].propertyValue.value.propertyBlob.cbBuf = sizeof(RECT) <br/> PrintPropertiesCollection::propertiesCollection\[i\].propertyValue.value.propertyBlob.pBuf <br/> |
| L"MxdcImageCompressionType"<br/> | kPropertyTypeInt32<br/>  | PrintPropertiesCollection::propertiesCollection\[i\].propertyValue.value.propertyInt32 <br/>                                                                                                                            |
| L"MxdcDotsPerInch"<br/>          | kPropertyTypeInt32<br/>  | PrintPropertiesCollection::propertiesCollection\[i\].propertyValue.value.propertyInt32 <br/>                                                                                                                            |
| L"MxdcLandscapeRotation" <br/>   | kPropertyTypeInt32<br/>  | PrintPropertiesCollection::propertiesCollection\[i\].propertyValue.value.propertyInt32 <br/>                                                                                                                            |



 

The following table lists the MXDC's supported data types and data values for the properties.



<table>
<thead>
<tr class="header">
<th>Property(propertyName)</th>
<th>Data types and values</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>L&quot;MxdcImageableArea&quot;<br/></td>
<td>Data Type: RECT<br/> Values:<br/> RECT::left (Same as FORM_INFO_1)<br/> RECT::right (Same as FORM_INFO_1)<br/> RECT::top (Same as FORM_INFO_1)<br/> RECT::bottom (Same as FORM_INFO_1)<br/></td>
</tr>
<tr class="even">
<td>L&quot;MxdcImageCompressionType&quot;<br/></td>
<td>Data Type: LONG<br/> Values:<br/> 1 = JPEG High Compression<br/> 2 = JPEG Medium Compression<br/> 3 = JPEG Low Compression<br/> 4 = PNG Compression<br/></td>
</tr>
<tr class="odd">
<td>L&quot;MxdcDotsPerInch&quot;<br/></td>
<td>Data Type: LONG<br/> Values: <br/> A positive value for Dots Per Inch<br/></td>
</tr>
<tr class="even">
<td>L&quot;MxdcLandscapeRotation&quot; <br/></td>
<td>Data Type: LONG <br/> Values:<br/> <dl> 90 = MXDC_LANDSCAPE_ROTATE_COUNTERCLOCKWISE_90_DEGREES<br />
0 = MXDC_LANDSCAPE_ROTATE_NONE<br />
-90 = MXDC_LANDSCAPE_ROTATE_COUNTERCLOCKWISE_270_DEGREES<br />
</dl></td>
</tr>
</tbody>
</table>



 

> [!Note]  
> **Notes**
>
> -   The `MxdcGetPDEVAdjustment` function is not a part of the MXDC. The MXDC calls back to this function in the driver's configuration DLL to obtain data for configuring the printer.
>
> -   The MXDC expects the imageable area to be expressed in unrotated coordinates (portrait orientation). The MXDC rotates both the page size and the imageable area according to the value of the **dmOrientation** member of the DEVMODE structure pointed to by *pDevMode*. Thus, the hardware vendor's implementation of `MxdcGetPDEVAdjustment` should avoid specifying the imageable area in rotated coordinates (landscape orientation) because this will cause landscape print jobs to print incorrectly.
>
> -   The default value in the MXDC will be MXDC\_LANDSCAPE\_ROTATE\_COUNTERCLOCKWISE\_270\_DEGREES, which is its current legacy behavior.
>
>     All rotation will be done on the imageable area. If a configuration component (UniDrv/PostScript, XPSDrv Monolithic) does not understand the new property bag values, then it should ignore them as is in the current design.
>
 

## Requirements



|                            |                                                                                                    |
|----------------------------|----------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                 |
| Version<br/>         | Available in Microsoft Windows XP and later versions of the Windows operating system.<br/>   |
| Header<br/>          | <dl> <dt>Mxdc.h (include Mxdc.h)</dt> </dl> |



## See also

<dl> <dt>

[**DrvEnablePDEV**](display.drvenablepdev)
</dt> <dt>

[**GDIINFO**](display.gdiinfo)
</dt> <dt>

[IPrintOemUIMXDC Interface](iprintoemuimxdc-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20MxdcGetPDEVAdjustment%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





