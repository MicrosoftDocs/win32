---
title: Visual Basic Script Constants
description: When using the Windows Image Acquisition (WIA) Library from an HTML Page or HTML Application (HTA) as illustrated in the examples, you need a file named Wiaaut.vbs that contains the following Microsoft Visual Basic Scripting Edition (VBScript) code.
ms.assetid: ff3e1ed9-ad60-4124-8433-f6061d1369ec
keywords:
- Windows Image Acquisition (WIA),Visual Basic
- WIA (Windows Image Acquisition),Visual Basic
- Windows Image Acquisition Automation Layer,Visual Basic
- WIA Automation Layer,Visual Basic
- Image Acquisition Automation Layer,Visual Basic
- Windows Image Acquisition (WIA),Visual Basic Scripting Edition (VBScript)
- WIA (Windows Image Acquisition),Visual Basic Scripting Edition (VBScript)
- Windows Image Acquisition Automation Layer,Visual Basic Scripting Edition (VBScript)
- WIA Automation Layer,Visual Basic Scripting Edition (VBScript)
- Image Acquisition Automation Layer,Visual Basic Scripting Edition (VBScript)
- Windows Image Acquisition (WIA),HTML Application (HTA)
- WIA (Windows Image Acquisition),HTML Application (HTA)
- Windows Image Acquisition Automation Layer,HTML Application (HTA)
- WIA Automation Layer,HTML Application (HTA)
- Image Acquisition Automation Layer,HTML Application (HTA)
- Wiaaut.vbs
- Visual Basic Scripting Edition (VBScript)
- VBScript (Visual Basic Scripting Edition)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Visual Basic Script Constants

When using the Windows Image Acquisition (WIA) Library from an HTML Page or HTML Application (HTA) as illustrated in the examples, you need a file named Wiaaut.vbs that contains the following Microsoft Visual Basic Scripting Edition (VBScript) code. For more information about each of these constants and enumerated types, see the reference topics.


