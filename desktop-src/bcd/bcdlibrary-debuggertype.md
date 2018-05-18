---
title: BcdLibrary\_DebuggerType enumeration
description: Specifies the debugger type.
ms.assetid: 'c7277bab-7047-451f-a671-e68adcfe0f90'
keywords: ["BcdLibrary_DebuggerType enumeration Boot Config"]
topic_type:
- apiref
api_name:
- BcdLibrary_DebuggerType
api_type:
- NA
---

# BcdLibrary\_DebuggerType enumeration

Specifies the debugger type.

## Syntax


```C++
typedef enum BcdLibrary_DebuggerType { 
  DebuggerSerial  = 0,
  Debugger1394    = 1,
  DebuggerUsb     = 2,
  DebuggerNet     = 3
} BcdLibrary_DebuggerType;
```



## Constants

<dl> <dt>

<span id="DebuggerSerial"></span><span id="debuggerserial"></span><span id="DEBUGGERSERIAL"></span>**DebuggerSerial**
</dt> <dd>

Serial debugger.

</dd> <dt>

<span id="Debugger1394"></span><span id="debugger1394"></span><span id="DEBUGGER1394"></span>**Debugger1394**
</dt> <dd>

1394 debugger.

</dd> <dt>

<span id="DebuggerUsb"></span><span id="debuggerusb"></span><span id="DEBUGGERUSB"></span>**DebuggerUsb**
</dt> <dd>

USB debugger.

</dd> <dt>

<span id="DebuggerNet"></span><span id="debuggernet"></span><span id="DEBUGGERNET"></span>**DebuggerNet**
</dt> <dd>

Network debugger.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[BCD WMI Provider Enumerations](bcd-enumerations.md)
</dt> <dt>

[**BcdLibraryElementTypes**](bcdlibraryelementtypes.md)
</dt> </dl>

 

 





