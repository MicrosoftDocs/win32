---
description: The PKEY\_AudioEngine\_OEMFormat property specifies the default format of the device that is used for rendering or capturing a stream. The values are populated by the OEM in an .inf file.
ms.assetid: 3a199ecf-642c-491c-a565-f0083783d180
title: PKEY_AudioEngine_OEMFormat (Mmdeviceapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PKEY\_AudioEngine\_OEMFormat

The PKEY\_AudioEngine\_OEMFormat property specifies the default format of the device that is used for rendering or capturing a stream. The values are populated by the OEM in an .inf file.

The **vt** member of the **PROPVARIANT** structure is set to VT\_BLOB.

The **blob** member of the **PROPVARIANT** structure is a structure of type **BLOB** that contains two members. Member **blob.cbSize** is a **DWORD** that specifies the number of bytes in the format description. Member **blob.pBlobData** points to a **WAVEFORMATEX** structure that contains the format description. For more information about BLOB, see the Windows SDK documentation. For more information about **WAVEFORMATEX**, see the Windows DDK documentation.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Mmdeviceapi.h</dt> </dl> |



## See also

<dl> <dt>

[**Audio Endpoint Properties**](audio-endpoint-properties.md)
</dt> <dt>

[Core Audio Properties](core-audio-properties.md)
</dt> </dl>

 

 




