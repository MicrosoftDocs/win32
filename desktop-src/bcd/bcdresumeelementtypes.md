---
title: BcdResumeElementTypes enumeration
description: Specifies the resume loader element types.
ms.assetid: '8C6A64CA-5113-4318-BEBD-81F6165B0354'
keywords: ["BcdResumeElementTypes enumeration Boot Config"]
topic_type:
- apiref
api_name:
- BcdResumeElementTypes
api_type:
- NA
---

# BcdResumeElementTypes enumeration

Specifies the resume loader element types.

## Syntax


```C++
typedef enum _BcdResumeElementTypes { 
  Reserved1                            = 0x21000001,
  Reserved2                            = 0x22000002,
  BcdResumeBoolean_UseCustomSettings   = 0x26000003,
  BcdResumeDevice_AssociatedOsDevice   = 0x21000005,
  BcdResumeBoolean_DebugOptionEnabled  = 0x26000006,
  BcdResumeInteger_BootMenuPolicy      = 0x25000008
} BcdResumeElementTypes;
```



## Constants

<dl> <dt>

<span id="Reserved1"></span><span id="reserved1"></span><span id="RESERVED1"></span>**Reserved1**
</dt> <dd>

This value is reserved. The element data format is [**BcdDeviceElement**](bcddeviceelement.md).

</dd> <dt>

<span id="Reserved2"></span><span id="reserved2"></span><span id="RESERVED2"></span>**Reserved2**
</dt> <dd>

This value is reserved. The element data format is [**BcdStringElement**](bcdstringelement.md).

</dd> <dt>

<span id="BcdResumeBoolean_UseCustomSettings"></span><span id="bcdresumeboolean_usecustomsettings"></span><span id="BCDRESUMEBOOLEAN_USECUSTOMSETTINGS"></span>**BcdResumeBoolean\_UseCustomSettings**
</dt> <dd>

Allows the resume loader BCD object to use custom settings. If this setting is not specified or is not enabled, default settings are applied by the OS before resume. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdResumeDevice_AssociatedOsDevice"></span><span id="bcdresumedevice_associatedosdevice"></span><span id="BCDRESUMEDEVICE_ASSOCIATEDOSDEVICE"></span>**BcdResumeDevice\_AssociatedOsDevice**
</dt> <dd>

Specifies the name of the OS device associated with the hibernated OS. This is only used if the hibernation file is not stored on the OS device. The element data format is [**BcdDeviceElement**](bcddeviceelement.md).

</dd> <dt>

<span id="BcdResumeBoolean_DebugOptionEnabled"></span><span id="bcdresumeboolean_debugoptionenabled"></span><span id="BCDRESUMEBOOLEAN_DEBUGOPTIONENABLED"></span>**BcdResumeBoolean\_DebugOptionEnabled**
</dt> <dd>

Enables kernel debugging on resume from hibernate. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdResumeInteger_BootMenuPolicy"></span><span id="bcdresumeinteger_bootmenupolicy"></span><span id="BCDRESUMEINTEGER_BOOTMENUPOLICY"></span>**BcdResumeInteger\_BootMenuPolicy**
</dt> <dd>

Defines the type of boot menus the system will use. Possible values are **menupolicylegacy (0)** or **menupolicystandard (1)**. The default setting is **menupolicylegacy (0)**. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>           |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/> |



 

 





