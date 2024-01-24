---
description: The GetPropById method of the Item object uses the ID of an item property to return its value.
ms.assetid: 00f7a91c-fd55-4016-a932-f710045a14b8
title: Item.GetPropById method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Item.GetPropById
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# Item.GetPropById method

The **GetPropById** method of the [**Item**](-wia-item.md) object uses the ID of an item property to return its value.

## Syntax


```JScript
retVal = Item.GetPropById(
  Id
)
```



## Parameters

<dl> <dt>

*Id* \[in\]
</dt> <dd>

Type: **[WiaItemPropertyId](-wia-wiaitempropertyid.md)**

Specifies the ID of the property.

</dd> </dl>

## Return value

Type: **VARIANT**

This method returns the value of the property specified by *Id*.

## Remarks

Use this method to find the value of an item property from its ID. For a list of property IDs, see [WIA Property Constant Definitions](-wia-wia-property-constant-definitions.md). For information about the properties themselves, see [WIA Property Constants](-wia-wia-property-constants.md).

For Microsoft Visual Basic applications, add a reference to "Windows Image Acquisition 1.01 Type Library". The following constants defined in that file are valid only for root items (device items):

``` syntax
const FirmwareVersion = 1026
const ConnectStatus = 1027
const DeviceTime = 1028
const PicturesTaken = 2050
const PicturesRemaining = 2051
const ExposureMode = 2052
const ExposureCompensation = 2053
const ExposureTime = 2054
const FNumber = 2055
const FlashMode = 2056
const FocusMode = 2057
const FocusManualDist = 2058
const ZoomPosition = 2059
const PanPosition = 2060
const TiltPostion = 2061
const TimerMode = 2062
const TimerValue = 2063
const PowerMode = 2064
const BatteryStatus = 2065
const Dimension = 2070
const HorizontalBedSize = 3074
const VerticalBedSize = 3075
const HorizontalSheetFeedSize = 3076
const VerticalSheetFeedSize = 3077
const SheetFeederRegistration = 3078
const HorizontalBedRegistration = 3079
const VerticalBedRegistraion = 3080
const PlatenColor = 3081
const PadColor = 3082
const FilterSelect = 3083
const DitherSelect = 3084
const DitherPatternData = 3085
const DocumentHandlingCapabilities = 3086
const DocumentHandlingStatus = 3087
const DocumentHandlingSelect = 3088
const DocumentHandlingCapacity = 3089
const HorizontalOpticalResolution = 3090
const VerticalOpticalResolution = 3091
const EndorserCharacters = 3092
const EndorserString = 3093
const ScanAheadPages = 3094
const MaxScanTime = 3095
const Pages = 3096
const PageSize = 3097
const PageWidth = 3098
const PageHeight = 3099
const Preview = 3100
const TransparencyAdapter = 3101
const TransparecnyAdapterSelect = 3102
```

## Examples

The following example demonstrates the use of the **GetPropById** method to retrieve a property value.


```JScript
<SCRIPT LANGUAGE="VBScript">
const DeviceType = 5
Dim objWia
Dim objDeviceInfoCollection
Dim objDeviceInfo
Dim objRootItem
Dim objSelectedItems
Dim objItem
Dim PropValue
 
Set objWIA = CreateObject("Wia.Script")
 
Set objDeviceInfoCollection = objWia.Devices
 
For Each objDeviceInfo In objDeviceInfoCollection
    objRootItem=objDeviceInfo.Create()
    objSelectedItems=objRootItem.GetItemsFromUI(0, 0)
    For Each objItem In objSelectedItem
    PropValue = objItem.GetPropById(DeviceType)
    Next
Next
</SCRIPT>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 




