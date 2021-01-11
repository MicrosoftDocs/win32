---
description: Sets the processing mode for the Voice Capture DSP.
ms.assetid: 479b3525-5beb-4c6b-b1ad-8fa72c0d0fd0
title: MFPKEY_WMAAECMA_SYSTEM_MODE Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMAAECMA\_SYSTEM\_MODE Property

Sets the processing mode for the Voice Capture DSP.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

VT\_I4

## Applies To

-   [Voice Capture DSP](voicecapturedmo.md)

## Remarks

The value of this property is a member of the [AEC\_SYSTEM\_MODE](/windows/desktop/api/wmcodecdsp/ne-wmcodecdsp-aec_system_mode) enumeration.

The property must be one of the following values.



| Value | Description                                 |
|-------|---------------------------------------------|
| 0     | Audio echo cancellation (AEC) only mode     |
| 2     | Microphone array processing (MAP) only mode |
| 4     | AEC and MAP mode                            |
| 5     | Neither AEC nor MAP mode                    |



 

You must set this property before using the Voice Capture DSP. After you set this property, you can use the DSP with its default settings, or set additional properties.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[Voice Capture DSP](voicecapturedmo.md)
</dt> </dl>

 

 