```
' Miscellaneous

Const wiaIDUnknown = "{00000000-0000-0000-0000-000000000000}"
Const wiaAnyDeviceID = "*"

' FormatID

Const wiaFormatBMP = "{B96B3CAB-0728-11D3-9D7B-0000F81EF32E}"
Const wiaFormatPNG = "{B96B3CAF-0728-11D3-9D7B-0000F81EF32E}"
Const wiaFormatGIF = "{B96B3CB0-0728-11D3-9D7B-0000F81EF32E}"
Const wiaFormatJPEG = "{B96B3CAE-0728-11D3-9D7B-0000F81EF32E}"
Const wiaFormatTIFF = "{B96B3CB1-0728-11D3-9D7B-0000F81EF32E}"

' EventID

Const wiaEventDeviceConnected = "{A28BBADE-64B6-11D2-A231-00C04FA31809}"
Const wiaEventDeviceDisconnected = "{143E4E83-6497-11D2-A231-00C04FA31809}"
Const wiaEventItemCreated = "{4C8F4EF5-E14F-11D2-B326-00C04F68CE61}"
Const wiaEventItemDeleted = "{1D22A559-E14F-11D2-B326-00C04F68CE61}"
Const wiaEventScanImage = "{A6C5A715-8C6E-11D2-977A-0000F87A926F}"
Const wiaEventScanPrintImage = "{B441F425-8C6E-11D2-977A-0000F87A926F}"
Const wiaEventScanFaxImage = "{C00EB793-8C6E-11D2-977A-0000F87A926F}"
Const wiaEventScanOCRImage = "{9D095B89-37D6-4877-AFED-62A297DC6DBE}"
Const wiaEventScanEmailImage = "{C686DCEE-54F2-419E-9A27-2FC7F2E98F9E}"
Const wiaEventScanFilmImage = "{9B2B662C-6185-438C-B68B-E39EE25E71CB}"
Const wiaEventScanImage2 = "{FC4767C1-C8B3-48A2-9CFA-2E90CB3D3590}"
Const wiaEventScanImage3 = "{154E27BE-B617-4653-ACC5-0FD7BD4C65CE}"
Const wiaEventScanImage4 = "{A65B704A-7F3C-4447-A75D-8A26DFCA1FDF}"

' CommandID

Const wiaCommandSynchronize = "{9B26B7B2-ACAD-11D2-A093-00C04F72DC3C}"
Const wiaCommandTakePicture = "{AF933CAC-ACAD-11D2-A093-00C04F72DC3C}"
Const wiaCommandDeleteAllItems = "{E208C170-ACAD-11D2-A093-00C04F72DC3C}"
Const wiaCommandChangeDocument = "{04E725B0-ACAE-11D2-A093-00C04F72DC3C}"
Const wiaCommandUnloadDocument = "{1F3B3D8E-ACAE-11D2-A093-00C04F72DC3C}"

' WiaSubType enumeration

Const UnspecifiedSubType = 0
Const RangeSubType = 1
Const ListSubType = 2
Const FlagSubType = 3

' WiaDeviceType enumeration

Const UnspecifiedDeviceType = 0
Const ScannerDeviceType = 1
Const CameraDeviceType = 2
Const VideoDeviceType = 3

' WiaItemFlag enumeration

Const FreeItemFlag = &amp;h0
Const ImageItemFlag = &amp;h1
Const FileItemFlag = &amp;h2
Const FolderItemFlag = &amp;h4
Const RootItemFlag = &amp;h8
Const AnalyzeItemFlag = &amp;h10
Const AudioItemFlag = &amp;h20
Const DeviceItemFlag = &amp;h40
Const DeletedItemFlag = &amp;h80
Const DisconnectedItemFlag = &amp;h100
Const HPanoramaItemFlag = &amp;h200
Const VPanoramaItemFlag = &amp;h400
Const BurstItemFlag = &amp;h800
Const StorageItemFlag = &amp;h1000
Const TransferItemFlag = &amp;h2000
Const GeneratedItemFlag = &amp;h4000
Const HasAttachmentsItemFlag = &amp;h8000
Const VideoItemFlag = &amp;h10000
Const RemovedItemFlag = &amp;h80000000

' WiaPropertyType enumeration

Const UnsupportedPropertyType = 0
Const BooleanPropertyType = 1
Const BytePropertyType = 2
Const IntegerPropertyType = 3
Const UnsignedIntegerPropertyType = 4
Const LongPropertyType = 5
Const UnsignedLongPropertyType = 6
Const ErrorCodePropertyType = 7
Const LargeIntegerPropertyType = 8
Const UnsignedLargeIntegerPropertyType = 9
Const SinglePropertyType = 10
Const DoublePropertyType = 11
Const CurrencyPropertyType = 12
Const DatePropertyType = 13
Const FileTimePropertyType = 14
Const ClassIDPropertyType = 15
Const StringPropertyType = 16
Const ObjectPropertyType = 17
Const HandlePropertyType = 18
Const VariantPropertyType = 19
Const VectorOfBooleansPropertyType = 101
Const VectorOfBytesPropertyType = 102
Const VectorOfIntegersPropertyType = 103
Const VectorOfUnsignedIntegersPropertyType = 104
Const VectorOfLongsPropertyType = 105
Const VectorOfUnsignedLongsPropertyType = 106
Const VectorOfErrorCodesPropertyType = 107
Const VectorOfLargeIntegersPropertyType = 108
Const VectorOfUnsignedLargeIntegersPropertyType = 109
Const VectorOfSinglesPropertyType = 110
Const VectorOfDoublesPropertyType = 111
Const VectorOfCurrenciesPropertyType = 112
Const VectorOfDatesPropertyType = 113
Const VectorOfFileTimesPropertyType = 114
Const VectorOfClassIDsPropertyType = 115
Const VectorOfStringsPropertyType = 116
Const VectorOfVariantsPropertyType = 119

' WiaImagePropertyType enumeration

Const UndefinedImagePropertyType = 1000
Const ByteImagePropertyType = 1001
Const StringImagePropertyType = 1002
Const UnsignedIntegerImagePropertyType = 1003
Const LongImagePropertyType = 1004
Const UnsignedLongImagePropertyType = 1005
Const RationalImagePropertyType = 1006
Const UnsignedRationalImagePropertyType = 1007
Const VectorOfUndefinedImagePropertyType = 1100
Const VectorOfBytesImagePropertyType = 1101
Const VectorOfUnsignedIntegersImagePropertyType = 1102
Const VectorOfLongsImagePropertyType = 1103
Const VectorOfUnsignedLongsImagePropertyType = 1104
Const VectorOfRationalsImagePropertyType = 1105
Const VectorOfUnsignedRationalsImagePropertyType = 1106

' WiaEventFlag enumeration

Const NotificationEvent = 1
Const ActionEvent = 2

' WiaImageIntent enumeration

Const UnspecifiedIntent = 0
Const ColorIntent = 1
Const GrayscaleIntent = 2
Const TextIntent = 4

' WiaImageBias enumeration

Const MinimizeSize = 65536
Const MaximizeQuality = 131072
```



 

 




