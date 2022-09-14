---
title: GetIcon method of the Win32_TSGetIcon class
description: Returns the contents of the specified icon.
ms.assetid: 9448181c-27b8-40eb-9369-8abe1422243b
ms.tgt_platform: multiple
keywords:
- GetIcon method Remote Desktop Services
- GetIcon method Remote Desktop Services , Win32_TSGetIcon class
- Win32_TSGetIcon class Remote Desktop Services , GetIcon method
topic_type:
- apiref
api_name:
- Win32_TSGetIcon.GetIcon
api_location:
- TsPubWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetIcon method of the Win32\_TSGetIcon class

Returns the contents of the specified icon.

## Syntax


```mof
uint32 GetIcon(
  [in]  string FilePath,
  [in]  sint32 Index,
  [out] uint8  IconContents[]
);
```



## Parameters

<dl> <dt>

*FilePath* \[in\]
</dt> <dd>

Specifies the path to the file that contains the icon

</dd> <dt>

*Index* \[in\]
</dt> <dd>

Specifies the index of the icon in the file.

</dd> <dt>

*IconContents* \[out\]
</dt> <dd>

On successful completion contains the contents of the icon.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TsAllow.mof</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>TsPubWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSGetIcon**](win32-tsgeticon.md)
</dt> </dl>

 

 





