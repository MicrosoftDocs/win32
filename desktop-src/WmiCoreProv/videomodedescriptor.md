---
description: Contains mode descriptor elements for the MonitorSourceModes array in the WmiMonitorListedSupportedSourceModes class.
ms.assetid: 6d6c846d-caec-41a8-8a88-1c1e14bc0473
title: VideoModeDescriptor class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- VideoModeDescriptor
- VideoModeDescriptor.CompositePolarityType
- VideoModeDescriptor.HorizontalActivePixels
- VideoModeDescriptor.HorizontalBlankingPixels
- VideoModeDescriptor.HorizontalBorder
- VideoModeDescriptor.HorizontalImageSize
- VideoModeDescriptor.HorizontalPolarityType
- VideoModeDescriptor.HorizontalRefreshRateDenominator
- VideoModeDescriptor.HorizontalRefreshRateNumerator
- VideoModeDescriptor.HorizontalSyncOffset
- VideoModeDescriptor.HorizontalSyncPulseWidth
- VideoModeDescriptor.IsInterlaced
- VideoModeDescriptor.IsSerrationRequired
- VideoModeDescriptor.IsSyncOnRGB
- VideoModeDescriptor.PixelClockRate
- VideoModeDescriptor.StereoModeType
- VideoModeDescriptor.SyncSignalType
- VideoModeDescriptor.VerticalActivePixels
- VideoModeDescriptor.VerticalBlankingPixels
- VideoModeDescriptor.VerticalBorder
- VideoModeDescriptor.VerticalImageSize
- VideoModeDescriptor.VerticalRefreshRateDenominator
- VideoModeDescriptor.VerticalRefreshRateNumerator
- VideoModeDescriptor.VerticalSyncOffset
- VideoModeDescriptor.VerticalPolarityType
- VideoModeDescriptor.VerticalSyncPulseWidth
- VideoModeDescriptor.VideoStandardType
api_type: 
- DllExport
api_location: 
- WmiProv.dll
---

# VideoModeDescriptor class

The **VideoModeDescriptorVideo** WMI class contains mode descriptor elements for the **MonitorSourceModes** array in the [**WmiMonitorListedSupportedSourceModes**](wmimonitorlistedsupportedsourcemodes.md) class. These elements include monitor features such as refresh rate, pixel characteristics, or image size. The **VideoModeDescriptorVideo** class contains information that is a superset of the data available from established, standard, and detailed timing blocks.

## Syntax

``` syntax
class VideoModeDescriptor : WmiMonitorSupportedVideoModes
{
  uint8   CompositePolarityType;
  uint16  HorizontalActivePixels;
  uint16  HorizontalBlankingPixels;
  uint16  HorizontalBorder;
  uint16  HorizontalImageSize;
  uint8   HorizontalPolarityType;
  uint16  HorizontalRefreshRateDenominator;
  uint16  HorizontalRefreshRateNumerator;
  uint16  HorizontalSyncOffset;
  uint16  HorizontalSyncPulseWidth;
  boolean IsInterlaced;
  uint8   IsSerrationRequired;
  uint8   IsSyncOnRGB;
  uint32  PixelClockRate;
  uint8   StereoModeType;
  uint8   SyncSignalType;
  uint16  VerticalActivePixels;
  uint16  VerticalBlankingPixels;
  uint16  VerticalBorder;
  uint16  VerticalImageSize;
  uint16  VerticalRefreshRateDenominator;
  uint16  VerticalRefreshRateNumerator;
  uint16  VerticalSyncOffset;
  uint8   VerticalPolarityType;
  uint16  VerticalSyncPulseWidth;
  uint8   VideoStandardType;
};
```

## Members

The **VideoModeDescriptor** class has these types of members:

