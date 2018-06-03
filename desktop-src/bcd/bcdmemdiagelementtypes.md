---
title: BcdMemDiagElementTypes enumeration
description: Specifies the memory diagnostic element types.
ms.assetid: 105acf3a-60bf-42ab-905d-f890f302cbd3
keywords:
- BcdMemDiagElementTypes enumeration Boot Config
topic_type:
- apiref
api_name:
- BcdMemDiagElementTypes
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# BcdMemDiagElementTypes enumeration

Specifies the memory diagnostic element types.

## Syntax


```C++
typedef enum BcdMemDiagElementTypes { 
  BcdMemDiagInteger_PassCount     = 0x25000001,
  BcdMemDiagInteger_FailureCount  = 0x25000003
} BcdMemDiagElementTypes;
```



## Constants

<dl> <dt>

<span id="BcdMemDiagInteger_PassCount"></span><span id="bcdmemdiaginteger_passcount"></span><span id="BCDMEMDIAGINTEGER_PASSCOUNT"></span>**BcdMemDiagInteger\_PassCount**
</dt> <dd>

The number of passes for the current test mix. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

If this value is not specified, the default is to run memory diagnostic tests until the computer is powered off or the user logs off.

</dd> <dt>

<span id="BcdMemDiagInteger_FailureCount"></span><span id="bcdmemdiaginteger_failurecount"></span><span id="BCDMEMDIAGINTEGER_FAILURECOUNT"></span>**BcdMemDiagInteger\_FailureCount**
</dt> <dd>

The number of pages that contain errors. This is useful for simulating error flows in the absence of bad physical memory. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

**Note**  This setting is no longer available in Windows 8 and Windows Server 2012.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[BCD WMI Provider Enumerations](bcd-enumerations.md)
</dt> <dt>

[**BcdIntegerElement**](bcdintegerelement.md)
</dt> <dt>

[**GetElement**](getelement-bcdobject.md)
</dt> </dl>

 

 