-   [Properties](#properties)

### Properties

The **VideoModeDescriptor** class has these properties.

<dl> <dt>

**CompositePolarityType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Composite polarity type. This is polarity of horizontal sync pulses outside of vertical sync.



| Value                                                                              | Meaning                                                                    |
|------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Composite polarity is positive.<br/>                                 |
| <dl> <dt>1 (0x1)</dt> </dl> | Composite polarity is negative.<br/>                                 |
| <dl> <dt>2 (0x2)</dt> </dl> | Not applicable. The signal sync type must be digital composite.<br/> |



 

</dd> <dt>

**HorizontalActivePixels**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of horizontally active pixels.

</dd> <dt>

**HorizontalBlankingPixels**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of horizontally blanking pixels

</dd> <dt>

**HorizontalBorder**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Horizontal border.

</dd> <dt>

**HorizontalImageSize**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Horizontal image size in millimeters (mm).

</dd> <dt>

**HorizontalPolarityType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Horizontal polarity type.



| Value                                                                              | Meaning                                                                   |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Horizontal polarity is positive.<br/>                               |
| <dl> <dt>1 (0x1)</dt> </dl> | Horizontal polarity is negative.<br/>                               |
| <dl> <dt>2 (0x2)</dt> </dl> | Not applicable. The signal sync type must be digital separate.<br/> |



 

</dd> <dt>

**HorizontalRefreshRateDenominator**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Horizontal refresh rate denominator.

</dd> <dt>

**HorizontalRefreshRateNumerator**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Horizontal refresh rate numerator in Hertz (Hz).

</dd> <dt>

**HorizontalSyncOffset**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Horizontal sync offset.

</dd> <dt>

**HorizontalSyncPulseWidth**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Horizontal sync pulse width.

</dd> <dt>

**IsInterlaced**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the display mode is interlaced.

</dd> <dt>

**IsSerrationRequired**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates what type of serration is required, if appropriate.



| Value                                                                              | Meaning                                                                                                  |
|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Controller shall supply horizontal sync during vertical sync.<br/>                                 |
| <dl> <dt>1 (0x1)</dt> </dl> | Controller shall not supply horizontal sync during vertical sync.<br/>                             |
| <dl> <dt>2 (0x2)</dt> </dl> | Not applicable. The signal sync type must be bipolar, analog composite, or digital composite.<br/> |



 

</dd> <dt>

**IsSyncOnRGB**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates which video signal lines should be synchronized, if appropriate.



| Value                                                                              | Meaning                                                                           |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Sync pulse should appear on all 3 video signal lines.<br/>                  |
| <dl> <dt>1 (0x1)</dt> </dl> | Sync pulse should only appear on the green video signal line.<br/>          |
| <dl> <dt>2 (0x2)</dt> </dl> | Not applicable. The signal sync type must be bipolar analog composite.<br/> |



 

</dd> <dt>

**PixelClockRate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Pixel clock rate in Hertz (Hz).

</dd> <dt>

**StereoModeType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Stereo mode type. The following table lists the possible values.



| Value                                                                              | Meaning                                                             |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | No stereo.<br/>                                               |
| <dl> <dt>1 (0x1)</dt> </dl> | Field sequential stereo with right image on stereo sync.<br/> |
| <dl> <dt>2 (0x2)</dt> </dl> | Field sequential stereo with left image on stereo sync.<br/>  |
| <dl> <dt>3 (0x3)</dt> </dl> | 2-way Interleaved Stereo with Right Image on Even Lines.<br/> |
| <dl> <dt>4 (0x4)</dt> </dl> | 2-way Interleaved Stereo with Left Image on Even Lines.<br/>  |
| <dl> <dt>5 (0x5)</dt> </dl> | 4-way Interleaved Stereo.<br/>                                |
| <dl> <dt>6 (0x6)</dt> </dl> | Side-by-Side Interleaved Stereo.<br/>                         |



 

</dd> <dt>

**SyncSignalType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Signal sync type. The following table lists the possible values.



| Value                                                                              | Meaning                             |
|------------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Analog Composite<br/>         |
| <dl> <dt>1 (0x1)</dt> </dl> | Bipolar Analog Composite<br/> |
| <dl> <dt>2 (0x2)</dt> </dl> | Digital Composite<br/>        |
| <dl> <dt>3 (0x3)</dt> </dl> | Digital Separate<br/>         |



 

</dd> <dt>

**VerticalActivePixels**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of vertically active pixels.

</dd> <dt>

**VerticalBlankingPixels**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of vertically blanking pixels.

</dd> <dt>

**VerticalBorder**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Vertical border.

</dd> <dt>

**VerticalImageSize**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Vertical image size in millimeters (mm).

</dd> <dt>

**VerticalPolarityType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Vertical polarity type.



| Value                                                                              | Meaning                                                                   |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl> | Vertical polarity is positive.<br/>                                 |
| <dl> <dt>1 (0x1)</dt> </dl> | Vertical polarity is negative<br/>                                  |
| <dl> <dt>2 (0x2)</dt> </dl> | Not applicable. The signal sync type must be digital separate.<br/> |



 

</dd> <dt>

**VerticalRefreshRateDenominator**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Vertical refresh rate denominator.

</dd> <dt>

**VerticalRefreshRateNumerator**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Vertical refresh rate numerator in Hertz (Hz).

</dd> <dt>

**VerticalSyncOffset**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Vertical sync offset.

</dd> <dt>

**VerticalSyncPulseWidth**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Vertical sync pulse width.

</dd> <dt>

VideoStandardType
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Video standard type.



| Value                                                                                | Meaning                                                                                                        |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0 (0x0)</dt> </dl>   | Other<br/>                                                                                               |
| <dl> <dt>1 (0x1)</dt> </dl>   | VESA DMT. From Video Electronics Standard Association (VESA) Display Monitor Timings specification.<br/> |
| <dl> <dt>2 (0x2)</dt> </dl>   | VESA GTF. From VESA Generalized Timing Formula standard.<br/>                                            |
| <dl> <dt>3 (0x3)</dt> </dl>   | VESA CVT/ From VESA Coordinated Video Timings standard.<br/>                                             |
| <dl> <dt>4 (0x4)</dt> </dl>   | IBM<br/>                                                                                                 |
| <dl> <dt>5 (0x5)</dt> </dl>   | APPLE<br/>                                                                                               |
| <dl> <dt>6 (0x6)</dt> </dl>   | NTSC M<br/>                                                                                              |
| <dl> <dt>7 (0x7)</dt> </dl>   | NTSC J<br/>                                                                                              |
| <dl> <dt>8 (0x8)</dt> </dl>   | NTSC 433<br/>                                                                                            |
| <dl> <dt>9 (0x9)</dt> </dl>   | PAL B<br/>                                                                                               |
| <dl> <dt>10 (0xA)</dt> </dl>  | PAL B1<br/>                                                                                              |
| <dl> <dt>11 (0xB)</dt> </dl>  | PAL G<br/>                                                                                               |
| <dl> <dt>12 (0xC)</dt> </dl>  | PAL H<br/>                                                                                               |
| <dl> <dt>13 (0xD)</dt> </dl>  | PAL I<br/>                                                                                               |
| <dl> <dt>14 (0xE)</dt> </dl>  | PAL D<br/>                                                                                               |
| <dl> <dt>15 (0xF)</dt> </dl>  | PAL N<br/>                                                                                               |
| <dl> <dt>16 (0x10)</dt> </dl> | PAL NC<br/>                                                                                              |
| <dl> <dt>17 (0x11)</dt> </dl> | SECAM B<br/>                                                                                             |
| <dl> <dt>18 (0x12)</dt> </dl> | SECAM D<br/>                                                                                             |
| <dl> <dt>19 (0x13)</dt> </dl> | SECAM G<br/>                                                                                             |
| <dl> <dt>20 (0x14)</dt> </dl> | SECAM H<br/>                                                                                             |
| <dl> <dt>21 (0x15)</dt> </dl> | SECAM K<br/>                                                                                             |
| <dl> <dt>22 (0x16)</dt> </dl> | SECAM K1<br/>                                                                                            |
| <dl> <dt>23 (0x17)</dt> </dl> | SECAM L<br/>                                                                                             |
| <dl> <dt>24 (0x18)</dt> </dl> | SECAM L1<br/>                                                                                            |
| <dl> <dt>25 (0x19)</dt> </dl> | EIA861<br/>                                                                                              |
| <dl> <dt>26 (0x1A)</dt> </dl> | EIA861A<br/>                                                                                             |
| <dl> <dt>27 (0x1B)</dt> </dl> | EIA861B<br/>                                                                                             |



 

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\wmi<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>WmiCore.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSMonitorClass**](msmonitorclass.md)
</dt> </dl>

 

 




